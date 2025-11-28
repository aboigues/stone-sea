# Guide d'utilisation — Prompt Builder

Ce guide explique comment utiliser les **helpers de création de prompts** pour faciliter la combinaison de wrappers et de prompts spécifiques.

## 📋 Table des matières

1. [Vue d'ensemble](#vue-densemble)
2. [Installation](#installation)
3. [Méthode 1 : Script interactif (recommandé)](#méthode-1--script-interactif-recommandé)
4. [Méthode 2 : Module Python (avancé)](#méthode-2--module-python-avancé)
5. [Méthode 3 : Configuration JSON](#méthode-3--configuration-json)
6. [Exemples pratiques](#exemples-pratiques)
7. [Référence API](#référence-api)

---

## Vue d'ensemble

Le **Prompt Builder** simplifie la création de prompts en automatisant :

- ✅ La sélection et combinaison de **wrappers** (1-8)
- ✅ La sélection de **prompts** par module et sujet
- ✅ Le remplacement automatique des **variables** (`{PROJET}`, `{LOT}`, etc.)
- ✅ La génération d'un prompt final **prêt à copier-coller**

### Schéma du processus

```
Wrappers (1-8)  +  Prompt MODULE_XX  +  Variables  →  Prompt Final
    │                    │                   │              │
    └─ Contraintes       └─ Tâche           └─ Contexte    └─ Copier/Coller
       génériques           spécifique         projet          dans LLM
```

---

## Installation

**Aucune installation requise** si vous êtes dans le répertoire `stone-sea/`.

Les fichiers nécessaires :
- `prompt_builder.py` — Module Python avec les helpers
- `build_prompt.py` — Script CLI interactif

**Dépendances optionnelles** :
```bash
pip install pyperclip  # Pour copier automatiquement dans le presse-papier
```

---

## Méthode 1 : Script interactif (recommandé)

### Usage de base

```bash
python build_prompt.py
```

Le script vous guide étape par étape :

1. **Sélection des wrappers** (1 à 8, multiples possibles)
2. **Sélection du module** (MODULE_04, MODULE_05, etc.)
3. **Sélection du prompt** dans le module
4. **Saisie des variables** détectées automatiquement
5. **Génération et sauvegarde** du prompt final

### Exemple d'exécution

```
============================================================
  🏗️  Stone-Sea — Générateur de Prompts Interactif
============================================================

Quels wrappers souhaitez-vous utiliser?
  1. Wrapper 1: Contexte limité - Pas d'extrapolation
  2. Wrapper 2: Sources obligatoires - Datation/éditions
  ...

💡 Entrez les numéros séparés par des virgules (ex: 1,3,5)
Votre choix: 1,2

✅ 2 wrapper(s) ajouté(s): [1, 2]

Sélectionnez un module (1-4):
  1. MODULE_04
  2. MODULE_05
  ...

Votre choix: 1

Prompts disponibles dans MODULE_04:
  1. prompt_redaction_cctp
  2. prompt_cr_chantier
  ...

Votre choix: 1

Variables du Prompt:
  • {PROJET}
  • {LOT}
  • {LOTS}

  {PROJET}: Résidence Les Acacias
  {LOT}: Couverture
  {LOTS}: Couverture, Maçonnerie, Électricité

✅ Prompt généré (12543 caractères)
✅ Prompt sauvegardé dans: mon_prompt.md
```

### Options avancées

```bash
# Spécifier le fichier de sortie directement
python build_prompt.py --output mon_prompt.md

# Utiliser un fichier de configuration
python build_prompt.py --config ma_config.json --output resultat.md
```

---

## Méthode 2 : Module Python (avancé)

Pour intégrer dans vos propres scripts Python.

### Import et usage de base

```python
from prompt_builder import PromptBuilder

# Créer un builder
builder = PromptBuilder()

# Ajouter wrappers + prompt + variables
prompt = builder \
    .wrapper(1, 2) \
    .prompt("MODULE_04", "prompt_redaction_cctp") \
    .variables(
        PROJET="Résidence Les Acacias",
        LOT="Couverture"
    ) \
    .build()

print(prompt)
```

### Fonction raccourcie

```python
from prompt_builder import quick_prompt

prompt = quick_prompt(
    wrapper_ids=[1, 2],
    module="MODULE_04",
    prompt_name="prompt_redaction_cctp",
    PROJET="Résidence Les Acacias",
    LOT="Couverture"
)

print(prompt)
```

### Sauvegarder directement

```python
builder = PromptBuilder()
builder \
    .wrapper(1, 2) \
    .prompt("MODULE_04", "prompt_redaction_cctp") \
    .variables(PROJET="Résidence X", LOT="Couverture") \
    .save("mon_prompt.md")
```

### Ajouter un prompt personnalisé

```python
builder = PromptBuilder()
builder \
    .wrapper(1) \
    .custom_prompt("""
# Mon prompt personnalisé

Tu es un assistant BTP spécialisé en {DOMAINE}.

Tâches:
1. Analyser {DOCUMENT}
2. Produire un rapport
""") \
    .variables(DOMAINE="Couverture", DOCUMENT="Plan de toiture") \
    .build()
```

### Fonctions utilitaires

```python
from prompt_builder import list_wrappers, list_prompts, extract_variables

# Lister tous les wrappers disponibles
wrappers = list_wrappers()
print(wrappers)
# ['wrapper1_contexte_limite.md', 'wrapper2_sources.md', ...]

# Lister les prompts d'un module
prompts = list_prompts("MODULE_04")
print(prompts)
# ['prompt_redaction_cctp', 'prompt_cr_chantier', ...]

# Extraire les variables d'un texte
variables = extract_variables("Projet {PROJET} lot {LOT}")
print(variables)
# ['LOT', 'PROJET']
```

---

## Méthode 3 : Configuration JSON

Créez un fichier de configuration réutilisable.

### Format du fichier de configuration

**Fichier: `config_cctp_couverture.json`**
```json
{
  "wrappers": [1, 2],
  "module": "MODULE_04",
  "prompt": "prompt_redaction_cctp",
  "variables": {
    "PROJET": "Résidence Les Acacias",
    "LOT": "Couverture",
    "LOTS": "Couverture, Maçonnerie, Électricité, CVC"
  }
}
```

### Utilisation

```bash
# Générer le prompt depuis la config
python build_prompt.py --config config_cctp_couverture.json --output prompt_final.md
```

### Génération de config depuis le mode interactif

Le script interactif propose de sauvegarder votre configuration :

```
Sauvegarder cette configuration pour réutilisation? (o/N): o
Nom du fichier de config (ex: config.json): ma_config.json
✅ Configuration sauvegardée dans ma_config.json
```

---

## Exemples pratiques

### Exemple 1 : CCTP Couverture avec contrôle strict

**Objectif** : Rédiger un CCTP pour le lot Couverture avec contrôle des sources et traçabilité.

**Code Python** :
```python
from prompt_builder import PromptBuilder

prompt = PromptBuilder() \
    .wrapper(1, 2, 6) \
    .prompt("MODULE_04", "prompt_redaction_cctp") \
    .variables(
        PROJET="Résidence Les Tilleuls - Rénovation R+3",
        LOT="Couverture",
        LOTS="Couverture, Charpente, Étanchéité"
    ) \
    .save("cctp_couverture.md")
```

**Ou en CLI** :
```bash
python build_prompt.py
# Sélectionner : wrappers 1,2,6 + MODULE_04 + prompt_redaction_cctp
# Remplir les variables
```

---

### Exemple 2 : Contrôle de conformité normative

**Objectif** : Vérifier la conformité d'un CCTP aux DTU.

**Code Python** :
```python
from prompt_builder import quick_prompt

prompt = quick_prompt(
    wrapper_ids=[2, 8],  # Sources + Contrôle normatif
    module="MODULE_05",
    prompt_name="prompt_controle_cctp",
    PROJET="Immeuble Haussmannien",
    LOT="Maçonnerie"
)

print(prompt)
```

---

### Exemple 3 : Génération de CR de chantier

**Fichier config** : `config_cr_chantier.json`
```json
{
  "wrappers": [1, 4, 7],
  "module": "MODULE_04",
  "prompt": "prompt_cr_chantier",
  "variables": {
    "PROJET": "ZAC des Lilas - Lot B",
    "DATE": "2025-11-28",
    "PHASE": "Gros œuvre"
  }
}
```

**Commande** :
```bash
python build_prompt.py --config config_cr_chantier.json --output cr_chantier.md
```

---

### Exemple 4 : Audit technique multi-lots

**Code Python** :
```python
from prompt_builder import PromptBuilder

lots = ["Couverture", "Maçonnerie", "CVC", "Électricité"]

for lot in lots:
    prompt = PromptBuilder() \
        .wrapper(1, 2, 5) \
        .prompt("MODULE_05", "prompt_controle_cctp") \
        .variables(PROJET="Tour Horizon", LOT=lot) \
        .save(f"audit_{lot.lower()}.md")

    print(f"✅ Généré: audit_{lot.lower()}.md")
```

---

## Référence API

### Classe `PromptBuilder`

#### Méthodes principales

| Méthode | Description | Retour |
|---------|-------------|--------|
| `wrapper(*ids)` | Ajoute un ou plusieurs wrappers (1-8) | `self` |
| `prompt(module, name)` | Ajoute un prompt depuis un module | `self` |
| `custom_prompt(text)` | Ajoute un prompt personnalisé | `self` |
| `variables(**vars)` | Définit les variables à remplacer | `self` |
| `separator(sep)` | Change le séparateur de sections | `self` |
| `build(replace_vars=True)` | Construit le prompt final | `str` |
| `save(path, replace_vars=True)` | Construit et sauvegarde | `str` |
| `reset()` | Réinitialise le builder | `self` |

#### Exemple de chaînage

```python
prompt = PromptBuilder() \
    .wrapper(1, 2) \
    .prompt("MODULE_04", "prompt_redaction_cctp") \
    .variables(PROJET="X", LOT="Y") \
    .separator("\n\n===\n\n") \
    .build()
```

### Fonctions utilitaires

| Fonction | Description | Retour |
|----------|-------------|--------|
| `quick_prompt(wrapper_ids, module, prompt_name, **vars)` | Créer un prompt rapidement | `str` |
| `list_wrappers()` | Liste les wrappers disponibles | `List[str]` |
| `list_prompts(module)` | Liste les prompts d'un module | `List[str]` |
| `extract_variables(text)` | Extrait les variables `{VAR}` | `List[str]` |

---

## Conseils d'utilisation

### Choix des wrappers

| Wrapper | Quand l'utiliser ? |
|---------|-------------------|
| **1** | Pour éviter les hallucinations (contexte strict) |
| **2** | Pour les documents avec références normatives |
| **3** | Pour générer des tableaux de vérification |
| **4** | Pour traiter des données sensibles (RGPD) |
| **5** | Pour analyser des décisions (avantages/risques) |
| **6** | Pour une traçabilité complète des sources |
| **7** | Pour des citations précises avec timestamps |
| **8** | Pour vérifier la conformité DTU/Eurocode |

### Combinaisons recommandées

**Rédaction CCTP** : Wrappers 1, 2, 6
- Contexte strict + Sources datées + Traçabilité

**Contrôle qualité** : Wrappers 2, 3, 8
- Sources + Tableaux vérifiables + Conformité normative

**Compte-rendu chantier** : Wrappers 1, 4, 7
- Contexte limité + RGPD + Citations datées

**Analyse technique** : Wrappers 2, 5, 8
- Sources + Analyse risques + Normes

---

## Dépannage

### Erreur : "Wrapper X non trouvé"

**Cause** : Les fichiers wrapper ne sont pas générés.

**Solution** :
```bash
python gen-wrapper.py
```

### Erreur : "Prompt 'xxx' non trouvé"

**Cause** : Le module n'a pas été généré.

**Solution** :
```bash
python gen-mod4.py  # Pour MODULE_04
python gen-mod5.py  # Pour MODULE_05
# etc.
```

### Variables non remplacées

**Cause** : La variable n'est pas définie ou mal orthographiée.

**Solution** :
```python
# Vérifier les variables attendues
from prompt_builder import extract_variables
vars = extract_variables(prompt_text)
print(vars)  # Liste les variables à fournir
```

---

## Support et contributions

Pour toute question ou amélioration :
- 📖 Consultez la documentation principale dans `README.md`
- 🐛 Signalez les bugs via les issues GitHub
- 💡 Proposez des améliorations via pull requests

---

**Dernière mise à jour** : 2025-11-28
**Version** : 1.0
