# Guide d'Anonymisation des Documents BTP

## 📋 Vue d'ensemble

Ce guide présente la solution complète d'anonymisation pour les documents BTP, conforme RGPD et au secret des affaires.

### Objectifs

- **Conformité RGPD** : Protection des données personnelles
- **Secret des affaires** : Anonymisation des montants, prix, n° de marché
- **Traçabilité** : Journalisation complète des anonymisations
- **Sécurité** : Hash SHA-256 avant/après, rapports détaillés

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│ 1. DÉTECTION PRÉVENTIVE (Wrapper 4)                     │
│    └─> Contrôle avant traitement IA                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ 2. ANONYMISATION AUTOMATISÉE (anonymize.py)             │
│    └─> Application des règles d'anonymisation          │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│ 3. VÉRIFICATION POST-TRAITEMENT (verify_anonymization)  │
│    └─> Détection de fuites résiduelles                 │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation et Prérequis

### Dépendances

```bash
# Le script utilise uniquement la bibliothèque standard Python
python3 --version  # Python 3.8+ requis

# Pour le support YAML (optionnel)
pip install pyyaml
```

### Fichiers du module

```
MODULE_02/export_pack/05_Pipeline/
├── anonymize.py                    # Script principal d'anonymisation
├── verify_anonymization.py         # Script de vérification
├── anonymisation_rules.yaml        # Configuration des règles
└── README_Anonymisation.md         # Ce fichier
```

---

## 📖 Utilisation

### 1. Anonymisation simple

```bash
python anonymize.py document_original.md document_anonymise.md
```

**Résultat** :
- `document_anonymise.md` : Document anonymisé
- `document_anonymise.anonymization_report.json` : Rapport d'anonymisation

### 2. Anonymisation avec règles personnalisées

```bash
python anonymize.py \
  document_original.md \
  document_anonymise.md \
  anonymisation_rules.yaml
```

### 3. Vérification post-anonymisation

```bash
python verify_anonymization.py document_anonymise.md
```

**Résultat** :
- Affichage console des détections
- `document_anonymise.verification_report.json` : Rapport JSON
- `document_anonymise.verification_report.txt` : Rapport texte

### 4. Workflow complet

```bash
# Étape 1: Anonymisation
python anonymize.py cctp_original.md cctp_anon.md

# Étape 2: Vérification
python verify_anonymization.py cctp_anon.md

# Étape 3: Si conforme, traitement IA (avec Wrapper 4 actif)
# ... utilisation du document anonymisé ...
```

---

## 🔍 Catégories de Données Traitées

### Données Personnelles (RGPD)

| Catégorie | Pattern | Remplacement | Exemple |
|-----------|---------|--------------|---------|
| **Emails** | `user@domain.com` | `[EMAIL]` | jean.dupont@entreprise.fr → [EMAIL] |
| **Téléphones** | `06 12 34 56 78` | `[TEL]` | 0612345678 → [TEL] |
| **Noms** | `M. Dupont` | `[NOM]` | Monsieur Dupont → [NOM] |
| **N° Sécu** | `1 85 12 75 123 456 78` | `[NUM-SECU]` | 1851275123 → [NUM-SECU] |
| **IBAN** | `FR76 1234 5678 9012` | `[IBAN]` | FR76 1234... → [IBAN] |

### Secret des Affaires

| Catégorie | Pattern | Remplacement | Exemple |
|-----------|---------|--------------|---------|
| **Montants** | `Prix: 125 000 €` | `[MONTANT]` | Prix: 125 000 € → Prix: [MONTANT] |
| **N° Marché** | `Marché n° 2024-123` | `[MARCHE-XXX]` | Marché n° 2024-123 → Marché n° [MARCHE-XXX] |
| **SIRET** | `12345678901234` | `[SIRET]` | 12345678901234 → [SIRET] |

### Données Techniques BTP

| Catégorie | Pattern | Remplacement | Exemple |
|-----------|---------|--------------|---------|
| **Plaques** | `AB-123-CD` | `[PLAQUE-XXX]` | AB-123-CD → [PLAQUE-XXX] |
| **Dates** | `12/03/2024` | `[DATE]` | 12/03/2024 → [DATE] (optionnel) |

### Données Préservées

Les références techniques **ne sont pas** anonymisées :
- NF DTU 20.1, NF DTU 40.21
- EN 206/CN, EN 12350-2
- AT 12-345
- Classes béton (C25/30, etc.)

---

## ⚙️ Configuration Avancée

### Fichier `anonymisation_rules.yaml`

#### Activer/désactiver des catégories

```yaml
pii:
  emails:
    enabled: true      # Active l'anonymisation des emails
  telephones:
    enabled: true

commercial:
  montants:
    enabled: true      # Active l'anonymisation des montants
    use_price_classes: false  # Remplace par classes de prix si true
```

#### Remplacements contextuels

```yaml
pii:
  noms:
    contextual_replacements:
      MOE: '[MOE-Init.]'      # Maître d'œuvre
      MOA: '[MOA-Init.]'      # Maître d'ouvrage
      Entreprise: '[ENT-Init.]'
```

#### Exclusions

```yaml
exclusions:
  preserve_patterns:
    - 'NF DTU.*'
    - 'EN \d+.*'
    - 'AT \d{2}-\d+'
```

---

## 📊 Rapports Générés

### Rapport d'Anonymisation

**Fichier** : `document.anonymization_report.json`

```json
{
  "timestamp": "2025-11-21T14:30:00",
  "input_file": "document_original.md",
  "output_file": "document_anonymise.md",
  "statistics": {
    "total_redactions": 15,
    "by_category": {
      "emails": 3,
      "telephones": 2,
      "montants": 5,
      "num_marche": 1,
      "pii_noms": 4
    }
  },
  "categories_applied": ["emails", "telephones", "montants", ...]
}
```

### Rapport de Vérification

**Fichier** : `document.verification_report.json`

```json
{
  "timestamp": "2025-11-21T14:31:00",
  "file_path": "document_anonymise.md",
  "is_clean": false,
  "total_findings": 2,
  "severity_summary": {
    "HIGH": 1,
    "MEDIUM": 1,
    "LOW": 0
  },
  "findings": [
    {
      "type": "emails",
      "category": "RGPD - Données personnelles",
      "severity": "HIGH",
      "line_number": 42,
      "matched_text": "contact@exemple.fr",
      "context": "Pour plus d'informations: contact@exemple.fr"
    }
  ]
}
```

---

## 🛡️ Sécurité et Conformité

### Niveaux de Sévérité

| Niveau | Description | Action requise |
|--------|-------------|----------------|
| **HIGH** | Données personnelles/bancaires | **Blocage immédiat** - Re-anonymisation obligatoire |
| **MEDIUM** | Secret des affaires | **Alerte** - Vérification manuelle recommandée |
| **LOW** | Informations mineures | **Information** - Validation à discrétion |

### Traçabilité

Tous les scripts génèrent automatiquement :
- ✅ Timestamp de traitement
- ✅ Hash SHA-256 (si activé dans config)
- ✅ Statistiques détaillées par catégorie
- ✅ Historique des anonymisations

### Journalisation

```yaml
logging:
  enabled: true
  level: 'INFO'
  save_reports: true
  track_history: true
  history_retention_days: 365
```

---

## 💡 Cas d'Usage

### Cas 1 : CCTP avant envoi client

```bash
# 1. Anonymisation
python anonymize.py CCTP_complet.md CCTP_anonymise.md

# 2. Vérification
python verify_anonymization.py CCTP_anonymise.md

# 3. Vérification manuelle si nécessaire
# 4. Envoi du document anonymisé
```

### Cas 2 : DQE avec montants sensibles

```bash
# Anonymisation avec règles strictes
python anonymize.py DQE_detaille.json DQE_anon.json anonymisation_rules.yaml
```

### Cas 3 : Compte-rendu de chantier

```bash
# Les dates peuvent être préservées (enabled: false dans config)
# Seules les données personnelles et prix sont anonymisés
python anonymize.py CR_chantier_2024-03.md CR_anon.md
```

---

## 🔧 Personnalisation

### Ajouter un Pattern Personnalisé

Modifier `anonymize.py` :

```python
self.patterns = {
    # ... patterns existants ...
    'custom_pattern': [
        r'votre_regex_ici',
    ]
}

self.replacements = {
    # ... remplacements existants ...
    'custom_pattern': '[VOTRE-REMPLACEMENT]'
}
```

### Créer une Whitelist Spécifique

Modifier `verify_anonymization.py` :

```python
self.whitelist_patterns = [
    r'NF DTU.*',
    r'VOTRE_PATTERN_À_IGNORER',
]
```

---

## 📌 Bonnes Pratiques

### ✅ À FAIRE

1. **Toujours vérifier** après anonymisation
2. **Conserver les rapports** pour audit
3. **Tester sur échantillon** avant traitement de masse
4. **Documenter les exclusions** si règles personnalisées
5. **Backup du document original** avant anonymisation

### ❌ À ÉVITER

1. **Ne pas désactiver** la vérification post-anonymisation
2. **Ne pas supprimer** les rapports d'anonymisation
3. **Ne pas modifier** les documents anonymisés manuellement
4. **Ne pas réutiliser** les mappings réversibles sans sécurisation
5. **Ne pas anonymiser** les références normatives (NF DTU, etc.)

---

## 🐛 Dépannage

### Problème : YAML non chargé

```bash
# Solution: Installer PyYAML
pip install pyyaml
```

### Problème : Faux positifs (ex: SIRET détecte codes techniques)

```yaml
# Solution: Activer strict_mode
commercial:
  siret_siren:
    strict_mode: true  # N'anonymise que SIRET (14 chiffres)
```

### Problème : Références normatives anonymisées par erreur

```yaml
# Solution: Vérifier les exclusions
exclusions:
  preserve_patterns:
    - 'NF DTU.*'
    - 'EN \d+.*'
```

---

## 📚 Références

### Documentation RGPD
- [CNIL - Guide de l'anonymisation](https://www.cnil.fr/fr/lanonymisation-de-donnees-un-traitement-cle-pour-lopen-data)
- [RGPD - Article 4](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre1#Article4)

### Normes BTP Référencées
- NF DTU (Documents Techniques Unifiés)
- EN 206/CN (Béton)
- Eurocodes

### Modules Complémentaires
- **MODULE_01/Wrapper 4** : Détection préventive données sensibles
- **MODULE_01/Wrapper 6** : Journal des sources (traçabilité)
- **MODULE_02/Pack Industrialisation** : Pipeline complet

---

## 📞 Support

Pour toute question ou problème :
1. Vérifier ce guide
2. Consulter les rapports d'erreur générés
3. Tester avec un échantillon réduit
4. Documenter le cas problématique

---

**Version** : 2.0
**Dernière mise à jour** : 2025-11-21
**Auteur** : Stone-Sea - Système de gestion conformité BTP
