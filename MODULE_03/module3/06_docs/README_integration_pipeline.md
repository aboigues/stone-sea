# Intégration Pipeline — Module 03

Étapes recommandées
1. Après génération de la sortie IA, produire evidence.json conforme au schéma.
2. Valider: python 03_scripts/validate_evidence.py evidence.json 01_schema/evidence_schema.json
3. Générer un PDF/A du rapport basé sur 05_modeles/rapport_AQ_modele.md.
4. Zipper le paquet de preuves: evidence.json, captures, rapport PDF/A, hash des entrées.
5. Pousser vers l’archive (dossier par lot + version).

Métriques à remonter
- exactitude_pct, reponses_ssourcees_pct, non_conformites_majeures_nb, temps_validation_sec.
