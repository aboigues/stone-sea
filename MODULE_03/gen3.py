#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de livrables — Module 03 : Contrôle de conformité normative et AQ (BTP)

Usage:
  python generate_module03.py --out ./module_03 [--zip]

Sorties (arborescence):
  module_03/
    01_schema/
      evidence_schema.json
    02_prompts/
      prompt_verificateur_normatif.md
    03_scripts/
      validate_evidence.py
    04_tests/
      jeu_or_minimal.csv
    05_modeles/
      rapport_AQ_modele.md
      checklist_revue_AQ.md
      matrice_risques.md
    06_docs/
      README_integration_pipeline.md
      references_normatives_exemples.md
"""

import argparse
import json
import os
from pathlib import Path
import textwrap
import zipfile
import hashlib

CONTENT = {}

def _dedent(s: str) -> str:
    return textwrap.dedent(s).lstrip("\n").rstrip() + "\n"

# 1) Schéma JSON d’évidence
CONTENT["01_schema/evidence_schema.json"] = _dedent(r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Evidence de conformité BTP",
  "type": "object",
  "required": ["meta", "references", "constats", "synthese"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["chantier", "lot", "document_source", "modele_ia", "version_prompts"],
      "properties": {
        "chantier": {"type": "string"},
        "lot": {"type": "string"},
        "document_source": {"type": "array", "items": {"type": "string"}},
        "modele_ia": {"type": "string"},
        "version_prompts": {"type": "string"},
        "horodatage_utc": {"type": "string"},
        "hash_entrees": {
          "type": "object",
          "additionalProperties": {"type": "string"}
        }
      },
      "additionalProperties": true
    },
    "references": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["famille", "numero", "couverture"],
        "properties": {
          "famille": {"type": "string", "enum": ["NF DTU", "Eurocode", "CCTP", "Guide interne", "Autre"]},
          "numero": {"type": "string"},
          "edition": {"type": "string"},
          "articles": {"type": "array", "items": {"type": "string"}},
          "couverture": {"type": "string", "enum": ["totale", "partielle", "hors_perimetre"]}
        },
        "additionalProperties": false
      }
    },
    "constats": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "objet", "exigence", "conforme"],
        "properties": {
          "id": {"type": "string"},
          "objet": {"type": "string"},
          "exigence": {"type": "string"},
          "valeur_requise": {"type": ["string", "number", "null"]},
          "valeur_constatee": {"type": ["string", "number", "null"]},
          "unite": {"type": ["string", "null"]},
          "conforme": {"type": "boolean"},
          "gravite": {"type": "string", "enum": ["mineure", "significative", "majeure"]},
          "preuve": {
            "type": "object",
            "properties": {
              "extrait": {"type": "string"},
              "page_plan": {"type": "string"},
              "coordonnees": {
                "type": "object",
                "properties": {
                  "x": {"type": "number"},
                  "y": {"type": "number"},
                  "w": {"type": "number"},
                  "h": {"type": "number"}
                },
                "additionalProperties": false
              },
              "captures": {"type": "array", "items": {"type": "string"}}
            },
            "additionalProperties": true
          },
          "citations_sources": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["source"],
              "properties": {
                "source": {"type": "string"},
                "citation": {"type": "string"}
              },
              "additionalProperties": false
            }
          },
          "recommandation": {"type": "string"}
        },
        "additionalProperties": false
      }
    },
    "synthese": {
      "type": "object",
      "required": ["non_conformites_majeures", "non_conformites_mineures", "points_attention", "risque_global", "decision"],
      "properties": {
        "non_conformites_majeures": {"type": "integer", "minimum": 0},
        "non_conformites_mineures": {"type": "integer", "minimum": 0},
        "points_attention": {"type": "integer", "minimum": 0},
        "risque_global": {"type": "string", "enum": ["faible", "modéré", "élevé"]},
        "decision": {"type": "string", "enum": ["conforme", "acceptation_conditionnelle", "retravail_requis"]}
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
""")

# 2) Prompt Vérificateur
CONTENT["02_prompts/prompt_verificateur_normatif.md"] = _dedent(r"""
# Prompt — Vérificateur Normatif (BTP)

Rôle
- Tu es Vérificateur AQ BTP. Tu contrôles la conformité technique aux prescriptions du marché et aux règles de l’art.
- Tu ne fais aucune invention: tu relies chaque constat à une preuve documentaire.

Entrées (à fournir côté pipeline)
- Contexte chantier, lot, contraintes (exposition, support, classes, pente, feu, acoustique).
- Documents: CCTP, plans, fiches techniques/FDES, PV d’essais.
- Liste des références applicables (ex.: NF DTU 20.1, 21, 36.5, 40.xx, 45.x, 60.5, 65.14, 68.3). Éditions à préciser.
- Règles internes et tolérances projet.

Exigences
1) Sortie JSON strict conforme au schéma 01_schema/evidence_schema.json.
2) Citer pour chaque constat au moins une source primaire (nom_fichier#page ou repère de plan). Si tu cites une norme, indiquer famille/numéro et l’édition si fournie.
3) Classer gravité: mineure (forme), significative (performance), majeure (sécurité/solidité/étanchéité).
4) Si l’info est manquante: 'hors_perimetre' ou 'non documenté', ne pas extrapoler.
5) Recommandations concrètes, vérifiables, avec action mesurable.

Sortie
- Un unique JSON, plus la liste des captures à produire (coordonnées ou repères).
""")

# 3) Script de validation (sans dépendances externes)
CONTENT["03_scripts/validate_evidence.py"] = _dedent(r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation de l'évidence JSON (structure minimale + règles qualité).
Utilisation:
  python validate_evidence.py evidence.json schema.json
"""

import json, sys, re

def load_json(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def check_required_keys(obj, keys, ctx="root"):
    missing = [k for k in keys if k not in obj]
    return (len(missing) == 0, [f"[{ctx}] manquant: {k}" for k in missing])

def percent_traced(constats):
    if not constats: return 0.0
    traced = [c for c in constats if c.get("citations_sources")]
    return 100.0 * len(traced) / max(1, len(constats))

def check_units(constats):
    msgs = []
    for c in constats:
        if c.get("valeur_constatee") is not None and not c.get("unite"):
            msgs.append(f"Constat {c.get('id')} sans unité.")
    return (len(msgs) == 0, msgs)

def validate_schema_min(evidence):
    ok, msgs = True, []

    # Blocs requis
    ok0, m0 = check_required_keys(evidence, ["meta", "references", "constats", "synthese"], "root")
    ok &= ok0; msgs += m0

    # Meta
    if "meta" in evidence:
        ok1, m1 = check_required_keys(
            evidence["meta"],
            ["chantier", "lot", "document_source", "modele_ia", "version_prompts"],
            "meta"
        )
        ok &= ok1; msgs += m1

    # Références
    if "references" in evidence and not isinstance(evidence["references"], list):
        ok = False; msgs.append("[references] doit être une liste.")
    else:
        for i, ref in enumerate(evidence.get("references", [])):
            okr, mr = check_required_keys(ref, ["famille", "numero", "couverture"], f"references[{i}]")
            ok &= okr; msgs += mr

    # Constats
    if "constats" in evidence and not isinstance(evidence["constats"], list):
        ok = False; msgs.append("[constats] doit être une liste.")
    else:
        for i, c in enumerate(evidence.get("constats", [])):
            okc, mc = check_required_keys(c, ["id", "objet", "exigence", "conforme"], f"constats[{i}]")
            ok &= okc; msgs += mc

    # Synthèse
    if "synthese" in evidence:
        oks, ms = check_required_keys(
            evidence["synthese"],
            ["non_conformites_majeures", "non_conformites_mineures", "points_attention", "risque_global", "decision"],
            "synthese"
        )
        ok &= oks; msgs += ms

    return ok, msgs

def main():
    if len(sys.argv) < 3:
        print("Usage: python validate_evidence.py evidence.json schema.json")
        sys.exit(2)

    evidence = load_json(sys.argv[1])
    schema = load_json(sys.argv[2])  # non utilisé pour jsonschema strict afin d'éviter une dépendance externe

    ok, msgs = validate_schema_min(evidence)
    if not ok:
        print("[ERROR] Structure invalide:")
        for m in msgs: print(" -", m)
        sys.exit(2)

    pct = percent_traced(evidence.get("constats", []))
    ok_units, msg_units = check_units(evidence.get("constats", []))

    print(f"[INFO] Constats={len(evidence.get('constats', []))} | Traçabilité={pct:.1f}%")
    if pct < 90.0:
        print("[WARN] Traçabilité < 90% (objectif).")
    if not ok_units:
        print("[ERROR] Unités manquantes:")
        for m in msg_units: print(" -", m)
        sys.exit(2)

    print("[OK] Validation passée.")
    sys.exit(0)

if __name__ == "__main__":
    main()
''')

# 4) Jeu d’essai “or”
CONTENT["04_tests/jeu_or_minimal.csv"] = _dedent(r"""
id,lot,document_source,exigence,valeur_requise,valeur_constatee,unite,conforme,gravite,source_ref
C-001,CVC,CCTP_P2_Clim.pdf,Epaisseur enrobage mini,>=30,28,mm,false,majeure,"CCTP p.42 ; NF DTU 65.14 (édition à préciser)"
C-002,Couverture,Plan_TOIT_01.pdf,Pente mini membrane,>=2,1.5,%,false,significative,"Plan repère P2 ; Famille NF DTU 40.xx"
C-003,Maçonnerie,PV_Reception_MUR_A.pdf,Planeite mur,<5,<5,mm,true,mineure,"PV §3 ; NF DTU 20.1 (édition à préciser)"
""")

# 5) Modèle Rapport AQ
CONTENT["05_modeles/rapport_AQ_modele.md"] = _dedent(r"""
# Rapport AQ — [Projet] — [Lot]
- Synthèse: [x] majeures / [y] mineures / [z] attentions — Décision: [...]
- Références appliquées: [liste + éditions]
- Détails constats: tableau avec lien vers preuves/captures
- Arbitrages: [texte]
- Plan d’actions: qui / quoi / quand / critère de succès
- Annexe: hachages, versions modèle/prompts, logs techniques (horodatage, identifiants de versions)

Conseils
- Pour les normes, toujours renseigner l’édition exacte (registre marché).
- Lier chaque constat à au moins une source primaire (page/repère).
""")

# 6) Checklist Revue AQ
CONTENT["05_modeles/checklist_revue_AQ.md"] = _dedent(r"""
# Checklist Revue Humaine AQ
- [ ] Périmètre vérifié correspond au marché (lots/variantes/avenants)
- [ ] Éditions des références normatives renseignées
- [ ] Constats majeurs recoupés avec documents primaires
- [ ] Recommandations concrètes et mesurables
- [ ] Décision motivée ; plan d’actions (responsables, échéances)
- [ ] Rapport PDF/A généré ; paquet de preuves haché et archivé
""")

# 7) Matrice de risques
CONTENT["05_modeles/matrice_risques.md"] = _dedent(r"""
# Matrice de Risques — Méthode simple
- Criticité = Gravité × Probabilité × Détectabilité (1–5)
- Seuil d’alerte: Criticité ≥ 12 → action corrective obligatoire avant exécution

Catégories usuelles
- Sécurité incendie / structure / étanchéité: gravité 5
- Performance énergétique / acoustique: 3–4
- Documentaire / traçabilité: 2
""")

# 8) README d’intégration pipeline
CONTENT["06_docs/README_integration_pipeline.md"] = _dedent(r"""
# Intégration Pipeline — Module 03

Étapes recommandées
1. Après génération de la sortie IA, produire evidence.json conforme au schéma.
2. Valider: python 03_scripts/validate_evidence.py evidence.json 01_schema/evidence_schema.json
3. Générer un PDF/A du rapport basé sur 05_modeles/rapport_AQ_modele.md.
4. Zipper le paquet de preuves: evidence.json, captures, rapport PDF/A, hash des entrées.
5. Pousser vers l’archive (dossier par lot + version).

Métriques à remonter
- exactitude_pct, reponses_ssourcees_pct, non_conformites_majeures_nb, temps_validation_sec.
""")

# 9) Doc de références normatives — exemples de familles (à compléter par vos éditions)
CONTENT["06_docs/references_normatives_exemples.md"] = _dedent(r"""
# Références normatives — Exemples de familles à cadrer
- Sols et fondations: NF DTU 13.1, 13.2, 13.3, 14.1
- Maçonnerie / Béton: NF DTU 20.1, 20.12, 20.13, 21, 22.1
- Enveloppe / Façades: NF DTU 26.1, 33.1, XP 33.2, 41.2, 42.1, 44.1, 52.2, 55.2
- Isolation par l’extérieur: FD 45.3, NF DTU 45.4
- Menuiseries / Fermetures: NF DTU 34.1, FD 34.3, 34.4, 34.5
- Réseaux fluides / Plomberie: NF DTU 60.1x / 60.5, 60.33, 64.1
- Gaz: NF DTU 61.1
- CVC / Chauffage: NF DTU 65.xx (ex. planchers chauffants, sous-stations)
- Ventilation: NF DTU 68.3

Note importante
- Renseignez toujours l’édition précise appliquée à votre marché et les clauses/articles utilisés pour les contrôles. Ce document n’extrait aucun contenu normatif; il sert à structurer la traçabilité.
""")

# README racine
CONTENT["README.md"] = _dedent(r"""
# Module 03 — Contrôle de conformité normative et AQ (BTP)

Contenus
- 01_schema/evidence_schema.json — schéma JSON de l’évidence
- 02_prompts/prompt_verificateur_normatif.md — prompt de contrôle
- 03_scripts/validate_evidence.py — validation structurelle + règles qualité
- 04_tests/jeu_or_minimal.csv — jeu d’essai “or”
- 05_modeles/ — modèles Rapport, Checklist, Matrice
- 06_docs/ — intégration pipeline et rappel des familles de références

Démarrage rapide
- Produire un evidence.json
- Valider: python 03_scripts/validate_evidence.py evidence.json 01_schema/evidence_schema.json
- Générer le rapport AQ à partir du modèle
""")

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
    parser = argparse.ArgumentParser(description="Générer les livrables du Module 03 (BTP).")
    parser.add_argument("--out", required=True, help="Dossier de sortie (ex: ./module_03)")
    parser.add_argument("--zip", action="store_true", help="Créer un .zip des livrables")
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


