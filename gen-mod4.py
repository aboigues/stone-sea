#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de livrables — Module 04 : Production documentaire assistée (CCTP, DQE/DPGF, CR) et extraction de quantités

Usage:
  python generate_module04.py --out ./module_04 [--zip]

Arborescence produite:
  module_04/
    01_schemas/
      poste_dqe.schema.json
      cr_chantier.schema.json
    02_prompts/
      prompt_redaction_cctp.md
      prompt_structuration_dqe.md
      prompt_cr_chantier.md
    03_scripts/
      csv_dqe_to_json.py
      check_dqe_json.py
      cr_json_to_md.py
    04_modeles/
      trame_cctp.md
      dqe_minimal.csv
      cr_modele.md
    05_docs/
      README_integration_module04.md
      checklists.md
    06_examples/
      dqe_exemple.json
      cr_exemple.json
    PACKAGE_SHA256.txt
"""

import argparse
import json
from pathlib import Path
import textwrap
import zipfile
import hashlib

CONTENT = {}

def _d(s: str) -> str:
    return textwrap.dedent(s).lstrip("\n").rstrip() + "\n"

# ------------------------
# 01_schemas
# ------------------------
CONTENT["01_schemas/poste_dqe.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Poste DQE/DPGF",
  "type": "object",
  "required": ["code","intitule","unite","quantite","prix_unitaire","montant","sources"],
  "properties": {
    "code": {"type": "string"},
    "intitule": {"type": "string"},
    "description": {"type": "string"},
    "unite": {"type": "string", "enum": ["m","m2","m3","u","kg","h","forfait"]},
    "quantite": {"type": "number", "minimum": 0},
    "prix_unitaire": {"type": "number", "minimum": 0},
    "montant": {"type": "number", "minimum": 0},
    "hypotheses": {"type": "string"},
    "sources": {"type": "array", "items": {"type": "string"}},
    "liens_normatifs": {"type": "array", "items": {"type": "string"}},
    "tags": {"type": "array", "items": {"type": "string"}}
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/cr_chantier.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CR Chantier",
  "type": "object",
  "required": ["meta","avancement","points","photos","actions"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["projet","date","lot","participants"],
      "properties": {
        "projet": {"type":"string"},
        "date": {"type":"string"},
        "lot": {"type":"string"},
        "participants": {"type":"array","items":{"type":"string"}},
        "meteo": {"type":"string"},
        "documents_consultes": {"type":"array","items":{"type":"string"}}
      },
      "additionalProperties": false
    },
    "avancement": {
      "type":"object",
      "required":["taches_prevues","taches_realisees","ecarts"],
      "properties": {
        "taches_prevues":{"type":"array","items":{"type":"string"}},
        "taches_realisees":{"type":"array","items":{"type":"string"}},
        "ecarts":{"type":"array","items":{"type":"string"}}
      },
      "additionalProperties": false
    },
    "points": {
      "type":"array",
      "items":{
        "type":"object",
        "required":["id","type","description","gravite"],
        "properties": {
          "id":{"type":"string"},
          "type":{"type":"string","enum":["risque","NC","point_attention","info"]},
          "description":{"type":"string"},
          "gravite":{"type":"string","enum":["mineure","significative","majeure"]},
          "liens":{"type":"array","items":{"type":"string"}}
        },
        "additionalProperties": false
      }
    },
    "photos": {
      "type":"array",
      "items":{
        "type":"object",
        "required":["fichier"],
        "properties":{
          "fichier":{"type":"string"},
          "repere_plan":{"type":"string"},
          "commentaire":{"type":"string"}
        },
        "additionalProperties": false
      }
    },
    "actions": {
      "type":"array",
      "items":{
        "type":"object",
        "required":["qui","quoi","quand"],
        "properties":{
          "qui":{"type":"string"},
          "quoi":{"type":"string"},
          "quand":{"type":"string"},
          "critere_succes":{"type":"string"}
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
""")

# ------------------------
# 02_prompts
# ------------------------
CONTENT["02_prompts/prompt_redaction_cctp.md"] = _d(r"""
# Prompt — Co‑rédaction / Mise à jour CCTP (par lot)

Rôle: Rédacteur CCTP du lot [LOT]. Tu produis ou mets à jour les articles en t’appuyant sur:
- Contrat (CCTP/avenants), plans, fiches techniques, exigences MOA/MOE.
- Règles de l’art et référentiels applicables (liste fournie; éditions à préciser).

Exigences:
1) Structure: Objet – Références – Définitions – Matériaux – Mise en œuvre – Contrôles – Tolérances – Essais – Documents à remettre.
2) Pour chaque exigence technique, ajouter une balise [Preuve:] avec la source (nom_fichier#page ou repère plan).
3) Ajouter les sections “Points de vigilance” et “Dérogations contractuelles”.
4) Sortie: Markdown H2/H3; pas d’invention — mentionner “à compléter” si l’info manque.

Entrées: {Contexte_Projet}, {Liste_Documents}, {Références_Applicables}.
Sortie: Markdown CCTP du lot [LOT].
""")

CONTENT["02_prompts/prompt_structuration_dqe.md"] = _d(r"""
# Prompt — Structuration DQE/DPGF

Rôle: “Structureur DQE”. À partir d’un CSV/Excel et d’extraits CCTP/plans, normalise les postes.

Exigences:
- Retourner un JSON (liste de postes) conforme au schéma Poste DQE/DPGF.
- Calculer montant = quantite × prix_unitaire (arrondi 2 décimales).
- Renseigner hypothèses et au moins une source par poste (fichier#page/repère plan).
- Signaler incohérences (unités, montants, doublons, champs manquants) dans un court rapport.

Entrées: {CSV_DQE}, {Extraits_CCTP/Plans}. Sortie: JSON conforme + rapport anomalies.
""")

CONTENT["02_prompts/prompt_cr_chantier.md"] = _d(r"""
# Prompt — CR de chantier assisté

Rôle: “Secrétaire de chantier”. Tu produis un CR structuré à partir de notes, photos et planning.

Exigences:
- Sortie JSON conforme au schéma CR Chantier, puis rendu Markdown.
- Lier chaque point important à une photo ou référence (repère plan/document).
- Plan d’actions avec qui/quoi/quand/critère de succès. Classer risques/NC.

Entrées: {Notes}, {Photos+repères}, {Planning}, {Écarts}. Sortie: JSON + Markdown.
""")

# ------------------------
# 03_scripts
# ------------------------
CONTENT["03_scripts/csv_dqe_to_json.py"] = _d(r"""
#!/usr/bin/env python3
# csv_dqe_to_json.py
import csv, json, sys

def row_to_item(r):
    def fnum(v, default=0.0):
        try: return float(v)
        except: return default
    q = fnum(r.get("quantite", 0))
    pu = fnum(r.get("prix_unitaire", 0))
    m = round(q * pu, 2)
    return {
        "code": (r.get("code") or "").strip(),
        "intitule": (r.get("intitule") or "").strip(),
        "description": (r.get("description") or "").strip(),
        "unite": (r.get("unite") or "").strip(),
        "quantite": q,
        "prix_unitaire": pu,
        "montant": m,
        "hypotheses": (r.get("hypotheses") or "").strip(),
        "sources": [s.strip() for s in (r.get("sources") or "").split(";") if s.strip()],
        "liens_normatifs": [s.strip() for s in (r.get("liens_normatifs") or "").split(";") if s.strip()],
        "tags": [t.strip() for t in (r.get("tags") or "").split(";") if t.strip()]
    }

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_dqe_to_json.py in.csv out.json"); sys.exit(2)
    with open(sys.argv[1], newline="", encoding="utf-8") as f:
        items = [row_to_item(r) for r in csv.DictReader(f)]
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"[OK] {len(items)} postes exportés -> {sys.argv[2]}")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/check_dqe_json.py"] = _d(r"""
#!/usr/bin/env python3
# check_dqe_json.py
import json, sys

VALID_UNITS = {"m","m2","m3","u","kg","h","forfait"}

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_dqe_json.py dqe.json"); sys.exit(2)
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    errs = []
    for i, it in enumerate(data):
        if it.get("unite") not in VALID_UNITS:
            errs.append(f"[{i}] unité invalide: {it.get('unite')}")
        q = it.get("quantite", 0)
        pu = it.get("prix_unitaire", 0)
        if (q < 0) or (pu < 0):
            errs.append(f"[{i}] quantite/prix négatif")
        m = round(q * pu, 2)
        if abs(m - it.get("montant", 0)) > 0.01:
            errs.append(f"[{i}] montant incohérent, attendu {m}")
        if not it.get("sources"):
            errs.append(f"[{i}] sources manquantes")
        if not it.get("code") or not it.get("intitule"):
            errs.append(f"[{i}] code/intitule manquant")
    if errs:
        print("[ERROR] DQE invalide:"); [print(" -", e) for e in errs]; sys.exit(2)
    print("[OK] DQE validé.")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/cr_json_to_md.py"] = _d(r"""
#!/usr/bin/env python3
# cr_json_to_md.py
import json, sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python cr_json_to_md.py cr.json out.md"); sys.exit(2)
    cr = json.load(open(sys.argv[1], encoding="utf-8"))
    meta = cr["meta"]
    md = []
    md.append(f"# CR Chantier — {meta['projet']} — {meta['date']}")
    md.append(f"- Participants: {', '.join(meta['participants'])}")
    if meta.get("meteo"): md.append(f"- Météo: {meta['meteo']}")
    if meta.get("documents_consultes"):
        md.append("- Docs consultés: " + ", ".join(meta["documents_consultes"]))
    md.append("\n## Avancement")
    md.append("- Tâches prévues: " + "; ".join(cr["avancement"]["taches_prevues"]))
    md.append("- Tâches réalisées: " + "; ".join(cr["avancement"]["taches_realisees"]))
    if cr["avancement"]["ecarts"]: md.append("- Écarts: " + "; ".join(cr["avancement"]["ecarts"]))
    md.append("\n## Points")
    for p in cr["points"]:
        md.append(f"- [{p['type']}/{p['gravite']}] {p['id']} — {p['description']}")
        if p.get("liens"): md.append(f"  - Liens: {', '.join(p['liens'])}")
    if cr["photos"]:
        md.append("\n## Photos")
        for ph in cr["photos"]:
            rep = f" ({ph['repere_plan']})" if ph.get("repere_plan") else ""
            com = f" — {ph['commentaire']}" if ph.get("commentaire") else ""
            md.append(f"- {ph['fichier']}{rep}{com}")
    if cr["actions"]:
        md.append("\n## Actions")
        for a in cr["actions"]:
            crit = f" — critère: {a['critere_succes']}" if a.get("critere_succes") else ""
            md.append(f"- {a['qui']} ▶ {a['quoi']} pour {a['quand']}{crit}")
    open(sys.argv[2], "w", encoding="utf-8").write("\n".join(md))
    print(f"[OK] CR exporté -> {sys.argv[2]}")

if __name__ == "__main__":
    main()
""")

# ------------------------
# 04_modeles
# ------------------------
CONTENT["04_modeles/trame_cctp.md"] = _d(r"""
## Objet du lot
[Décrire l'objet, périmètre et interfaces]

## Références
- Marché: [CCTP/CCAP/avenants]
- Règles de l’art applicables: [liste + édition à préciser]
- Autres: [FDES/FDS, guides, etc.]

## Définitions
[Glossaire et abréviations]

## Matériaux
[Exigences, performances, marques admises, PV d'essais]

## Mise en œuvre
[Conditions, préparation supports, tolérances, essais]

## Contrôles / Essais / Tolérances
[Auto-contrôles, essais, critères d'acceptation]

## Documents à remettre
[Fiches techniques, PV, DOE, plans de récolement]

## Points de vigilance
[Listes des points sensibles]

## Dérogations contractuelles
[Dérogations explicitement acceptées]
""")

CONTENT["04_modeles/dqe_minimal.csv"] = _d(r"""
code,intitule,description,unite,quantite,prix_unitaire,hypotheses,sources,liens_normatifs,tags
L01-001,Fourniture et pose d'isolant 200 mm,,m2,0,0,"Surfaces nettes d'après Plan A-203","CCTP_L01.pdf#p12;Plan_A-203","NF DTU 45.x (édition à préciser)","L01;isolation"
""")

CONTENT["04_modeles/cr_modele.md"] = _d(r"""
# CR Chantier — [Projet] — [Date]
- Participants: [...]
- Météo: [...]
- Docs consultés: [...]

## Avancement
- Tâches prévues: [...]
- Tâches réalisées: [...]
- Écarts: [...]

## Points (risques/NC/points d'attention)
- [NC/majeure] P-XX — description (liens: Photo_xxx.jpg, Plan#repère)
- [...]

## Photos
- Photo_001.jpg (A12) — commentaire

## Actions
- Qui ▶ Quoi pour Quand — critère: [...]
""")

# ------------------------
# 05_docs
# ------------------------
CONTENT["05_docs/README_integration_module04.md"] = _d(r"""
# Intégration — Module 04

Pipeline conseillé:
1) Ingestion des sources (CCTP existants, plans, CSV/Excel DQE, notes/Photos).
2) Prompts (02_prompts) -> Génération IA.
3) Scripts (03_scripts) -> Contrôles et rendus:
   - csv_dqe_to_json.py : CSV -> JSON conforme schéma DQE
   - check_dqe_json.py  : vérifications (unités, montants, sources, champs)
   - cr_json_to_md.py   : CR JSON -> Markdown diffusé
4) Évidences Module 03: créer une évidence par livrable clé (CCTP/DQE/CR).
5) Validation -> Rapport PDF/A + archivage (version + horodatage).

Commandes rapides:
- Conversion DQE:  python 03_scripts/csv_dqe_to_json.py 04_modeles/dqe_minimal.csv ./out_dqe.json
- Vérification DQE: python 03_scripts/check_dqe_json.py ./out_dqe.json
- CR JSON -> MD:  python 03_scripts/cr_json_to_md.py 06_examples/cr_exemple.json ./CR_S+1.md
""")

CONTENT["05_docs/checklists.md"] = _d(r"""
# Checklists qualité — Module 04

## CCTP
- [ ] Références et éditions renseignées
- [ ] Points de vigilance listés
- [ ] Dérogations contractuelles explicites
- [ ] Preuves [Preuve: ...] pour exigences clés

## DQE/DPGF
- [ ] Unités normalisées (m, m2, m3, u, kg, h, forfait)
- [ ] Montant = quantite × prix_unitaire
- [ ] Sources/hypothèses par poste
- [ ] Doublons et postes “risque” identifiés

## CR Chantier
- [ ] Points NC/risques classés par gravité
- [ ] Actions qui/quoi/quand/critère
- [ ] Lien photos/repères systématique
""")

# ------------------------
# 06_examples
# ------------------------
CONTENT["06_examples/dqe_exemple.json"] = _d(r"""
[
  {
    "code": "L01-001",
    "intitule": "Isolation sous toiture, laine minérale 200 mm",
    "description": "Fourniture et pose, y c. fixations",
    "unite": "m2",
    "quantite": 125.0,
    "prix_unitaire": 18.5,
    "montant": 2312.5,
    "hypotheses": "Surfaces nettes d'après Plan A-203, hors trémies",
    "sources": ["CCTP_L01.pdf#p15", "Plan_A-203"],
    "liens_normatifs": ["NF DTU 45.x (édition à préciser)"],
    "tags": ["isolation","couverture"]
  }
]
""")

CONTENT["06_examples/cr_exemple.json"] = _d(r"""
{
  "meta": {
    "projet": "Opération X",
    "date": "2025-11-13",
    "lot": "CVC",
    "participants": ["MOE", "Entreprise", "CSPS"],
    "meteo": "Couvert 12°C",
    "documents_consultes": ["Planning_S+8", "Plan_MEP_L2"]
  },
  "avancement": {
    "taches_prevues": ["Pose gaines R+2", "Essais étanchéité réseau A"],
    "taches_realisees": ["Pose gaines R+2"],
    "ecarts": ["Essais étanchéité reportés faute d'accès local CTA"]
  },
  "points": [
    {"id":"P-01","type":"NC","description":"Manchon sans collier coupe‑feu zone cage A","gravite":"majeure","liens":["Photo_001.jpg","Plan_MEP_L2#A12"]},
    {"id":"P-02","type":"point_attention","description":"Réception supports avant isolant","gravite":"significative","liens":["Photo_004.jpg"]}
  ],
  "photos": [
    {"fichier":"Photo_001.jpg","repere_plan":"A12","commentaire":"Traversée mur CF 2h"},
    {"fichier":"Photo_004.jpg","repere_plan":"B07","commentaire":"Support attente"}
  ],
  "actions": [
    {"qui":"Entreprise CVC","quoi":"Poser collier CF et PV","quand":"S+1","critere_succes":"PV essais CF"},
    {"qui":"MOE","quoi":"Valider supports","quand":"J+3","critere_succes":"Visa MOE"}
  ]
}
""")

# ------------------------
# Génération fichiers / zip / hash
# ------------------------
def write_file(base: Path, relpath: str, content: str):
    target = base / relpath
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

def sha256_of_tree(base: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(base.rglob("*")):
        if p.is_file():
            h.update(p.relative_to(base).as_posix().encode("utf-8"))
            with open(p, "rb") as f:
                h.update(f.read())
    return h.hexdigest()

def make_zip(base: Path, zip_path: Path):
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in base.rglob("*"):
            if p.is_file():
                z.write(p, arcname=p.relative_to(base))

def main():
    parser = argparse.ArgumentParser(description="Générer les livrables du Module 04.")
    parser.add_argument("--out", required=True, help="Dossier de sortie (ex: ./module_04)")
    parser.add_argument("--zip", action="store_true", help="Créer aussi une archive .zip")
    args = parser.parse_args()

    base = Path(args.out)
    for rel, txt in CONTENT.items():
        write_file(base, rel, txt)

    digest = sha256_of_tree(base)
    with open(base / "PACKAGE_SHA256.txt", "w", encoding="utf-8") as f:
        f.write(digest + "\n")

    print(f"[OK] Livrables écrits dans: {base.resolve()}")
    print(f"[INFO] SHA-256 du package (contenu): {digest}")

    if args.zip:
        zip_path = base.with_suffix(".zip")
        make_zip(base, zip_path)
        print(f"[OK] Archive créée: {zip_path.resolve()}")

if __name__ == "__main__":
    main()


