# TP MODULE 06 - Plan d'essais, contrôles et PV chantier

**Formation pratique à la planification et au suivi des essais et contrôles**

---

## 📋 Informations générales

**Durée estimée** : 4 heures
**Niveau** : Intermédiaire
**Prérequis** :
- Connaissances des essais et contrôles BTP (béton, chapes, etc.)
- Notions de normes NF EN, NF DTU et plans qualité
- Maîtrise de base de Python et JSON
- Avoir lu le README.md du projet et le README_integration_module06.md

**Objectifs pédagogiques** :
1. Maîtriser la création d'un plan de contrôle structuré en JSON
2. Comprendre les différents modes d'échantillonnage et de fréquence d'essais
3. Savoir planifier automatiquement les essais à partir d'un quantitatif
4. Valider la conformité des PV par rapport aux critères du plan
5. Analyser les KPIs de couverture des essais et identifier les écarts

---

## 📚 Partie 1 : Contexte et enjeux (15 min)

### 1.1 Pourquoi un plan d'essais structuré ?

Dans tout projet BTP, la maîtrise de la qualité repose sur la réalisation d'essais et contrôles conformes aux normes et au CCTP. Les enjeux sont majeurs :

- **Conformité réglementaire** : Respect des NF DTU, Eurocodes et spécifications projet
- **Traçabilité** : Justification de la qualité en cas de contentieux ou de sinistre
- **Optimisation** : Ni trop d'essais (coût), ni trop peu (risques)
- **Pilotage** : Suivi en temps réel de l'avancement des contrôles
- **Réactivité** : Détection rapide des non-conformités pour corrections

**Problèmes classiques sans plan structuré** :
- ❌ Oubli d'essais obligatoires (découvert lors de l'OPR ou du DOE)
- ❌ Fréquences incorrectes (sous-contrôle ou sur-contrôle)
- ❌ PV non validés ou perdus
- ❌ Impossibilité de générer des KPIs de couverture
- ❌ Difficultés à prouver la conformité a posteriori

### 1.2 Le MODULE_06 : vue d'ensemble

Le MODULE_06 de Stone-Sea fournit une chaîne complète de gestion des essais :

**1. Schémas JSON standardisés**
- `plan_controle.schema.json` : Structure du plan de contrôle par lot
- `essai.schema.json` : Définition d'un essai (fréquence, critères, échantillonnage)
- `pv.schema.json` : Procès-verbal ou mesure
- `echantillonnage.schema.json` : Règles d'échantillonnage (fixe, %, surface, volume)

**2. Règles métier prédéfinies**
- `controles_beton.json` : Essais béton (résistance, slump, etc.)
- `controles_chapes.json` : Contrôles chapes (planéité, épaisseur, etc.)
- `mapping_unites.json` : Conversion d'unités

**3. Scripts Python opérationnels**
- `planificateur_essais.py` : Calcul du nombre d'essais à partir du quantitatif
- `validate_pv_vs_exigences.py` : Validation des PV par rapport aux critères
- `echantillonnage_calcul.py` : Calcul d'échantillonnage pour un essai donné
- `kpi_essais.py` : KPIs de couverture (% réalisé, % conforme)

**4. Prompts et modèles**
- Prompts pour génération de plans avec IA
- Modèles de rapports de contrôle

### 1.3 Workflow type

```
1. Création du plan de contrôle
   ↓ (JSON structuré par lot/essai)
2. Planification des essais
   ↓ (Quantitatifs projet → Nb essais à réaliser)
3. Réalisation et saisie des PV
   ↓ (Laboratoires, contrôles chantier)
4. Validation des PV
   ↓ (Comparaison valeurs vs critères)
5. Analyse KPIs et pilotage
   ↓ (Couverture, conformité, écarts)
6. DOE et archivage
```

---

## 🎯 Partie 2 : Exercices pratiques

### Exercice 1 : Créer un plan de contrôle pour un lot Gros-œuvre

**Objectif** : Comprendre la structure d'un plan de contrôle et créer un essai de contrôle béton.

**Contexte** : Vous êtes conducteur de travaux sur un projet de construction d'un immeuble R+5. Vous devez créer un plan de contrôle pour le lot Gros-œuvre avec contrôle de la résistance du béton.

**Consigne** :
1. Lisez le schéma `plan_controle.schema.json` et `essai.schema.json`
2. Créez un fichier JSON `mon_plan_controle.json` avec :
   - Métadonnées projet : "Immeuble Les Chênes", version 1.0, date du jour
   - Un lot "Gros-œuvre"
   - Un essai de résistance béton à 28 jours (id: BET-R28)

**Informations de l'essai** :
- Référence : NF EN 206/CN
- Type : essai
- Fréquence : 1 série tous les 150 m³
- Critère d'acceptation : fck ≥ 30 MPa
- Unité : MPa
- Échantillonnage : mode "unites_ouvrage", paramètre "par_volume_m3": 150
- Preuves attendues : "PV laboratoire COFRAC", "Fiche DOD béton"

**Réponse attendue** :

```json
{
  "meta": {
    "projet": "Immeuble Les Chênes",
    "version": "1.0",
    "date": "2025-11-20"
  },
  "lots": ["Gros-œuvre"],
  "essais": [
    {
      "id": "BET-R28",
      "lot": "Gros-œuvre",
      "intitule": "Résistance béton à 28 jours",
      "reference": "NF EN 206/CN",
      "type": "essai",
      "frequence": "1 série/150 m³",
      "critere_acceptation": "fck ≥ 30 MPa",
      "unite": "MPa",
      "cible": 30,
      "tol_minus": "-",
      "tol_plus": "-",
      "echantillonnage": {
        "mode": "unites_ouvrage",
        "parametres": {
          "par_volume_m3": 150
        }
      },
      "evidences_attendues": [
        "PV laboratoire COFRAC",
        "Fiche DOD béton"
      ]
    }
  ]
}
```

**Validation** :
```bash
# Validez votre JSON avec un validateur JSON Schema
python -m json.tool mon_plan_controle.json
```

**Questions à vous poser** :
- Pourquoi utiliser "unites_ouvrage" plutôt que "fixe" ou "pourcentage" ?
- Quelle est la différence entre "cible" et "critere_acceptation" ?
- Que signifie "-" dans tol_minus et tol_plus ?

---

### Exercice 2 : Planifier les essais à partir du quantitatif

**Objectif** : Utiliser le script `planificateur_essais.py` pour calculer le nombre d'essais à réaliser.

**Contexte** : Le projet "Immeuble Les Chênes" prévoit 450 m³ de béton pour le gros-œuvre et 380 m² de chapes. Vous devez planifier les essais.

**Plan de contrôle (fichier `plan_exercice2.json`)** :
```json
{
  "meta": {"projet": "Immeuble Les Chênes", "version": "1.0", "date": "2025-11-20"},
  "lots": ["Gros-œuvre", "Chapes"],
  "essais": [
    {
      "id": "BET-R28",
      "lot": "Gros-œuvre",
      "intitule": "Résistance béton à 28 jours",
      "reference": "NF EN 206/CN",
      "type": "essai",
      "frequence": "1 série/150 m³",
      "critere_acceptation": "fck ≥ 30 MPa",
      "unite": "MPa",
      "cible": 30,
      "echantillonnage": {"mode": "unites_ouvrage", "parametres": {"par_volume_m3": 150}},
      "evidences_attendues": ["PV labo"]
    },
    {
      "id": "CHA-PLAN",
      "lot": "Chapes",
      "intitule": "Planéité chapes",
      "reference": "NF DTU 26.2",
      "type": "mesure",
      "frequence": "1 mesure/20 m²",
      "critere_acceptation": "Écart max ≤ 5 mm sous règle 2m (P3)",
      "unite": "mm",
      "cible": 5,
      "tol_plus": 0,
      "echantillonnage": {"mode": "surface", "parametres": {"surface": 20}},
      "evidences_attendues": ["PV planéité", "Photos"]
    }
  ]
}
```

**Quantitatifs (fichier `quantites_exercice2.json`)** :
```json
{
  "projet": "Immeuble Les Chênes",
  "volume_beton_m3": 450,
  "surface_m2": 380
}
```

**Consigne** :
1. Créez les deux fichiers JSON ci-dessus
2. Exécutez le script de planification :
```bash
python MODULE_06/03_scripts/planificateur_essais.py \
  --plan plan_exercice2.json \
  --quantites quantites_exercice2.json \
  --out planning_exercice2.json
```
3. Analysez le résultat

**Réponse attendue** :

Le script doit générer un fichier `planning_exercice2.json` :
```json
{
  "meta": {
    "date": "2025-11-20T...",
    "projet": "Immeuble Les Chênes"
  },
  "planning": [
    {
      "essai_id": "BET-R28",
      "intitule": "Résistance béton à 28 jours",
      "lot": "Gros-œuvre",
      "a_realiser": 3,
      "frequence": "1 série/150 m³",
      "reference": "NF EN 206/CN"
    },
    {
      "essai_id": "CHA-PLAN",
      "intitule": "Planéité chapes",
      "lot": "Chapes",
      "a_realiser": 19,
      "frequence": "1 mesure/20 m²",
      "reference": "NF DTU 26.2"
    }
  ]
}
```

**Calculs à vérifier** :
- Béton : 450 m³ / 150 m³ = 3 séries d'essais
- Chapes : 380 m² / 20 m² = 19 mesures

**Questions** :
- Que se passe-t-il si le volume béton était 470 m³ ? (Réponse : ceil(470/150) = 4 séries)
- Comment adapter pour un mode "pourcentage" ?
- Pourquoi utiliser `math.ceil` plutôt que `math.floor` ?

---

### Exercice 3 : Saisir et valider des PV d'essais

**Objectif** : Créer des PV conformes au schéma et les valider automatiquement.

**Contexte** : Les 3 séries d'essais béton ont été réalisées. Vous devez saisir les PV et vérifier la conformité.

**Résultats laboratoire** :
- Série 1 (Zone A - Fondations) : 32.5 MPa, 31.8 MPa, 33.1 MPa → Moyenne 32.5 MPa
- Série 2 (Zone B - Poteaux R+1) : 29.2 MPa, 30.1 MPa, 28.9 MPa → Moyenne 29.4 MPa
- Série 3 (Zone C - Dalles R+2) : 35.0 MPa, 34.2 MPa, 34.8 MPa → Moyenne 34.7 MPa

**Consigne** :
1. Créez un fichier `pv_exercice3.json` avec les 3 PV
2. Utilisez le script de validation :
```bash
python MODULE_06/03_scripts/validate_pv_vs_exigences.py \
  --plan plan_exercice2.json \
  --pv pv_exercice3.json \
  --out pv_valides_exercice3.json
```

**Fichier PV à créer** :
```json
{
  "pv": [
    {
      "id": "PV-BET-001",
      "essai_id": "BET-R28",
      "date": "2025-10-15",
      "ouvrage": "Fondations",
      "zone": "Zone A",
      "type": "essai",
      "valeurs": {
        "eprouvette_1": 32.5,
        "eprouvette_2": 31.8,
        "eprouvette_3": 33.1,
        "mesure": 32.5
      },
      "unite": "MPa",
      "conformite": "OK",
      "fichier": "PV-BET-001-COFRAC.pdf"
    },
    {
      "id": "PV-BET-002",
      "essai_id": "BET-R28",
      "date": "2025-10-22",
      "ouvrage": "Poteaux R+1",
      "zone": "Zone B",
      "type": "essai",
      "valeurs": {
        "eprouvette_1": 29.2,
        "eprouvette_2": 30.1,
        "eprouvette_3": 28.9,
        "mesure": 29.4
      },
      "unite": "MPa",
      "conformite": "KO",
      "commentaire": "Résistance inférieure à fck. Note de calcul BET requise.",
      "fichier": "PV-BET-002-COFRAC.pdf"
    },
    {
      "id": "PV-BET-003",
      "essai_id": "BET-R28",
      "date": "2025-10-29",
      "ouvrage": "Dalles R+2",
      "zone": "Zone C",
      "type": "essai",
      "valeurs": {
        "eprouvette_1": 35.0,
        "eprouvette_2": 34.2,
        "eprouvette_3": 34.8,
        "mesure": 34.7
      },
      "unite": "MPa",
      "conformite": "OK",
      "fichier": "PV-BET-003-COFRAC.pdf"
    }
  ]
}
```

**Résultat attendu (fichier `pv_valides_exercice3.json`)** :
```json
{
  "results": [
    {
      "pv_id": "PV-BET-001",
      "essai_id": "BET-R28",
      "intitule": "Résistance béton à 28 jours",
      "reference": "NF EN 206/CN",
      "unite": "MPa",
      "valeurs": {
        "eprouvette_1": 32.5,
        "eprouvette_2": 31.8,
        "eprouvette_3": 33.1,
        "mesure": 32.5
      },
      "conformite_calculee": "OK",
      "conformite_declares": "OK"
    },
    {
      "pv_id": "PV-BET-002",
      "essai_id": "BET-R28",
      "intitule": "Résistance béton à 28 jours",
      "reference": "NF EN 206/CN",
      "unite": "MPa",
      "valeurs": {
        "eprouvette_1": 29.2,
        "eprouvette_2": 30.1,
        "eprouvette_3": 28.9,
        "mesure": 29.4
      },
      "conformite_calculee": "KO",
      "conformite_declares": "KO"
    },
    {
      "pv_id": "PV-BET-003",
      "essai_id": "BET-R28",
      "intitule": "Résistance béton à 28 jours",
      "reference": "NF EN 206/CN",
      "unite": "MPa",
      "valeurs": {
        "eprouvette_1": 35.0,
        "eprouvette_2": 34.2,
        "eprouvette_3": 34.8,
        "mesure": 34.7
      },
      "conformite_calculee": "OK",
      "conformite_declares": "OK"
    }
  ]
}
```

**Points d'attention** :
- Le PV-BET-002 est non conforme (29.4 MPa < 30 MPa)
- La conformité calculée par le script doit correspondre à la conformité déclarée
- Le champ "mesure" dans "valeurs" est utilisé pour la validation automatique

**Actions correctives** :
- PV-BET-002 : Demander note de calcul BET pour justification ou décision maître d'œuvre
- Enregistrer la NC dans le registre du MODULE_05
- Tracer la décision (reprise, dérogation, renforcement)

---

### Exercice 4 : Calculer l'échantillonnage pour un essai

**Objectif** : Utiliser le script `echantillonnage_calcul.py` pour vérifier le nombre d'essais requis.

**Contexte** : Vous devez vérifier que le nombre de contrôles de planéité des chapes est conforme au DTU 26.2.

**Consigne** :
```bash
python MODULE_06/03_scripts/echantillonnage_calcul.py \
  --essai_id CHA-PLAN \
  --plan plan_exercice2.json \
  --quantites quantites_exercice2.json
```

**Résultat attendu** :
```
[ECHANTILLONNAGE] Essai: CHA-PLAN | Mode: surface
[ECHANTILLONNAGE] Surface projet: 380 m² | Fréquence: 1/20 m²
[ECHANTILLONNAGE] Nombre d'échantillons requis: 19
```

**Vérification** :
- Surface chapes : 380 m²
- Fréquence : 1 mesure / 20 m²
- Calcul : ceil(380 / 20) = 19 mesures

**Questions** :
- Pourquoi arrondir au supérieur (ceil) plutôt qu'à l'inférieur ?
- Que faire si vous avez déjà réalisé seulement 15 mesures ?
- Comment modifier le plan si le CCTP exige 1 mesure / 15 m² ?

---

### Exercice 5 : Analyser les KPIs de couverture

**Objectif** : Utiliser le script `kpi_essais.py` pour piloter l'avancement des contrôles.

**Contexte** : Vous êtes en phase de suivi de chantier. Vous avez planifié 3 essais béton et réalisé les 3 PV. Vous voulez connaître le taux de couverture et de conformité.

**Consigne** :
```bash
python MODULE_06/03_scripts/kpi_essais.py \
  --planning planning_exercice2.json \
  --pv pv_exercice3.json
```

**Réponse attendue (affichage console)** :
```
[KPI] === TABLEAU DE BORD ESSAIS ===
[KPI] Projet: Immeuble Les Chênes

[KPI] Essai: BET-R28 (Résistance béton à 28 jours)
[KPI]   Planifié: 3 | Réalisé: 3 | Couverture: 100.0%
[KPI]   Conforme: 2 | Non-conforme: 1 | Taux conformité: 66.7%

[KPI] Essai: CHA-PLAN (Planéité chapes)
[KPI]   Planifié: 19 | Réalisé: 0 | Couverture: 0.0%
[KPI]   Conforme: 0 | Non-conforme: 0 | Taux conformité: N/A

[KPI] === SYNTHÈSE GLOBALE ===
[KPI] Total planifié: 22 | Total réalisé: 3 | Couverture globale: 13.6%
[KPI] Total conforme: 2 | Total non-conforme: 1 | Taux conformité global: 66.7%

⚠️ ALERTES :
- Essai CHA-PLAN : 0% de couverture (19 mesures manquantes)
- Essai BET-R28 : 1 non-conformité détectée (PV-BET-002)
```

**Analyse** :
- ✅ Béton : 100% de couverture, mais seulement 66.7% de conformité → Action corrective requise
- ❌ Chapes : 0% de couverture → Planifier rapidement les mesures

**Utilisation pour le pilotage** :
- Tableau de bord hebdomadaire pour réunions de chantier
- Alerte automatique si couverture < seuil (ex: 80%)
- Export pour rapports mensuels maître d'ouvrage
- Traçabilité pour DOE et OPR

---

## 🏆 Partie 3 : Évaluation finale (1h30)

### Cas pratique intégré

**Contexte général** :
Vous êtes responsable qualité sur le chantier de construction d'une école maternelle. Le projet comprend :
- **Lot Gros-œuvre** : 280 m³ de béton (fondations, voiles, dalles)
- **Lot Chapes** : 520 m² de chapes flottantes
- **Lot Menuiseries extérieures** : 45 fenêtres

Vous devez :
1. Créer un plan de contrôle complet pour les 3 lots
2. Planifier les essais à partir des quantitatifs
3. Saisir les PV d'essais reçus
4. Valider la conformité
5. Analyser les KPIs et proposer des actions correctives

---

### Partie A : Création du plan de contrôle (20 points)

**Consigne** : Créez un fichier JSON `plan_ecole.json` avec les essais suivants.

**LOT GROS-ŒUVRE** :

1. **Essai résistance béton (BET-R28)**
   - Référence : NF EN 206/CN
   - Fréquence : 1 série / 150 m³
   - Critère : fck ≥ 25 MPa (C25/30)
   - Échantillonnage : unites_ouvrage, par_volume_m3 = 150

2. **Contrôle affaissement béton (BET-SLUMP)**
   - Référence : NF EN 12350-2
   - Fréquence : 1 par camion (fixe, nb=1)
   - Critère : Classe S3 (100-150 mm)
   - Échantillonnage : fixe, nb = 1

**LOT CHAPES** :

3. **Mesure planéité (CHA-PLAN)**
   - Référence : NF DTU 26.2
   - Fréquence : 1 mesure / 25 m²
   - Critère : Écart ≤ 5 mm sous règle 2m (P3)
   - Échantillonnage : surface, surface = 25

4. **Mesure épaisseur (CHA-EPAIS)**
   - Référence : NF DTU 26.2
   - Fréquence : 1 mesure / 50 m²
   - Critère : ≥ 50 mm
   - Échantillonnage : surface, surface = 50

**LOT MENUISERIES** :

5. **Contrôle étanchéité à l'air (MENU-AIR)**
   - Référence : NF DTU 36.5 + Avis Technique
   - Fréquence : 10% des menuiseries (pourcentage)
   - Critère : Perméabilité classe A*4
   - Échantillonnage : pourcentage, pct = 10, base = 45

**Barème** :
- Structure JSON correcte : 5 points
- Métadonnées complètes : 2 points
- 5 essais correctement définis : 10 points (2 pts/essai)
- Cohérence échantillonnage/fréquence : 3 points

---

### Partie B : Planification des essais (15 points)

**Consigne** : Créez un fichier `quantites_ecole.json` et exécutez le planificateur.

**Quantitatifs** :
```json
{
  "projet": "École maternelle Les Hirondelles",
  "volume_beton_m3": 280,
  "surface_m2": 520,
  "base": 45
}
```

**Commande** :
```bash
python MODULE_06/03_scripts/planificateur_essais.py \
  --plan plan_ecole.json \
  --quantites quantites_ecole.json \
  --out planning_ecole.json
```

**Questions** :
1. Combien de séries d'essais béton sont planifiées ? (2 points)
2. Combien de mesures de planéité chapes ? (2 points)
3. Combien de contrôles d'étanchéité menuiseries ? (2 points)
4. Vérifiez les calculs manuellement pour chaque essai. (6 points)
5. Identifiez l'essai le plus fréquent. (3 points)

**Réponses attendues** :
1. BET-R28 : ceil(280 / 150) = 2 séries
2. CHA-PLAN : ceil(520 / 25) = 21 mesures
3. MENU-AIR : ceil(45 * 10 / 100) = 5 contrôles (10% de 45)
4. Détail des calculs (voir ci-dessus)
5. CHA-PLAN (21 mesures)

---

### Partie C : Saisie et validation des PV (25 points)

**Consigne** : Créez un fichier `pv_ecole.json` avec les PV suivants, puis validez-les.

**PV reçus** :

1. **PV-BET-001** : Résistance béton Série 1
   - Zone : Fondations
   - Date : 2025-09-10
   - Valeurs : 27.2, 26.8, 27.5 MPa → Moyenne 27.2 MPa
   - Conformité laboratoire : OK

2. **PV-BET-002** : Résistance béton Série 2
   - Zone : Dalles R+1
   - Date : 2025-09-24
   - Valeurs : 24.1, 23.9, 24.3 MPa → Moyenne 24.1 MPa
   - Conformité laboratoire : KO (< 25 MPa)

3. **PV-CHA-001** : Planéité chape Salle 101
   - Date : 2025-10-05
   - Valeur : 3 mm
   - Conformité : OK

4. **PV-CHA-002** : Planéité chape Salle 102
   - Date : 2025-10-05
   - Valeur : 7 mm
   - Conformité : KO (> 5 mm)

5. **PV-MENU-001** : Étanchéité fenêtre F12
   - Date : 2025-10-18
   - Valeur : Classe A*3
   - Conformité : KO (A*3 < A*4)

**Commande** :
```bash
python MODULE_06/03_scripts/validate_pv_vs_exigences.py \
  --plan plan_ecole.json \
  --pv pv_ecole.json \
  --out pv_valides_ecole.json
```

**Questions** :
1. Créez le fichier `pv_ecole.json` conforme au schéma. (10 points)
2. Exécutez le script de validation. (3 points)
3. Vérifiez que la conformité calculée correspond à la conformité déclarée. (5 points)
4. Listez les PV non conformes et proposez une action corrective pour chacun. (7 points)

**Réponses attendues** :
- PV non conformes : PV-BET-002, PV-CHA-002, PV-MENU-001
- Actions correctives :
  - PV-BET-002 : Note de calcul BET pour justification ou reprise béton
  - PV-CHA-002 : Ragréage chape ou dérogation avec justification
  - PV-MENU-001 : Remplacement fenêtre ou tests complémentaires

---

### Partie D : Analyse KPIs et pilotage (25 points)

**Consigne** : Exécutez le script KPI et analysez les résultats.

```bash
python MODULE_06/03_scripts/kpi_essais.py \
  --planning planning_ecole.json \
  --pv pv_ecole.json
```

**Questions** :

1. **Taux de couverture par essai** (10 points)
   - BET-R28 : Planifié vs Réalisé
   - CHA-PLAN : Planifié vs Réalisé
   - CHA-EPAIS : Planifié vs Réalisé
   - MENU-AIR : Planifié vs Réalisé
   - BET-SLUMP : Planifié vs Réalisé

2. **Taux de conformité par essai** (5 points)
   - BET-R28 : % conforme
   - CHA-PLAN : % conforme
   - MENU-AIR : % conforme

3. **Couverture globale** (3 points)
   - Total planifié / Total réalisé / %

4. **Identification des priorités** (7 points)
   - Quels essais ont une couverture < 20% ?
   - Quels essais ont un taux de conformité < 70% ?
   - Proposez un plan d'action priorisé pour les 2 prochaines semaines

**Réponses attendues** :

1. Taux de couverture :
   - BET-R28 : 2 planifiés / 2 réalisés = 100%
   - CHA-PLAN : 21 planifiés / 2 réalisés = 9.5%
   - CHA-EPAIS : 11 planifiés / 0 réalisé = 0%
   - MENU-AIR : 5 planifiés / 1 réalisé = 20%
   - BET-SLUMP : 1 planifié / 0 réalisé = 0%

2. Taux de conformité :
   - BET-R28 : 1/2 = 50%
   - CHA-PLAN : 1/2 = 50%
   - MENU-AIR : 0/1 = 0%

3. Couverture globale : 5 réalisés / 40 planifiés = 12.5%

4. Plan d'action priorisé :
   - **URGENT** : CHA-EPAIS (0% couverture) → Planifier 11 mesures immédiatement
   - **URGENT** : CHA-PLAN (9.5% couverture) → Planifier 19 mesures manquantes
   - **PRIORITAIRE** : BET-SLUMP (0% couverture) → Contrôler prochaine livraison
   - **CORRECTIF** : PV-BET-002 (NC béton) → Note de calcul BET sous 48h
   - **CORRECTIF** : PV-CHA-002 (NC planéité) → Ragréage Salle 102
   - **CORRECTIF** : PV-MENU-001 (NC étanchéité) → Contrôle contradictoire ou remplacement

---

### Partie E : Reporting et traçabilité (15 points)

**Consigne** : Rédigez un rapport de synthèse pour la réunion de chantier hebdomadaire.

**Structure attendue** :

```markdown
# Rapport hebdomadaire - Essais et contrôles
## Projet : École maternelle Les Hirondelles
## Date : 2025-11-20

### 1. Synthèse globale
- Taux de couverture : XX%
- Taux de conformité : XX%
- Nombre de NC actives : X

### 2. Avancement par lot
#### Lot Gros-œuvre
- BET-R28 : X/X réalisés (XX%)
- BET-SLUMP : X/X réalisés (XX%)
- Points d'attention : [...]

#### Lot Chapes
- CHA-PLAN : X/X réalisés (XX%)
- CHA-EPAIS : X/X réalisés (XX%)
- Points d'attention : [...]

#### Lot Menuiseries
- MENU-AIR : X/X réalisés (XX%)
- Points d'attention : [...]

### 3. Non-conformités
| PV | Essai | Écart | Gravité | Action | Délai | Responsable |
|----|-------|-------|---------|--------|-------|-------------|
| ... | ... | ... | ... | ... | ... | ... |

### 4. Actions prioritaires semaine prochaine
1. [Action 1]
2. [Action 2]
3. [Action 3]

### 5. Prévisions à J+15
- Essais à planifier : [...]
- Risques identifiés : [...]
```

**Barème** :
- Structure complète du rapport : 5 points
- Données chiffrées exactes : 5 points
- Tableau NC complet et pertinent : 3 points
- Actions prioritaires cohérentes : 2 points

---

## 📖 Partie 4 : Ressources et bonnes pratiques

### 4.1 Modes d'échantillonnage

| Mode | Usage | Exemple | Calcul |
|------|-------|---------|--------|
| **fixe** | Nombre constant | 1 essai destructif sur lot complet | `nb = 1` |
| **pourcentage** | % d'une population | 10% des menuiseries | `ceil(base * pct / 100)` |
| **surface** | Fréquence par m² | 1 mesure / 20 m² de chape | `ceil(surface_totale / surface)` |
| **unites_ouvrage** | Fréquence par volume/quantité | 1 série / 150 m³ béton | `ceil(volume_total / par_volume_m3)` |

### 4.2 Bonnes pratiques de saisie des PV

✅ **À faire** :
- Toujours renseigner le champ "fichier" (lien vers PV PDF signé)
- Utiliser des ID uniques et traçables (ex: PV-BET-001, PV-CHA-002)
- Renseigner la zone/ouvrage pour localisation
- Saisir toutes les valeurs brutes (éprouvettes) et la moyenne
- Indiquer la conformité déclarée par le laboratoire

❌ **À éviter** :
- PV sans référence au fichier original
- Valeurs arrondies ou approximatives
- Absence de date de prélèvement
- Confusion entre conformité déclarée et calculée

### 4.3 Gestion des non-conformités

**Workflow recommandé** :

1. **Détection** : Validation automatique des PV (script `validate_pv_vs_exigences.py`)
2. **Enregistrement** : Création d'une NC dans le registre du MODULE_05
3. **Analyse** : Gravité (mineure/majeure/critique), cause racine
4. **Action** :
   - Correction immédiate (reprise, ragréage)
   - Dérogation justifiée (note de calcul BET)
   - Renforcement (armatures complémentaires)
5. **Traçabilité** : Lien PV → NC → Action → Preuve de levée
6. **Clôture** : Validation maître d'œuvre + archivage DOE

### 4.4 KPIs de pilotage recommandés

**Indicateurs de couverture** :
- Taux de couverture global : `réalisés / planifiés`
- Taux de couverture par lot
- Taux de couverture par essai
- Écart planning (nombre d'essais en retard)

**Indicateurs de conformité** :
- Taux de conformité global : `conformes / réalisés`
- Taux de NC par lot
- Temps moyen de levée de NC
- % NC avec dérogation vs reprise

**Indicateurs de traçabilité** :
- % PV avec fichier joint
- % PV avec accréditation COFRAC
- % essais avec preuves complètes (DOE)

**Seuils d'alerte recommandés** :
- Couverture < 80% → Alerte jaune
- Couverture < 50% → Alerte rouge
- Conformité < 90% → Analyse causes
- Conformité < 70% → Revue qualité urgente

### 4.5 Intégration avec les autres modules

**MODULE_01 (Wrappers IA)** :
- Wrapper 2 : Vérifier les références normatives (NF EN, NF DTU)
- Wrapper 3 : Tableaux de validation PV (source vs critère)
- Wrapper 6 : Journal des sources (PV, BL béton, fiches techniques)

**MODULE_04 (Production documentaire)** :
- Export des CR de chantier avec statut des essais
- Intégration planning essais dans CCTP

**MODULE_05 (Conformité normative)** :
- Enregistrement des NC détectées
- Preuves de conformité (PV comme preuve)
- Registre normatif (exigences → essais)

**Workflow intégré type** :
```
MODULE_06 : Détection NC (PV non conforme)
    ↓
MODULE_05 : Enregistrement NC + Qualification
    ↓
MODULE_04 : Mention dans CR chantier
    ↓
MODULE_01 : Analyse avec wrapper 5 (matrice avantages/risques)
    ↓
MODULE_05 : Action corrective + Preuve de levée
    ↓
MODULE_06 : Mise à jour KPI + Archivage DOE
```

### 4.6 Archivage et DOE

**Documents à archiver** :
- Plan de contrôle JSON + version PDF
- Planning des essais JSON + version Excel
- Tous les PV (PDF originaux + JSON structuré)
- Rapport de validation (pv_valides.json)
- Rapport KPI (capture ou export)
- Registre des NC associées

**Format d'archivage recommandé** :
- JSON : Traçabilité et exploitation ultérieure
- PDF/A : Archivage probant (norme ISO 19005)
- SHA-256 : Hash de chaque fichier pour intégrité

**Structure DOE recommandée** :
```
DOE/
├── 01_Plans_controle/
│   ├── plan_controle_v1.0.json
│   ├── plan_controle_v1.0.pdf
│   └── PACKAGE_SHA256.txt
├── 02_Planning/
│   ├── planning_essais.json
│   └── planning_essais.xlsx
├── 03_PV/
│   ├── PV-BET-001.pdf
│   ├── PV-BET-002.pdf
│   └── pv_tous.json
├── 04_Validations/
│   ├── pv_valides.json
│   └── rapport_kpi_final.pdf
└── 05_NC/
    ├── registre_nc.json
    └── preuves_levee/
```

---

## 📝 Annexes

### Annexe A : Référentiel normatif

**Normes essais béton** :
- NF EN 206/CN : Béton - Spécification, performance, production et conformité
- NF EN 12350-2 : Essais pour béton frais - Essai d'affaissement
- NF EN 12390-3 : Essais pour béton durci - Résistance à la compression

**Normes chapes** :
- NF DTU 26.2 (Avril 2008) : Chapes et dalles à base de liants hydrauliques
- NF P 14-201 : Planéité des supports

**Normes menuiseries** :
- NF DTU 36.5 : Mise en œuvre des fenêtres et portes extérieures
- NF EN 12207 : Perméabilité à l'air

### Annexe B : Exemples de fréquences normatives

| Ouvrage | Essai | Fréquence normative | Référence |
|---------|-------|---------------------|-----------|
| Béton | Résistance (éprouvettes) | 1 série / 150 m³ ou 1/jour si < 150 m³ | NF EN 206/CN |
| Béton | Affaissement (slump) | 1 par camion | NF EN 12350-2 |
| Chape | Planéité | Selon classe P1-P5 | NF DTU 26.2 |
| Chape | Épaisseur | 1 / 50 m² mini | NF DTU 26.2 |
| Menuiserie | Étanchéité air/eau | 10% ou 1 par type | NF DTU 36.5 |
| Étanchéité toiture | Essai d'eau | 100% surface | NF DTU 43.x |

### Annexe C : Glossaire

**BL** : Bordereau de Livraison
**COFRAC** : Comité Français d'Accréditation
**DOE** : Dossier des Ouvrages Exécutés
**DOD** : Document d'Origine du Donataire (fiche béton)
**fck** : Résistance caractéristique en compression du béton (MPa)
**KPI** : Key Performance Indicator (indicateur de performance)
**NC** : Non-Conformité
**OPR** : Opération Préalable à la Réception
**PV** : Procès-Verbal (d'essai, de contrôle)

### Annexe D : Scripts Python - Mode d'emploi

**Installation** :
Aucune dépendance externe requise (Python 3.8+ avec bibliothèque standard).

**Usage type** :

```bash
# 1. Planifier les essais
python MODULE_06/03_scripts/planificateur_essais.py \
  --plan mon_plan.json \
  --quantites mes_quantites.json \
  --out mon_planning.json

# 2. Valider les PV
python MODULE_06/03_scripts/validate_pv_vs_exigences.py \
  --plan mon_plan.json \
  --pv mes_pv.json \
  --out pv_valides.json

# 3. Calculer l'échantillonnage
python MODULE_06/03_scripts/echantillonnage_calcul.py \
  --essai_id BET-R28 \
  --plan mon_plan.json \
  --quantites mes_quantites.json

# 4. Générer les KPIs
python MODULE_06/03_scripts/kpi_essais.py \
  --planning mon_planning.json \
  --pv mes_pv.json
```

**Personnalisation** :
Les scripts sont conçus comme des bases opérationnelles. Vous pouvez les adapter :
- Ajouter des modes d'échantillonnage personnalisés
- Modifier les règles de validation
- Ajouter des exports (Excel, PDF)
- Intégrer des API laboratoires

---

## 🎓 Conclusion

Vous avez maintenant parcouru l'ensemble du MODULE_06 de Stone-Sea. Ces outils vous permettent de :

✅ **Structurer** : Plans de contrôle normalisés et traçables
✅ **Planifier** : Calcul automatique des essais requis
✅ **Valider** : Contrôle automatique de la conformité des PV
✅ **Piloter** : KPIs temps réel pour décisions rapides
✅ **Tracer** : Archivage complet pour DOE et contentieux

**Prochaines étapes** :
1. Appliquer le MODULE_06 sur un chantier pilote
2. Former les équipes (conducteurs de travaux, chefs de chantier)
3. Intégrer avec les autres modules Stone-Sea (01, 04, 05)
4. Automatiser les exports (dashboards, rapports hebdomadaires)
5. Constituer une base de données de référence par type d'ouvrage

**Rappel important** :
Les scripts et schémas fournis constituent une **base opérationnelle**. Ils doivent être adaptés :
- Aux spécificités de chaque projet (CCTP, notes de calcul)
- Aux éditions en vigueur des normes
- Aux exigences du maître d'ouvrage et du contrôleur technique
- Aux procédures qualité de votre entreprise

La validation humaine par un professionnel qualifié reste **obligatoire** pour toute décision engageante (levée de réserve, dérogation, reprise d'ouvrage).

---

**Auteur** : Formation Stone-Sea MODULE_06
**Date de création** : 2025-11-20
**Version** : 1.0
