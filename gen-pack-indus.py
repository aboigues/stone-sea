#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splitteur Pack_Industrialisation_IA_BTP.md -> arborescence de fichiers.
Usage:
  python split_pack.py "Pack_Industrialisation_IA_BTP.md" "./export_pack"
"""

import sys, re, os
from pathlib import Path

# Mapping des sorties attendues (section -> sous-fichiers)
MAP = {
    # 1) README
    r"^##\s*1\)\s*README": [("README.md", "code")],

    # 2) Fiche Cas d’Usage
    r"^##\s*2\)\s*Fiche\s+Cas.*": [("01_Fiche_Cas_Usage.md", "code_or_section_md")],

    # 3) Charte des Sources
    r"^##\s*3\)\s*Charte\s+des\s+Sources": [("02_Charte_Sources.md", "code_or_section_md")],

    # 4) Prompts et Schéma JSON (sous-sections 4.1 à 4.6)
    r"^###\s*4\.1\s*Prompt.*Contrôlé.*CCTP": [("03_Prompts/prompt_controle_CCTP.md", "code")],
    r"^###\s*4\.2\s*Prompt.*DQE": [("03_Prompts/prompt_DQE_quantites.md", "code")],
    r"^###\s*4\.3\s*Prompt.*CR\s*de\s*Chantier": [("03_Prompts/prompt_CR_chantier.md", "code")],
    r"^###\s*4\.4\s*Prompt.*Photo": [("03_Prompts/prompt_analyse_photos.md", "code")],
    r"^###\s*4\.5\s*Prompt.*Vérificateur": [("03_Prompts/prompt_verif_normative.md", "code")],
    r"^###\s*4\.6\s*Schéma\s*JSON": [("03_Prompts/schema_sortie_generique.json", "code")],

    # 5) Grilles de Conformité
    r"^###\s*5\.1\s*Couverture": [("04_Grille_Conformite/grille_Couverture_DTU40xx.xlsx.md", "code_or_section_md")],
    r"^###\s*5\.2\s*Maçonnerie": [("04_Grille_Conformite/grille_Maconnerie_Beton_DTU20_21.xlsx.md", "code_or_section_md")],
    r"^###\s*5\.3\s*CVC/Plomberie": [("04_Grille_Conformite/grille_CVC_Plomberie_DTU60_65.xlsx.md", "code_or_section_md")],
    r"^###\s*5\.4\s*Electricité|Électricité": [("04_Grille_Conformite/grille_Electricite_DTU70_1.xlsx.md", "code_or_section_md")],

    # 6) Pipeline (règles, scripts, orchestrateur)
    r"^###\s*6\.1\s*Règles.*anonymisation": [("05_Pipeline/anonymisation_rules.yaml", "code")],
    r"^###\s*6\.2\s*Script\s*anonymize\.py": [("05_Pipeline/anonymize.py", "code")],
    r"^###\s*6\.3\s*validators\.py": [("05_Pipeline/validators.py", "code")],
    r"^###\s*6\.4\s*orchestrate_pipeline\.py": [("05_Pipeline/orchestrate_pipeline.py", "code")],

    # 7) Tests et évaluation
    r"^###\s*7\.1\s*golden_set_example\.csv": [("06_Tests/golden_set_example.csv", "code")],
    r"^###\s*7\.2\s*evaluator\.py": [("06_Tests/evaluator.py", "code")],
    r"^###\s*7\.3\s*red_teaming_cases\.md": [("06_Tests/red_teaming_cases.md", "code_or_section_md")],

    # 8) SOP et Playbook
    r"^###\s*8\.1\s*SOP_Exploitation": [("07_SOP/SOP_Exploitation.md", "code")],
    r"^###\s*8\.2\s*Playbook.*Incidents": [("07_SOP/Playbook_Incidents_IA.md", "code")],

    # 9) Dashboards
    r"^###\s*9\.1\s*metrics_schema\.json": [("08_Dashboards/metrics_schema.json", "code")],
    r"^###\s*9\.2\s*sample_queries\.sql": [("08_Dashboards/sample_queries.sql", "code")],

    # 10) Plan de Réversibilité
    r"^##\s*10\)\s*Plan\s+de\s+Réversibilité": [("09_Reversibilite/Plan_Reversibilite_Archivage.md", "code_or_section_md")],

    # 1) README déjà mappé plus haut; doublon non nécessaire
}

FENCE_RE = re.compile(r"^```(\w+)?\s*$")
H2_H3_RE = re.compile(r"^(##|###)\s+.*")

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def ensure_parent(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

def extract_sections(lines):
    # Découpe en sections par titres H2/H3 avec leur contenu
    sections = []
    cur_title = None
    cur_buf = []
    for ln in lines:
        if H2_H3_RE.match(ln):
            if cur_title is not None:
                sections.append((cur_title, cur_buf))
            cur_title = ln.strip()
            cur_buf = [ln]
        else:
            if cur_title is not None:
                cur_buf.append(ln)
    if cur_title is not None:
        sections.append((cur_title, cur_buf))
    return sections

def get_code_blocks(block_lines):
    # Renvoie la liste des blocs de code (lang, content)
    code_blocks = []
    in_code = False
    lang = ""
    buf = []
    for ln in block_lines:
        m = FENCE_RE.match(ln.rstrip("\n"))
        if m:
            if not in_code:
                in_code = True
                lang = (m.group(1) or "").strip()
                buf = []
            else:
                # fermeture
                code_blocks.append((lang, "".join(buf)))
                in_code = False
                lang = ""
                buf = []
            continue
        if in_code:
            buf.append(ln)
    return code_blocks

def write_file(root_out: Path, relpath: str, content: str):
    out = root_out / relpath
    ensure_parent(out)
    out.write_text(content, encoding="utf-8")
    print(f"[OK] {relpath} ({len(content)} chars)")

def first_block_or_section_md(section_title, section_lines, mode):
    """
    mode:
      - "code": force extraction du premier bloc de code
      - "code_or_section_md": prend le premier bloc de code sinon tout le markdown de la section (sans titre)
    """
    code_blocks = get_code_blocks(section_lines)
    if mode == "code":
        if not code_blocks:
            raise RuntimeError(f"Aucun bloc de code trouvé pour: {section_title}")
        return code_blocks[0][1]
    else:
        if code_blocks:
            return code_blocks[0][1]
        # sinon, on renvoie le markdown de la section (sans le titre de section)
        body = "".join(section_lines[1:]).strip()
        return body + ("\n" if not body.endswith("\n") else "")

def main():
    if len(sys.argv) < 3:
        print("Usage: python split_pack.py Pack_Industrialisation_IA_BTP.md ./export_pack")
        sys.exit(1)

    src = Path(sys.argv[1])
    outdir = Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)

    text = load_text(src)
    lines = text.splitlines(keepends=True)
    sections = extract_sections(lines)

    # Index sections par leur titre H2/H3
    # Pour faciliter les regex du mapping
    for regex, targets in MAP.items():
        pattern = re.compile(regex, flags=re.IGNORECASE)
        # Trouver la première section dont le titre matche
        matched = False
        for title, content in sections:
            if pattern.match(title.strip()):
                for relpath, mode in targets:
                    payload = first_block_or_section_md(title, content, mode)
                    write_file(outdir, relpath, payload)
                matched = True
                break
        if not matched:
            print(f"[WARN] Section non trouvée pour motif: {regex}")

    # Créer fichiers vides utiles à la navigation
    for folder in [
        "03_Prompts", "04_Grille_Conformite", "05_Pipeline",
        "06_Tests", "07_SOP", "08_Dashboards", "09_Reversibilite"
    ]:
        (outdir / folder / ".keep").parent.mkdir(parents=True, exist_ok=True)

    print("\nTerminé. Arborescence créée dans:", outdir.resolve())

if __name__ == "__main__":
    main()



