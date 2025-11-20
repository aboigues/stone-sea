# Stone-Sea

Système de gestion de la conformité et de la documentation pour le secteur BTP (Bâtiment et Travaux Publics).

## 📋 Vue d'ensemble

Stone-Sea est un ensemble d'outils et de modules permettant de gérer la conformité normative, la production documentaire et le suivi des essais dans les projets de construction. Le projet s'articule autour de :

- **Contrôles normatifs** basés sur les référentiels NF DTU, Eurocodes et Avis techniques
- **Production documentaire assistée** (CCTP, DQE/DPGF, CR de chantier)
- **Gestion des non-conformités** et des preuves de conformité
- **Planification et suivi des essais** et contrôles chantier
- **Traçabilité complète** avec journalisation des sources et versioning

## 🏗️ Architecture

Le projet est organisé en 6 modules principaux :

### MODULE_01 : Wrappers IA
Ensemble de 8 wrappers pour encadrer et sécuriser les interactions avec les systèmes d'IA :
- **Wrapper 1** : Contexte limité (pas d'extrapolation)
- **Wrapper 2** : Sources obligatoires et datation
- **Wrapper 3** : Sortie vérifiable (tableau 2 colonnes)
- **Wrapper 4** : Données sensibles (RGPD, refus/alerte)
- **Wrapper 5** : Double raisonnement + matrice avantages/risques
- **Wrapper 6** : Journal des sources (traçabilité)
- **Wrapper 7** : Citations numérotées et horodatage
- **Wrapper 8** : Contrôle normatif DTU/Eurocodes

📁 Emplacement : `MODULE_01/wrappers_markdown/`

### MODULE_02 : Pack d'industrialisation
Pack complet d'industrialisation pour déployer des cas d'usage IA BTP conformes :
- Fiche cas d'usage
- Charte des sources
- Prompts contrôlés + schémas JSON
- Pipeline (anonymisation, traitement, vérification, archivage)
- Tests et évaluation
- SOP exploitation et playbook incidents
- Dashboards métriques
- Plan de réversibilité

📁 Emplacement : `MODULE_02/export_pack/`

### MODULE_03 : Module 3
Module complémentaire (à documenter plus en détail).

📁 Emplacement : `MODULE_03/module3/`

### MODULE_04 : Production documentaire
Outils pour la production assistée de documents BTP :
- **Schémas JSON** : DQE, CR de chantier
- **Prompts** : Rédaction CCTP, structuration DQE, CR chantier
- **Scripts** :
  - `csv_dqe_to_json.py` : Conversion CSV → JSON
  - `check_dqe_json.py` : Validation DQE
  - `cr_json_to_md.py` : Export CR JSON → Markdown
- **Modèles** : Trames CCTP, DQE, CR
- **Exemples** prêts à l'emploi

📁 Emplacement : `MODULE_04/`

### MODULE_05 : Conformité normative
Gestion de la conformité aux référentiels (NF DTU, Eurocodes, AT) :
- **Schémas JSON** : Exigences normatives, preuves, NC, registre normatif
- **Règles** : Exigences couverture, menuiseries, mapping
- **Scripts** :
  - `check_cctp_vs_normes.py` : Contrôle CCTP vs normes
  - `check_cr_pv_preuves.py` : Vérification des preuves
  - `nc_register_merge.py` : Fusion des registres NC
  - `dashboard_kpis.py` : KPIs de conformité
- **Prompts** : Contrôle CCTP, qualification NC
- **Registre NC** et rapports de conformité

📁 Emplacement : `MODULE_05/`

### MODULE_06 : Plan d'essais et PV
Planification et suivi des essais et contrôles chantier :
- **Schémas JSON** : Plan de contrôle, essais, PV, échantillonnage
- **Règles** : Contrôles béton, chapes, mapping unités
- **Scripts** :
  - `planificateur_essais.py` : Planification automatique
  - `validate_pv_vs_exigences.py` : Validation PV
  - `echantillonnage_calcul.py` : Calcul d'échantillonnage
  - `kpi_essais.py` : KPIs des essais
- **Prompts** : Génération plan de contrôle, analyse PV
- **Modèles** et exemples de plans de contrôle

📁 Emplacement : `MODULE_06/`

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- Aucune dépendance externe requise (bibliothèque standard uniquement)

### Génération des modules

Chaque module peut être généré indépendamment :

```bash
# Module 04 - Production documentaire
python gen-mod4.py --out ./MODULE_04 --zip

# Module 05 - Conformité normative
python gen-mod5.py --out ./MODULE_05 --zip

# Module 06 - Plan d'essais
python gen-mod6.py --out ./MODULE_06 --zip

# Wrappers IA
python gen-wrapper.py

# Pack d'industrialisation complet
python gen-pack-indus.py
```

## 📖 Guide d'utilisation

### MODULE_04 : Production documentaire

#### Conversion DQE (CSV → JSON)
```bash
python MODULE_04/03_scripts/csv_dqe_to_json.py input.csv output.json
```

#### Validation DQE
```bash
python MODULE_04/03_scripts/check_dqe_json.py dqe.json
```

#### Export CR de chantier (JSON → Markdown)
```bash
python MODULE_04/03_scripts/cr_json_to_md.py cr.json rapport.md
```

### MODULE_05 : Conformité normative

#### Contrôle CCTP vs normes
```bash
python MODULE_05/03_scripts/check_cctp_vs_normes.py \
  --cctp ./cctp.md \
  --exigences ./MODULE_05/02_regles/exigences_couverture.json \
  --out_md rapport.md
```

#### Vérification des preuves
```bash
python MODULE_05/03_scripts/check_cr_pv_preuves.py \
  --registre registre.json \
  --out_json preuves.json
```

#### Fusion des NC
```bash
python MODULE_05/03_scripts/nc_register_merge.py \
  --inputs nc1.json nc2.json nc3.json \
  --out registre_nc_merged.json
```

#### KPIs de conformité
```bash
python MODULE_05/03_scripts/dashboard_kpis.py \
  --registre registre.json
```

### MODULE_06 : Plan d'essais

#### Planification des essais
```bash
python MODULE_06/03_scripts/planificateur_essais.py \
  --plan plan_controle.json \
  --quantites mesures.json \
  --out planning.json
```

#### Validation des PV
```bash
python MODULE_06/03_scripts/validate_pv_vs_exigences.py \
  --plan plan_controle.json \
  --pv pv_exemples.json \
  --out pv_valides.json
```

#### Calcul d'échantillonnage
```bash
python MODULE_06/03_scripts/echantillonnage_calcul.py \
  --essai_id BET-RESIST \
  --plan plan_controle.json \
  --quantites mesures.json
```

#### KPIs des essais
```bash
python MODULE_06/03_scripts/kpi_essais.py \
  --planning planning.json \
  --pv pv_exemples.json
```

## 🔒 Sécurité et conformité

### Données sensibles
Le MODULE_01 (Wrapper 4) intègre des contrôles pour :
- Détection des données personnelles (RGPD)
- Protection du secret des affaires (prix, montants)
- Anonymisation des identifiants contractuels

### Anonymisation
Le MODULE_02 fournit des règles d'anonymisation pour :
- Plaques d'immatriculation
- Dates
- Données PII (noms, emails, téléphones)
- Métadonnées de documents
- Propriétés IFC sensibles

### Traçabilité
Tous les modules intègrent :
- Journalisation des sources utilisées
- Horodatage des opérations
- Hash SHA-256 des packages
- Citations numérotées avec références précises

## 📊 Formats de données

Tous les modules utilisent des schémas JSON standardisés pour assurer :
- Interopérabilité entre modules
- Validation automatique des données
- Traçabilité complète
- Export et archivage pérenne

### Schémas principaux
- `poste_dqe.schema.json` - Postes DQE/DPGF
- `cr_chantier.schema.json` - Comptes-rendus de chantier
- `exigence_normative.schema.json` - Exigences normatives
- `preuve_conformite.schema.json` - Preuves de conformité
- `nc.schema.json` - Non-conformités
- `plan_controle.schema.json` - Plans de contrôle
- `essai.schema.json` - Essais et mesures
- `pv.schema.json` - Procès-verbaux

## 🎯 Référentiels normatifs

Le projet s'appuie sur les référentiels suivants :
- **NF DTU** (Documents Techniques Unifiés) : 20.1, 21, 26.2, 36.5, 40.21, 40.29, 45.x, 60.5, 65.x, 70.1, etc.
- **Eurocodes** : EN 206/CN, EN 12350-2, etc.
- **Avis techniques** (AT)
- **Règles professionnelles**

⚠️ **Important** : Les éditions et dates des normes doivent toujours être renseignées précisément dans vos projets.

## 📁 Structure du projet

```
stone-sea/
├── MODULE_01/              # Wrappers IA
│   └── wrappers_markdown/
├── MODULE_02/              # Pack industrialisation
│   └── export_pack/
├── MODULE_03/              # Module 3
│   └── module3/
├── MODULE_04/              # Production documentaire
│   ├── 01_schemas/
│   ├── 02_prompts/
│   ├── 03_scripts/
│   ├── 04_modeles/
│   ├── 05_docs/
│   └── 06_examples/
├── MODULE_05/              # Conformité normative
│   ├── 01_schemas/
│   ├── 02_regles/
│   ├── 03_scripts/
│   ├── 04_prompts/
│   ├── 05_modeles/
│   ├── 06_examples/
│   └── 07_docs/
├── MODULE_06/              # Plan d'essais et PV
│   ├── 01_schemas/
│   ├── 02_regles/
│   ├── 03_scripts/
│   ├── 04_prompts/
│   ├── 05_modeles/
│   ├── 06_examples/
│   └── 07_docs/
├── gen-mod4.py             # Générateur module 04
├── gen-mod5.py             # Générateur module 05
├── gen-mod6.py             # Générateur module 06
├── gen-pack-indus.py       # Générateur pack industrialisation
├── gen-wrapper.py          # Générateur wrappers IA
├── pack_indus.md           # Documentation pack industrialisation
└── README.md               # Ce fichier
```

## 🔄 Workflow type

1. **Préparation**
   - Génération des modules nécessaires
   - Configuration des règles d'anonymisation
   - Préparation des référentiels normatifs

2. **Production documentaire** (MODULE_04)
   - Rédaction/mise à jour CCTP
   - Structuration DQE/DPGF
   - Génération CR de chantier

3. **Contrôle conformité** (MODULE_05)
   - Vérification CCTP vs normes
   - Collecte et validation des preuves
   - Gestion des non-conformités

4. **Planification essais** (MODULE_06)
   - Génération du plan de contrôle
   - Planification des essais
   - Suivi et validation des PV

5. **Reporting et archivage**
   - Export des rapports (JSON, Markdown, PDF/A)
   - Archivage probant avec hash
   - Génération des KPIs et dashboards

## 🤝 Bonnes pratiques

### Utilisation des wrappers IA
- Toujours utiliser le wrapper approprié selon le contexte
- Exiger systématiquement les sources et éditions
- Activer les contrôles de données sensibles
- Journaliser toutes les interactions

### Gestion des référentiels
- Maintenir à jour les éditions des normes
- Documenter toute dérogation contractuelle
- Archiver les versions successives
- Tracer les modifications

### Sécurité
- Cloisonnement par chantier/lot (RBAC)
- MFA/SSO pour l'accès aux outils
- DLP (Data Loss Prevention)
- Anonymisation systématique des données sensibles

### Qualité
- Double validation humaine pour les décisions critiques
- Tests de régression après modification
- Audit trail complet
- Revue périodique des KPIs

## 📝 Licence

[À renseigner]

## 👥 Contributions

[À renseigner]

## 📞 Support

[À renseigner]

## 📚 Documentation complémentaire

- `pack_indus.md` : Documentation détaillée du pack d'industrialisation
- `MODULE_04/05_docs/README_integration_module04.md` : Intégration module 04
- `MODULE_05/07_docs/README_integration_module05.md` : Intégration module 05
- `MODULE_06/07_docs/README_integration_module06.md` : Intégration module 06

---

**Version** : 1.0
**Dernière mise à jour** : 2025-11-20
