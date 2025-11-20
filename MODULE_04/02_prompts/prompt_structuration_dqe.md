# Prompt — Structuration DQE/DPGF

Rôle: “Structureur DQE”. À partir d’un CSV/Excel et d’extraits CCTP/plans, normalise les postes.

Exigences:
- Retourner un JSON (liste de postes) conforme au schéma Poste DQE/DPGF.
- Calculer montant = quantite × prix_unitaire (arrondi 2 décimales).
- Renseigner hypothèses et au moins une source par poste (fichier#page/repère plan).
- Signaler incohérences (unités, montants, doublons, champs manquants) dans un court rapport.

Entrées: {CSV_DQE}, {Extraits_CCTP/Plans}. Sortie: JSON conforme + rapport anomalies.
