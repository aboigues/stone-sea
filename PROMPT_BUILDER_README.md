# 🏗️ Stone-Sea — Prompt Builder

**Méthode simple pour créer des prompts en combinant wrappers et sujets**

---

## 🎯 Objectif

Faciliter la création de prompts en automatisant la combinaison de :
- **Wrappers** (contraintes génériques 1-8)
- **Prompts spécifiques** (par module et sujet)
- **Variables de contexte** (projet, lot, etc.)

## ⚡ Démarrage rapide

### Méthode 1 : Script interactif (recommandé)

```bash
python build_prompt.py
```

Le script vous guide pas à pas pour :
1. Choisir vos wrappers (1-8)
2. Sélectionner un module et prompt
3. Remplir les variables
4. Générer le prompt final

### Méthode 2 : Configuration JSON (réutilisable)

**1. Créez un fichier de configuration :**

```json
{
  "wrappers": [1, 2, 6],
  "module": "MODULE_04",
  "prompt": "prompt_redaction_cctp",
  "variables": {
    "PROJET": "Résidence Les Acacias",
    "LOT": "Couverture"
  }
}
```

**2. Générez le prompt :**

```bash
python build_prompt.py --config ma_config.json --output prompt_final.md
```

### Méthode 3 : Code Python (pour scripts)

```python
from prompt_builder import PromptBuilder

# Créer et sauvegarder un prompt
prompt = PromptBuilder() \
    .wrapper(1, 2) \
    .prompt("MODULE_04", "prompt_redaction_cctp") \
    .variables(PROJET="Mon Projet", LOT="Couverture") \
    .save("mon_prompt.md")
```

**Fonction raccourcie :**

```python
from prompt_builder import quick_prompt

prompt = quick_prompt(
    wrapper_ids=[1, 2],
    module="MODULE_04",
    prompt_name="prompt_redaction_cctp",
    PROJET="Mon Projet",
    LOT="Couverture"
)

print(prompt)
```

---

## 📚 Wrappers disponibles

| # | Description | Usage typique |
|---|-------------|---------------|
| **1** | Contexte limité | Éviter les hallucinations |
| **2** | Sources obligatoires | Documents avec références |
| **3** | Sortie vérifiable | Tableaux de vérification |
| **4** | Données sensibles | RGPD / confidentialité |
| **5** | Double raisonnement | Analyse avantages/risques |
| **6** | Journal des sources | Traçabilité complète |
| **7** | Traçabilité citations | Citations horodatées |
| **8** | Contrôle normatif | Conformité DTU/Eurocode |

### Combinaisons recommandées

- **Rédaction CCTP** : `1, 2, 6` (contexte + sources + traçabilité)
- **Contrôle qualité** : `2, 3, 8` (sources + tableaux + normes)
- **CR chantier** : `1, 4, 7` (contexte + RGPD + citations)
- **Analyse technique** : `2, 5, 8` (sources + analyse + normes)

---

## 📂 Modules et prompts

| Module | Domaine | Prompts disponibles |
|--------|---------|---------------------|
| **MODULE_04** | Production documentaire | `prompt_redaction_cctp`<br>`prompt_cr_chantier`<br>`prompt_structuration_dqe` |
| **MODULE_05** | Conformité normative | `prompt_controle_cctp` |
| **MODULE_06** | Plan d'essais | `prompt_generation_plan_controle` |

**Lister les prompts d'un module :**
```python
from prompt_builder import list_prompts
print(list_prompts("MODULE_04"))
```

---

## 💡 Exemples pratiques

### Exemple 1 : CCTP Couverture

**Fichier : `config_cctp.json`**
```json
{
  "wrappers": [1, 2, 6],
  "module": "MODULE_04",
  "prompt": "prompt_redaction_cctp",
  "variables": {
    "PROJET": "Résidence Les Tilleuls",
    "LOT": "Couverture"
  }
}
```

**Commande :**
```bash
python build_prompt.py --config config_cctp.json -o prompt_cctp.md
```

### Exemple 2 : Contrôle conformité

**Code Python :**
```python
from prompt_builder import quick_prompt

prompt = quick_prompt(
    wrapper_ids=[2, 8],  # Sources + Normes
    module="MODULE_05",
    prompt_name="prompt_controle_cctp",
    PROJET="Tour Horizon",
    LOT="Maçonnerie"
)

# Copier ou sauvegarder
print(prompt)
```

### Exemple 3 : Génération multi-lots

```python
from prompt_builder import PromptBuilder

lots = ["Couverture", "Maçonnerie", "CVC", "Électricité"]

for lot in lots:
    PromptBuilder() \
        .wrapper(1, 2) \
        .prompt("MODULE_04", "prompt_redaction_cctp") \
        .variables(PROJET="Mon Projet", LOT=lot) \
        .save(f"prompt_{lot.lower()}.md")

    print(f"✅ prompt_{lot.lower()}.md")
```

---

## 🛠️ Fonctions utilitaires

```python
from prompt_builder import list_wrappers, list_prompts, extract_variables

# Lister les wrappers disponibles
wrappers = list_wrappers()

# Lister les prompts d'un module
prompts = list_prompts("MODULE_04")

# Extraire les variables d'un texte
variables = extract_variables("Projet {PROJET} lot {LOT}")
# → ['LOT', 'PROJET']
```

---

## 📖 Documentation complète

Pour plus de détails, consultez :
- **[GUIDE_PROMPT_BUILDER.md](GUIDE_PROMPT_BUILDER.md)** — Guide complet avec exemples avancés
- **Exemples de configs** : `/exemples_configs/`

---

## 🔧 Dépannage

### "Wrapper X non trouvé"
```bash
python gen-wrapper.py
```

### "Prompt 'xxx' non trouvé"
```bash
python gen-mod4.py  # Pour MODULE_04
python gen-mod5.py  # Pour MODULE_05
```

### Installer la copie automatique dans le presse-papier
```bash
pip install pyperclip
```

---

## 📋 Référence rapide — API Python

### Classe PromptBuilder

| Méthode | Description |
|---------|-------------|
| `.wrapper(*ids)` | Ajoute des wrappers (1-8) |
| `.prompt(module, name)` | Ajoute un prompt |
| `.custom_prompt(text)` | Ajoute un prompt personnalisé |
| `.variables(**vars)` | Définit les variables |
| `.build()` | Génère le prompt |
| `.save(path)` | Génère et sauvegarde |

### Exemple complet

```python
from prompt_builder import PromptBuilder

prompt = PromptBuilder() \
    .wrapper(1, 2, 6) \
    .prompt("MODULE_04", "prompt_redaction_cctp") \
    .variables(
        PROJET="Résidence Les Acacias",
        LOT="Couverture",
        LOTS="Couverture, Maçonnerie, CVC"
    ) \
    .build()

print(prompt)  # Affiche le prompt complet
```

---

**Version** : 1.0
**Dernière mise à jour** : 2025-11-28
