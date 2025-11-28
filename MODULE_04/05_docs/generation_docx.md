# Génération de documents .docx - Guide d'utilisation

## Vue d'ensemble

Ce module permet de générer des documents .docx de deux manières :
1. **Avec template** : remplacement de marqueurs `{{variable}}` dans un fichier .docx existant
2. **Programmatique** : génération complète du document avec mise en forme avancée

## Installation

### Prérequis

Installer la dépendance `python-docx` :

```bash
pip install -r requirements.txt
```

ou directement :

```bash
pip install python-docx>=0.8.11
```

## Méthode 1 : Génération avec template

### Principe

Un template .docx contient des marqueurs de type `{{variable}}` qui seront remplacés par les valeurs fournies.

### Avantages
- Contrôle total de la mise en forme dans Word
- Simple à maintenir pour des non-développeurs
- Idéal pour des documents à structure fixe

### Inconvénients
- Limité aux remplacements textuels simples
- Difficile pour les tableaux dynamiques ou listes variables
- Pas de logique conditionnelle

### Étape 1 : Créer un template

#### Option A : Créer manuellement dans Word

1. Ouvrir Word et créer votre document
2. Insérer des marqueurs `{{variable}}` où vous voulez les valeurs dynamiques
3. Sauvegarder en .docx

Exemple :
```
Compte Rendu de Chantier
{{projet}} — {{date}}

Participants : {{participants}}
Météo : {{meteo}}

Avancement :
{{taches_realisees}}
```

#### Option B : Générer un template automatiquement

Pour un CR Chantier :

```bash
cd MODULE_04/03_scripts
python create_cr_template.py ../04_modeles/cr_template.docx
```

Cela crée un template prêt à l'emploi avec tous les marqueurs standards.

### Étape 2 : Préparer les données

Les données peuvent être au format JSON (fichier ou chaîne) :

**Fichier `data.json` :**
```json
{
  "projet": "Construction Immeuble Résidentiel",
  "date": "2025-11-28",
  "participants": "Jean Dupont (MOE), Marie Martin (Entreprise), Pierre Durand (MOA)",
  "meteo": "Ensoleillé, 18°C",
  "taches_prevues": "Coulage dalle niveau 2; Pose menuiseries extérieures",
  "taches_realisees": "Coulage dalle niveau 2 effectué (100%)",
  "ecarts": "Retard livraison menuiseries (2 jours)"
}
```

### Étape 3 : Générer le document

#### Avec le générateur générique :

```bash
python docx_generator.py template.docx output.docx data.json
```

ou avec une chaîne JSON :

```bash
python docx_generator.py template.docx output.docx '{"projet":"Mon Projet", "date":"2025-11-28"}'
```

#### Avec le script CR Chantier :

```bash
python cr_json_to_docx.py cr_chantier.json output.docx --template ../04_modeles/cr_template.docx
```

## Méthode 2 : Génération programmatique

### Principe

Le document est construit entièrement par code Python, permettant une mise en forme avancée et une logique dynamique.

### Avantages
- Mise en forme avancée (couleurs, tableaux dynamiques, images)
- Logique conditionnelle (afficher seulement si présent)
- Tableaux avec nombre de lignes variable
- Insertion d'images

### Inconvénients
- Nécessite des compétences en Python
- Changements de mise en forme nécessitent du code

### Exemple : CR Chantier

```bash
python cr_json_to_docx.py cr_chantier.json output.docx
```

**Sans** l'option `--template`, le script génère programmatiquement le document avec :
- Titre et sous-titre formatés
- Tableau d'informations générales
- Listes à puces colorées (vert pour réalisé, orange pour écarts)
- Points remarquables avec codes couleur par gravité :
  - Rouge : critique
  - Orange : majeure
  - Jaune : mineure
- Insertion automatique des photos (si fichiers trouvés)
- Tableau d'actions avec colonnes Qui/Quoi/Quand/Critère

### Structure du JSON pour CR Chantier

Voir le schéma complet : `MODULE_04/01_schemas/cr_chantier.schema.json`

**Exemple minimal :**
```json
{
  "meta": {
    "projet": "Construction Immeuble",
    "date": "2025-11-28",
    "participants": ["Jean Dupont", "Marie Martin"],
    "meteo": "Ensoleillé",
    "redacteur": "Jean Dupont"
  },
  "avancement": {
    "taches_prevues": ["Coulage dalle"],
    "taches_realisees": ["Ferraillage terminé"],
    "ecarts": []
  },
  "points": [
    {
      "id": "NC-001",
      "type": "Non-conformité",
      "gravite": "majeure",
      "description": "Écartement des armatures non conforme",
      "liens": ["DQE_ITEM_045"]
    }
  ],
  "photos": [
    {
      "fichier": "photo_dalle_001.jpg",
      "repere_plan": "A-02",
      "commentaire": "Vue d'ensemble dalle niveau 2"
    }
  ],
  "actions": [
    {
      "qui": "Entreprise XYZ",
      "quoi": "Reprendre ferraillage zone A",
      "quand": "2025-12-01",
      "critere_succes": "Écartement conforme NF DTU 21"
    }
  ]
}
```

## Fonctions avancées (programmatique)

### Ajouter des éléments à un document

```python
from docx import Document
from docx_generator import add_heading_to_doc, add_table_to_doc, add_paragraph_to_doc

doc = Document()

# Ajouter un titre
add_heading_to_doc(doc, "Mon Titre", level=1)

# Ajouter un paragraphe
add_paragraph_to_doc(doc, "Mon texte", bold=True)

# Ajouter un tableau
headers = ["Colonne 1", "Colonne 2", "Colonne 3"]
data = [
    ["Ligne 1 Col1", "Ligne 1 Col2", "Ligne 1 Col3"],
    ["Ligne 2 Col1", "Ligne 2 Col2", "Ligne 2 Col3"]
]
add_table_to_doc(doc, data, headers=headers)

# Sauvegarder
doc.save("output.docx")
```

### Insérer des images

```python
from docx import Document
from docx.shared import Inches

doc = Document()
doc.add_heading("Photographies", 1)
doc.add_picture("photo.jpg", width=Inches(4))
doc.save("output.docx")
```

### Formatage de texte

```python
from docx import Document
from docx.shared import Pt, RGBColor

doc = Document()
p = doc.add_paragraph()
run = p.add_run("Texte important")
run.bold = True
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(255, 0, 0)  # Rouge
doc.save("output.docx")
```

## Cas d'usage

### Cas 1 : Document simple avec structure fixe
→ **Utiliser la méthode template**
- Créer le template dans Word
- Utiliser `docx_generator.py`

### Cas 2 : Document avec tableaux dynamiques
→ **Utiliser la méthode programmatique**
- Créer un script personnalisé comme `cr_json_to_docx.py`
- Utiliser `add_table_to_doc()` pour générer les tableaux

### Cas 3 : Document avec images et photos
→ **Utiliser la méthode programmatique**
- Utiliser `doc.add_picture()` pour insérer les images
- Exemple : voir `generate_programmatic()` dans `cr_json_to_docx.py`

### Cas 4 : Document avec mise en forme conditionnelle
→ **Utiliser la méthode programmatique**
- Logique `if/else` pour afficher seulement si données présentes
- Colorisation selon gravité, statut, etc.

## Bonnes pratiques

### 1. Validation des données

Toujours valider le JSON avant génération :

```bash
# Pour DQE
python check_dqe_json.py data.json

# Pour CR Chantier (si validateur existe)
python validate_cr_json.py cr.json
```

### 2. Gestion des images

- Vérifier l'existence des fichiers avant insertion
- Utiliser des chemins absolus ou relatifs au script
- Gérer les exceptions pour images manquantes

### 3. Encodage

Toujours utiliser `encoding='utf-8'` pour les fichiers JSON :

```python
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

### 4. Styles cohérents

Pour la méthode programmatique, définir des constantes pour les styles :

```python
# Couleurs
COLOR_CRITIQUE = RGBColor(255, 0, 0)
COLOR_MAJEURE = RGBColor(255, 140, 0)
COLOR_MINEURE = RGBColor(255, 215, 0)

# Tailles de police
SIZE_TITLE = Pt(16)
SIZE_HEADING = Pt(14)
SIZE_NORMAL = Pt(11)
```

## Dépannage

### Erreur "No module named 'docx'"

```bash
pip install python-docx
```

### Les marqueurs {{variable}} ne sont pas remplacés

- Vérifier l'orthographe exacte (sensible à la casse)
- Vérifier que le marqueur est bien dans le template
- Vérifier que la clé existe dans le JSON

### Images non insérées

- Vérifier le chemin du fichier
- Vérifier que le fichier existe
- Vérifier le format (jpg, png supportés)
- Vérifier les permissions de lecture

### Encodage incorrect (caractères bizarres)

```python
# Toujours utiliser UTF-8
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

## Exemples complets

### Exemple 1 : Générer un CR avec template

```bash
# Créer le template
python create_cr_template.py ../04_modeles/cr_template.docx

# Générer le document
python cr_json_to_docx.py ../06_examples/cr_exemple.json mon_cr.docx --template ../04_modeles/cr_template.docx
```

### Exemple 2 : Générer un CR programmatique

```bash
python cr_json_to_docx.py ../06_examples/cr_exemple.json mon_cr.docx
```

### Exemple 3 : Template personnalisé

```bash
# data.json
{
  "client": "ACME Corp",
  "montant": "150 000 €",
  "date_signature": "2025-12-01"
}

# Générer
python docx_generator.py mon_template.docx contrat.docx data.json
```

## Intégration dans le workflow Stone-Sea

1. **Collecte de données** : CR Chantier en JSON (saisie ou génération AI via Wrappers)
2. **Validation** : `validate_cr_json.py` (si disponible)
3. **Génération .docx** : `cr_json_to_docx.py`
4. **Archivage** : Copie dans `exports/` avec hash SHA-256
5. **Distribution** : Envoi aux parties prenantes

## Évolutions futures possibles

- [ ] Conversion automatique .docx → PDF/A (archivage long terme)
- [ ] Templates pour DQE/DPGF
- [ ] Templates pour PV d'essais
- [ ] Signature numérique des documents
- [ ] Génération batch (multiple CR en une fois)
- [ ] Intégration avec MODULE_02 (pack industrialisation)

## Références

- Documentation python-docx : https://python-docx.readthedocs.io/
- Schémas JSON : `MODULE_04/01_schemas/`
- Exemples : `MODULE_04/06_examples/`
- Scripts : `MODULE_04/03_scripts/`

---

**Document généré pour Stone-Sea - MODULE_04**
**Version 1.0 - 2025-11-28**
