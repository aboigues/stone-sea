# Module 06 — Plan d’essais, contrôles et PV chantier

Généré le 2025-11-13.
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
