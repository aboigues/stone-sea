# TP MODULE 04 - Production documentaire BTP

**Formation pratique aux outils de production documentaire assistée**

---

## 📋 Informations générales

**Durée estimée** : 4 heures
**Niveau** : Intermédiaire
**Prérequis** :
- Avoir complété le TP MODULE_01 (Wrappers IA)
- Connaissances solides en documents BTP (CCTP, DQE/DPGF, CR)
- Python 3.8+ installé
- Accès à un outil IA (Claude, ChatGPT, etc.)
- Avoir lu le README.md du MODULE_04

**Objectifs pédagogiques** :
1. Maîtriser la production et mise à jour de CCTP structurés et traçables
2. Savoir créer et valider des DQE/DPGF conformes aux schémas JSON
3. Produire des comptes-rendus de chantier normalisés
4. Utiliser les scripts de conversion, validation et export
5. Garantir la traçabilité complète des livrables documentaires

---

## 📚 Partie 1 : Contexte et enjeux (15 min)

### 1.1 Pourquoi automatiser la production documentaire ?

Dans le secteur BTP, la production documentaire représente un volume considérable :

**Problématiques courantes** :
- **Incohérences** entre CCTP, DQE et plans
- **Pertes de traçabilité** des sources et hypothèses
- **Erreurs de calcul** dans les DQE (quantités × prix)
- **Retards** dans la production des CR de chantier
- **Non-conformité** aux référentiels normatifs
- **Difficultés d'archivage** et de versioning

**Bénéfices de l'approche Stone-Sea** :
- ✅ Documents structurés et conformes aux schémas JSON
- ✅ Traçabilité complète des sources et hypothèses
- ✅ Validation automatique (unités, montants, champs obligatoires)
- ✅ Conversion multi-formats (CSV ↔ JSON ↔ Markdown)
- ✅ Intégration possible avec MODULE_03 (évidences) et MODULE_05 (conformité)

### 1.2 Architecture du MODULE_04

```
MODULE_04/
├── 01_schemas/           # Schémas JSON de validation
│   ├── poste_dqe.schema.json
│   └── cr_chantier.schema.json
├── 02_prompts/           # Prompts IA pour production assistée
│   ├── prompt_redaction_cctp.md
│   ├── prompt_structuration_dqe.md
│   └── prompt_cr_chantier.md
├── 03_scripts/           # Scripts Python de traitement
│   ├── csv_dqe_to_json.py
│   ├── check_dqe_json.py
│   └── cr_json_to_md.py
├── 04_modeles/           # Trames et modèles types
│   ├── trame_cctp.md
│   ├── dqe_minimal.csv
│   └── cr_modele.md
├── 05_docs/              # Documentation d'intégration
├── 06_examples/          # Exemples prêts à l'emploi
└── PACKAGE_SHA256.txt    # Hash du package
```

### 1.3 Workflow type

```
┌─────────────────┐
│  Sources        │
│ (CCTP, Plans,   │
│  CSV, Notes)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Prompts IA     │ ◄── Wrappers MODULE_01
│  (02_prompts)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Scripts        │
│  (03_scripts)   │
│  • Conversion   │
│  • Validation   │
│  • Export       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Livrables      │
│  JSON/Markdown  │
│  + Évidences    │
└─────────────────┘
```

---

## 🎯 Partie 2 : Exercices pratiques

### Exercice 1 : Rédaction CCTP assistée par IA

**Objectif** : Produire un article CCTP structuré et traçable pour un lot "Couverture"

**Contexte** : Vous êtes maître d'œuvre sur un projet de construction d'un bâtiment tertiaire. Vous devez rédiger l'article CCTP du lot "Couverture" à partir des documents fournis.

**Documents fournis** :

```markdown
# DOCUMENT 1 - Extrait cahier des charges MOA
Le bâtiment sera couvert d'une toiture terrasse accessible (zone technique).
Étanchéité bicouche bitumineuse.
Isolation thermique : R ≥ 5,0 m².K/W.
Évacuation EP par dalots diamètre 100 mm.

# DOCUMENT 2 - Extrait plan toiture (Plan A-301)
Surface toiture : 450 m²
Pente : 2%
Évacuation : 6 dalots Ø100 répartis
Protection lourde : dalles béton gravillonnées 50×50 cm

# DOCUMENT 3 - Exigences réglementaires
RE2020 applicable
Zone climatique : H1b
Classement feu : Broof(t3)
```

**Consigne** :

1. **Ouvrez** le prompt `/home/user/stone-sea/MODULE_04/02_prompts/prompt_redaction_cctp.md`
2. **Copiez** le prompt dans votre outil IA
3. **Remplacez** les variables :
   - `[LOT]` → "Couverture"
   - `{Contexte_Projet}` → Informations ci-dessus
   - `{Liste_Documents}` → Documents 1, 2, 3
   - `{Références_Applicables}` → "NF DTU 43.1 (Octobre 2019), NF EN 1991-1-1 (Eurocodes)"

4. **Lancez** la génération
5. **Vérifiez** que le CCTP produit contient :
   - Les 9 sections de la trame (Objet, Références, Définitions, etc.)
   - Des balises `[Preuve:]` avec sources précises
   - Une section "Points de vigilance"
   - Des mentions "à compléter" si informations manquantes

**Rendu attendu** (extrait) :

```markdown
## Objet du lot
Fourniture et mise en œuvre de l'étanchéité et de l'isolation de la toiture terrasse accessible (zone technique).
Surface : 450 m² [Preuve: Plan_A-301]
Pente : 2% [Preuve: Plan_A-301]

## Références
- Marché: CCTP/CCAP [à préciser]
- NF DTU 43.1 - Étanchéité des toitures-terrasses (Octobre 2019)
- NF EN 1991-1-1 - Eurocodes Actions sur les structures
- RE2020 - Réglementation environnementale

## Matériaux

### Isolation thermique
Performance exigée : R ≥ 5,0 m².K/W [Preuve: Document_1_MOA]
Matériau : [à compléter - à définir selon étude thermique]
Épaisseur : [à compléter]

### Étanchéité
Type : bicouche bitumineuse [Preuve: Document_1_MOA]
Classement feu : Broof(t3) [Preuve: Document_3_Exigences]
[...]

## Points de vigilance
- Coordination avec lot plomberie (évacuation EP)
- Respect classement feu Broof(t3) pour zone H1b
- Accessibilité zone technique : charges d'exploitation à définir
- Contrôle étanchéité avant mise en place protection
```

**Points de contrôle** :
- [ ] Structure conforme à la trame (9 sections)
- [ ] Toutes les exigences chiffrées sont sourcées avec `[Preuve:]`
- [ ] Les informations manquantes sont signalées "à compléter"
- [ ] Références normatives avec éditions
- [ ] Section "Points de vigilance" présente

---

### Exercice 2 : Structuration DQE depuis CSV

**Objectif** : Convertir un DQE CSV en JSON conforme et le valider

**Contexte** : Vous avez reçu un fichier DQE au format CSV avec des postes incomplets. Vous devez le normaliser et le valider.

**Fichier fourni** : `dqe_lot_couverture.csv`

```csv
code,intitule,description,unite,quantite,prix_unitaire,hypotheses,sources,liens_normatifs,tags
L05-001,Isolation thermique polyuréthane 140mm,Fourniture et pose y.c. fixations,m2,450,22.5,"Surface nette d'après plan A-301","CCTP_L05.pdf#p8;Plan_A-301","NF DTU 43.1 (Octobre 2019)","L05;isolation"
L05-002,Étanchéité bicouche bitumineuse,Revêtement + fixations,m2,450,35.8,"Idem ci-dessus + 10% recouvrement","CCTP_L05.pdf#p9","NF DTU 43.1 (Octobre 2019)","L05;etancheite"
L05-003,Dalots évacuation EP Ø100,,u,6,125.0,"6 dalots répartis sur toiture","Plan_A-301","NF DTU 43.1;NF DTU 60.11","L05;EP"
L05-004,Protection lourde dalles béton 50x50,Pose sur plots,m2,450,18.2,"Surface identique étanchéité","CCTP_L05.pdf#p12","","L05;protection"
```

**Consignes** :

**Étape 1 : Conversion CSV → JSON**

```bash
cd /home/user/stone-sea/MODULE_04
python 03_scripts/csv_dqe_to_json.py dqe_lot_couverture.csv dqe_lot_couverture.json
```

**Étape 2 : Validation du JSON**

```bash
python 03_scripts/check_dqe_json.py dqe_lot_couverture.json
```

**Étape 3 : Analyse du rapport de validation**

Le script devrait produire un rapport indiquant :
- ✅ Champs obligatoires présents
- ✅ Unités valides (m2, u)
- ⚠️ Poste L05-003 : description manquante
- ⚠️ Poste L05-004 : liens_normatifs vide
- ✅ Montants calculés correctement :
  - L05-001 : 450 × 22.5 = 10 125.00 €
  - L05-002 : 450 × 35.8 = 16 110.00 €
  - L05-003 : 6 × 125.0 = 750.00 €
  - L05-004 : 450 × 18.2 = 8 190.00 €
  - **TOTAL : 35 175.00 € HT**

**Étape 4 : Correction des anomalies**

Éditez le JSON généré et complétez :
- Poste L05-003 : `"description": "Fourniture et pose dalots PVC Ø100"`
- Poste L05-004 : `"liens_normatifs": ["NF DTU 43.1 (Octobre 2019)"]`

**Étape 5 : Validation finale**

```bash
python 03_scripts/check_dqe_json.py dqe_lot_couverture.json
```

Résultat attendu : `✅ DQE conforme - 0 erreurs, 0 avertissements`

**Rendu attendu** : Fichier `dqe_lot_couverture.json` valide et complet

**Points de contrôle** :
- [ ] Conversion CSV → JSON réussie
- [ ] Schéma JSON respecté (tous les champs obligatoires)
- [ ] Montants calculés = quantité × prix_unitaire (2 décimales)
- [ ] Au moins une source par poste
- [ ] Unités dans l'enum autorisé (m, m2, m3, u, kg, h, forfait)
- [ ] Anomalies corrigées

---

### Exercice 3 : Utilisation du prompt Structuration DQE avec IA

**Objectif** : Faire analyser et corriger un DQE incomplet par l'IA

**Contexte** : Vous avez un DQE brouillon avec des incohérences. Vous allez utiliser le prompt de structuration pour le normaliser.

**Fichier fourni** : `dqe_brouillon.csv`

```csv
code,intitule,unite,quantite,prix_unitaire
L06-001,Charpente métallique,kg,2500,4.5
L06-002,Couverture bac acier,m2,480,28
L06-003,Fourniture et pose,u,12,450
L06-004,Isolation laine de roche 100mm,m2,480,12.8
```

**Problèmes identifiés** :
- Descriptions manquantes
- Pas d'hypothèses ni de sources
- Poste L06-003 : intitulé trop vague
- Pas de références normatives

**Consigne** :

1. **Ouvrez** `/home/user/stone-sea/MODULE_04/02_prompts/prompt_structuration_dqe.md`
2. **Utilisez le Wrapper 2** (Sources obligatoires) + ce prompt
3. **Fournissez** à l'IA :
   - Le CSV brouillon ci-dessus
   - Cet extrait CCTP fictif :

```
CCTP Lot 06 - Charpente métallique et couverture
Article 6.1 : Charpente en acier S235JR, selon NF EN 1090-2
Poids estimé : 2500 kg (note de calcul BET-STRUCT-2024-12)
Article 6.2 : Couverture bac acier nervuré 0,75 mm
Surface de toiture : 480 m² (Plan A-401)
Article 6.3 : Lanterneaux de désenfumage
12 unités à prévoir (étude sécurité incendie)
Article 6.4 : Isolation sous couverture
Laine de roche 100 mm, lambda 0,035 W/m.K (NF DTU 45.10)
```

4. **Demandez** à l'IA : "Normalise ce DQE et retourne le JSON conforme + rapport d'anomalies"

**Réponse attendue** (extrait) :

```json
[
  {
    "code": "L06-001",
    "intitule": "Charpente métallique acier S235JR",
    "description": "Fourniture, fabrication et pose selon plans d'exécution",
    "unite": "kg",
    "quantite": 2500.0,
    "prix_unitaire": 4.5,
    "montant": 11250.0,
    "hypotheses": "Poids d'après note de calcul BET-STRUCT-2024-12",
    "sources": ["CCTP_L06.pdf#Art.6.1", "Note_Calcul_BET-STRUCT-2024-12"],
    "liens_normatifs": ["NF EN 1090-2"],
    "tags": ["L06", "charpente", "metal"]
  },
  {
    "code": "L06-002",
    "intitule": "Couverture bac acier nervuré 0,75 mm",
    "description": "Fourniture et pose y.c. accessoires de fixation et étanchéité",
    "unite": "m2",
    "quantite": 480.0,
    "prix_unitaire": 28.0,
    "montant": 13440.0,
    "hypotheses": "Surface nette d'après Plan A-401",
    "sources": ["CCTP_L06.pdf#Art.6.2", "Plan_A-401"],
    "liens_normatifs": ["NF DTU 40.35 (édition à préciser)"],
    "tags": ["L06", "couverture"]
  },
  {
    "code": "L06-003",
    "intitule": "Lanterneaux de désenfumage",
    "description": "Fourniture et pose de lanterneaux conformes à l'étude sécurité incendie",
    "unite": "u",
    "quantite": 12.0,
    "prix_unitaire": 450.0,
    "montant": 5400.0,
    "hypotheses": "12 unités d'après étude sécurité incendie",
    "sources": ["CCTP_L06.pdf#Art.6.3", "Etude_Incendie_2024"],
    "liens_normatifs": ["NF S 61-937 (édition à préciser)"],
    "tags": ["L06", "desenfumage"]
  },
  {
    "code": "L06-004",
    "intitule": "Isolation sous couverture laine de roche 100 mm",
    "description": "Fourniture et pose y.c. pare-vapeur et fixations",
    "unite": "m2",
    "quantite": 480.0,
    "prix_unitaire": 12.8,
    "montant": 6144.0,
    "hypotheses": "Surface identique à la couverture",
    "sources": ["CCTP_L06.pdf#Art.6.4", "Plan_A-401"],
    "liens_normatifs": ["NF DTU 45.10"],
    "tags": ["L06", "isolation"]
  }
]
```

**Rapport d'anomalies** (attendu de l'IA) :

```
ANOMALIES CORRIGÉES :
1. Poste L06-001 : Description ajoutée d'après CCTP Art.6.1
2. Poste L06-002 : Description + référence DTU 40.35 ajoutée
3. Poste L06-003 : Intitulé précisé "Lanterneaux de désenfumage"
4. Tous les postes : Sources et hypothèses ajoutées d'après CCTP

SOURCES MANQUANTES :
- Éditions précises des NF DTU 40.35 et NF S 61-937
- Plan d'exécution charpente (référence à ajouter)

MONTANT TOTAL : 36 234,00 € HT
```

**Points de contrôle** :
- [ ] Tous les postes ont une description explicite
- [ ] Hypothèses clairement documentées
- [ ] Sources tracées (fichier#article ou page)
- [ ] Références normatives identifiées
- [ ] Montants calculés correctement
- [ ] Rapport d'anomalies produit

---

### Exercice 4 : Production d'un CR de chantier structuré

**Objectif** : Transformer des notes de chantier en CR structuré JSON puis Markdown

**Contexte** : Vous êtes conducteur de travaux. Après une visite de chantier, vous avez pris des notes brutes. Vous devez produire un CR officiel.

**Notes de terrain** :

```
Date : 20/11/2024, 9h-11h30
Chantier : Résidence Les Érables, Bâtiment B
Présents : MOE (Dupont), Entreprise GO (Martin), CdT (moi)

AVANCEMENT :
- Dalle RDC coulée hier (19/11), décoffrage prévu 22/11
- Murs R+1 en cours, hauteur atteinte : 2,80m (sur 3,20m)
- Livraison préfabriqués escaliers prévue 25/11

PROBLÈMES :
1. Béton dalle : BL indique C25/30 mais CCTP prescrit C30/37 !!!
   Photo : IMG_2547.jpg (BL affiché)
   → Arrêt décoffrage, attente avis BET

2. Armatures R+1 : recouvrement insuffisant poteau P12 (15cm au lieu de 40cm)
   Photo : IMG_2551.jpg
   → NC à ouvrir, reprise avant coulage

MÉTÉO : Pluie annoncée 22-23/11 → protections à prévoir

DÉCISIONS :
- Dupont (MOE) : demande note calcul BET pour béton C25/30 → délai 24h
- Martin (GO) : reprise armatures P12 ce jour → contrôle demain 21/11
- Moi : commander bâches protection dalle
```

**Consignes** :

**Étape 1 : Structuration avec IA**

1. **Ouvrez** `/home/user/stone-sea/MODULE_04/02_prompts/prompt_cr_chantier.md`
2. **Utilisez** le prompt avec les notes ci-dessus
3. **Fournissez** également :
   - Photos : `IMG_2547.jpg` (BL béton), `IMG_2551.jpg` (armatures P12)
   - Planning : "Semaine 47 : Coulage dalles RDC + Élévation R+1"
   - Écarts : "Béton non-conforme, armatures NC"

**Réponse JSON attendue** :

```json
{
  "date": "2024-11-20",
  "heure_debut": "09:00",
  "heure_fin": "11:30",
  "chantier": "Résidence Les Érables - Bâtiment B",
  "participants": [
    {"nom": "Dupont", "fonction": "Maître d'œuvre", "organisme": "MOE"},
    {"nom": "Martin", "fonction": "Conducteur de travaux", "organisme": "Entreprise GO"},
    {"nom": "[Votre nom]", "fonction": "Conducteur de travaux", "organisme": "[Votre entreprise]"}
  ],
  "avancement": [
    {
      "lot": "Gros œuvre",
      "activite": "Dalle RDC coulée",
      "avancement_prevu": 100,
      "avancement_reel": 100,
      "ecart": 0,
      "commentaire": "Coulage effectué le 19/11, décoffrage suspendu (voir NC)",
      "photos": ["IMG_2547.jpg"]
    },
    {
      "lot": "Gros œuvre",
      "activite": "Élévation murs R+1",
      "avancement_prevu": 100,
      "avancement_reel": 87,
      "ecart": -13,
      "commentaire": "Hauteur atteinte 2,80m sur 3,20m requis",
      "photos": []
    }
  ],
  "nc_et_reserves": [
    {
      "id": "NC-2024-001",
      "gravite": "MAJEURE",
      "description": "Béton dalle RDC : BL indique C25/30 au lieu de C30/37 prescrit au CCTP",
      "lot": "Gros œuvre",
      "localisation": "Dalle RDC Bâtiment B",
      "photo": "IMG_2547.jpg",
      "impact": "Arrêt décoffrage, risque de non-conformité structurelle",
      "action_immediate": "Attente avis BET et note de calcul (délai 24h)"
    },
    {
      "id": "NC-2024-002",
      "gravite": "MAJEURE",
      "description": "Recouvrement armatures insuffisant poteau P12 : 15 cm constaté au lieu de 40 cm requis (NF DTU 21)",
      "lot": "Gros œuvre",
      "localisation": "Poteau P12 - R+1",
      "photo": "IMG_2551.jpg",
      "impact": "Non-conformité normative, risque structurel",
      "action_immediate": "Reprise armatures par entreprise GO ce jour (20/11)"
    }
  ],
  "risques": [
    {
      "type": "Météo",
      "description": "Pluie annoncée 22-23/11",
      "impact": "Risque d'infiltration dalle fraîche",
      "mesure_preventive": "Commande bâches de protection",
      "responsable": "[Votre nom]",
      "echeance": "21/11/2024"
    }
  ],
  "plan_actions": [
    {
      "id": "ACT-001",
      "description": "Demander note de calcul BET pour validation béton C25/30",
      "responsable": "Dupont (MOE)",
      "echeance": "21/11/2024",
      "critere_succes": "Note de calcul reçue et béton validé ou reprise prescrite",
      "statut": "En cours"
    },
    {
      "id": "ACT-002",
      "description": "Reprise recouvrement armatures poteau P12",
      "responsable": "Martin (GO)",
      "echeance": "20/11/2024",
      "critere_succes": "Recouvrement conforme 40 cm minimum (NF DTU 21)",
      "statut": "En cours"
    },
    {
      "id": "ACT-003",
      "description": "Contrôle contradictoire armatures P12 après reprise",
      "responsable": "[Votre nom]",
      "echeance": "21/11/2024",
      "critere_succes": "Validation visuelle + photos + levée NC-2024-002",
      "statut": "Planifié"
    },
    {
      "id": "ACT-004",
      "description": "Mise en place bâches protection dalle RDC",
      "responsable": "[Votre nom]",
      "echeance": "21/11/2024",
      "critere_succes": "Dalle entièrement protégée avant pluie du 22/11",
      "statut": "Planifié"
    }
  ],
  "prochaine_reunion": "27/11/2024",
  "redacteur": "[Votre nom]",
  "date_redaction": "2024-11-20"
}
```

**Étape 2 : Export Markdown**

```bash
python 03_scripts/cr_json_to_md.py cr_chantier_20241120.json cr_chantier_20241120.md
```

**Rendu Markdown attendu** (extrait) :

```markdown
# Compte-rendu de chantier

**Date** : 20/11/2024 (09:00 - 11:30)
**Chantier** : Résidence Les Érables - Bâtiment B

## Participants
- Dupont - Maître d'œuvre (MOE)
- Martin - Conducteur de travaux (Entreprise GO)
- [Votre nom] - Conducteur de travaux ([Votre entreprise])

## Avancement

| Lot | Activité | Prévu | Réel | Écart | Commentaire |
|-----|----------|-------|------|-------|-------------|
| Gros œuvre | Dalle RDC coulée | 100% | 100% | 0% | Coulage 19/11, décoffrage suspendu (voir NC) 📷 IMG_2547.jpg |
| Gros œuvre | Élévation murs R+1 | 100% | 87% | -13% | Hauteur 2,80m / 3,20m |

## Non-conformités et réserves

### ⚠️ NC-2024-001 - MAJEURE
**Lot** : Gros œuvre
**Description** : Béton dalle RDC : BL indique C25/30 au lieu de C30/37 prescrit au CCTP
**Localisation** : Dalle RDC Bâtiment B
**Photo** : 📷 IMG_2547.jpg
**Impact** : Arrêt décoffrage, risque de non-conformité structurelle
**Action immédiate** : Attente avis BET et note de calcul (délai 24h)

### ⚠️ NC-2024-002 - MAJEURE
**Lot** : Gros œuvre
**Description** : Recouvrement armatures insuffisant poteau P12 : 15 cm constaté au lieu de 40 cm requis (NF DTU 21)
**Localisation** : Poteau P12 - R+1
**Photo** : 📷 IMG_2551.jpg
**Impact** : Non-conformité normative, risque structurel
**Action immédiate** : Reprise armatures par entreprise GO ce jour (20/11)

## Plan d'actions

| ID | Action | Responsable | Échéance | Critère de succès | Statut |
|----|--------|-------------|----------|-------------------|--------|
| ACT-001 | Demander note de calcul BET pour validation béton C25/30 | Dupont (MOE) | 21/11/2024 | Note reçue et béton validé ou reprise prescrite | 🔄 En cours |
| ACT-002 | Reprise recouvrement armatures poteau P12 | Martin (GO) | 20/11/2024 | Recouvrement ≥ 40 cm (NF DTU 21) | 🔄 En cours |
| ACT-003 | Contrôle contradictoire armatures P12 | [Votre nom] | 21/11/2024 | Validation + photos + levée NC-2024-002 | 📅 Planifié |
| ACT-004 | Bâches protection dalle RDC | [Votre nom] | 21/11/2024 | Dalle protégée avant pluie 22/11 | 📅 Planifié |

## Risques identifiés
- **Météo** : Pluie 22-23/11 → Risque infiltration dalle → Mesure : Bâches protection (Resp: [Votre nom], échéance: 21/11)

---
**Prochaine réunion** : 27/11/2024
**Rédacteur** : [Votre nom] - Date : 20/11/2024
```

**Points de contrôle** :
- [ ] JSON conforme au schéma cr_chantier.schema.json
- [ ] Tous les points importants liés à une photo ou référence
- [ ] NC classées par gravité (MINEURE, MAJEURE, CRITIQUE)
- [ ] Plan d'actions avec qui/quoi/quand/critère de succès
- [ ] Export Markdown lisible et diffusable
- [ ] Traçabilité complète (dates, responsables, photos)

---

### Exercice 5 : Intégration complète - Projet "Extension bureaux"

**Objectif** : Produire l'ensemble documentaire complet pour un mini-projet (CCTP + DQE + CR)

**Contexte du projet** :
Vous êtes maître d'œuvre d'exécution sur l'extension d'un bâtiment de bureaux :
- Surface créée : 120 m²
- Lot unique : Structure + Couverture
- Durée : 6 semaines

**Livrables attendus** :
1. CCTP du lot (Markdown)
2. DQE du lot (JSON validé)
3. CR de la réunion de démarrage (JSON + Markdown)

---

**DOCUMENT 1 : Cahier des charges MOA**

```
PROJET : Extension bureaux - Site de Lyon
Surface créée : 120 m²
Structure : Ossature bois (douglas classe 2)
Fondations : Longrines béton C25/30
Couverture : Bac acier isolé, pente 15%
Performances :
- Isolation thermique : R ≥ 6,0 m².K/W
- Acoustique : isolement ≥ 45 dB (cloison bureaux)
Références : NF DTU 31.2 (ossature bois), NF DTU 40.35 (couverture acier)
```

**DOCUMENT 2 : Plans**

```
Plan ARCHI-01 : Emprise extension 120 m² (10m × 12m)
Plan STRUCT-02 : 12 poteaux bois 120×120mm, hauteur 3,00m
Plan TOIT-03 : Couverture 125 m² (surface développée avec pente)
```

**DOCUMENT 3 : DQE brouillon**

```csv
code,intitule,unite,quantite,prix_unitaire
EXT-001,Terrassement + longrines béton,ml,44,180
EXT-002,Poteaux bois douglas 120×120,u,12,220
EXT-003,Ossature bois complète,m2,120,95
EXT-004,Couverture bac acier isolé,m2,125,68
EXT-005,Menuiseries extérieures,forfait,1,8500
```

**DOCUMENT 4 : Notes réunion de démarrage (18/11/2024)**

```
Présents : MOA (Bertrand), MOE (vous), Entreprise (Léger Bois SARL)

- Démarrage travaux confirmé : 02/12/2024
- Livraison ossature préfabriquée : semaine du 09/12
- Terrassement + longrines : semaines 49-50
- Alerte : délai livraison menuiseries rallongé (8 → 10 semaines)
  → Impact planning : livraison prévue semaine 6 au lieu de semaine 4
  → Entreprise demande avenant délai global +2 semaines

Décision MOA : Accepte avenant si pas de surcoût
Action MOE : Produire planning révisé + avenant (délai 5j)
Action Entreprise : Confirmer aucun surcoût (délai 48h)
```

---

**TRAVAIL DEMANDÉ**

**Tâche 1 : CCTP** (1h)

Utilisez le prompt `prompt_redaction_cctp.md` pour produire le CCTP du lot "Structure + Couverture".

**Attendu** :
- Fichier `CCTP_Extension_Bureaux.md`
- Structure complète (9 sections)
- Toutes exigences sourcées avec `[Preuve:]`
- Section "Points de vigilance" incluant le délai menuiseries

---

**Tâche 2 : DQE** (45 min)

**a)** Complétez le CSV brouillon en ajoutant les colonnes manquantes :
   - `description`
   - `hypotheses`
   - `sources`
   - `liens_normatifs`
   - `tags`

**b)** Convertissez en JSON : `python csv_dqe_to_json.py dqe_extension.csv dqe_extension.json`

**c)** Validez : `python check_dqe_json.py dqe_extension.json`

**d)** Corrigez les anomalies détectées

**Attendu** :
- Fichier `dqe_extension.json` conforme (0 erreurs)
- Montant total calculé
- Toutes sources tracées

---

**Tâche 3 : CR de démarrage** (45 min)

Utilisez le prompt `prompt_cr_chantier.md` pour structurer le CR de la réunion du 18/11.

**Attendu** :
- Fichier `CR_Reunion_Demarrage_20241118.json`
- Export Markdown `CR_Reunion_Demarrage_20241118.md`
- Plan d'actions avec 3 actions minimum :
  - ACT-001 : Production planning révisé (MOE, délai 5j)
  - ACT-002 : Confirmation aucun surcoût (Entreprise, délai 48h)
  - ACT-003 : [Troisième action à identifier]
- Risque "Retard menuiseries" correctement documenté

---

**Tâche 4 : Traçabilité** (15 min)

Créez un fichier `TRACABILITE_Extension_Bureaux.md` listant :

```markdown
# Traçabilité documentaire - Projet Extension Bureaux

## Livrables produits

| Livrable | Version | Date | Hash SHA-256 | Statut |
|----------|---------|------|--------------|--------|
| CCTP_Extension_Bureaux.md | 1.0 | 20/11/2024 | [calculer] | ✅ Validé |
| dqe_extension.json | 1.1 | 20/11/2024 | [calculer] | ✅ Conforme |
| CR_Reunion_Demarrage_20241118.json | 1.0 | 20/11/2024 | [calculer] | ✅ Diffusé |

## Sources utilisées

| ID | Document | Version | Date | Utilisation |
|----|----------|---------|------|-------------|
| S001 | Cahier_Charges_MOA.pdf | v2.1 | 15/11/2024 | Exigences CCTP + DQE |
| S002 | Plan_ARCHI-01.dwg | Ind.B | 10/11/2024 | Quantitatifs DQE |
| S003 | Plan_STRUCT-02.dwg | Ind.A | 10/11/2024 | CCTP structure |
| S004 | Plan_TOIT-03.dwg | Ind.A | 10/11/2024 | DQE couverture |
| S005 | CR_Reunion_18nov.docx | - | 18/11/2024 | CR formalisé |

## Contrôles effectués

- [x] CCTP : Validation format trame (9 sections)
- [x] CCTP : Toutes exigences sourcées
- [x] DQE : Validation schéma JSON (check_dqe_json.py)
- [x] DQE : Montants calculés corrects
- [x] CR : Plan d'actions complet (qui/quoi/quand/critère)
- [x] CR : Export Markdown lisible

## Archivage

- Emplacement : `/projet/extension_bureaux/documents/`
- Backup : [serveur/cloud]
- Durée de conservation : 10 ans (garantie décennale)
```

Calculez les hash SHA-256 :
```bash
sha256sum CCTP_Extension_Bureaux.md
sha256sum dqe_extension.json
sha256sum CR_Reunion_Demarrage_20241118.json
```

---

**Points de contrôle finaux** :
- [ ] 3 livrables produits (CCTP, DQE, CR)
- [ ] Tous les fichiers JSON validés (schéma conforme)
- [ ] Traçabilité complète des sources
- [ ] Hash SHA-256 calculés et archivés
- [ ] Aucune information inventée (tout est sourcé)
- [ ] Export Markdown prêt à diffusion

---

## 🏆 Partie 3 : Évaluation finale (1h)

### Cas pratique : Contrôle qualité d'un ensemble documentaire

**Contexte** :
Un collègue vous transmet l'ensemble documentaire d'un projet de réhabilitation. Vous devez le contrôler et corriger les anomalies.

**Documents fournis** :

1. **CCTP_Rehabilitation.md** (extrait)

```markdown
## Objet du lot
Rénovation énergétique : isolation par l'extérieur + menuiseries

## Matériaux
Isolation : polystyrène expansé 120 mm
Menuiseries : PVC double vitrage

## Mise en œuvre
Selon règles de l'art
```

2. **dqe_rehabilitation.json** (extrait)

```json
[
  {
    "code": "R01-001",
    "intitule": "ITE polystyrène 120mm",
    "unite": "m2",
    "quantite": 280,
    "prix_unitaire": 65,
    "montant": 18200,
    "sources": [],
    "liens_normatifs": []
  },
  {
    "code": "R01-002",
    "intitule": "Menuiseries PVC",
    "description": "Fourniture et pose",
    "unite": "u",
    "quantite": 18,
    "prix_unitaire": 850,
    "montant": 15400
  }
]
```

3. **cr_chantier.json** (extrait)

```json
{
  "date": "2024-11-15",
  "participants": [],
  "nc_et_reserves": [
    {
      "id": "NC-001",
      "description": "Isolation posée sans pare-vapeur",
      "action_immediate": "À voir"
    }
  ],
  "plan_actions": [
    {
      "description": "Reprendre isolation",
      "responsable": "Entreprise"
    }
  ]
}
```

---

### Questions de l'évaluation

**Question 1** (20 points) : Listez toutes les anomalies détectées dans chaque document (CCTP, DQE, CR)

**Question 2** (20 points) : Corrigez le fichier `dqe_rehabilitation.json` pour le rendre conforme au schéma

**Question 3** (20 points) : Réécrivez la section "Matériaux" du CCTP en ajoutant :
- Références normatives avec éditions
- Balises `[Preuve:]`
- Performances chiffrées (R, Uw)

**Question 4** (20 points) : Complétez le CR en ajoutant :
- Participants (au moins 2)
- NC-001 : gravité, lot, localisation, impact, photo
- Plan d'actions : ACT-001 avec échéance, critère de succès, statut

**Question 5** (20 points) : Proposez un processus de contrôle qualité systématique pour éviter ces anomalies à l'avenir (checklist, scripts, validations)

### Barème

**Total : 100 points**

- **< 50 points** : Non acquis - Reprendre les exercices
- **50-69 points** : Partiellement acquis - Renforcer la validation
- **70-84 points** : Acquis - Utilisation correcte du MODULE_04
- **85-100 points** : Maîtrisé - Autonome en production

---

## 📖 Partie 4 : Ressources et bonnes pratiques

### 4.1 Checklist avant diffusion d'un document

**CCTP** :
- [ ] Structure complète (9 sections de la trame)
- [ ] Toutes exigences techniques sourcées avec `[Preuve:]`
- [ ] Références normatives avec éditions et dates
- [ ] Section "Points de vigilance" remplie
- [ ] Section "Dérogations contractuelles" si applicable
- [ ] Mentions "à compléter" pour infos manquantes
- [ ] Relu par un expert métier

**DQE/DPGF** :
- [ ] Conversion CSV → JSON réussie
- [ ] Validation schéma : `python check_dqe_json.py [fichier]`
- [ ] Tous les champs obligatoires présents (code, intitule, unite, quantite, prix_unitaire, montant, sources)
- [ ] Unités dans l'enum autorisé (m, m2, m3, u, kg, h, forfait)
- [ ] Montants = quantite × prix_unitaire (2 décimales)
- [ ] Au moins une source par poste
- [ ] Hypothèses documentées
- [ ] Montant total calculé et vérifié

**CR de chantier** :
- [ ] JSON conforme au schéma cr_chantier.schema.json
- [ ] Date, heure, chantier, participants renseignés
- [ ] Avancement avec écarts calculés (prévu vs réel)
- [ ] NC classées (MINEURE, MAJEURE, CRITIQUE) avec photos
- [ ] Plan d'actions complet : qui/quoi/quand/critère/statut
- [ ] Risques identifiés avec mesures préventives
- [ ] Export Markdown lisible : `python cr_json_to_md.py`
- [ ] Diffusé aux participants sous 48h

### 4.2 Workflows recommandés

**Workflow 1 : Nouveau projet**

```
1. Réception documents MOA/MOE
   ↓
2. Rédaction CCTP assistée (prompt + Wrapper 2)
   ↓
3. Structuration DQE depuis devis (CSV → JSON)
   ↓
4. Validation DQE (check_dqe_json.py)
   ↓
5. Création évidences MODULE_03
   ↓
6. Validation MOE + archivage (hash SHA-256)
```

**Workflow 2 : Suivi chantier**

```
1. Visite chantier + prise de notes/photos
   ↓
2. Structuration CR (prompt_cr_chantier.md)
   ↓
3. Génération JSON + validation schéma
   ↓
4. Export Markdown (cr_json_to_md.py)
   ↓
5. Diffusion participants sous 48h
   ↓
6. Suivi plan d'actions (statuts à jour)
```

### 4.3 Intégration avec autres modules

**MODULE_03 (Évidences)** :
- Créer une évidence par livrable clé (CCTP, DQE, CR)
- Tracer les sources et références normatives
- Générer rapport AQ avec matrice de risques

**MODULE_05 (Conformité)** :
- Contrôler CCTP vs normes (`check_cctp_vs_normes.py`)
- Vérifier preuves de conformité dans CR
- Gérer les NC détectées (registre normatif)

**MODULE_06 (Plan d'essais)** :
- Lier postes DQE aux essais planifiés
- Intégrer résultats PV dans CR de chantier
- Tracer validation des livrables

### 4.4 Erreurs fréquentes à éviter

❌ **Erreur 1** : CCTP sans sources ni preuves
→ ✅ Toujours ajouter `[Preuve: fichier#page]` pour chaque exigence

❌ **Erreur 2** : DQE avec montants incohérents
→ ✅ Laisser le script calculer : `montant = quantite × prix_unitaire`

❌ **Erreur 3** : CR sans plan d'actions ou avec actions vagues
→ ✅ Exiger : qui/quoi/quand/critère de succès/statut

❌ **Erreur 4** : Normes sans éditions
→ ✅ Format imposé : "NF DTU XX.X (Mois AAAA)" ou "[édition à préciser]"

❌ **Erreur 5** : Validation schéma JSON ignorée
→ ✅ Toujours lancer `check_dqe_json.py` avant diffusion

❌ **Erreur 6** : Documents sans traçabilité (pas de hash, pas de version)
→ ✅ Calculer hash SHA-256 et versionner (v1.0, v1.1...)

### 4.5 Outils complémentaires

**Validation JSON** :
```bash
# Validation manuelle avec Python
python -m json.tool fichier.json

# Avec jq (si installé)
jq . fichier.json
```

**Calcul hash SHA-256** :
```bash
sha256sum fichier.md
sha256sum fichier.json
```

**Conversion formats** :
```bash
# Markdown → PDF (nécessite pandoc)
pandoc CCTP.md -o CCTP.pdf

# JSON → CSV (si besoin inverse)
python json_to_csv.py [à développer si nécessaire]
```

---

## 📝 Annexes

### Annexe A : Schémas JSON récapitulatifs

**Schéma Poste DQE** (champs obligatoires) :
```json
{
  "code": "string",              // Ex: "L01-001"
  "intitule": "string",          // Ex: "Isolation 200mm"
  "unite": "enum",               // m, m2, m3, u, kg, h, forfait
  "quantite": "number ≥ 0",
  "prix_unitaire": "number ≥ 0",
  "montant": "number ≥ 0",       // = quantite × prix_unitaire
  "sources": ["array"]           // Au moins 1 source
}
```

**Schéma CR Chantier** (structure minimale) :
```json
{
  "date": "YYYY-MM-DD",
  "participants": [{"nom": "", "fonction": "", "organisme": ""}],
  "avancement": [...],
  "nc_et_reserves": [...],
  "plan_actions": [...]
}
```

### Annexe B : Commandes rapides

```bash
# MODULE_04 - Scripts

# Conversion DQE CSV → JSON
python 03_scripts/csv_dqe_to_json.py input.csv output.json

# Validation DQE JSON
python 03_scripts/check_dqe_json.py fichier.json

# Export CR JSON → Markdown
python 03_scripts/cr_json_to_md.py cr.json cr.md

# Calcul hash (archivage)
sha256sum fichier.md fichier.json > PACKAGE_SHA256.txt
```

### Annexe C : Ressources complémentaires

**Documentation Stone-Sea** :
- `README.md` : Vue d'ensemble du projet
- `MODULE_04/05_docs/README_integration_module04.md` : Pipeline complet
- `MODULE_04/05_docs/checklists.md` : Checklists de contrôle

**Normes BTP** :
- NF DTU 21 : Ouvrages en béton
- NF DTU 31.2 : Ossature bois
- NF DTU 40.35 : Couverture bac acier
- NF DTU 43.1 : Étanchéité toitures-terrasses

**Formats et standards** :
- JSON Schema : https://json-schema.org/
- Markdown (CommonMark) : https://commonmark.org/
- PDF/A (archivage pérenne) : ISO 19005

---

## 🎓 Conclusion

Vous maîtrisez maintenant les outils de production documentaire du MODULE_04 :

✅ **CCTP** : Rédaction structurée et traçable
✅ **DQE/DPGF** : Structuration, validation, conversion
✅ **CR de chantier** : Production normalisée et diffusable
✅ **Scripts** : Automatisation des contrôles et exports
✅ **Traçabilité** : Sources, versions, hash SHA-256

**Prochaines étapes** :
1. Intégrer MODULE_04 dans vos projets réels
2. Combiner avec MODULE_03 (évidences) et MODULE_05 (conformité)
3. Automatiser vos workflows documentaires
4. Former vos équipes aux prompts et scripts

**Rappel important** :
Les outils IA et scripts sont des **assistants**, pas des **substituts** à l'expertise métier. La validation humaine par un professionnel qualifié reste **obligatoire** pour tous les livrables contractuels.

---

**Version** : 1.0
**Date de création** : 2024-11-20
**Auteur** : Stone-Sea Project
**Contact** : [À compléter]
