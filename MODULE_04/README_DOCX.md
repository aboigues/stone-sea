# MODULE_04 - Génération de documents .docx

## 🎯 Objectif

Générer des comptes rendus de chantier et autres documents au format .docx à partir de données structurées (JSON) et de templates.

---

## 👥 Pour les utilisateurs NON TECHNIQUES

**Vous n'êtes pas développeur ?** Pas de problème !

### 🌐 Interface Web (Recommandée)
Double-cliquez sur :
- **Windows** : `MODULE_04/03_scripts/lancer_application_web.bat`
- **Mac/Linux** : `MODULE_04/03_scripts/lancer_application_web.sh`

→ Votre navigateur s'ouvre avec un formulaire simple
→ Remplissez et téléchargez votre CR en .docx

### 🖥️ Interface Graphique
Double-cliquez sur :
- **Windows** : `MODULE_04/03_scripts/lancer_interface_graphique.bat`
- **Mac/Linux** : `MODULE_04/03_scripts/lancer_interface_graphique.sh`

→ Application de bureau classique

### 📚 Documentation utilisateur
- **Installation** : [`INSTALLATION_FACILE.md`](INSTALLATION_FACILE.md)
- **Guide complet** : [`05_docs/guide_utilisateur_non_technique.md`](05_docs/guide_utilisateur_non_technique.md)

---

## 💻 Pour les développeurs

## 🚀 Démarrage rapide

### Installation

```bash
# Installer la dépendance
pip install -r ../requirements.txt
```

### Démonstration complète

```bash
cd MODULE_04/03_scripts
python demo_generation_docx.py
```

Ce script génère automatiquement :
- Un template .docx avec marqueurs
- Un CR avec méthode template
- Un CR avec méthode programmatique

## 📋 Deux méthodes de génération

### Méthode 1 : Avec template .docx

**Principe** : Remplace des marqueurs `{{variable}}` dans un fichier Word existant

**Usage** :
```bash
# Créer le template
python create_cr_template.py ../04_modeles/cr_template.docx

# Générer un document
python cr_json_to_docx.py ../06_examples/cr_exemple.json output.docx --template ../04_modeles/cr_template.docx
```

**Avantages** :
- ✅ Facile à utiliser
- ✅ Template modifiable dans Word
- ✅ Idéal pour structure fixe

**Limites** :
- ❌ Pas de tableaux dynamiques
- ❌ Pas d'images
- ❌ Pas de logique conditionnelle

### Méthode 2 : Génération programmatique

**Principe** : Construit le document entièrement en Python

**Usage** :
```bash
python cr_json_to_docx.py ../06_examples/cr_exemple.json output.docx
```

**Avantages** :
- ✅ Mise en forme avancée (couleurs, styles)
- ✅ Tableaux avec nombre de lignes variable
- ✅ Insertion d'images automatique
- ✅ Logique conditionnelle

**Limites** :
- ❌ Nécessite compétences Python
- ❌ Changements via code

## 🛠️ Scripts disponibles

| Script | Description | Usage |
|--------|-------------|-------|
| `docx_generator.py` | Générateur générique avec templates | `python docx_generator.py template.docx out.docx data.json` |
| `cr_json_to_docx.py` | Générateur spécifique CR Chantier | `python cr_json_to_docx.py cr.json out.docx [--template tpl.docx]` |
| `create_cr_template.py` | Créateur de template CR | `python create_cr_template.py output.docx` |
| `demo_generation_docx.py` | Démonstration complète | `python demo_generation_docx.py` |

## 📁 Structure

```
MODULE_04/
├── 01_schemas/
│   └── cr_chantier.schema.json    # Schéma JSON du CR
├── 03_scripts/
│   ├── docx_generator.py          # 🆕 Générateur générique
│   ├── cr_json_to_docx.py         # 🆕 Générateur CR
│   ├── create_cr_template.py      # 🆕 Créateur de template
│   ├── demo_generation_docx.py    # 🆕 Script de démo
│   ├── cr_json_to_md.py           # Existant (JSON → Markdown)
│   └── ...
├── 04_modeles/
│   ├── cr_template.docx           # 🆕 Template généré
│   └── ...
├── 05_docs/
│   └── generation_docx.md         # 🆕 Documentation complète
├── 06_examples/
│   └── cr_exemple.json            # Exemple de données
└── 07_output_docx/                # 🆕 Fichiers générés (démo)
```

## 📖 Exemples

### Exemple 1 : Générer avec template

```bash
# Données JSON
cat > data.json << EOF
{
  "projet": "Construction Immeuble A",
  "date": "2025-11-28",
  "participants": "Jean Dupont, Marie Martin",
  "taches_realisees": "Coulage dalle niveau 2"
}
EOF

# Générer
python docx_generator.py ../04_modeles/cr_template.docx mon_cr.docx data.json
```

### Exemple 2 : Générer programmatiquement avec images

```bash
# Le JSON contient des références aux photos
python cr_json_to_docx.py ../06_examples/cr_exemple.json cr_avec_photos.docx
```

Le script insère automatiquement les images si les fichiers existent.

## 🎨 Personnalisation

### Modifier le template

1. Générer le template de base :
   ```bash
   python create_cr_template.py mon_template.docx
   ```

2. Ouvrir dans Word et personnaliser :
   - Logo, en-tête, pied de page
   - Couleurs, polices
   - Disposition
   - **Conserver les marqueurs `{{variable}}`**

3. Utiliser le template personnalisé :
   ```bash
   python cr_json_to_docx.py data.json output.docx --template mon_template.docx
   ```

### Personnaliser la génération programmatique

Modifier `cr_json_to_docx.py` dans la fonction `generate_programmatic()` :

```python
# Exemple : changer les couleurs
COLOR_CRITIQUE = RGBColor(255, 0, 0)    # Rouge
COLOR_MAJEURE = RGBColor(255, 140, 0)   # Orange

# Exemple : ajouter un logo
doc.add_picture('logo.png', width=Inches(2))
```

## 🧪 Tests

### Tester avec l'exemple fourni

```bash
# Génération programmatique
python cr_json_to_docx.py ../06_examples/cr_exemple.json test_output.docx

# Vérifier le résultat
ls -lh test_output.docx
```

### Tester avec vos données

```bash
# Valider le JSON (si validateur disponible)
python validate_cr_json.py mon_cr.json

# Générer
python cr_json_to_docx.py mon_cr.json mon_output.docx
```

## 📚 Documentation complète

Voir : `MODULE_04/05_docs/generation_docx.md`

Cette documentation contient :
- Guide détaillé des deux méthodes
- API des fonctions programmatiques
- Cas d'usage recommandés
- Dépannage
- Intégration workflow Stone-Sea

## 🔄 Intégration workflow

```
Saisie données
     ↓
Validation JSON
     ↓
Génération .docx  ← VOUS ÊTES ICI
     ↓
Archivage (SHA-256)
     ↓
Distribution
```

## ❓ FAQ

**Q : Quelle méthode choisir ?**
- Structure simple fixe → Template
- Tableaux dynamiques, images, couleurs → Programmatique

**Q : Comment ajouter un logo ?**
- Méthode template : insérer dans le template Word
- Méthode programmatique : `doc.add_picture('logo.png')`

**Q : Les images ne s'affichent pas**
- Vérifier que les fichiers existent
- Utiliser chemins absolus ou relatifs corrects
- Vérifier les permissions

**Q : Erreur "No module named 'docx'"**
```bash
pip install python-docx
```

## 🛣️ Roadmap

- [ ] Templates pour DQE/DPGF
- [ ] Templates pour PV d'essais
- [ ] Conversion automatique .docx → PDF/A
- [ ] Génération batch (multiple documents)
- [ ] Signature numérique

## 📞 Support

- Documentation : `MODULE_04/05_docs/generation_docx.md`
- Exemples : `MODULE_04/06_examples/`
- Issues : GitHub du projet Stone-Sea

---

**Stone-Sea MODULE_04 - Génération .docx**
**Version 1.0 - 2025-11-28**
