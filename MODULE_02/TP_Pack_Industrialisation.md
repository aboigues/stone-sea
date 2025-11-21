# TP MODULE 02 - Pack d'industrialisation IA BTP

**Formation pratique au déploiement de cas d'usage IA conformes**

---

## 📋 Informations générales

**Durée estimée** : 3 heures
**Niveau** : Intermédiaire
**Prérequis** :
- Avoir complété le TP MODULE_01 (Wrappers IA)
- Connaissances en gestion de projet BTP
- Notions de conformité normative (DTU, Eurocodes)
- Accès à Python 3.8+ et un éditeur de texte

**Objectifs pédagogiques** :
1. Savoir structurer un cas d'usage IA pour le BTP
2. Mettre en place un pipeline de traitement sécurisé
3. Implémenter des tests et contrôles qualité
4. Déployer et exploiter un cas d'usage en production

---

## 📚 Partie 1 : Vue d'ensemble du pack (15 min)

### 1.1 Qu'est-ce que le pack d'industrialisation ?

Le pack d'industrialisation est un **ensemble complet d'outils et de processus** pour déployer des cas d'usage IA dans le secteur BTP de manière :
- **Conforme** : respect des normes DTU/Eurocodes
- **Sécurisée** : anonymisation, traçabilité, validation
- **Traçable** : journalisation complète des opérations
- **Réversible** : possibilité de sortie ou de changement de solution

### 1.2 Les 10 composants du pack

| Composant | Objectif | Utilisation |
|-----------|----------|-------------|
| **1. Fiche cas d'usage** | Cadrer le périmètre et les objectifs | Démarrage projet |
| **2. Charte des sources** | Définir les références autorisées | Cadrage technique |
| **3. Prompts contrôlés** | Encadrer les interactions IA | Développement |
| **4. Grilles de conformité** | Vérifier les exigences normatives | Contrôle qualité |
| **5. Pipeline** | Automatiser le traitement | Production |
| **6. Tests & évaluation** | Valider la qualité | Recette |
| **7. SOP & Playbook** | Exploiter et gérer les incidents | Exploitation |
| **8. Dashboards** | Suivre les performances | Pilotage |
| **9. Réversibilité** | Planifier la sortie | Gouvernance |

---

## 🎯 Partie 2 : Exercices pratiques

### Exercice 1 : Rédiger une fiche cas d'usage (30 min)

**Objectif** : Structurer un cas d'usage IA pour contrôler un CCTP de couverture

**Contexte** : Votre entreprise souhaite automatiser le contrôle de conformité des CCTP pour le lot couverture.

**Consigne** : Complétez la fiche cas d'usage suivante

```markdown
# Fiche Cas d'Usage IA — Contrôle CCTP Couverture

## Identification
- Propriétaire métier : [À COMPLÉTER]
- Sponsor : [À COMPLÉTER]
- Date : [À COMPLÉTER]

## Objectif mesurable
[Ex: Réduire de 50% le temps de contrôle CCTP et détecter 90%+ des non-conformités]

## Périmètre
- Documents traités : [Ex: CCTP sections couverture, plans toiture, fiches techniques tuiles]
- Lots concernés : [Ex: Couverture tuiles mécaniques, écrans de sous-toiture]
- Exclusions : [Ex: Couverture zinc, toitures végétalisées]

## Données d'entrée
- Formats acceptés : [Ex: PDF, DOCX]
- Taille maximale : [Ex: 50 pages, 10 Mo]
- Langue : [Ex: Français]

## Données interdites
- [Ex: Prix unitaires, données personnelles clients, RH]

## Sorties attendues
- Format : [Ex: JSON + Rapport PDF]
- Contenu : [Ex: Liste des non-conformités avec références DTU]

## Normes cibles
- [Ex: NF DTU 40.21, NF DTU 40.29]

## Validation
- Validation humaine : [Ex: Double contrôle par chef de chantier + bureau d'études]

## KPIs
- Temps de traitement : [Ex: < 5 min par CCTP]
- Exactitude : [Ex: > 90%]
- Taux de réponses sourcées : [Ex: 100%]
```

**Questions** :
1. Quels sont les risques spécifiques à ce cas d'usage ?
2. Qui doit valider les résultats avant envoi au client ?
3. Combien de temps devez-vous conserver les journaux de traitement ?

---

### Exercice 2 : Créer une charte des sources (20 min)

**Objectif** : Définir les références autorisées pour le contrôle CCTP

**Consigne** : Complétez la charte suivante

```markdown
# Charte des Sources — Contrôle CCTP Couverture

## Hiérarchie des sources (par ordre de priorité)

1. **Normes et DTU**
   - NF DTU 40.21 (Tuiles terre cuite à emboîtement) — [Édition à préciser]
   - NF DTU 40.211 (Tuiles plates) — [Édition à préciser]
   - NF DTU 40.29 (Écrans souples sous-toiture) — [Édition à préciser]

2. **Avis techniques et règles professionnelles**
   - Avis techniques CSTB pour produits spécifiques
   - [À COMPLÉTER]

3. **Documents fabricants**
   - Fiches techniques produits
   - [À COMPLÉTER]

4. **Documents projet**
   - CCTP, CCAP
   - Plans de toiture
   - [À COMPLÉTER]

## Règles de citation
- Toute affirmation DOIT citer : référence + édition/année + page/article
- Si source manquante → verdict "NON CONFORME" automatique
- Format de citation : "NF DTU 40.21 (Avril 2012), article 5.2.1"

## Traçabilité
- Journal JSON avec horodatage et hash des documents
- Conservation : [Durée à définir selon projet]
```

---

### Exercice 3 : Tester le pipeline d'anonymisation (30 min)

**Objectif** : Anonymiser un document avant traitement

**Document à anonymiser** :
```
MARCHÉ TRAVAUX N° 2024-BTP-789
Client : M. Pierre MARTIN
Adresse : 45 avenue Victor Hugo, 69003 Lyon
Tel : 06 12 34 56 78
Email : p.martin@exemple.fr

Véhicule chantier : AA-123-BB

CCTP COUVERTURE
Date : 15/11/2024

LOT 5 - COUVERTURE
Tuiles terre cuite EDILIANS modèle OMEGA 10
Prix forfaitaire : 45 600 € HT

Pente minimale : 30%
Recouvrement : 110 mm
```

**Consigne** :
1. Ouvrez le fichier `MODULE_02/export_pack/05_Pipeline/anonymize.py`
2. Exécutez le script sur le document ci-dessus :
```bash
python MODULE_02/export_pack/05_Pipeline/anonymize.py input.txt output.txt
```

**Résultat attendu** :
```
MARCHÉ TRAVAUX N° [ANON]
Client : [ANON]
Adresse : [ANON]
Tel : [ANON]
Email : [ANON]

Véhicule chantier : [ANON]

CCTP COUVERTURE
Date : [ANON]

LOT 5 - COUVERTURE
Tuiles terre cuite EDILIANS modèle OMEGA 10
Prix forfaitaire : [ANON]

Pente minimale : 30%
Recouvrement : 110 mm
```

**Questions** :
1. Quelles données ont été anonymisées ?
2. Quelles données techniques ont été conservées ?
3. Le document anonymisé est-il exploitable pour un contrôle technique ?

---

### Exercice 4 : Créer un jeu de tests (30 min)

**Objectif** : Préparer des cas de test pour valider le contrôle CCTP

**Consigne** : Complétez le fichier CSV suivant avec 5 cas de test

```csv
doc_id,lot,exigence,verdict_attendu,source_attendue,edition_attendue
TEST_001,Couverture,Pente minimale tuiles OMEGA 10,CONFORME,NF DTU 40.21,Avril 2012
TEST_002,Couverture,Recouvrement tuiles < 100mm,NON CONFORME,NF DTU 40.21,Avril 2012
[À COMPLÉTER - 3 autres cas]
```

**Exemples de cas à tester** :
- Pente minimale conforme
- Recouvrement insuffisant (non conforme)
- Écran sous-toiture manquant (non conforme)
- Fixation tuiles conforme
- Ventilation toiture conforme

**Questions** :
1. Pourquoi est-il important d'avoir des cas conformes ET non conformes ?
2. Combien de cas minimum recommandez-vous pour un test robuste ?

---

### Exercice 5 : Rédiger une procédure d'exploitation (SOP) (30 min)

**Objectif** : Définir comment exploiter le cas d'usage au quotidien

**Consigne** : Complétez la SOP suivante

```markdown
# SOP — Exploitation Contrôle CCTP Couverture

## 1. Réception du document
- [ ] Vérifier le format (PDF/DOCX uniquement)
- [ ] Vérifier la taille (< 10 Mo)
- [ ] Calculer le hash SHA-256
- [ ] Scanner antivirus
- [ ] Anonymiser avec le script `anonymize.py`

## 2. Qualification
- [ ] Identifier le lot (couverture)
- [ ] Vérifier que le CCTP contient les sections attendues
- [ ] Enregistrer dans le journal de traitement

## 3. Exécution
- [ ] Lancer le prompt contrôlé de contrôle CCTP
- [ ] Exécuter le vérificateur indépendant
- [ ] Valider le format JSON de sortie

## 4. Contrôle qualité
- [ ] Vérifier que toutes les exigences ont une source
- [ ] Vérifier que les éditions des normes sont présentes
- [ ] Double validation humaine par [RÔLE 1] et [RÔLE 2]

## 5. Archivage
- [ ] Sauvegarder le document source (anonymisé)
- [ ] Sauvegarder le JSON de sortie
- [ ] Sauvegarder le journal de traitement
- [ ] Durée de conservation : [À DÉFINIR]

## Rôles et responsabilités
- Exploitant IA : [NOM]
- Référent Qualité : [NOM]
- Référent Sécurité/DPD : [NOM]
```

---

## 🏆 Partie 3 : Cas pratique final (45 min)

### Déploiement complet d'un cas d'usage

**Contexte** :
Vous devez déployer le cas d'usage "Contrôle CCTP Couverture" pour un nouveau chantier.

**Livrables attendus** :
1. Fiche cas d'usage complète
2. Charte des sources avec 5+ références
3. Fichier de test CSV avec 5 cas minimum
4. SOP d'exploitation complète
5. Plan de réversibilité (1 page)

**Critères d'évaluation** :
- ✅ Fiche cas d'usage : objectifs mesurables, périmètre clair, KPIs définis (20 points)
- ✅ Charte des sources : hiérarchie claire, règles de citation précises (20 points)
- ✅ Jeux de tests : cas conformes et non conformes, sources attendues (20 points)
- ✅ SOP : étapes claires, rôles définis, contrôles qualité (20 points)
- ✅ Plan de réversibilité : formats d'export, procédure de sortie (20 points)

**Total : 100 points**

---

## 📖 Partie 4 : Ressources et bonnes pratiques

### 4.1 Checklist de déploiement

Avant de mettre en production un cas d'usage IA :

- [ ] Fiche cas d'usage validée par le sponsor
- [ ] Charte des sources approuvée par le référent technique
- [ ] Pipeline testé avec anonymisation fonctionnelle
- [ ] Jeux de tests validés (>80% de succès)
- [ ] SOP rédigée et approuvée
- [ ] Formation des utilisateurs réalisée
- [ ] Playbook incidents préparé
- [ ] Dashboards configurés
- [ ] Plan de réversibilité documenté

### 4.2 Erreurs fréquentes à éviter

❌ **Erreur 1** : Périmètre trop large dès le départ
→ ✅ Commencer par un lot/type de document, puis étendre

❌ **Erreur 2** : Oublier l'anonymisation
→ ✅ Toujours anonymiser avant traitement IA

❌ **Erreur 3** : Pas de validation humaine
→ ✅ Double contrôle obligatoire pour décisions critiques

❌ **Erreur 4** : Tests insuffisants
→ ✅ Minimum 20-30 cas de test représentatifs

❌ **Erreur 5** : Pas de plan de réversibilité
→ ✅ Prévoir la sortie dès le début

### 4.3 Métriques clés à suivre

**Qualité** :
- Taux de réponses sourcées : objectif 100%
- Exactitude : objectif > 90%
- Faux positifs : < 5%
- Faux négatifs : < 2%

**Performance** :
- Temps de traitement moyen
- Disponibilité du service
- Délai de réponse

**Adoption** :
- Nombre d'utilisateurs actifs
- Nombre de documents traités
- Taux de satisfaction utilisateurs

**Sécurité** :
- Incidents critiques : 0
- Non-conformités RGPD : 0
- Audits réussis

---

## 📝 Conclusion

Vous avez maintenant les outils pour déployer un cas d'usage IA BTP de manière industrielle et conforme.

**Points clés à retenir** :
1. Le pack d'industrialisation structure le déploiement de bout en bout
2. L'anonymisation et la traçabilité sont obligatoires
3. Les tests et la validation humaine garantissent la qualité
4. La réversibilité doit être planifiée dès le début

**Prochaines étapes** :
1. Déployer votre premier cas d'usage sur un chantier pilote
2. Mesurer les résultats avec les dashboards
3. Itérer et améliorer selon les retours terrain
4. Étendre à d'autres lots et chantiers

---

**Version** : 1.0
**Date** : 2024-11-21
**Auteur** : Stone-Sea Project
