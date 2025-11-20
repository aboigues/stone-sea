# TP MODULE 05 - Conformité Normative BTP

**Formation pratique aux outils de contrôle de conformité normative**

---

## 📋 Informations générales

**Durée estimée** : 4 heures
**Niveau** : Intermédiaire
**Prérequis** :
- Connaissances solides du secteur BTP et des normes (DTU, Eurocodes)
- Familiarité avec les documents techniques (CCTP, PV, CR chantier)
- Notions de base en JSON et Python (lecture de scripts)
- Avoir complété le MODULE_01 (Wrappers IA)
- Avoir lu le README du MODULE_05

**Objectifs pédagogiques** :
1. Maîtriser la structuration des exigences normatives au format JSON
2. Utiliser les scripts de contrôle pour vérifier la conformité CCTP/PV
3. Qualifier et gérer les non-conformités (NC) de manière systématique
4. Produire des rapports de conformité et tableaux de bord KPIs
5. Garantir la traçabilité complète du processus de contrôle

---

## 📚 Partie 1 : Contexte et enjeux (20 min)

### 1.1 Pourquoi la conformité normative est-elle critique en BTP ?

Dans le secteur du bâtiment, le non-respect des normes techniques peut entraîner :

- **Risques juridiques** : Responsabilité décennale, contentieux, pénalités contractuelles
- **Risques techniques** : Défauts structurels, pathologies, non-conformités RE2020
- **Risques financiers** : Reprises de travaux coûteuses, retards de chantier, refus de réception
- **Risques réglementaires** : Non-conformité aux DTU, Eurocodes, Avis Techniques
- **Risques assurantiels** : Refus de prise en charge par les assurances

**Chiffres clés** :
- 60% des sinistres en construction résultent d'écarts aux DTU
- Coût moyen d'une reprise de non-conformité majeure : 15 000 € à 80 000 €
- Délai moyen de résolution d'un contentieux normatif : 18 mois

Le MODULE_05 de Stone-Sea fournit un **système de contrôle systématique** pour :
- ✅ Identifier les exigences normatives applicables à chaque lot
- ✅ Contrôler automatiquement les CCTP, PV et CR
- ✅ Tracer les non-conformités et piloter leur résolution
- ✅ Produire des rapports opposables et auditables

### 1.2 Les 4 processus clés du MODULE_05

| Processus | Outil principal | Cas d'usage |
|-----------|----------------|-------------|
| **1 - Structuration des exigences** | Schémas JSON | Définir le référentiel normatif du projet |
| **2 - Contrôle CCTP vs normes** | `check_cctp_vs_normes.py` | Vérifier la couverture normative du CCTP |
| **3 - Vérification des preuves** | `check_cr_pv_preuves.py` | Contrôler que les PV/CR apportent les preuves |
| **4 - Pilotage des NC et KPIs** | `nc_register_merge.py` + `dashboard_kpis.py` | Suivi de la conformité globale |

### 1.3 Architecture du MODULE_05

```
MODULE_05/
├── 01_schemas/          → Structures JSON (exigences, preuves, NC, registre)
├── 02_regles/           → Référentiels normatifs pré-remplis (couverture, menuiseries)
├── 03_scripts/          → 4 scripts Python (contrôle, fusion, KPIs)
├── 04_prompts/          → Prompts IA pour assistance au contrôle
├── 05_modeles/          → Templates de rapports et registres
├── 06_examples/         → Exemples concrets (CCTP, exigences, registre)
└── 07_docs/             → Documentation d'intégration
```

---

## 🎯 Partie 2 : Exercices pratiques

### Exercice 1 : Structurer une exigence normative (JSON)

**Objectif** : Apprendre à traduire une clause de norme en exigence structurée au format JSON

**Contexte** : Vous préparez le contrôle d'un chantier de couverture. Vous devez extraire les exigences du NF DTU 40.21 et les structurer dans le référentiel normatif du projet.

**Extrait de norme fourni** :
```
NF DTU 40.21 - Couverture en tuiles de terre cuite à emboîtement
ou à glissement à relief (Mai 2019)

Section 5.2.1 - Pente minimale
"La pente minimale de la couverture doit être déterminée selon :
- La zone de neige (A, B, C, D, E)
- L'exposition au vent (site normal, protégé, exposé)
- Le type de tuile (selon Avis Technique)

Pour une tuile grand moule en zone B site normal : pente minimale = 25%."

Section 5.3.2 - Écran sous-toiture
"Un écran souple de type HPV (Haute Perméabilité à la Vapeur) conforme
au CPT 3651-v3 doit être mis en œuvre. Recouvrements : 10 cm minimum
en partie courante, 20 cm au faîtage."
```

**Consigne** :
1. Ouvrez le fichier `MODULE_05/01_schemas/exigence_normative.schema.json` pour comprendre la structure
2. Créez deux exigences JSON (une pour la pente, une pour l'écran HPV)
3. Remplissez tous les champs obligatoires

**Réponse attendue** :

```json
{
  "exigences": [
    {
      "id": "COV-001",
      "lot": "Couverture",
      "objet_ouvrage": "Couverture tuiles terre cuite",
      "ref_norme": "NF DTU 40.21",
      "edition": "Mai 2019",
      "paragraphe": "Section 5.2.1",
      "intitule": "Pente minimale selon zone et exposition",
      "type_controle": "documentaire",
      "critere_acceptation": "Pente ≥ seuil tableau selon zone/exposition/tuile",
      "severite": "majeure",
      "mots_cles": [
        "pente",
        "zone neige",
        "exposition",
        "tuile",
        "DTU 40.21"
      ],
      "preuves_attendues": [
        "CCTP : mention pente et zone climatique",
        "Plans : indication pente sur coupes",
        "Fiche technique tuile : pente mini selon AT"
      ]
    },
    {
      "id": "COV-002",
      "lot": "Couverture",
      "objet_ouvrage": "Écran sous-toiture",
      "ref_norme": "NF DTU 40.21",
      "edition": "Mai 2019",
      "paragraphe": "Section 5.3.2",
      "intitule": "Écran HPV conforme CPT 3651 avec recouvrements",
      "type_controle": "visuel",
      "critere_acceptation": "Écran HPV CPT 3651 + recouvrements ≥ 10 cm (20 cm faîtage)",
      "severite": "majeure",
      "mots_cles": [
        "écran",
        "HPV",
        "CPT 3651",
        "recouvrement"
      ],
      "preuves_attendues": [
        "CCTP : spécification écran HPV",
        "Fiche produit : conformité CPT 3651-v3",
        "Photos chantier : recouvrements visibles",
        "PV réception support : écran posé avant tuiles"
      ]
    }
  ]
}
```

**Points de vérification** :
- ✅ Chaque exigence a un ID unique (COV-XXX pour couverture)
- ✅ Référence normative complète avec édition
- ✅ Sévérité justifiée (majeure : risque étanchéité)
- ✅ Mots-clés pertinents pour recherche automatique
- ✅ Preuves attendues listées (CCTP, AT, photos, PV)

---

### Exercice 2 : Contrôler un CCTP avec le script Python

**Objectif** : Utiliser `check_cctp_vs_normes.py` pour vérifier la couverture normative d'un CCTP

**Contexte** : Le maître d'œuvre vous transmet un CCTP pour validation. Vous devez vérifier que toutes les exigences du lot couverture sont bien couvertes.

**Documents fournis** :

**Fichier `cctp_projet_alpilles.md`** :
```markdown
# CCTP - Résidence Les Alpilles

## LOT 03 - COUVERTURE

### Article 3.1 - Généralités
La couverture sera réalisée en tuiles terre cuite grand moule de type OMEGA 10.
Zone climatique : Zone B (Provence).
Site d'implantation : site normal (résidentiel périurbain).

### Article 3.2 - Support et écran
Charpente traditionnelle avec voliges.
Écran sous-toiture : écran souple respirant conforme au CPT 3651-v3.
Recouvrements conformes aux prescriptions du fabricant.

### Article 3.3 - Pose des tuiles
Pose selon NF DTU 40.21.
Pente de toiture : 28%.
Fixation des tuiles selon prescriptions de l'Avis Technique.
```

**Fichier `exigences_couverture.json`** :
```json
{
  "exigences": [
    {
      "id": "COV-001",
      "lot": "Couverture",
      "objet_ouvrage": "Couverture tuiles",
      "ref_norme": "NF DTU 40.21",
      "edition": "Mai 2019",
      "paragraphe": "Section 5.2.1",
      "intitule": "Pente minimale selon zone et exposition",
      "type_controle": "documentaire",
      "critere_acceptation": "Pente ≥ 25% (zone B site normal grand moule)",
      "severite": "majeure",
      "mots_cles": ["pente", "zone", "exposition", "DTU 40.21"]
    },
    {
      "id": "COV-002",
      "lot": "Couverture",
      "objet_ouvrage": "Écran sous-toiture",
      "ref_norme": "NF DTU 40.21",
      "edition": "Mai 2019",
      "paragraphe": "Section 5.3.2",
      "intitule": "Écran HPV conforme CPT 3651",
      "type_controle": "documentaire",
      "criterе_acceptation": "Écran HPV CPT 3651 + recouvrements 10 cm mini",
      "severite": "majeure",
      "mots_cles": ["écran", "HPV", "CPT 3651", "recouvrement"]
    },
    {
      "id": "COV-003",
      "lot": "Couverture",
      "objet_ouvrage": "Tuiles terre cuite",
      "ref_norme": "NF DTU 40.21",
      "edition": "Mai 2019",
      "paragraphe": "Section 4.1",
      "intitule": "Tuiles conformes à Avis Technique en vigueur",
      "type_controle": "documentaire",
      "critere_acceptation": "Référence Avis Technique + date de validité",
      "severite": "majeure",
      "mots_cles": ["Avis Technique", "tuile", "AT"]
    }
  ]
}
```

**Consigne** :
1. Placez-vous dans le répertoire `MODULE_05/03_scripts/`
2. Exécutez la commande :
```bash
python3 check_cctp_vs_normes.py \
  --cctp ../06_examples/cctp_projet_alpilles.md \
  --exigences ../06_examples/exigences_couverture.json \
  --out_json rapport_alpilles.json \
  --out_md rapport_alpilles.md
```
3. Analysez les résultats (STDOUT, JSON, Markdown)

**Réponse attendue** :

**Sortie STDOUT** :
```
[CCTP] Exigences: 3 | OK: 2 | KO: 1 | Taux OK: 66.7%
```

**Contenu `rapport_alpilles.json`** (extrait) :
```json
{
  "meta": {
    "date": "2025-11-20T10:30:00Z"
  },
  "resultats": [
    {
      "exigence_id": "COV-001",
      "ref_norme": "NF DTU 40.21",
      "severite": "majeure",
      "intitule": "Pente minimale selon zone et exposition",
      "doc_presence": "OK",
      "mots_cles_trouves": ["pente", "zone", "DTU 40.21"]
    },
    {
      "exigence_id": "COV-002",
      "ref_norme": "NF DTU 40.21",
      "severite": "majeure",
      "intitule": "Écran HPV conforme CPT 3651",
      "doc_presence": "OK",
      "mots_cles_trouves": ["écran", "CPT 3651"]
    },
    {
      "exigence_id": "COV-003",
      "ref_norme": "NF DTU 40.21",
      "severite": "majeure",
      "intitule": "Tuiles conformes à Avis Technique en vigueur",
      "doc_presence": "KO",
      "mots_cles_trouves": []
    }
  ],
  "synthese": {
    "total": 3,
    "OK": 2,
    "KO": 1,
    "taux_ok": 66.7
  }
}
```

**Analyse des résultats** :

| Exigence | Statut | Commentaire |
|----------|--------|-------------|
| COV-001 (Pente) | ✅ OK | CCTP mentionne "pente 28%" et "zone B" |
| COV-002 (Écran HPV) | ✅ OK | CCTP cite "CPT 3651-v3" |
| COV-003 (Avis Technique) | ❌ KO | CCTP ne mentionne pas l'AT de la tuile OMEGA 10 |

**Action corrective requise** :
→ Compléter l'article 3.1 du CCTP avec : *"Tuiles OMEGA 10 conformes à l'Avis Technique n° [numéro] en vigueur à la date de signature du marché."*

---

### Exercice 3 : Qualifier une non-conformité (NC)

**Objectif** : Savoir qualifier une NC selon sa gravité et proposer une action corrective

**Contexte** : Lors d'une visite chantier, vous constatez que l'écran sous-toiture a été posé avec des recouvrements de seulement 5 cm au lieu des 10 cm prescrits.

**Exigence de référence** (COV-002) :
```json
{
  "id": "COV-002",
  "ref_norme": "NF DTU 40.21",
  "edition": "Mai 2019",
  "paragraphe": "Section 5.3.2",
  "intitule": "Écran HPV - Recouvrements minimaux",
  "critere_acceptation": "Recouvrements ≥ 10 cm partie courante, ≥ 20 cm faîtage",
  "severite": "majeure"
}
```

**Constat** :
- Date : 18/11/2024
- Localisation : Bâtiment A, versant Sud, zones 3 à 7
- Mesuré : Recouvrements entre 4 cm et 6 cm
- Photos : IMG_1234.jpg à IMG_1239.jpg

**Consigne** :
1. Utilisez le schéma `MODULE_05/01_schemas/nc.schema.json`
2. Créez une fiche NC structurée
3. Qualifiez la gravité (mineure, majeure, critique)
4. Proposez une action corrective et un délai

**Réponse attendue** :

```json
{
  "nc_id": "NC-2024-011",
  "date_constat": "2024-11-18",
  "exigence_id": "COV-002",
  "ref_norme": "NF DTU 40.21 (Mai 2019) - Section 5.3.2",
  "description": "Recouvrements écran sous-toiture insuffisants : 4 à 6 cm constatés au lieu de 10 cm minimum prescrits",
  "localisation": "Bâtiment A, versant Sud, zones 3 à 7",
  "gravite": "majeure",
  "justification_gravite": "Risque d'infiltration d'eau par les joints mal recouverts, compromettant l'étanchéité de la sous-toiture. Pathologie potentielle : humidification charpente.",
  "statut": "ouvert",
  "action_corrective_proposee": "Dépose partielle des tuiles zones 3-7, repositionnement de l'écran avec recouvrements conformes (≥10 cm), repose tuiles",
  "responsable_action": "Entreprise COUV-PRO (titulaire lot couverture)",
  "delai_cible": "2024-11-29",
  "preuves": [
    "Photos IMG_1234.jpg à IMG_1239.jpg",
    "Mesures contradictoires avec maître d'œuvre (PV du 18/11/2024)",
    "Plan de calepinage écran (version initiale non respectée)"
  ],
  "risque_residuel": "Infiltrations, dégradation charpente, refus de réception",
  "cout_estime_reprise": "3 500 € HT (dépose/repose 45 m²)"
}
```

**Grille de qualification de gravité** :

| Gravité | Définition | Exemples | Délai type |
|---------|------------|----------|------------|
| **Mineure** | Écart sans impact structurel ni fonctionnel | Défaut esthétique, tolérance dépassée de <10% | 2 mois |
| **Majeure** | Écart avec risque pathologique ou dysfonctionnel | Non-conformité DTU, risque infiltration, résistance | 1 mois |
| **Critique** | Écart avec danger immédiat ou impossibilité d'usage | Risque effondrement, insécurité, inhabitable | 1 semaine |

**Ici : gravité MAJEURE** car risque d'infiltration avéré, mais pas de danger immédiat.

---

### Exercice 4 : Gérer le registre des NC

**Objectif** : Utiliser `nc_register_merge.py` pour consolider plusieurs registres de NC

**Contexte** : Vous avez 3 lots (Gros Œuvre, Couverture, Menuiseries). Chaque entreprise a produit son propre registre NC. Vous devez fusionner ces registres pour avoir une vue consolidée.

**Fichiers fournis** :
- `nc_go.json` (5 NC lot Gros Œuvre)
- `nc_couverture.json` (3 NC lot Couverture)
- `nc_menuiseries.json` (7 NC lot Menuiseries)

**Consigne** :
1. Créez les 3 fichiers JSON avec quelques NC de test
2. Exécutez :
```bash
python3 nc_register_merge.py \
  --inputs nc_go.json nc_couverture.json nc_menuiseries.json \
  --output nc_registre_consolide.json
```
3. Vérifiez la sortie consolidée

**Exemple de NC dans `nc_go.json`** :
```json
{
  "ncs": [
    {
      "nc_id": "NC-GO-001",
      "date_constat": "2024-10-12",
      "exigence_id": "GO-015",
      "description": "Enrobage armatures < 20 mm (mesuré 17 mm)",
      "gravite": "mineure",
      "statut": "clos",
      "date_cloture": "2024-10-25"
    },
    {
      "nc_id": "NC-GO-002",
      "date_constat": "2024-11-03",
      "exigence_id": "GO-022",
      "description": "Résistance béton 23 MPa au lieu de 25 MPa",
      "gravite": "majeure",
      "statut": "ouvert"
    }
  ]
}
```

**Réponse attendue** :

Après fusion, `nc_registre_consolide.json` contient :
```json
{
  "meta": {
    "date_fusion": "2024-11-20T11:00:00Z",
    "fichiers_sources": [
      "nc_go.json",
      "nc_couverture.json",
      "nc_menuiseries.json"
    ]
  },
  "ncs": [
    // 15 NC au total (5 + 3 + 7)
    // Toutes les NC des 3 fichiers consolidées
  ],
  "statistiques": {
    "total_nc": 15,
    "ouvertes": 8,
    "closes": 7,
    "par_gravite": {
      "mineure": 4,
      "majeure": 9,
      "critique": 2
    }
  }
}
```

**Usage** : Ce registre consolidé devient la **source unique de vérité** pour le pilotage des NC du projet.

---

### Exercice 5 : Générer les KPIs de conformité

**Objectif** : Utiliser `dashboard_kpis.py` pour calculer le taux de conformité global

**Contexte** : Vous devez présenter l'état de la conformité au comité de pilotage. Vous utilisez le registre normatif complet du projet.

**Fichier fourni `registre_projet_alpilles.json`** :
```json
{
  "projet": "Résidence Les Alpilles",
  "date": "2024-11-20",
  "exigences": [
    {"id": "GO-001", "lot": "Gros Œuvre", "severite": "majeure"},
    {"id": "GO-002", "lot": "Gros Œuvre", "severite": "majeure"},
    {"id": "COV-001", "lot": "Couverture", "severite": "majeure"},
    {"id": "COV-002", "lot": "Couverture", "severite": "majeure"},
    {"id": "MEN-001", "lot": "Menuiseries", "severite": "critique"}
  ],
  "preuves": [
    {"exigence_id": "GO-001", "resultat": "OK", "date": "2024-10-15"},
    {"exigence_id": "GO-002", "resultat": "OK", "date": "2024-10-20"},
    {"exigence_id": "COV-001", "resultat": "OK", "date": "2024-11-10"},
    {"exigence_id": "COV-002", "resultat": "KO", "date": "2024-11-12"}
  ],
  "ncs": [
    {"nc_id": "NC-001", "exigence_id": "COV-002", "gravite": "majeure", "statut": "ouvert"},
    {"nc_id": "NC-002", "exigence_id": "MEN-001", "gravite": "critique", "statut": "ouvert"}
  ]
}
```

**Consigne** :
1. Exécutez :
```bash
python3 dashboard_kpis.py --registre registre_projet_alpilles.json
```
2. Analysez les KPIs affichés

**Réponse attendue** :

```
=== KPIs conformité ===
- Exigences applicables: 5
- Exigences avec ≥1 preuve OK: 3
- Taux de conformité (approx.): 60.0%
- NC ouvertes: 2
- NC majeures ouvertes: 1
```

**Interprétation** :
- **Taux de conformité 60%** : Seulement 3 exigences sur 5 sont couvertes par des preuves conformes
- **2 NC ouvertes** dont **1 critique** (MEN-001) → Action prioritaire requise
- **Exigences sans preuve** : MEN-001 (critique) → Nécessite contrôle urgent

**Actions pour comité de pilotage** :
1. 🔴 **Priorité 1** : Contrôler MEN-001 (critique, sans preuve)
2. 🟠 **Priorité 2** : Clôturer NC-001 (COV-002, majeure ouverte)
3. 🟡 **Priorité 3** : Apporter preuve pour COV-002

---

## 🏆 Partie 3 : Évaluation finale - Cas pratique intégré (1h15)

### Contexte général

Vous êtes conducteur de travaux sur la **Résidence Les Cèdres**, immeuble de logements collectifs. Le lot **Menuiseries extérieures** est en phase de réception. Le maître d'œuvre vous demande de produire un **rapport de conformité complet** avant la levée des réserves.

**Documents fournis** :

### Document 1 - Extrait CCTP Menuiseries

```markdown
# CCTP - Résidence Les Cèdres

## LOT 05 - MENUISERIES EXTÉRIEURES

### Article 5.1 - Fenêtres PVC
Fenêtres PVC 2 vantaux oscillo-battants.
Dimensions courantes : 1,35 m × 1,45 m (L × H).
Vitrage : double vitrage 4/16/4 faiblement émissif, argon.
Performance thermique : Uw ≤ 1,4 W/m².K.
Performance acoustique : Rw ≥ 32 dB.

### Article 5.2 - Pose
Pose en applique avec isolation thermique renforcée (ITR).
Fixation selon NF DTU 36.5 (Octobre 2010).
Étanchéité : joints de calfeutrement SNJF, épaisseur ≥ 5 mm.

### Article 5.3 - Normes applicables
- NF DTU 36.5 - Mise en œuvre fenêtres et portes extérieures
- Cahier CSTB 3606 - Menuiseries PVC
```

### Document 2 - PV de contrôle menuiseries

```
PROCES-VERBAL DE CONTRÔLE N° 2024-MEN-0156
Organisme : Bureau Véritas - Accréditation COFRAC

Chantier : Résidence Les Cèdres - Bâtiment C
Date contrôle : 15/11/2024
Échantillon : Fenêtres F08, F12, F15, F22 (4 fenêtres)

--- Fenêtre F12 (Appartement C304, Séjour) ---
Dimensions : 1,35 m × 1,60 m

1) Fixation (NF DTU 36.5 section 6.2.3)
Exigence : Hauteur > 1,50 m → 4 fixations par montant
Constaté : 3 fixations par montant (insuffisant)
→ NON CONFORME

2) Répartition fixations
Exigence : Point à 15 cm max des angles
Constaté : Fixation haute à 22 cm de l'angle
→ NON CONFORME

3) Joint périphérique (NF DTU 36.5 section 6.3.1)
Exigence : Joint continu ≥ 5 mm
Constaté : Joint présent mais discontinu (absent sur traverse haute)
→ NON CONFORME

4) Performance thermique (selon fiche produit)
Exigence : Uw ≤ 1,4 W/m².K
Constaté : Certificat ACOTHERM Uw = 1,3 W/m².K
→ CONFORME

--- Fenêtres F08, F15, F22 ---
Contrôles identiques effectués : CONFORMES (4 fixations/montant, joints OK)

CONCLUSION GLOBALE :
- Fenêtre F12 : 3 non-conformités MAJEURES (fixation et étanchéité)
- Fenêtres F08, F15, F22 : Conformes
- Taux de conformité échantillon : 75% (3/4 fenêtres)
```

### Document 3 - Référentiel normatif (extrait)

```json
{
  "exigences": [
    {
      "id": "MEN-001",
      "lot": "Menuiseries",
      "ref_norme": "NF DTU 36.5",
      "edition": "Octobre 2010",
      "paragraphe": "Section 6.2.3",
      "intitule": "Nombre de fixations selon hauteur menuiserie",
      "critere_acceptation": "H ≤ 1,50 m : 3 fix/montant | H > 1,50 m : 4 fix/montant",
      "severite": "majeure",
      "type_controle": "visuel"
    },
    {
      "id": "MEN-002",
      "lot": "Menuiseries",
      "ref_norme": "NF DTU 36.5",
      "edition": "Octobre 2010",
      "paragraphe": "Section 6.2.3",
      "intitule": "Répartition fixations avec point d'angle",
      "critere_acceptation": "Point de fixation à 15 cm maximum des angles",
      "severite": "majeure",
      "type_controle": "mesure"
    },
    {
      "id": "MEN-003",
      "lot": "Menuiseries",
      "ref_norme": "NF DTU 36.5",
      "edition": "Octobre 2010",
      "paragraphe": "Section 6.3.1",
      "intitule": "Joint de calfeutrement périphérique continu",
      "critere_acceptation": "Joint continu sur tout le pourtour, épaisseur ≥ 5 mm",
      "severite": "majeure",
      "type_controle": "visuel"
    },
    {
      "id": "MEN-004",
      "lot": "Menuiseries",
      "ref_norme": "CCTP Article 5.1",
      "edition": "Version marché",
      "paragraphe": "Article 5.1",
      "intitule": "Performance thermique Uw",
      "critere_acceptation": "Uw ≤ 1,4 W/m².K selon certificat",
      "severite": "mineure",
      "type_controle": "documentaire"
    }
  ]
}
```

---

### Questions de l'évaluation

#### Question 1 - Contrôle CCTP (15 points)
Utilisez le processus du MODULE_05 pour contrôler le CCTP.
1. Identifiez les **sources normatives manquantes** dans le CCTP (éditions, références incomplètes)
2. Créez un tableau listant :
   - Référence citée
   - Information manquante
   - Gravité de l'omission (mineure/majeure)

#### Question 2 - Structuration des NC (25 points)
Pour la fenêtre F12, créez **3 fiches NC** au format JSON (une par non-conformité constatée).
Chaque fiche doit contenir :
- ID unique, date, exigence associée
- Description précise et localisation
- Gravité qualifiée (avec justification)
- Action corrective proposée avec responsable et délai

#### Question 3 - Registre et fusion (15 points)
1. Créez un fichier `nc_menuiseries.json` contenant les 3 NC de la fenêtre F12
2. Rédigez la commande pour fusionner ce registre avec deux autres lots (fictifs)
3. Expliquez l'intérêt de la consolidation pour le pilotage projet

#### Question 4 - Calcul des KPIs (20 points)
À partir des données fournies :
1. Calculez le **taux de conformité** du lot menuiseries :
   - Nombre d'exigences applicables
   - Nombre d'exigences avec preuve conforme
   - Taux de conformité en %
2. Calculez les **KPIs NC** :
   - NC ouvertes / closes
   - NC par gravité
3. Produisez un **tableau de bord** synthétique pour le comité de pilotage

#### Question 5 - Rapport de conformité (15 points)
Rédigez un **rapport de conformité** (format Markdown) destiné au maître d'œuvre, contenant :
- Résumé exécutif (statut global, taux de conformité)
- Tableau des NC avec gravité et actions
- Recommandations pour levée de réserves
- Sources et traçabilité (PV, photos, normes)

#### Question 6 - Aide à la décision (10 points)
Le maître d'ouvrage demande : *"Peut-on réceptionner le lot menuiseries en l'état avec réserves, ou faut-il refuser la réception ?"*

Utilisez le **Wrapper 5 (Double raisonnement)** du MODULE_01 pour produire une matrice avantages/risques des deux options :
- **Option A** : Réception avec réserves (délai de levée 1 mois)
- **Option B** : Refus de réception et reprise immédiate

---

### Barème et critères d'évaluation

**Total : 100 points**

| Note | Appréciation | Commentaire |
|------|--------------|-------------|
| < 50 | Non acquis | Reprendre les exercices 1 à 5 |
| 50-69 | Partiellement acquis | Revoir la qualification des NC et les scripts |
| 70-84 | Acquis | Utilisation correcte du MODULE_05 |
| 85-100 | Maîtrisé | Prêt pour déploiement en production |

**Critères de qualité** :
- ✅ Structuration JSON conforme aux schémas
- ✅ Qualification de gravité justifiée et cohérente
- ✅ Actions correctives réalistes et chiffrées
- ✅ Scripts Python utilisés correctement (syntaxe, arguments)
- ✅ Rapports exploitables et opposables (traçabilité, sources)
- ✅ Raisonnement technique pertinent (risques, délais, coûts)

---

## 📖 Partie 4 : Ressources et bonnes pratiques

### 4.1 Matrice de sévérité des exigences

| Sévérité | Impact | Exemples BTP | Délai de résolution |
|----------|--------|--------------|---------------------|
| **Critique** | Sécurité, stabilité, inhabitabilité | Résistance structure, garde-corps, sortie de secours | < 1 semaine |
| **Majeure** | Pathologie, dysfonctionnement, non-conformité DTU | Étanchéité, isolation, ventilation | < 1 mois |
| **Mineure** | Esthétique, tolérance, confort | Finitions, teintes, planéité admissible | < 3 mois |

### 4.2 Processus complet de contrôle de conformité

**Étape 1 : Préparation** (Avant chantier)
→ Structurer le référentiel normatif (JSON) : exigences par lot
→ Valider avec maître d'œuvre et bureau de contrôle

**Étape 2 : Contrôle documentaire** (Phase CCTP)
→ `check_cctp_vs_normes.py` : vérifier couverture normative CCTP
→ Compléter le CCTP si exigences manquantes

**Étape 3 : Contrôle d'exécution** (Chantier)
→ Visites chantier avec grille d'exigences
→ `check_cr_pv_preuves.py` : contrôler que PV/CR apportent les preuves
→ Créer fiches NC pour chaque écart constaté

**Étape 4 : Suivi et pilotage** (Hebdomadaire)
→ `nc_register_merge.py` : consolider les NC de tous les lots
→ `dashboard_kpis.py` : calculer taux de conformité et NC ouvertes
→ Comité de pilotage : prioriser actions correctives

**Étape 5 : Réception** (Fin de chantier)
→ Rapport de conformité final (Markdown/PDF)
→ Levée de réserves conditionnée à clôture des NC majeures
→ Archivage du registre normatif pour DOE

### 4.3 Checklist contrôle de conformité

Avant de valider un contrôle, vérifiez :

**Référentiel normatif**
- [ ] Toutes les exigences ont un ID unique
- [ ] Références normatives complètes (norme + édition + paragraphe)
- [ ] Sévérité qualifiée pour chaque exigence
- [ ] Mots-clés pertinents pour recherche automatique
- [ ] Preuves attendues listées (CCTP, PV, photos, etc.)

**Contrôle CCTP**
- [ ] Script `check_cctp_vs_normes.py` exécuté sans erreur
- [ ] Taux de couverture ≥ 95% visé
- [ ] Exigences KO → Compléments CCTP rédigés et validés
- [ ] Rapport JSON et Markdown générés et archivés

**Gestion des NC**
- [ ] Chaque NC a une fiche structurée (JSON conforme)
- [ ] Gravité qualifiée avec justification technique
- [ ] Action corrective chiffrée (coût + délai)
- [ ] Responsable identifié (entreprise + contact)
- [ ] Photos et mesures en preuve

**Pilotage et reporting**
- [ ] Registre consolidé produit hebdomadairement
- [ ] KPIs calculés (taux conformité, NC ouvertes)
- [ ] Tableau de bord présenté en comité de pilotage
- [ ] NC critiques/majeures traitées en priorité

### 4.4 Erreurs fréquentes à éviter

❌ **Erreur 1** : Référentiel normatif incomplet
→ ✅ Impliquer le bureau de contrôle dès la phase CCTP pour lister toutes les exigences

❌ **Erreur 2** : Oublier l'édition des normes dans le CCTP
→ ✅ Toujours préciser "NF DTU XX (mois année)" pour éviter les ambiguïtés

❌ **Erreur 3** : Sous-qualifier la gravité des NC
→ ✅ Utiliser la matrice de sévérité (critique/majeure/mineure) de manière rigoureuse

❌ **Erreur 4** : NC sans action corrective chiffrée
→ ✅ Chaque NC doit avoir : responsable, délai, coût estimé

❌ **Erreur 5** : Absence de traçabilité des contrôles
→ ✅ Archiver tous les rapports JSON/MD, photos, PV dans le DOE

### 4.5 Intégration avec les autres modules Stone-Sea

**MODULE_01 (Wrappers IA)** + **MODULE_05 (Conformité)**
→ Utiliser les wrappers pour analyser les PV et CCTP avant contrôle automatisé
→ Exemple : Wrapper 8 (Contrôle normatif DTU) + `check_cctp_vs_normes.py`

**MODULE_04 (Production documentaire)** → **MODULE_05**
→ CCTP produits avec MODULE_04 → Contrôlés avec MODULE_05
→ Garantir la cohérence CCTP/DQE/Normes

**MODULE_05** → **MODULE_06 (Plan d'essais)**
→ Exigences de type "essai" ou "mesure" → Planifiées dans MODULE_06
→ PV d'essais → Vérifiés avec `check_cr_pv_preuves.py`

### 4.6 Outils complémentaires

**Pour aller plus loin** :
- **Gestion de projet** : Intégrer les NC dans un outil de ticketing (Jira, Monday, etc.)
- **BIM** : Lier les exigences aux objets IFC pour contrôle 3D
- **Blockchain** : Horodater les registres NC pour traçabilité juridique

---

## 📝 Annexes

### Annexe A : Tableau récapitulatif des outils MODULE_05

| Outil | Type | Entrée | Sortie | Cas d'usage |
|-------|------|--------|--------|-------------|
| **Schémas JSON** | Structure | - | Templates | Créer exigences, NC, preuves |
| **check_cctp_vs_normes.py** | Script Python | CCTP + Exigences JSON | Rapport JSON/MD | Contrôle couverture CCTP |
| **check_cr_pv_preuves.py** | Script Python | CR/PV + Exigences JSON | Rapport preuves | Vérifier apport de preuves |
| **nc_register_merge.py** | Script Python | Plusieurs NC JSON | NC consolidé | Fusion registres multi-lots |
| **dashboard_kpis.py** | Script Python | Registre normatif | KPIs (taux, NC) | Pilotage conformité |
| **Prompts IA** | Prompt | CCTP ou NC | Analyse assistée | Aide au contrôle et qualification |

### Annexe B : Exemple de workflow complet

**Projet** : Construction immeuble 45 logements
**Lot pilote** : Couverture

**Semaine 1 (Phase CCTP)** :
1. Créer `exigences_couverture.json` (15 exigences DTU 40.21)
2. Lancer `check_cctp_vs_normes.py` → Taux 73% (4 exigences manquantes)
3. Compléter le CCTP articles 3.2 et 3.5
4. Relancer le contrôle → Taux 100%

**Semaine 8 (Début pose couverture)** :
1. Visite chantier : 2 NC constatées (recouvrement écran, fixation tuiles)
2. Créer `nc_couverture.json` avec 2 fiches NC (majeure + mineure)
3. Transmettre à entreprise pour action corrective

**Semaine 12 (Suivi)** :
1. Fusionner `nc_couverture.json` + `nc_charpente.json` + `nc_zinguerie.json`
2. Lancer `dashboard_kpis.py` → 8 NC ouvertes (dont 2 majeures)
3. Comité de pilotage : prioriser clôture des 2 majeures sous 15 jours

**Semaine 16 (Réception)** :
1. Contrôle final : toutes NC closes sauf 1 mineure (report DOE)
2. Générer rapport conformité final (Markdown)
3. Réception avec réserve mineure, levée sous 2 mois

### Annexe C : Ressources normatives BTP

**Normes DTU principales** :
- **NF DTU 20.1** : Maçonnerie (parois et murs)
- **NF DTU 21** : Ouvrages en béton
- **NF DTU 36.5** : Menuiseries extérieures
- **NF DTU 40.21** : Couverture tuiles terre cuite
- **NF DTU 40.41** : Couverture zinc
- **NF DTU 45.1** : Isolation thermique des combles

**Eurocodes** :
- **EN 1990** : Bases de calcul structures
- **EN 1991** : Actions sur les structures (neige, vent)
- **EN 1992** : Calcul structures béton (Eurocode 2)
- **EN 1995** : Calcul structures bois (Eurocode 5)

**Cahiers CSTB** :
- **CPT 3651** : Écrans souples de sous-toiture
- **Cahier 3606** : Menuiseries PVC

**Avis Techniques** : Consultables sur [www.cstb.fr](https://www.cstb.fr)

---

## 🎓 Conclusion

Vous avez maintenant parcouru l'ensemble du MODULE_05 de Stone-Sea. Vous maîtrisez :

✅ **Structuration des exigences normatives** : Traduire les DTU/Eurocodes en exigences JSON exploitables
✅ **Contrôle automatisé** : Utiliser les scripts Python pour vérifier CCTP et PV
✅ **Gestion des NC** : Qualifier, tracer et piloter les non-conformités
✅ **Pilotage de la conformité** : Produire des KPIs et tableaux de bord décisionnels
✅ **Traçabilité et opposabilité** : Générer des rapports auditables pour réception et contentieux

**Prochaines étapes** :
1. **Déployer** le MODULE_05 sur un projet pilote (1 lot)
2. **Former** les conducteurs de travaux et contrôleurs
3. **Industrialiser** : Créer des bibliothèques d'exigences par lot (couverture, GO, menuiseries, etc.)
4. **Intégrer** avec vos outils métier (ERP, GED, BIM)

**Rappel crucial** :
Le MODULE_05 **assiste** le contrôle de conformité, mais **ne remplace pas** :
- L'expertise du bureau de contrôle (Véritas, Apave, Socotec, etc.)
- La validation du maître d'œuvre
- La responsabilité des entreprises titulaires des lots

La conformité normative est un **processus collaboratif** impliquant tous les acteurs du projet.

---

**Formateur** : [À compléter]
**Date de création du TP** : 2024-11-20
**Version** : 1.0
**Contact** : [À compléter]
**Licence** : Projet Stone-Sea

---

## 📚 Pour aller plus loin

**Documentation Stone-Sea** :
- `README.md` : Vue d'ensemble du projet
- `MODULE_00/` : Introduction pour débutants
- `MODULE_01/TP_Wrappers_IA_BTP.md` : Wrappers IA (prérequis)
- `MODULE_05/07_docs/README_integration_module05.md` : Guide d'intégration technique

**Formations complémentaires** :
- Normes DTU (CSTB, AFNOR)
- Eurocodes (formations SOCOTEC, Bureau Veritas)
- Contrôle qualité chantier (FFB, OPPBTP)
- Gestion des réserves et contentieux (UNTEC)

**Communauté Stone-Sea** :
- Issues GitHub : Retours d'expérience et questions
- Contributions : Nouveaux lots, scripts, référentiels normatifs
