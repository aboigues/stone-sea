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
