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
