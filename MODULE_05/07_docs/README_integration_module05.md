# Module 05 — Conformité normative et technique

Généré le 2025-11-13. Ce module fournit:
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
