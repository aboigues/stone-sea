#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de livrables — Module 06 : Plan d’essais, contrôles et PV chantier
Périmètre: structuration du plan de contrôle, suivi des essais, rapprochement des PV, tableau de bord.

Usage:
  python generate_module06.py --out ./module_06 [--zip]

Produit:
  module_06/
    01_schemas/
      plan_controle.schema.json
      essai.schema.json
      pv.schema.json
      echantillonnage.schema.json
    02_regles/
      controles_beton.json
      controles_chapes.json
      mapping_unites.json
    03_scripts/
      planificateur_essais.py
      validate_pv_vs_exigences.py
      echantillonnage_calcul.py
      kpi_essais.py
    04_prompts/
      prompt_generation_plan_controle.md
      prompt_analyse_pv.md
    05_modeles/
      plan_controle_modele.json
      pv_register_modele.json
      rapport_controle_modele.md
    06_examples/
      plan_controle_exemple.json
      pv_exemples.json
      mesures_exemple.json
    07_docs/
      README_integration_module06.md
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
CONTENT["01_schemas/plan_controle.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Plan de contrôle chantier",
  "type": "object",
  "required": ["meta","lots","essais"],
  "properties": {
    "meta": {
      "type":"object",
      "required":["projet","version","date"],
      "properties":{
        "projet":{"type":"string"},
        "version":{"type":"string"},
        "date":{"type":"string"}
      }
    },
    "lots": {
      "type":"array",
      "items":{"type":"string"},
      "description":"Liste des lots/corps d’état concernés"
    },
    "essais": {
      "type":"array",
      "items":{"$ref":"essai.schema.json"}
    }
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/essai.schema.json"] = _d(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Essai/Contrôle",
  "type": "object",
  "required": ["id","lot","intitule","reference","type","frequence","critere_acceptation"],
  "properties": {
    "id":{"type":"string"},
    "lot":{"type":"string"},
    "intitule":{"type":"string"},
    "reference":{"type":"string","description":"Ex: NF EN / NF DTU / AT / Spéc. projet"},
    "type":{"type":"string","enum":["essai","mesure","controle_visuel","documentaire"]},
    "frequence":{"type":"string","description":"Ex: 1/50 m2, 1 par lot, N prélèvements/sem."},
    "critere_acceptation":{"type":"string"},
    "unite":{"type":"string"},
    "cible":{"type":["number","string"]},
    "tol_minus":{"type":["number","string"]},
    "tol_plus":{"type":["number","string"]},
    "echantillonnage":{"$ref":"echantillonnage.schema.json"},
    "evidences_attendues":{"type":"array","items":{"type":"string"}}
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/pv.schema.json"] = _d(r"""
{
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "title":"Procès-verbal (PV) / Mesure",
  "type":"object",
  "required":["id","essai_id","date","type","valeurs","conformite"],
  "properties":{
    "id":{"type":"string"},
    "essai_id":{"type":"string"},
    "date":{"type":"string"},
    "ouvrage":{"type":"string"},
    "zone":{"type":"string"},
    "type":{"type":"string","enum":["essai","mesure","controle_visuel","documentaire"]},
    "valeurs":{"type":"object","additionalProperties": {"type":["number","string"]}},
    "unite":{"type":"string"},
    "conformite":{"type":"string","enum":["OK","KO","NA"]},
    "commentaire":{"type":"string"},
    "fichier":{"type":"string","description":"chemin/URL vers le PV signé ou photo"}
  },
  "additionalProperties": false
}
""")

CONTENT["01_schemas/echantillonnage.schema.json"] = _d(r"""
{
  "$schema":"https://json-schema.org/draft/2020-12/schema",
  "title":"Règle d’échantillonnage",
  "type":"object",
  "required":["mode","parametres"],
  "properties":{
    "mode":{"type":"string","enum":["fixe","pourcentage","surface","unites_ouvrage"]},
    "parametres":{
      "type":"object",
      "additionalProperties": {"type":["number","string"]},
      "description":"Ex: {\"nb\":3} ou {\"pct\":10} ou {\"surface\":50}"
    }
  },
  "additionalProperties": false
}
""")

# ------------------------
# 02_regles — Exemples (adapter avec vos éditions de normes)
# ------------------------
CONTENT["02_regles/controles_beton.json"] = _d(rf"""
{{
  "meta": {{"lot":"Gros-œuvre (béton)","ref":"NF EN 206/CN + Spéc. projet","date_generation":"{TODAY}"}},
  "essais": [
    {{
      "id":"BET-RESIST",
      "lot":"Gros-œuvre",
      "intitule":"Résistance à la compression (éprouvettes)",
      "reference":"NF EN 206/CN (fréquence selon classe d'exposition et volume)",
      "type":"essai",
      "frequence":"selon volume béton (typ. 1 série/150 m3)",
      "critere_acceptation":"fck, écrasement ≥ valeur cible",
      "unite":"MPa",
      "cible":"selon note de calcul",
      "tol_minus":"-",
      "tol_plus":"-",
      "echantillonnage":{{"mode":"unites_ouvrage","parametres":{{"par_volume_m3":150}}}},
      "evidences_attendues":["PV laboratoire","Fiches béton (DOD)"]
    }},
    {{
      "id":"BET-SLUMP",
      "lot":"Gros-œuvre",
      "intitule":"Affaissement (consistance) à la livraison",
      "reference":"NF EN 12350-2 (contrôle réception)",
      "type":"mesure",
      "frequence":"1 par camion ou selon plan de contrôle",
      "critere_acceptation":"Classe d'affaissement conforme à la commande",
      "unite":"mm",
      "cible":"classe Sx",
      "echantillonnage":{{"mode":"fixe","parametres":{{"nb":1}}}},
      "evidences_attendues":["PV réception","Photo cône d'Abrams"]
    }}
  ]
}}
""")

CONTENT["02_regles/controles_chapes.json"] = _d(rf"""
{{
  "meta": {{"lot":"Chapes (référence DTU)","ref":"NF DTU 26.2 (à vérifier selon édition)","date_generation":"{TODAY}"}},
  "essais": [
    {{
      "id":"CHA-PLAN",
      "lot":"Chapes",
      "intitule":"Planéité chapes",
      "reference":"NF DTU 26.2 — tolérances de surface",
      "type":"mesure",
      "frequence":"1 mesure/20 m² min.",
      "critere_acceptation":"écarts sous règle de 2 m ≤ tolérance",
      "unite":"mm",
      "cible":"≤ tolérance DTU",
      "echantillonnage":{{"mode":"surface","parametres":{{"surface":20}}}},
      "evidences_attendues":["PV planéité","Photos règle 2 m + cale"]
    }},
    {{
      "id":"CHA-HUM",
      "lot":"Chapes",
      "intitule":"Humidité résiduelle avant revêtement",
      "reference":"NF DTU 26.2 / Avis fabricant revêtement",
      "type":"mesure",
      "frequence":"1 mesure/50 m²",
      "critere_acceptation":"Teneur en humidité compatible revêtement",
      "unite":"% CM",
      "cible":"≤ seuil compatible",
      "echantillonnage":{{"mode":"surface","parametres":{{"surface":50}}}},
      "evidences_attendues":["PV humidité","Trace mesure"]
    }}
  ]
}}
""")

CONTENT["02_regles/mapping_unites.json"] = _d(r"""
{
  "unites_equivalences": {
    "MPa": ["N/mm2"],
    "mm": ["millimetre","millimètre"]
  }
}
""")

# ------------------------
# 03_scripts — docstrings en '''...''' pour éviter conflit de guillemets
# ------------------------
CONTENT["03_scripts/planificateur_essais.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Planifie les essais à partir d'un plan de contrôle et d'un quantitatif.
Entrées:
  --plan plan_controle.json
  --quantites mesures_exemple.json
  --out planning.json
'''
import argparse, json, math
from pathlib import Path
from datetime import datetime

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def compute_nb_samples(rule: dict, quantites: dict) -> int:
    ech = rule.get("echantillonnage", {}) or {}
    mode = ech.get("mode")
    params = (ech.get("parametres") or {})
    if mode == "fixe":
        return int(params.get("nb", 0))
    if mode == "pourcentage":
        pct = float(params.get("pct", 0))
        base = float(quantites.get("base", 0))
        return max(1, math.ceil(base * pct / 100.0)) if base > 0 else 0
    if mode == "surface":
        pas = float(params.get("surface", 0))
        s = float(quantites.get("surface_m2", 0))
        return max(1, math.ceil(s / pas)) if pas > 0 else 0
    if mode == "unites_ouvrage":
        par_vol = float(params.get("par_volume_m3", 0))
        v = float(quantites.get("volume_beton_m3", 0))
        return max(1, math.ceil(v / par_vol)) if par_vol > 0 else 0
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--quantites", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.plan))
    quants = jload(Path(args.quantites))
    essais = plan.get("essais", [])
    planning = []
    for e in essais:
        n = compute_nb_samples(e, quants)
        planning.append({
            "essai_id": e.get("id"),
            "intitule": e.get("intitule"),
            "lot": e.get("lot"),
            "a_realiser": n,
            "frequence": e.get("frequence"),
            "reference": e.get("reference")
        })
    out = {"meta":{"date":datetime.utcnow().isoformat()+"Z","projet":plan.get("meta",{}).get("projet")}, "planning":planning}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[PLANIF] Essais: {len(essais)} | Tâches générées: {len(planning)} → {args.out}")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/validate_pv_vs_exigences.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Valide les PV/mesures par rapport aux critères du plan de contrôle.
Entrées:
  --plan plan_controle.json
  --pv pv_exemples.json
  --out pv_valides.json
'''
import argparse, json
from pathlib import Path
from statistics import mean

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def is_ok(value, cible, tol_minus=None, tol_plus=None):
    try:
        v = float(value)
        if cible in (None,"","-"):
            return True
        c = float(cible) if isinstance(cible,(int,float,str)) and str(cible).replace(',','.').replace(' ','').replace('+','').replace('-','').isdigit() else None
        if c is None:
            return True
        tmin = float(tol_minus) if tol_minus not in (None,"","-") else 0.0
        tplus = float(tol_plus) if tol_plus not in (None,"","-") else 0.0
        return (c - abs(tmin)) <= v <= (c + abs(tplus))
    except Exception:
        return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--pv", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.plan))
    pv = jload(Path(args.pv))
    rules = {e.get("id"): e for e in plan.get("essais", [])}
    results = []
    for item in pv.get("pv", []):
        essai_id = item.get("essai_id")
        rule = rules.get(essai_id, {})
        cible = rule.get("cible")
        ok = True
        if isinstance(item.get("valeurs"), dict) and "mesure" in item["valeurs"]:
            ok = is_ok(item["valeurs"]["mesure"], cible, rule.get("tol_minus"), rule.get("tol_plus"))
        results.append({
            "pv_id": item.get("id"),
            "essai_id": essai_id,
            "intitule": rule.get("intitule"),
            "reference": rule.get("reference"),
            "unite": item.get("unite", rule.get("unite")),
            "valeurs": item.get("valeurs"),
            "conformite_calculee": "OK" if ok else "KO",
            "conformite_declares": item.get("conformite")
        })
    Path(args.out).write_text(json.dumps({"results":results}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[VALID] PV traités: {len(results)} → {args.out}")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/echantillonnage_calcul.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Calcule un échantillonnage pour un essai donné.
Entrées:
  --essai_id BET-RESIST (ou autre)
  --plan plan_controle.json
  --quantites mesures_exemple.json
'''
import argparse, json, math
from pathlib import Path

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def calc(rule: dict, quants: dict) -> int:
    ech = rule.get("echantillonnage", {}) or {}
    mode = ech.get("mode")
    p = ech.get("parametres") or {}
    if mode == "fixe": return int(p.get("nb",0))
    if mode == "pourcentage":
        base = float(quants.get("base",0)); pct = float(p.get("pct",0))
        return max(1, math.ceil(base*pct/100)) if base>0 else 0
    if mode == "surface":
        s = float(quants.get("surface_m2",0)); pas=float(p.get("surface",0))
        return max(1, math.ceil(s/pas)) if pas>0 else 0
    if mode == "unites_ouvrage":
        v = float(quants.get("volume_beton_m3",0)); par=float(p.get("par_volume_m3",0))
        return max(1, math.ceil(v/par)) if par>0 else 0
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--essai_id", required=True)
    ap.add_argument("--plan", required=True)
    ap.add_argument("--quantites", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.plan))
    quants = jload(Path(args.quantites))
    d = {e.get("id"):e for e in plan.get("essais",[])}
    rule = d.get(args.essai_id)
    if not rule:
        print("[ERR] Essai introuvable"); return
    n = calc(rule, quants)
    print(f"[ECHANT] {args.essai_id} → {n} prélèvements/mesures")

if __name__ == "__main__":
    main()
""")

CONTENT["03_scripts/kpi_essais.py"] = _d(r"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
KPIs de réalisation et de conformité des essais.
Entrées:
  --planning planning.json
  --pv pv_exemples.json
'''
import argparse, json
from pathlib import Path

def jload(p: Path): return json.loads(p.read_text(encoding="utf-8"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--planning", required=True)
    ap.add_argument("--pv", required=True)
    args = ap.parse_args()

    plan = jload(Path(args.planning))
    pv = jload(Path(args.pv))
    a_faire = {t["essai_id"]: t["a_realiser"] for t in plan.get("planning", [])}
    faits_par_essai = {}
    oks = 0; kos = 0
    for item in pv.get("pv", []):
        eid = item.get("essai_id")
        faits_par_essai[eid] = faits_par_essai.get(eid, 0) + 1
        if item.get("conformite") == "OK": oks += 1
        elif item.get("conformite") == "KO": kos += 1
    couverture = {eid: f"{min(faits_par_essai.get(eid,0), a_faire.get(eid,0))}/{a_faire.get(eid,0)}" for eid in a_faire}
    print("=== KPIs Essais ===")
    print(f"- Essais planifiés: {len(a_faire)}")
    print(f"- PV: OK={oks} | KO={kos}")
    print("- Couverture par essai:")
    for eid, val in couverture.items():
        print(f"  · {eid}: {val}")

if __name__ == "__main__":
    main()
""")

# ------------------------
# 04_prompts
# ------------------------
CONTENT["04_prompts/prompt_generation_plan_controle.md"] = _d(rf"""
# Prompt — Génération d’un plan de contrôle (Module 06)

Objectif: produire une liste d’essais/mesures pour chaque lot à partir des exigences projet.
Contrainte: ne pas citer textuellement les normes; résumer les exigences et indiquer la logique de fréquence.

Contexte:
- Projet: {{PROJET}}
- Date: {TODAY}
- Lots: {{LOTS}}

Livrable:
- JSON conforme à plan_controle.schema.json (fréquence, critère d’acceptation, unité, échantillonnage).
""")

CONTENT["04_prompts/prompt_analyse_pv.md"] = _d(r"""
# Prompt — Analyse des PV et mesures

Objectif: qualifier la conformité des PV/mesures par rapport aux critères du plan de contrôle, détecter les écarts et proposer des actions.
Étapes:
1) Faire correspondre PV ↔ essai du plan.
2) Évaluer la conformité (OK/KO/NA) et l’incertitude éventuelle.
3) Lister les compléments à demander (photos, signature, étalonnage).
""")

# ------------------------
# 05_modeles
# ------------------------
CONTENT["05_modeles/plan_controle_modele.json"] = _d(rf"""
{{
  "meta": {{"projet":"<à renseigner>","version":"0.1","date":"{TODAY}"}},
  "lots": ["Gros-œuvre","Chapes"],
  "essais": []
}}
""")

CONTENT["05_modeles/pv_register_modele.json"] = _d(r"""
{
  "pv": [
    {
      "id":"PV-XXXX",
      "essai_id":"<ID essai>",
      "date":"<YYYY-MM-DD>",
      "ouvrage":"<Zone>",
      "zone":"<Repère>",
      "type":"mesure",
      "valeurs":{"mesure":0},
      "unite":"<unit>",
      "conformite":"NA",
      "commentaire":"",
      "fichier":"./pv/..."
    }
  ]
}
""")

CONTENT["05_modeles/rapport_controle_modele.md"] = _d(r"""
# Rapport — Plan d’essais et PV

- Projet: <nom>
- Périmètre: <lots>
- Synthèse couverture: <%>
- Points KO: <liste>
""")

# ------------------------
# 06_examples
# ------------------------
CONTENT["06_examples/plan_controle_exemple.json"] = _d(rf"""
{{
  "meta": {{"projet":"Opération Démo","version":"0.1","date":"{TODAY}"}},
  "lots": ["Gros-œuvre","Chapes"],
  "essais": [
    {{
      "id":"BET-RESIST","lot":"Gros-œuvre","intitule":"Résistance béton","reference":"NF EN 206/CN",
      "type":"essai","frequence":"1 série/150 m3","critere_acceptation":"fck conforme",
      "unite":"MPa","cible":"30","tol_minus":"-","tol_plus":"-",
      "echantillonnage":{{"mode":"unites_ouvrage","parametres":{{"par_volume_m3":150}}}},
      "evidences_attendues":["PV labo","DOD"]
    }},
    {{
      "id":"CHA-PLAN","lot":"Chapes","intitule":"Planéité chapes","reference":"NF DTU 26.2",
      "type":"mesure","frequence":"1/20 m²","critere_acceptation":"écart ≤ tolérance",
      "unite":"mm","cible":"-",
      "echantillonnage":{{"mode":"surface","parametres":{{"surface":20}}}},
      "evidences_attendues":["PV planéité","Photo règle 2 m"]
    }}
  ]
}}
""")

CONTENT["06_examples/pv_exemples.json"] = _d(rf"""
{{
  "pv": [
    {{"id":"PV-BET-001","essai_id":"BET-RESIST","date":"{TODAY}","ouvrage":"Voile V1","zone":"Niv. R+1",
      "type":"essai","valeurs":{{"mesure":31.2}},"unite":"MPa","conformite":"OK","commentaire":"—","fichier":"./pv/31d_V1.pdf"}},
    {{"id":"PV-CHA-001","essai_id":"CHA-PLAN","date":"{TODAY}","ouvrage":"Plateau Bureau","zone":"Zone A",
      "type":"mesure","valeurs":{{"mesure":4}},"unite":"mm","conformite":"OK","commentaire":"—","fichier":"./pv/planeite_A.pdf"}}
  ]
}}
""")

CONTENT["06_examples/mesures_exemple.json"] = _d(r"""
{
  "base": 100,
  "surface_m2": 820,
  "volume_beton_m3": 460
}
""")

# ------------------------
# 07_docs
# ------------------------
CONTENT["07_docs/README_integration_module06.md"] = _d(rf"""
# Module 06 — Plan d’essais, contrôles et PV chantier

Généré le {TODAY}.
Contenu:
- Schémas JSON (plan, essai, PV, échantillonnage)
- Règles d’exemple (béton, chapes)
- Scripts: planification, validation PV, calcul échantillonnage, KPIs
- Prompts, modèles, exemples

Démarrage rapide
1) Générer le module:
   python generate_module06.py --out ./module_06 --zip
2) Calcul du planning:
   python ./module_06/03_scripts/planificateur_essais.py --plan ./module_06/06_examples/plan_controle_exemple.json --quantites ./module_06/06_examples/mesures_exemple.json --out ./module_06/planning.json
3) Validation PV ↔ critères:
   python ./module_06/03_scripts/validate_pv_vs_exigences.py --plan ./module_06/06_examples/plan_controle_exemple.json --pv ./module_06/06_examples/pv_exemples.json --out ./module_06/pv_valides.json
4) KPIs:
   python ./module_06/03_scripts/kpi_essais.py --planning ./module_06/planning.json --pv ./module_06/06_examples/pv_exemples.json

Notes
- Adaptez les références normatives à l’édition applicable (ex: NF DTU 26.2 pour chapes).
- Les scripts fournissent une base opérationnelle à compléter (étalonnage appareils, incertitudes, seuils projet, etc.).
""")

# ------------------------
# Génération / ZIP / Hash
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
    parser = argparse.ArgumentParser(description="Générer les livrables du Module 06.")
    parser.add_argument("--out", required=True, help="Dossier de sortie (ex: ./module_06)")
    parser.add_argument("--zip", action="store_true", help="Créer aussi une archive .zip")
    args = parser.parse_args()

    base = Path(args.out)
    for rel, txt in CONTENT.items():
        write_file(base, rel, txt)

    digest = sha256_of_tree(base)
    with open(base / "PACKAGE_SHA256.txt", "w", encoding="utf-8") as f:
        f.write(digest + "\n")

    print(f"[OK] Livrables Module 06 écrits dans: {base.resolve()}")
    print(f"[INFO] SHA-256 du package (contenu): {digest}")

    if args.zip:
        zip_path = base.with_suffix(".zip")
        make_zip(base, zip_path)
        print(f"[OK] Archive créée: {zip_path.resolve()}")

if __name__ == "__main__":
    main()

