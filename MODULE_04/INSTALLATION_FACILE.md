# 🚀 Installation Facile - Générateur de CR Chantier

> **Pour les utilisateurs sans compétences techniques**
>
> ⏱️ Temps d'installation : **5 minutes**
>
> 💻 Compatible : **Windows, Mac, Linux**

---

## 📋 Ce dont vous avez besoin

- ✅ Un ordinateur
- ✅ Une connexion internet (pour l'installation uniquement)
- ✅ 10 minutes de votre temps

**Vous N'avez PAS besoin de :**
- ❌ Compétences en programmation
- ❌ Connaître le Terminal ou la ligne de commande
- ❌ Acheter un logiciel

---

## 📥 ÉTAPE 1 : Installer Python (une seule fois)

Python est gratuit et nécessaire pour faire tourner l'application.

### 🪟 Windows

1. **Télécharger Python**
   - Allez sur : https://www.python.org/downloads/
   - Cliquez sur le **gros bouton jaune** "Download Python 3.x.x"

2. **Installer Python**
   - Double-cliquez sur le fichier téléchargé
   - ⚠️ **TRÈS IMPORTANT** : Cochez la case **"Add Python to PATH"** en bas !

   ```
   ┌─────────────────────────────────────┐
   │  Install Python 3.x.x               │
   ├─────────────────────────────────────┤
   │                                     │
   │  ☑ Add Python to PATH   ← COCHEZ ! │
   │                                     │
   │  [ Install Now ]                    │
   │  [ Customize Installation ]         │
   └─────────────────────────────────────┘
   ```

   - Cliquez sur **"Install Now"**
   - Attendez la fin de l'installation (2-3 minutes)
   - Cliquez sur **"Close"**

3. **Vérifier l'installation**
   - Appuyez sur `Windows + R`
   - Tapez `cmd` et appuyez sur Entrée
   - Dans la fenêtre noire qui s'ouvre, tapez : `python --version`
   - Vous devriez voir : `Python 3.x.x` ✅

---

### 🍎 Mac

1. **Option A : Avec l'installeur officiel (recommandé)**
   - Allez sur : https://www.python.org/downloads/
   - Téléchargez "macOS 64-bit installer"
   - Double-cliquez sur le fichier .pkg téléchargé
   - Suivez les instructions à l'écran

2. **Option B : Avec Homebrew (si vous l'avez)**
   - Ouvrez le **Terminal** (Applications > Utilitaires > Terminal)
   - Tapez : `brew install python3`
   - Appuyez sur Entrée

3. **Vérifier l'installation**
   - Ouvrez le Terminal
   - Tapez : `python3 --version`
   - Vous devriez voir : `Python 3.x.x` ✅

---

### 🐧 Linux (Ubuntu/Debian)

1. **Ouvrir le Terminal**
   - Appuyez sur `Ctrl + Alt + T`

2. **Installer Python**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```
   - Entrez votre mot de passe administrateur si demandé
   - Appuyez sur `Y` (Oui) quand demandé

3. **Vérifier l'installation**
   ```bash
   python3 --version
   ```
   - Vous devriez voir : `Python 3.x.x` ✅

---

## 📂 ÉTAPE 2 : Télécharger le dossier Stone-Sea

1. **Télécharger le projet**
   - Demandez à votre responsable IT le dossier `MODULE_04`
   - Ou téléchargez depuis le dépôt GitHub du projet

2. **Placer le dossier**
   - Mettez le dossier `MODULE_04` dans un endroit facile à retrouver
   - Exemple : `Documents/Stone-Sea/MODULE_04`
   - ⚠️ **Évitez** les chemins avec des espaces ou des caractères spéciaux

```
📁 Documents
  └─📁 Stone-Sea
      └─📁 MODULE_04
          ├─📁 01_schemas
          ├─📁 03_scripts      ← C'est ici !
          ├─📁 04_modeles
          ├─📁 05_docs
          └─📁 06_examples
```

---

## 🎯 ÉTAPE 3 : Premier lancement

Vous avez **deux options** pour utiliser l'application :

### Option A : Application Web (Recommandée) 🌐

**Avantages :** Interface moderne, facile à utiliser, fonctionne dans le navigateur

#### Windows
1. Ouvrez le dossier `MODULE_04/03_scripts`
2. **Double-cliquez** sur le fichier : `lancer_application_web.bat`
3. Une fenêtre noire s'ouvre (ne la fermez pas !)
4. Votre navigateur s'ouvre automatiquement
5. Si non, ouvrez manuellement : http://localhost:5000

```
📁 MODULE_04/03_scripts
  └─ 📄 lancer_application_web.bat  ← Double-cliquez ici !
```

#### Mac / Linux
1. Ouvrez le dossier `MODULE_04/03_scripts`
2. Clic droit sur `lancer_application_web.sh`
3. Choisir "Ouvrir avec" > "Terminal"
4. Ouvrez votre navigateur et allez sur : http://localhost:5000

---

### Option B : Interface Graphique 🖥️

**Avantages :** Application de bureau classique, pas besoin de navigateur

#### Windows
1. Ouvrez le dossier `MODULE_04/03_scripts`
2. **Double-cliquez** sur : `lancer_interface_graphique.bat`
3. L'application s'ouvre dans une fenêtre

#### Mac / Linux
1. Ouvrez le dossier `MODULE_04/03_scripts`
2. Clic droit sur `lancer_interface_graphique.sh`
3. Choisir "Ouvrir avec" > "Terminal"

---

## ✅ ÉTAPE 4 : Créer votre premier CR

### Application Web

Vous verrez cette interface dans votre navigateur :

```
┌──────────────────────────────────────────────────────┐
│  🏗️ Générateur de CR Chantier                        │
│  Stone-Sea MODULE_04                                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  📝 Instructions                                     │
│  • Remplissez les informations du chantier          │
│  • Ajoutez les points remarquables                  │
│  • Cliquez sur "Générer le CR"                       │
│                                                      │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. Informations générales                          │
│                                                      │
│  Nom du projet *     [____________________]         │
│  Date du CR *        [2025-11-28__________]         │
│  Participants *      [____________________]         │
│                                                      │
│  2. Avancement des travaux                          │
│  ...                                                 │
│                                                      │
│  [  🚀 Générer le CR .docx  ]                        │
│                                                      │
└──────────────────────────────────────────────────────┘
```

1. **Remplissez le formulaire**
   - Les champs avec `*` sont obligatoires
   - Suivez les exemples dans les placeholders

2. **Ajoutez des points et actions**
   - Cliquez sur "+ Ajouter un point"
   - Cliquez sur "+ Ajouter une action"

3. **Générez le document**
   - Cliquez sur "🚀 Générer le CR .docx"
   - Le document Word est téléchargé automatiquement

4. **Ouvrez le document**
   - Ouvrez le fichier .docx téléchargé
   - Utilisez Word, LibreOffice ou Google Docs

---

## 🎉 C'est terminé !

Vous pouvez maintenant :
- ✅ Générer des CR professionnels en quelques clics
- ✅ Modifier les documents dans Word
- ✅ Les partager avec vos équipes

---

## ❓ Problèmes courants

### "Python n'est pas reconnu..."

**Cause :** Python n'est pas dans le PATH

**Solution Windows :**
1. Désinstallez Python (Panneau de configuration > Programmes)
2. Réinstallez en cochant bien "Add Python to PATH"

**Solution Mac/Linux :**
- Utilisez `python3` au lieu de `python`

---

### "No module named 'flask'" ou "No module named 'docx'"

**Cause :** Les bibliothèques ne sont pas installées

**Solution automatique :**
- Les scripts d'installation les installent automatiquement
- Relancez le script de lancement

**Solution manuelle :**
Ouvrez un Terminal et tapez :
```bash
pip install python-docx flask
```

Ou sur Mac/Linux :
```bash
pip3 install python-docx flask
```

---

### L'application web ne s'ouvre pas

**Vérifications :**
1. La fenêtre noire est toujours ouverte ?
2. Ouvrez manuellement votre navigateur
3. Tapez dans la barre d'adresse : `http://localhost:5000`
4. Vérifiez que le port 5000 n'est pas utilisé par autre chose

---

### "Permission denied" (Mac/Linux)

**Solution :**
Rendez les scripts exécutables :
```bash
cd MODULE_04/03_scripts
chmod +x *.sh
```

---

### Le document généré est vide

**Vérifications :**
1. Vous avez rempli les champs obligatoires (avec *) ?
2. Les participants sont bien séparés par des **virgules**
3. Les tâches sont sur des **lignes séparées** (pas de virgules)

---

## 📞 Besoin d'aide ?

### Documentation complète
- **Guide utilisateur** : `MODULE_04/05_docs/guide_utilisateur_non_technique.md`
- **Documentation technique** : `MODULE_04/05_docs/generation_docx.md`

### Support
- **IT de votre entreprise**
- **GitHub Issues** : Pour signaler un bug
- **Email support** : support@stone-sea.example.com (à adapter)

---

## 🔄 Pour arrêter l'application

### Application Web
- **Windows** : Fermez la fenêtre noire
- **Mac/Linux** : Dans le Terminal, appuyez sur `Ctrl + C`

### Interface Graphique
- Fermez simplement la fenêtre

---

## 📖 Ressources supplémentaires

- [x] Guide d'installation (ce document)
- [x] Guide utilisateur non technique
- [x] Documentation technique complète
- [ ] Vidéos tutorielles (à venir)
- [ ] FAQ étendue (à venir)

---

## ✨ Prochaines étapes

Maintenant que l'installation est terminée, consultez :
- **Guide utilisateur** : Pour apprendre toutes les fonctionnalités
- **Exemples** : Dans `MODULE_04/06_examples/`

---

**Installation Stone-Sea MODULE_04**
**Version 1.0 - Guide d'installation simplifié**
**Dernière mise à jour : 2025-11-28**

---

## 🎯 Checklist rapide

- [ ] Python installé et dans le PATH
- [ ] Dossier MODULE_04 téléchargé et placé
- [ ] Script de lancement double-cliqué
- [ ] Application ouverte (web ou graphique)
- [ ] Premier CR généré avec succès
- [ ] Document Word ouvert et vérifié

**✅ Tous cochés ? Parfait ! Vous êtes prêt à utiliser l'application.**
