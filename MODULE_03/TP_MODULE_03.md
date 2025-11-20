# TP MODULE 03 - Contrôle de conformité normative et Assurance Qualité

**Formation pratique au contrôle normatif BTP avec preuves traçables**

---

## 📋 Informations générales

**Durée estimée** : 4 heures
**Niveau** : Intermédiaire
**Prérequis** :
- Avoir suivi le TP MODULE_01 (Wrappers IA)
- Connaissances solides des normes BTP (DTU, Eurocodes)
- Maîtrise de la lecture de CCTP, plans et PV d'essais
- Notions de base en JSON
- Python 3.8+ installé
- Avoir lu le README.md du MODULE_03

**Objectifs pédagogiques** :
1. Maîtriser la structure des "evidences" de conformité au format JSON
2. Utiliser le prompt de vérification normative pour générer des contrôles traçables
3. Valider structurellement et qualitativement des evidences avec le script Python
4. Produire des rapports AQ complets et opposables
5. Comprendre la traçabilité complète des sources et preuves

---

## 📚 Partie 1 : Contexte et enjeux (20 min)

### 1.1 Qu'est-ce qu'une "evidence" de conformité ?

Dans le secteur BTP, la conformité aux normes (NF DTU, Eurocodes, CCTP) doit être **documentée** et **traçable**. Une "evidence" est un document structuré qui :

- **Relie chaque constat** à une source primaire (CCTP, plan, PV, norme)
- **Classe les non-conformités** par gravité (mineure, significative, majeure)
- **Propose des recommandations** mesurables et actionnables
- **Garantit la traçabilité** : versions IA, horodatage, hash des sources
- **Permet l'audit** : revue humaine avec checklist qualité

**Exemple concret** :
```
Constat : "L'enrobage du béton est de 28 mm"
Exigence : "≥ 30 mm selon NF DTU 65.14"
Source : "CCTP p.42"
Conformité : NON (gravité majeure)
Recommandation : "Augmenter l'enrobage de 2 mm minimum"
```

### 1.2 Pourquoi un format JSON structuré ?

Le MODULE_03 utilise un **schéma JSON strict** (`evidence_schema.json`) pour garantir :

✅ **Interopérabilité** : Les evidences peuvent être échangées entre outils
✅ **Validation automatique** : Le script vérifie la structure et les règles qualité
✅ **Traçabilité complète** : Métadonnées, versions, hash des sources
✅ **Auditabilité** : Revue humaine facilitée par la structure standardisée
✅ **Archivage pérenne** : Format ouvert, lisible, versionné

### 1.3 Architecture du MODULE_03

```
MODULE_03/module3/
├── 01_schema/
│   └── evidence_schema.json          # Schéma JSON des evidences
├── 02_prompts/
│   └── prompt_verificateur_normatif.md  # Prompt IA pour contrôle
├── 03_scripts/
│   └── validate_evidence.py           # Validation Python
├── 04_tests/
│   └── jeu_or_minimal.csv             # Jeu de test "or"
├── 05_modeles/
│   ├── rapport_AQ_modele.md           # Modèle de rapport AQ
│   ├── checklist_revue_AQ.md          # Checklist revue humaine
│   └── matrice_risques.md             # Matrice d'analyse de risques
└── 06_docs/
    ├── references_normatives_exemples.md
    └── README_integration_pipeline.md
```

### 1.4 Workflow type

1. **Collecte** : CCTP, plans, PV, normes applicables
2. **Contrôle IA** : Utilisation du prompt vérificateur normatif
3. **Génération JSON** : Production de l'evidence au format structuré
4. **Validation automatique** : Script Python `validate_evidence.py`
5. **Revue humaine** : Checklist AQ, recoupement des sources
6. **Rapport final** : Génération du rapport AQ avec preuves
7. **Archivage** : Hash SHA-256, versioning, PDF/A

---

## 🎯 Partie 2 : Exercices pratiques

### Exercice 1 : Comprendre le schéma JSON (30 min)

**Objectif** : Maîtriser la structure d'une evidence de conformité

**Contexte** : Vous devez créer manuellement votre première evidence JSON pour un contrôle simple.

**Consigne** :
1. Ouvrez le fichier `01_schema/evidence_schema.json`
2. Analysez les 4 blocs obligatoires : `meta`, `references`, `constats`, `synthese`
3. Créez un fichier `exercice1_evidence.json` avec le contenu suivant

**Document à analyser** :
```
CCTP - Article 7.2 Dalle béton rez-de-chaussée
Béton C25/30 XC1, épaisseur 15 cm.
Mise en œuvre selon NF DTU 21 (mars 2021).

Constat chantier :
Épaisseur mesurée : 14 cm
Classe béton BL : C30/37 XC1
```

**Evidence JSON à créer** :
```json
{
  "meta": {
    "chantier": "Résidence Les Érables",
    "lot": "Gros œuvre",
    "document_source": ["CCTP_GO_v2.1.pdf", "CR_chantier_20241115.pdf"],
    "modele_ia": "claude-sonnet-4.5",
    "version_prompts": "v1.0",
    "horodatage_utc": "2024-11-20T10:30:00Z"
  },
  "references": [
    {
      "famille": "CCTP",
      "numero": "Article 7.2",
      "edition": "v2.1",
      "couverture": "totale"
    },
    {
      "famille": "NF DTU",
      "numero": "21",
      "edition": "mars 2021",
      "articles": ["5.2.1", "7.3"],
      "couverture": "partielle"
    }
  ],
  "constats": [
    {
      "id": "C-001",
      "objet": "Épaisseur dalle béton RDC",
      "exigence": "Épaisseur minimale 15 cm selon CCTP Article 7.2",
      "valeur_requise": 15,
      "valeur_constatee": 14,
      "unite": "cm",
      "conforme": false,
      "gravite": "majeure",
      "citations_sources": [
        {
          "source": "CCTP_GO_v2.1.pdf#p.12",
          "citation": "Béton C25/30 XC1, épaisseur 15 cm."
        }
      ],
      "recommandation": "Dépose et repose de la dalle, ou note de calcul BE justifiant l'acceptabilité de 14 cm."
    },
    {
      "id": "C-002",
      "objet": "Classe de béton",
      "exigence": "Béton C25/30 minimum selon CCTP",
      "valeur_requise": "C25/30",
      "valeur_constatee": "C30/37",
      "unite": null,
      "conforme": true,
      "gravite": "mineure",
      "citations_sources": [
        {
          "source": "BL_beton_20241115.pdf",
          "citation": "Classe béton BL : C30/37 XC1"
        }
      ],
      "recommandation": "RAS - Conforme"
    }
  ],
  "synthese": {
    "non_conformites_majeures": 1,
    "non_conformites_mineures": 0,
    "points_attention": 0,
    "risque_global": "élevé",
    "decision": "retravail_requis"
  }
}
```

**Questions** :
- Quel est le rôle du bloc `meta` ?
- Pourquoi distinguer les `references` par famille (NF DTU, CCTP, Eurocode) ?
- Quelle est la différence entre `gravite: majeure` et `gravite: mineure` ?
- Que signifie `couverture: partielle` dans les références ?

**Réponses attendues** :
- **meta** : Traçabilité complète (chantier, lot, sources, IA utilisée, horodatage)
- **famille** : Permet de distinguer les sources contractuelles (CCTP) des normes réglementaires
- **gravité majeure** : Risque pour sécurité/solidité/étanchéité → retravail obligatoire
- **gravité mineure** : Non-conformité de forme, sans impact structurel → acceptation possible
- **couverture partielle** : La norme est citée mais seuls certains articles s'appliquent

---

### Exercice 2 : Utiliser le prompt vérificateur normatif (45 min)

**Objectif** : Générer une evidence JSON avec le prompt IA

**Contexte** : Vous devez contrôler la conformité d'une installation CVC (Climatisation, Ventilation, Chauffage) en utilisant le prompt du MODULE_03.

**Documents fournis** :

**CCTP - Article 12.3 Isolation tuyauteries CVC** :
```
Isolation des canalisations frigorifiques :
- Tuyauterie cuivre Ø < 35 mm : épaisseur isolant 13 mm minimum
- Tuyauterie cuivre Ø ≥ 35 mm : épaisseur isolant 19 mm minimum
- Matériau : mousse élastomère, classe M1 (réaction au feu)
- Jonctions : collage + manchons adhésifs étanches
Référence : NF DTU 65.14 (juin 2016)
```

**Constat chantier** :
```
Tuyauterie frigorifique Ø 28 mm : isolant 10 mm constaté (mesure au pied à coulisse)
Tuyauterie frigorifique Ø 42 mm : isolant 19 mm conforme
Matériau : mousse élastomère, étiquetage M1 présent
Jonctions : collage visible, mais absence de manchons adhésifs sur 3 raccords
```

**Consigne** :
1. Ouvrez le fichier `02_prompts/prompt_verificateur_normatif.md`
2. Copiez le prompt dans votre outil IA (Claude, ChatGPT, etc.)
3. Fournissez à l'IA :
   - Le contexte (chantier, lot CVC)
   - Les documents (CCTP, constat)
   - La liste des références (NF DTU 65.14 juin 2016)
4. Demandez : "Produis une evidence JSON conforme au schéma"

**Sortie attendue** :
L'IA doit produire un JSON avec :
- **2 non-conformités majeures** :
  - C-001 : Épaisseur isolant Ø28 mm insuffisante (10 mm au lieu de 13 mm)
  - C-002 : Absence de manchons adhésifs sur 3 raccords
- **2 conformités** :
  - C-003 : Épaisseur isolant Ø42 mm conforme (19 mm)
  - C-004 : Matériau M1 conforme
- **Synthèse** : `decision: "retravail_requis"`, `risque_global: "élevé"`

**Critères de validation** :
- [ ] Chaque constat a un `id` unique
- [ ] Les `valeur_requise` et `valeur_constatee` sont renseignées
- [ ] Les `unite` sont présentes (mm, -)
- [ ] Les `citations_sources` citent le CCTP et/ou la norme
- [ ] Les `gravite` sont cohérentes (isolant = sécurité incendie → majeure)
- [ ] La `synthese` correspond au nombre de NC

---

### Exercice 3 : Valider une evidence avec le script Python (30 min)

**Objectif** : Utiliser le script de validation pour détecter les erreurs

**Contexte** : Vous avez reçu une evidence JSON d'un sous-traitant. Vous devez la valider avant de l'intégrer au dossier AQ.

**Consigne** :
1. Créez un fichier `exercice3_mauvaise_evidence.json` avec le contenu suivant (volontairement incomplet)

```json
{
  "meta": {
    "chantier": "Immeuble Horizon",
    "lot": "Menuiseries"
  },
  "references": [
    {
      "famille": "NF DTU",
      "numero": "36.5"
    }
  ],
  "constats": [
    {
      "id": "M-001",
      "objet": "Fixation fenêtre F12",
      "exigence": "4 pattes par montant",
      "valeur_constatee": 2,
      "conforme": false,
      "gravite": "majeure"
    }
  ],
  "synthese": {
    "non_conformites_majeures": 1,
    "non_conformites_mineures": 0
  }
}
```

2. Lancez la validation :
```bash
python MODULE_03/module3/03_scripts/validate_evidence.py \
  exercice3_mauvaise_evidence.json \
  MODULE_03/module3/01_schema/evidence_schema.json
```

**Résultat attendu** :
```
[ERROR] Structure invalide:
 - [meta] manquant: document_source
 - [meta] manquant: modele_ia
 - [meta] manquant: version_prompts
 - [references[0]] manquant: couverture
 - [constats[0]] manquant: valeur_requise
 - [synthese] manquant: points_attention
 - [synthese] manquant: risque_global
 - [synthese] manquant: decision
[ERROR] Unités manquantes:
 - Constat M-001 sans unité.
[WARN] Traçabilité < 90% (objectif).
```

**Questions** :
- Quels sont les champs obligatoires manquants dans `meta` ?
- Pourquoi le script exige-t-il une `unite` même si la valeur est un nombre ?
- Que signifie "Traçabilité < 90%" ?

**Correction de l'evidence** :
Corrigez le fichier JSON en ajoutant tous les champs manquants, puis relancez la validation jusqu'à obtenir :
```
[INFO] Constats=1 | Traçabilité=100.0%
[OK] Validation passée.
```

---

### Exercice 4 : Générer un rapport AQ complet (45 min)

**Objectif** : Produire un rapport AQ final à partir d'une evidence validée

**Contexte** : Vous avez validé une evidence JSON pour le lot "Couverture". Vous devez maintenant générer le rapport AQ destiné au maître d'œuvre.

**Evidence validée** : `exercice4_evidence_couverture.json`
```json
{
  "meta": {
    "chantier": "Résidence Les Pins",
    "lot": "Couverture",
    "document_source": ["CCTP_Couverture_v3.2.pdf", "Plan_TOIT_01.dwg", "PV_pente_20241118.pdf"],
    "modele_ia": "claude-sonnet-4.5",
    "version_prompts": "v1.0",
    "horodatage_utc": "2024-11-20T14:15:00Z",
    "hash_entrees": {
      "CCTP_Couverture_v3.2.pdf": "a3f5d8e2c1b4...",
      "Plan_TOIT_01.dwg": "b8e2c1d9a3f5...",
      "PV_pente_20241118.pdf": "c1d9a3f5b8e2..."
    }
  },
  "references": [
    {
      "famille": "NF DTU",
      "numero": "40.21",
      "edition": "mai 2019",
      "articles": ["5.2.3", "6.1.1"],
      "couverture": "totale"
    },
    {
      "famille": "CCTP",
      "numero": "Article 9.1",
      "edition": "v3.2",
      "couverture": "totale"
    }
  ],
  "constats": [
    {
      "id": "T-001",
      "objet": "Pente membrane EPDM zone P2",
      "exigence": "Pente minimale 2% selon NF DTU 40.21 §5.2.3",
      "valeur_requise": 2,
      "valeur_constatee": 1.5,
      "unite": "%",
      "conforme": false,
      "gravite": "majeure",
      "preuve": {
        "extrait": "Pente mesurée au niveau laser : 1.5%",
        "page_plan": "Plan_TOIT_01 repère P2",
        "captures": ["photo_pente_P2_20241118.jpg"]
      },
      "citations_sources": [
        {
          "source": "NF DTU 40.21 mai 2019 §5.2.3",
          "citation": "La pente minimale des supports pour membrane EPDM doit être de 2%."
        },
        {
          "source": "PV_pente_20241118.pdf",
          "citation": "Zone P2 : pente mesurée 1.5%"
        }
      ],
      "recommandation": "Reprise du support avec correction de pente à 2% minimum avant pose membrane."
    },
    {
      "id": "T-002",
      "objet": "Fixation mécanique membrane",
      "exigence": "Barres de fixation tous les 1,5 m maximum selon CCTP Article 9.1",
      "valeur_requise": 1.5,
      "valeur_constatee": 1.4,
      "unite": "m",
      "conforme": true,
      "gravite": "mineure",
      "citations_sources": [
        {
          "source": "CCTP_Couverture_v3.2.pdf p.18",
          "citation": "Barres de fixation espacées de 1,5 m maximum"
        }
      ],
      "recommandation": "RAS - Conforme"
    }
  ],
  "synthese": {
    "non_conformites_majeures": 1,
    "non_conformites_mineures": 0,
    "points_attention": 0,
    "risque_global": "élevé",
    "decision": "retravail_requis"
  }
}
```

**Consigne** :
1. Ouvrez le modèle `05_modeles/rapport_AQ_modele.md`
2. Remplissez le rapport avec les données de l'evidence JSON
3. Utilisez la checklist `05_modeles/checklist_revue_AQ.md` pour la revue humaine

**Rapport AQ attendu** :

```markdown
# Rapport AQ — Résidence Les Pins — Couverture

**Date** : 2024-11-20
**Contrôleur** : [VOTRE NOM]
**Version** : 1.0

---

## 1. SYNTHÈSE EXÉCUTIVE

- **Non-conformités majeures** : 1
- **Non-conformités mineures** : 0
- **Points d'attention** : 0
- **Risque global** : ÉLEVÉ
- **Décision** : RETRAVAIL REQUIS

---

## 2. RÉFÉRENCES APPLIQUÉES

| Famille | Numéro | Édition | Articles | Couverture |
|---------|--------|---------|----------|------------|
| NF DTU | 40.21 | Mai 2019 | 5.2.3, 6.1.1 | Totale |
| CCTP | Article 9.1 | v3.2 | - | Totale |

---

## 3. DÉTAILS DES CONSTATS

### 3.1 Non-conformité T-001 (MAJEURE)

**Objet** : Pente membrane EPDM zone P2

**Exigence** : Pente minimale 2% selon NF DTU 40.21 §5.2.3

| Valeur requise | Valeur constatée | Unité | Conformité |
|----------------|------------------|-------|------------|
| 2 | 1.5 | % | ❌ NON CONFORME |

**Preuves** :
- Plan : Plan_TOIT_01 repère P2
- Photo : photo_pente_P2_20241118.jpg
- Mesure : Pente mesurée au niveau laser : 1.5%

**Citation normative** :
> "La pente minimale des supports pour membrane EPDM doit être de 2%."
> — NF DTU 40.21 mai 2019 §5.2.3

**Recommandation** :
Reprise du support avec correction de pente à 2% minimum avant pose membrane.

---

### 3.2 Constat T-002 (Conforme)

**Objet** : Fixation mécanique membrane

| Valeur requise | Valeur constatée | Unité | Conformité |
|----------------|------------------|-------|------------|
| 1.5 | 1.4 | m | ✅ CONFORME |

**Recommandation** : RAS - Conforme

---

## 4. ARBITRAGES

**NC T-001** : La pente de 1.5% est insuffisante pour assurer l'évacuation des eaux pluviales. Risque de stagnation et de dégradation prématurée de la membrane EPDM. Retravail obligatoire avant réception.

---

## 5. PLAN D'ACTIONS

| ID | Action | Responsable | Échéance | Critère de succès |
|----|--------|-------------|----------|-------------------|
| T-001 | Reprise support + correction pente | Entreprise Toiture Plus | 2024-12-05 | Pente ≥ 2% mesurée au niveau laser |
| T-001 | Contrôle contradictoire pente | MOE + Contrôleur | 2024-12-06 | PV signé avec mesures conformes |

---

## 6. ANNEXES

### 6.1 Traçabilité technique

- **Modèle IA** : claude-sonnet-4.5
- **Version prompts** : v1.0
- **Horodatage** : 2024-11-20T14:15:00Z

### 6.2 Hash des sources

| Document | Hash SHA-256 |
|----------|--------------|
| CCTP_Couverture_v3.2.pdf | a3f5d8e2c1b4... |
| Plan_TOIT_01.dwg | b8e2c1d9a3f5... |
| PV_pente_20241118.pdf | c1d9a3f5b8e2... |

---

**Signatures** :
- Contrôleur : ______________________
- MOE : ______________________
- Date : ______________________
```

**Checklist revue humaine** :
- [x] Périmètre vérifié correspond au marché
- [x] Éditions des références normatives renseignées (NF DTU 40.21 mai 2019)
- [x] Constats majeurs recoupés avec documents primaires (PV pente, plans)
- [x] Recommandations concrètes et mesurables (pente ≥ 2%)
- [x] Décision motivée ; plan d'actions (responsables, échéances)
- [x] Paquet de preuves haché et archivé (SHA-256)

---

### Exercice 5 : Traiter un jeu d'essai "or" (30 min)

**Objectif** : Valider plusieurs evidences avec le jeu de test minimal

**Contexte** : Le MODULE_03 fournit un jeu de test CSV (`04_tests/jeu_or_minimal.csv`) pour tester rapidement le pipeline.

**Consigne** :
1. Ouvrez le fichier `04_tests/jeu_or_minimal.csv`
2. Convertissez manuellement chaque ligne en constat JSON
3. Créez 3 evidences distinctes (une par lot : CVC, Couverture, Maçonnerie)
4. Validez chaque evidence avec le script Python

**Jeu de test CSV** :
```csv
id,lot,document_source,exigence,valeur_requise,valeur_constatee,unite,conforme,gravite,source_ref
C-001,CVC,CCTP_P2_Clim.pdf,Epaisseur enrobage mini,>=30,28,mm,false,majeure,"CCTP p.42 ; NF DTU 65.14"
C-002,Couverture,Plan_TOIT_01.pdf,Pente mini membrane,>=2,1.5,%,false,significative,"Plan repère P2 ; NF DTU 40.xx"
C-003,Maçonnerie,PV_Reception_MUR_A.pdf,Planeite mur,<5,<5,mm,true,mineure,"PV §3 ; NF DTU 20.1"
```

**Questions** :
- Pourquoi la NC C-001 est-elle classée "majeure" ?
- Que signifie `gravite: significative` pour C-002 ?
- Comment interpréter `valeur_requise: "<5"` pour C-003 (planéité) ?

**Réponses attendues** :
- **C-001 majeure** : L'enrobage du béton protège les armatures de la corrosion → sécurité structurelle
- **significative** : Impact sur la performance (étanchéité, isolation, acoustique) sans risque immédiat
- **"<5"** : Tolérance maximale. La planéité mesurée doit être inférieure à 5 mm sous règle de 2 m

---

## 🏆 Partie 3 : Évaluation finale (1h30)

### Cas pratique intégré : Contrôle d'un lot Électricité

**Contexte général** :
Vous êtes responsable AQ sur un chantier de rénovation d'un immeuble de bureaux. Le lot électricité vient d'être achevé. Vous devez :
1. Analyser le CCTP et les constats de réception
2. Produire une evidence JSON complète et validée
3. Rédiger le rapport AQ final

**Document 1 - Extrait CCTP Électricité** :
```
ARTICLE 15 - TABLEAU GÉNÉRAL BASSE TENSION (TGBT)

15.1 Caractéristiques techniques
- Indice de protection : IP 43 minimum (selon NF EN 60529)
- Disjoncteur général : 4P 250A courbe C avec différentiel 300 mA type S
- Parafoudre : Type 2, Uc = 440V, Imax = 40 kA
- Sélectivité : totale entre disjoncteur général et divisionnaires

15.2 Installation
- Hauteur socle TGBT : 20 cm minimum au-dessus du sol fini
- Distance minimale aux points d'eau : 60 cm
- Fixation murale : chevilles métalliques Ø 12 mm, profondeur 80 mm minimum
- Mise à la terre : conducteur cuivre nu 25 mm² raccordé au réseau de terre général

15.3 Normes applicables
- NF C 15-100 (édition décembre 2022) - Installations électriques BT
- NF EN 60529 - Degrés de protection (indices IP)

15.4 Essais et vérifications
- Mesure de résistance d'isolement : ≥ 500 kΩ (500V DC)
- Mesure de continuité des liaisons équipotentielles : ≤ 0,5 Ω
- Test différentiel 300 mA : déclenchement entre 150 et 300 mA
- PV d'essai CONSUEL obligatoire avant mise sous tension
```

**Document 2 - Procès-verbal de réception (extraits)** :
```
PV DE RÉCEPTION - Lot Électricité
Date : 18/11/2024
Contrôleur : Bureau Veritas - Inspecteur M. Dubois

TABLEAU GÉNÉRAL BASSE TENSION (TGBT) - Local technique RDC

1. Caractéristiques techniques
✅ Indice de protection : IP 43 (plaque signalétique conforme)
✅ Disjoncteur général : 4P 250A courbe C avec différentiel 300 mA type S (ABB)
❌ Parafoudre : Type 2 installé, mais Uc = 400V (au lieu de 440V prescrit CCTP)
✅ Sélectivité : Courbes fournies par BE, sélectivité totale validée

2. Installation
✅ Hauteur socle : 22 cm (mesure au mètre)
❌ Distance au point d'eau (évier local) : 45 cm (insuffisant, CCTP prescrit 60 cm)
✅ Fixation murale : 6 chevilles métalliques Ø 12 mm, profondeur 85 mm constatée
✅ Mise à la terre : conducteur cuivre nu 25 mm² raccordé, serrage vérifié

3. Essais électriques (rapport CONSUEL n° 2024-EL-1234)
✅ Résistance d'isolement : 1,2 MΩ (≥ 500 kΩ requis)
❌ Continuité équipotentielle : 0,8 Ω mesurée (seuil 0,5 Ω NF C 15-100)
✅ Test différentiel : déclenchement à 280 mA (conforme 150-300 mA)

4. Documentation
✅ Schémas unifilaires fournis
✅ Notice d'utilisation et d'entretien fournie
❌ Certificat de conformité parafoudre manquant

CONCLUSION PROVISOIRE : 4 réserves (dont 2 majeures)
```

### Questions de l'évaluation

**Question 1** (20 points) : Analyse des constats
Listez tous les constats (conformes et non-conformes) avec leur gravité. Justifiez la classification de chaque gravité.

**Question 2** (25 points) : Evidence JSON complète
Produisez l'evidence JSON complète avec :
- Bloc `meta` (chantier fictif "Immeuble Horizon", lot "Électricité")
- Bloc `references` (NF C 15-100, NF EN 60529, CCTP)
- Bloc `constats` (au minimum 8 constats identifiés)
- Bloc `synthese` (nombre de NC, risque global, décision)

**Question 3** (15 points) : Validation Python
Validez votre evidence JSON avec le script `validate_evidence.py`. Corrigez toutes les erreurs jusqu'à obtenir `[OK] Validation passée.`

**Question 4** (25 points) : Rapport AQ
Rédigez le rapport AQ complet en suivant le modèle `rapport_AQ_modele.md`. Incluez :
- Synthèse exécutive
- Tableau des références
- Détails des non-conformités avec citations normatives
- Arbitrages (justification des gravités)
- Plan d'actions avec responsables et échéances

**Question 5** (15 points) : Checklist revue humaine
Appliquez la checklist `checklist_revue_AQ.md` et listez les points d'attention ou manquements éventuels.

---

### Barème et critères d'évaluation

**Total : 100 points**

- **< 50 points** : Non acquis - Réviser le MODULE_03 et refaire les exercices
- **50-69 points** : Partiellement acquis - Reprendre les exercices sur la structure JSON
- **70-84 points** : Acquis - Maîtrise correcte du contrôle normatif
- **85-100 points** : Expert - Prêt pour production autonome en AQ chantier

**Critères de qualité** :
- ✅ Structure JSON strictement conforme au schéma
- ✅ Toutes les unités renseignées (mm, cm, Ω, mA, kV, etc.)
- ✅ Citations sources précises (norme + article, CCTP + page)
- ✅ Gravités cohérentes (majeure = sécurité/solidité, significative = performance, mineure = forme)
- ✅ Recommandations mesurables et actionnables
- ✅ Synthèse cohérente avec les constats
- ✅ Traçabilité complète (hash, horodatage, versions)

---

## 📖 Partie 4 : Ressources et bonnes pratiques

### 4.1 Classification des gravités

**Majeure** (retravail obligatoire) :
- Sécurité des personnes (électricité, incendie, chute)
- Solidité structurelle (béton, acier, fondations)
- Étanchéité (toiture, façade, sous-sol)
- Non-conformité réglementaire bloquante (CONSUEL, sécurité incendie)

**Significative** (arbitrage requis) :
- Performance dégradée (isolation thermique, acoustique)
- Risque de désordre à moyen terme (durabilité réduite)
- Non-conformité contractuelle avec impact fonctionnel

**Mineure** (acceptation possible) :
- Défaut esthétique sans impact fonctionnel
- Non-conformité de forme (documentation, étiquetage)
- Écart tolérable avec accord du maître d'œuvre

### 4.2 Workflow complet de contrôle AQ

```
1. COLLECTE DES SOURCES
   ├─ CCTP / Plans / DPGF
   ├─ PV de réception / essais
   ├─ Fiches techniques produits
   └─ Normes applicables (éditions exactes)

2. CONTRÔLE AVEC IA
   ├─ Utilisation du prompt vérificateur normatif
   ├─ Génération de l'evidence JSON
   └─ Export JSON brut

3. VALIDATION AUTOMATIQUE
   ├─ Script validate_evidence.py
   ├─ Correction des erreurs de structure
   └─ Vérification traçabilité ≥ 90%

4. REVUE HUMAINE
   ├─ Checklist AQ
   ├─ Recoupement sources primaires (NC majeures)
   ├─ Validation gravités
   └─ Arbitrages techniques

5. RAPPORT FINAL
   ├─ Génération rapport AQ (Markdown → PDF/A)
   ├─ Annexe preuves (photos, extraits, plans)
   └─ Signature contrôleur + MOE

6. ARCHIVAGE
   ├─ Hash SHA-256 du paquet (evidence + preuves + rapport)
   ├─ Versioning (v1.0, v1.1...)
   └─ Stockage pérenne (GED, archivage probant)
```

### 4.3 Erreurs fréquentes à éviter

❌ **Erreur 1** : Oublier les unités
→ ✅ Toujours renseigner `unite` (mm, cm, m, %, °C, MPa, Ω, etc.)

❌ **Erreur 2** : Éditions de normes absentes
→ ✅ Exiger l'édition exacte (ex: NF DTU 21 mars 2021, NF C 15-100 décembre 2022)

❌ **Erreur 3** : Citations sources imprécises
→ ✅ Format : `NF_DTU_21_mars_2021.pdf#p.42 §5.2.1` ou `CCTP_GO_v2.1.pdf#Article 7.2`

❌ **Erreur 4** : Gravités incohérentes
→ ✅ Sécurité/solidité/étanchéité = toujours majeure

❌ **Erreur 5** : Synthèse incohérente
→ ✅ Compter précisément les NC majeures/mineures dans les constats

❌ **Erreur 6** : Recommandations vagues
→ ✅ "Reprendre l'enrobage à 30 mm minimum" (mesurable) ≠ "Améliorer l'enrobage" (flou)

### 4.4 Checklist avant livraison d'une evidence

Avant de livrer une evidence au maître d'œuvre ou au contrôleur :

- [ ] Structure JSON valide (validation script passée)
- [ ] Traçabilité ≥ 90% (citations sources sur tous les constats critiques)
- [ ] Unités renseignées pour toutes les valeurs numériques
- [ ] Éditions de normes exactes (mois + année)
- [ ] Gravités cohérentes avec les enjeux (sécurité → majeure)
- [ ] Recommandations mesurables et actionnables
- [ ] Synthèse cohérente (comptage NC, risque global, décision)
- [ ] Hash SHA-256 des sources d'entrée calculé
- [ ] Horodatage UTC présent
- [ ] Revue humaine effectuée (checklist AQ cochée)

### 4.5 Intégration dans un pipeline industriel

Le MODULE_03 s'intègre naturellement avec les autres modules Stone-Sea :

**MODULE_01 (Wrappers IA)** → Utiliser Wrapper 8 (Contrôle normatif) + Wrapper 6 (Journal sources)

**MODULE_02 (Pack industrialisation)** → Pipeline : anonymisation → contrôle → validation → archivage

**MODULE_04 (Production documentaire)** → Analyser les CCTP/DQE générés avec le MODULE_03

**MODULE_05 (Conformité normative)** → Croiser les exigences normatives avec les evidences

**MODULE_06 (Plan d'essais)** → Valider les PV d'essais avec le vérificateur normatif

---

## 📝 Annexes

### Annexe A : Structure complète d'une evidence JSON

```json
{
  "meta": {
    "chantier": "string",
    "lot": "string",
    "document_source": ["array"],
    "modele_ia": "string",
    "version_prompts": "string",
    "horodatage_utc": "ISO 8601",
    "hash_entrees": {"file": "sha256"}
  },
  "references": [
    {
      "famille": "NF DTU|Eurocode|CCTP|Guide interne|Autre",
      "numero": "string",
      "edition": "string",
      "articles": ["array"],
      "couverture": "totale|partielle|hors_perimetre"
    }
  ],
  "constats": [
    {
      "id": "string",
      "objet": "string",
      "exigence": "string",
      "valeur_requise": "string|number|null",
      "valeur_constatee": "string|number|null",
      "unite": "string|null",
      "conforme": "boolean",
      "gravite": "mineure|significative|majeure",
      "preuve": {
        "extrait": "string",
        "page_plan": "string",
        "coordonnees": {"x": 0, "y": 0, "w": 0, "h": 0},
        "captures": ["array"]
      },
      "citations_sources": [
        {"source": "string", "citation": "string"}
      ],
      "recommandation": "string"
    }
  ],
  "synthese": {
    "non_conformites_majeures": "integer",
    "non_conformites_mineures": "integer",
    "points_attention": "integer",
    "risque_global": "faible|modéré|élevé",
    "decision": "conforme|acceptation_conditionnelle|retravail_requis"
  }
}
```

### Annexe B : Principales normes BTP par lot

| Lot | Normes applicables | Éditions récentes |
|-----|-------------------|-------------------|
| Gros œuvre | NF DTU 20.1, 21, EN 206/CN | Mars 2020, Mars 2021 |
| Charpente bois | NF DTU 31.1, 31.2 | Janvier 2022 |
| Menuiseries | NF DTU 36.5 | Octobre 2010 |
| Couverture | NF DTU 40.x (tuiles, zinc, membrane) | Variable selon matériau |
| Plomberie | NF DTU 60.x | Variable selon corps d'état |
| CVC | NF DTU 65.x | Variable selon installation |
| Électricité | NF C 15-100 | Décembre 2022 |
| Isolation | NF DTU 45.x | Variable selon technique |

### Annexe C : Correspondance gravité / décision

| Non-conformités majeures | Non-conformités mineures | Risque global | Décision recommandée |
|--------------------------|--------------------------|---------------|----------------------|
| 0 | 0 | Faible | `conforme` |
| 0 | 1-3 | Faible | `conforme` ou `acceptation_conditionnelle` |
| 0 | ≥4 | Modéré | `acceptation_conditionnelle` |
| 1 | - | Modéré à Élevé | `retravail_requis` ou `acceptation_conditionnelle` (arbitrage MOE) |
| ≥2 | - | Élevé | `retravail_requis` |

---

## 🎓 Conclusion

Vous maîtrisez maintenant le MODULE_03 de Stone-Sea pour produire des **evidences de conformité traçables** et opposables. Les compétences acquises :

✅ **Structure JSON** : Maîtrise du schéma evidence_schema.json
✅ **Prompt IA** : Utilisation du vérificateur normatif pour automatiser les contrôles
✅ **Validation** : Script Python pour garantir la qualité structurelle
✅ **Rapports AQ** : Production de rapports complets avec preuves et traçabilité
✅ **Workflow industriel** : Intégration dans un pipeline qualité complet

**Prochaines étapes** :
1. Pratiquer avec des documents réels de vos chantiers
2. Intégrer le MODULE_03 dans vos processus AQ
3. Former vos équipes (conducteurs de travaux, contrôleurs, BE)
4. Combiner avec les MODULE_04, 05, 06 pour un workflow complet

**Rappel important** :
L'IA est un **outil d'aide à la décision**, pas un **contrôleur autonome**. La revue humaine par un professionnel qualifié (ingénieur, contrôleur technique) reste **obligatoire** pour valider les non-conformités majeures et les décisions d'acceptation ou de retravail.

---

**Formateur** : [À compléter]
**Date de création du TP** : 2024-11-20
**Version** : 1.0
**Contact** : [À compléter]
