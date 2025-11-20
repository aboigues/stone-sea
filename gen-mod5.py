#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de livrables — Module 05 : Conformité normative et technique
Référentiels: NF DTU / Eurocodes / Avis techniques (catalogue d’exigences, moteur de règles, registre NC)

Usage:
  python generate_module05.py --out ./module_05 [--zip]

Produit:
  module_05/
    01_schemas/
      exigence_normative.schema.json
      preuve_conformite.schema.json
      nc.schema.json
      registre_normatif.schema.json
    02_regles/
      exigences_couverture.json
      exigences_menuiseries.json
      mapping_mots_cles.json
    03_scripts/
      check_cctp_vs_normes.py
      check_cr_pv_preuves.py
      nc_register_merge.py
      dashboard_kpis.py
    04_prompts/
      prompt_controle_cctp.md
      prompt_qualification_nc.md
    05_modeles/
      registre_NC_modele.csv
      rapport_conformite_modele.md
      tableau_bord_kpis_modele.md
    06_examples/
      cctp_couverture_exemple.md
      exigences_couverture_exemple.json
      exigences_menuiseries_exemple.json
      registre_exemple.json
      cr_pv_exemple.json
    07_docs/
      README_integration_module05.md
    PACKAGE_SHA256.txt
"""

import argparse
import json
from pathlib import Path
import textwrap
import zipfile
import hashlib
import datetime

TODAY = datetime.date.today().isoformat()

CONTENT = {}

def _d(s: str) -> str:
    return textwrap.dedent(s).lstrip("\n").rstrip() + "\n"

# ------------------------
# 01_schemas
# ------------------------
CONTENT["01_schemas/exigence_normative.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Exigence normative",
  "type": "object",
  "required": ["id","lot","ref_norme","paragraphe","type_controle","critere_acceptation","severite"],
  "properties": {
    "id": {"type":"string", "description":"Identifiant unique de l’exigence"},
    "lot": {"type":"string", "description":"Lot / corps d’état"},
    "objet_ouvrage": {"type":"string"},
    "ref_norme": {"type":"string", "description":"Ex: NF DTU 36.5"},
    "edition": {"type":"string", "description":"Edition/version de la norme"},
    "date_publication": {"type":"string"},
    "paragraphe": {"type":"string", "description":"Article/§ concerné"},
    "intitule": {"type":"string"},
    "type_controle": {"type":"string", "enum":["documentaire","visuel","essai","mesure"]},
    "critere_acceptation": {"type":"string"},
    "severite": {"type":"string", "enum":["mineure","majeure","critique"]},
    "mots_cles": {"type":"array","items":{"type":"string"}},
    "preuves_attendues": {"type":"array","items":{"type":"string"}},
    "applicabilite": {"type":"string", "description":"Condition d’application éventuelle"}
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/preuve_conformite.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Preuve de conformité",
  "type": "object",
  "required": ["id","exigence_id","type","resultat","lien","date"],
  "properties": {
    "id": {"type":"string"},
    "exigence_id": {"type":"string"},
    "type": {"type":"string","enum":["photo","PV","CR","mesure","attestation"]},
    "resultat": {"type":"string","enum":["OK","KO","NA"]},
    "commentaire": {"type":"string"},
    "lien": {"type":"string", "description":"Chemin/URL vers la preuve"},
    "date": {"type":"string"}
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/nc.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Non-conformité (NC)",
  "type": "object",
  "required": ["id","exigence_id","description","gravite","statut"],
  "properties": {
    "id": {"type":"string"},
    "exigence_id": {"type":"string"},
    "description": {"type":"string"},
    "gravite": {"type":"string","enum":["mineure","majeure","critique"]},
    "statut": {"type":"string","enum":["ouvert","clos","en_attente"]},
    "date_ouverture": {"type":"string"},
    "date_cloture": {"type":"string"},
    "action_corrections": {"type":"string"},
    "responsable": {"type":"string"}
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/registre_normatif.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Registre normatif",
  "type": "object",
  "required": ["meta","exigences","preuves","ncs"],
  "properties": {
    "meta": {
      "type":"object",
      "required":["projet","date"],
      "properties":{
        "projet":{"type":"string"},
        "date":{"type":"string"},
        "version":{"type":"string"}
      }
    },
    "exigences":{"type":"array","items":{"$ref":"exigence_normative.schema.json"}},
    "preuves":{"type":"array","items":{"$ref":"preuve_conformite.schema.json"}},
    "ncs":{"type":"array","items":{"$ref":"nc.schema.json"}}
  },
  "additionalProperties": false
}
""")

# ------------------------
# 02_regles (exemples minimalistes)
# ------------------------
CONTENT["02_regles/exigences_couverture.json"] = _d(rf"""
{{
  "meta": {{"lot":"Couverture","ref":"NF DTU 40.xx","edition":"à renseigner","date_generation":"{TODAY}"}},
  "exigences": [
    {{
      "id": "COV-001",
      "lot": "Couverture",
      "objet_ouvrage": "Couverture tuiles",
      "ref_norme": "NF DTU 40.21",
      "edition": "à renseigner",
      "date_publication": "",
      "paragraphe": "Tolérances de pente",
      "intitule": "Respect de la pente minimale selon zone et exposition",
      "type_controle": "documentaire",
      "critere_acceptation": "Pente ≥ seuil tableau DTU correspondant",
      "severite": "majeure",
      "mots_cles": ["pente","zone neige","exposition","DTU 40.21"],
      "preuves_attendues": ["Note de calcul pente","Plan de toiture coté"],
      "applicabilite": ""
    }},
    {{
      "id": "COV-002",
      "lot": "Couverture",
      "objet_ouvrage": "Écrans sous-toiture",
      "ref_norme": "NF DTU 40.29",
      "edition": "à renseigner",
      "date_publication": "",
      "paragraphe": "Mise en œuvre",
      "intitule": "Écran HPV posé selon recouvrements prescrits",
      "type_controle": "visuel",
      "critere_acceptation": "Recouvrement ≥ valeur prescrite en fonction de la pente",
      "severite": "majeure",
      "mots_cles": ["écran","HPV","recouvrement","DTU 40.29"],
      "preuves_attendues": ["Photo recouvrement avec mètre"],
      "applicabilite": ""
    }}
  ]
}}
""")

CONTENT["02_regles/exigences_menuiseries.json"] = _d(rf"""
{{
  "meta": {{"lot":"Menuiseries extérieures","ref":"NF DTU 36.5","edition":"à renseigner","date_generation":"{TODAY}"}},
  "exigences": [
    {{
      "id": "MEN-001",
      "lot": "Menuiseries extérieures",
      "objet_ouvrage": "Fenêtres PVC",
      "ref_norme": "NF DTU 36.5",
      "edition": "à renseigner",
      "date_publication": "",
      "paragraphe": "Calfeutrement",
      "intitule": "Calfeutrement adapté à la classe d’exposition",
      "type_controle": "documentaire",
      "critere_acceptation": "Système de calfeutrement compatible support/ouvrant et classe d’exposition",
      "severite": "majeure",
      "mots_cles": ["calfeutrement","mousse imprégnée","fond de joint","DTU 36.5"],
      "preuves_attendues": ["Fiche produit","Détail coupe calfeutrement"],
      "applicabilite": ""
    }},
    {{
      "id": "MEN-002",
      "lot": "Menuiseries extérieures",
      "objet_ouvrage": "Pose en applique",
      "ref_norme": "NF DTU 36.5",
      "edition": "à renseigner",
      "date_publication": "",
      "paragraphe": "Fixations",
      "intitule": "Nombre et entraxe de fixations conformes",
      "type_controle": "visuel",
      "critere_acceptation": "Entraxe et ancrages selon prescriptions du DTU et AT",
      "severite": "majeure",
      "mots_cles": ["fixation","entraxe","cheville","DTU 36.5"],
      "preuves_attendues": ["Photo ancrage","PV réception menuiseries"],
      "applicabilite": ""
    }}
  ]
}}
""")

CONTENT["02_regles/mapping_mots_cles.json"] = _d(r"""
{
  "synonymes": {
    "pente": ["inclinaison","slope"],
    "calfeutrement": ["étanchéité joint","mousse imprégnée","compribande"]
  }
}
""")

# ------------------------
# 03_scripts (docstrings internes en ''' ... ''' pour éviter le conflit)
# ------------------------
CONTENT["03_scripts/check_cctp_vs_normes.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Contrôle documentaire CCTP vs exigences normatives (sans dépendances externes).
Heuristique: recherche de mots-clés des exigences dans le CCTP.
Entrées:
  --cctp <fichier.md>
  --exigences <exigences.json>
Sorties:
  STDOUT: résumé
  --out_json rapport.json
  --out_md rapport.md
'''
import argparse, json
from pathlib import Path
from datetime import datetime

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def check(cctp_text: str, exigences: list) -> list:
    c = cctp_text.lower()
    results = []
    for ex in exigences:
        hits = []
        for kw in ex.get("mots_cles", []):
            if kw and kw.lower() in c:
                hits.append(kw)
        statut = "OK" if hits else "KO"
        results.append({
            "exigence_id": ex.get("id"),
            "ref_norme": ex.get("ref_norme"),
            "severite": ex.get("severite"),
            "intitule": ex.get("intitule"),
            "doc_presence": statut,
            "mots_cles_trouves": hits
        })
    return results

def summarize(results):
    total = len(results)
    oks = sum(1 for r in results if r["doc_presence"]=="OK")
    kos = total - oks
    return {"total":total,"OK":oks,"KO":kos,"taux_ok": round(100*oks/total,1) if total>0 else 0.0}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cctp", required=True)
    ap.add_argument("--exigences", required=True)
    ap.add_argument("--out_json", default=None)
    ap.add_argument("--out_md", default=None)
    args = ap.parse_args()

    cctp_text = load_text(Path(args.cctp))
    ex_obj = load_json(Path(args.exigences))
    exigences = ex_obj.get("exigences", ex_obj if isinstance(ex_obj, list) else [])
    results = check(cctp_text, exigences)
    synth = summarize(results)
    print(f"[CCTP] Exigences: {synth['total']} | OK: {synth['OK']} | KO: {synth['KO']} | Taux OK: {synth['taux_ok']}%")

    if args.out_json:
        Path(args.out_json).write_text(
            json.dumps({"meta":{"date":datetime.utcnow().isoformat()+"Z"}, "resultats":results, "synthese":synth}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
    if args.out_md:
        lines = ["# Rapport contrôle CCTP vs Normes", ""]
        lines.append(f"- Date: {datetime.utcnow().isoformat()}Z")
        lines.append(f"- Exigences: {synth['total']} | OK: {synth['OK']} | KO: {synth['KO']} | Taux OK: {synth['taux_ok']}%")
        lines.append("\n## Détail")
        for r in results:
            mc = ", ".join(r['mots_cles_trouves']) if r['mots_cles_trouves'] else "—"
            lines.append(f"- {r['exigence_id']} ({r['ref_norme']}) — {r['intitule']}: {r['doc_presence']} | mots-clés: {mc}")
        Path(args.out_md).write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/check_cr_pv_preuves.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Contrôle de présence de preuves pour exigences à sévérité 'majeure'.
Entrées:
  --registre <registre.json>
Sortie:
  STDOUT + JSON optionnel
'''
import argparse, json
from pathlib import Path
from datetime import datetime

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", required=True)
    ap.add_argument("--out_json", default=None)
    args = ap.parse_args()

    reg = load_json(Path(args.registre))
    exigs = reg.get("exigences", [])
    preuves = reg.get("preuves", [])
    preuves_by_ex = {}
    for p in preuves:
        preuves_by_ex.setdefault(p.get("exigence_id"), []).append(p)
    manquantes = []
    majeures = [e for e in exigs if e.get("severite") == "majeure"]
    for e in majeures:
        if len(preuves_by_ex.get(e.get("id"), [])) == 0:
            manquantes.append(e.get("id"))
    print(f"[PREUVES] Exigences majeures: {len(majeures)} | Avec preuves: {len([eid for eid in preuves_by_ex if eid in [x.get('id') for x in majeures]])} | Manquantes: {len(manquantes)}")
    if manquantes:
        print("Manquantes:", ", ".join(manquantes))
    if args.out_json:
        Path(args.out_json).write_text(
            json.dumps({"date":datetime.utcnow().isoformat()+"Z","exigences_majeures_sans_preuve":manquantes}, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/nc_register_merge.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Fusion de fichiers NC JSON en un registre consolidé.
Entrées:
  --inputs f1.json f2.json ...
  --out registre_nc_merged.json
'''
import argparse, json, uuid
from pathlib import Path
from datetime import datetime

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    merged = []
    for f in args.inputs:
        obj = load_json(Path(f))
        if isinstance(obj, list):
            merged.extend(obj)
        elif isinstance(obj, dict) and "ncs" in obj:
            merged.extend(obj["ncs"])
        else:
            merged.append(obj)
    # dédoublonnage simple par (exigence_id, description)
    seen = set()
    uniq = []
    for nc in merged:
        key = (nc.get("exigence_id"), (nc.get("description") or "").strip())
        if key not in seen:
            seen.add(key)
            if "id" not in nc or not nc["id"]:
                nc["id"] = "NC-" + uuid.uuid4().hex[:8]
            uniq.append(nc)
    out = {"meta":{"date":datetime.utcnow().isoformat()+"Z","nb_nc":len(uniq)},"ncs":uniq}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[MERGE] NC uniques: {len(uniq)} → {args.out}")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/dashboard_kpis.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
KPIs de conformité sur registre_normatif.json
Entrées:
  --registre registre_normatif.json
'''
import argparse, json
from pathlib import Path

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", required=True)
    args = ap.parse_args()

    reg = load_json(Path(args.registre))
    exigs = reg.get("exigences", [])
    preuves = reg.get("preuves", [])
    ncs = reg.get("ncs", [])

    ok_ids = {p.get("exigence_id") for p in preuves if p.get("resultat")=="OK"}
    applicables = [e for e in exigs]
    taux = round(100*len([e for e in applicables if e.get("id") in ok_ids])/len(applicables),1) if applicables else 0.0

    ncs_ouvertes = [n for n in ncs if n.get("statut")=="ouvert"]
    ncs_majeures_ouvertes = [n for n in ncs_ouvertes if n.get("gravite")=="majeure"]

    print("=== KPIs conformité ===")
    print(f"- Exigences applicables: {len(applicables)}")
    print(f"- Exigences avec ≥1 preuve OK: {len(ok_ids)}")
    print(f"- Taux de conformité (approx.): {taux}%")
    print(f"- NC ouvertes: {len(ncs_ouvertes)}")
    print(f"- NC majeures ouvertes: {len(ncs_majeures_ouvertes)}")

if __name__ == "__main__":
    main()
""")

# ------------------------
# 04_prompts
# ------------------------
CONTENT["04_prompts/prompt_controle_cctp.md"] = _d(rf"""
# Prompt — Contrôle CCTP vs Normes (Module 05)

Objectif: vérifier la présence explicite des exigences normatives clés dans le CCTP.

Contexte:
- Projet: {{PROJET}}
- Date: {TODAY}
- Lot: {{LOT}}

Tâche:
1) Parcourir le CCTP fourni et relever les clauses qui couvrent les exigences listées.
2) Identifier les manques et proposer des formulations contractuelles adaptées (sans citer textuellement les normes).
3) Classer les écarts par sévérité (mineure/majeure/critique).

Livrable attendu:
- Tableau des exigences: Couverture OK/KO, références internes CCTP, proposition de texte si KO.
""")

CONTENT["04_prompts/prompt_qualification_nc.md"] = _d(r"""
# Prompt — Qualification des Non-Conformités (NC)

Objectif: qualifier chaque NC avec gravité, cause probable, action corrective, responsable et délai cible.

Étapes:
1) Lire la description de la NC et l’exigence associée.
2) Évaluer la gravité (mineure/majeure/critique) et le risque résiduel.
3) Proposer une action corrective, un responsable et une date de clôture cible.
4) Mettre à jour le registre NC.
""")

# ------------------------
# 05_modeles
# ------------------------
CONTENT["05_modeles/registre_NC_modele.csv"] = _d(r"""
id;exigence_id;description;gravite;statut;date_ouverture;date_cloture;action_corrections;responsable
NC-XXXXXXX;MEN-001;Calfeutrement non conforme;majeure;ouvert;2025-01-10;;Refaire calfeutrement;Entreprise MEN
""")

CONTENT["05_modeles/rapport_conformite_modele.md"] = _d(r"""
# Rapport de conformité — Modèle

- Projet: <à renseigner>
- Date: <auto>
- Périmètre: <lots>

## Synthèse
- Exigences: <N> | OK: <N> | KO: <N> | Taux: <X>%

## Détail par exigence
- <ID> (<REF>) — <Intitulé> : OK/KO — Preuves: <liens>
""")

CONTENT["05_modeles/tableau_bord_kpis_modele.md"] = _d(r"""
# Tableau de bord KPIs — Modèle

- Taux de conformité global
- NC ouvertes / majeures ouvertes
- Délai moyen de clôture
- Couverture des preuves (exigences majeures)
""")

# ------------------------
# 06_examples
# ------------------------
CONTENT["06_examples/cctp_couverture_exemple.md"] = _d(r"""
# CCTP — Extrait Couverture (exemple)

La pente de toiture sera conforme aux prescriptions applicables selon la zone de neige et l’exposition.
Un écran sous-toiture de type HPV sera mis en œuvre, avec recouvrements conformes au guide de pose.
""")

CONTENT["06_examples/exigences_couverture_exemple.json"] = _d(rf"""
{{
  "exigences": [
    {{
      "id": "COV-001",
      "lot": "Couverture",
      "objet_ouvrage": "Couverture tuiles",
      "ref_norme": "NF DTU 40.21",
      "edition": "à renseigner",
      "paragraphe": "Tolérances de pente",
      "intitule": "Respect de la pente minimale selon zone et exposition",
      "type_controle": "documentaire",
      "critere_acceptation": "Pente ≥ seuil tableau DTU correspondant",
      "severite": "majeure",
      "mots_cles": ["pente","zone neige","exposition","DTU 40.21"]
    }}
  ]
}}
""")

CONTENT["06_examples/exigences_menuiseries_exemple.json"] = _d(r"""
{
  "exigences": [
    {
      "id": "MEN-001",
      "lot": "Menuiseries extérieures",
      "objet_ouvrage": "Fenêtres PVC",
      "ref_norme": "NF DTU 36.5",
      "edition": "à renseigner",
      "paragraphe": "Calfeutrement",
      "intitule": "Calfeutrement adapté à la classe d’exposition",
      "type_controle": "documentaire",
      "critere_acceptation": "Système compatible classe d’exposition",
      "severite": "majeure",
      "mots_cles": ["calfeutrement","mousse imprégnée","fond de joint","DTU 36.5"]
    }
  ]
}
""")

CONTENT["06_examples/registre_exemple.json"] = _d(rf"""
{{
  "meta": {{"projet":"Opération Démo","date":"{TODAY}","version":"0.1"}},
  "exigences": [
    {{"id":"MEN-001","lot":"Menuiseries extérieures","ref_norme":"NF DTU 36.5","paragraphe":"Calfeutrement","intitule":"Calfeutrement adapté","severite":"majeure"}},
    {{"id":"COV-001","lot":"Couverture","ref_norme":"NF DTU 40.21","paragraphe":"Pente","intitule":"Pente minimale","severite":"majeure"}}
  ],
  "preuves": [
    {{"id":"PR-1","exigence_id":"MEN-001","type":"photo","resultat":"OK","lien":"./photos/men-001.jpg","date":"{TODAY}"}}
  ],
  "ncs": [
    {{"id":"NC-AB12CD34","exigence_id":"COV-001","description":"Pente constatée insuffisante","gravite":"majeure","statut":"ouvert","date_ouverture":"{TODAY}"}}
  ]
}}
""")

CONTENT["06_examples/cr_pv_exemple.json"] = _d(rf"""
{{
  "cr": [
    {{"date":"{TODAY}","objet":"Réunion de calage menuiseries","points":["Choix calfeutrement","Plan de pose"]}}
  ],
  "pv": [
    {{"date":"{TODAY}","essai":"Échantillon calfeutrement","resultat":"conforme"}}
  ]
}}
""")

# ------------------------
# 07_docs
# ------------------------
CONTENT["07_docs/README_integration_module05.md"] = _d(rf"""
# Module 05 — Conformité normative et technique

Généré le {TODAY}. Ce module fournit:
- Schémas JSON pour exigences, preuves, NC, registre
- Règles d’exemple (couverture, menuiseries)
- Scripts de contrôle et KPIs
- Prompts, modèles, exemples

Installation
- Python 3.8+
- Génération: `python generate_module05.py --out ./module_05 --zip`

Utilisation rapide
1) Contrôle CCTP:
   python ./module_05/03_scripts/check_cctp_vs_normes.py --cctp ./module_05/06_examples/cctp_couverture_exemple.md --exigences ./module_05/02_regles/exigences_couverture.json --out_md ./rapport.md
2) Vérif. preuves majeures:
   python ./module_05/03_scripts/check_cr_pv_preuves.py --registre ./module_05/06_examples/registre_exemple.json --out_json ./preuves.json
3) Merge NC:
   python ./module_05/03_scripts/nc_register_merge.py --inputs ./module_05/06_examples/registre_exemple.json --out ./merged_nc.json
4) KPIs:
   python ./module_05/03_scripts/dashboard_kpis.py --registre ./module_05/06_examples/registre_exemple.json

Notes
- Remplir les champs "edition" des normes avec la véritable édition en vigueur sur votre projet.
- Les contrôles fournis sont heuristiques pour démonstration; adaptez-les à votre contexte.
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
    parser = argparse.ArgumentParser(description="Générer les livrables du Module 05.")
    parser.add_argument("--out", required=True, help="Dossier de sortie (ex: ./module_05)")
    parser.add_argument("--zip", action="store_true", help="Créer aussi une archive .zip")
    args = parser.parse_args()

    base = Path(args.out)
    for rel, txt in CONTENT.items():
        write_file(base, rel, txt)

    digest = sha256_of_tree(base)
    with open(base / "PACKAGE_SHA256.txt", "w", encoding="utf-8") as f:
        f.write(digest + "\n")

    print(f"[OK] Livrables Module 05 écrits dans: {base.resolve()}")
    print(f"[INFO] SHA-256 du package (contenu): {digest}")

    if args.zip:
        zip_path = base.with_suffix(".zip")
        make_zip(base, zip_path)
        print(f"[OK] Archive créée: {zip_path.resolve()}")

if __name__ == "__main__":
    main()


