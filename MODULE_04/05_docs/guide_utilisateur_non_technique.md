# Guide Utilisateur Non Technique
## Générateur de CR Chantier - Stone-Sea

> 📖 **Ce guide est destiné aux utilisateurs sans compétences techniques** qui souhaitent générer des comptes rendus de chantier au format Word (.docx) sans écrire de code.

---

## 🎯 Qu'est-ce que c'est ?

Le **Générateur de CR Chantier** vous permet de créer facilement des comptes rendus professionnels au format Word en remplissant simplement un formulaire.

**Pas besoin de :**
- ❌ Connaître la programmation
- ❌ Utiliser la ligne de commande
- ❌ Écrire du code

**Vous avez besoin de :**
- ✅ Un ordinateur Windows, Mac ou Linux
- ✅ Une connexion internet (pour l'installation uniquement)
- ✅ 5 minutes pour l'installation

---

## 🚀 Installation (une seule fois)

### Étape 1 : Installer Python

Python est le logiciel qui fait tourner l'application.

#### **Windows**
1. Allez sur https://www.python.org/downloads/
2. Cliquez sur le gros bouton jaune "Download Python"
3. Lancez le fichier téléchargé
4. **IMPORTANT** : Cochez la case "Add Python to PATH" avant de cliquer sur "Install"
5. Cliquez sur "Install Now"
6. Attendez la fin de l'installation

#### **Mac**
1. Ouvrez le **Terminal** (dans Applications > Utilitaires)
2. Installez Homebrew (si pas déjà fait) :
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Installez Python :
   ```bash
   brew install python3
   ```

#### **Linux (Ubuntu/Debian)**
1. Ouvrez le **Terminal**
2. Tapez :
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-tk
   ```

### Étape 2 : Télécharger les fichiers

1. Téléchargez le dossier `MODULE_04` du projet Stone-Sea
2. Placez-le dans un dossier facile à retrouver (par exemple : `Documents/Stone-Sea`)

### Étape 3 : Vérifier l'installation

L'installation se fera automatiquement au premier lancement !

---

## 💻 Deux façons d'utiliser l'application

Vous avez le choix entre **deux interfaces** :

### Option A : Application Web (recommandée) 🌐

**Avantages :**
- ✅ Interface moderne et colorée
- ✅ Fonctionne dans votre navigateur
- ✅ Plus facile à utiliser
- ✅ Peut être utilisée sur un réseau local

**Comment lancer :**

#### Windows
1. Allez dans le dossier `MODULE_04/03_scripts`
2. **Double-cliquez** sur `lancer_application_web.bat`
3. Une fenêtre noire s'ouvre (ne la fermez pas !)
4. Votre navigateur s'ouvre automatiquement sur `http://localhost:5000`
5. Si le navigateur ne s'ouvre pas, ouvrez-le manuellement et tapez : `http://localhost:5000`

#### Mac / Linux
1. Allez dans le dossier `MODULE_04/03_scripts`
2. Clic droit sur `lancer_application_web.sh` > "Ouvrir avec" > "Terminal"
3. Ou dans le Terminal :
   ```bash
   cd chemin/vers/MODULE_04/03_scripts
   ./lancer_application_web.sh
   ```
4. Ouvrez votre navigateur et allez sur `http://localhost:5000`

**Pour arrêter l'application :**
- Fermez la fenêtre noire (Windows) ou tapez Ctrl+C dans le Terminal (Mac/Linux)

---

### Option B : Interface Graphique 🖥️

**Avantages :**
- ✅ Application de bureau classique
- ✅ Fonctionne hors ligne
- ✅ Pas besoin de navigateur

**Comment lancer :**

#### Windows
1. Allez dans le dossier `MODULE_04/03_scripts`
2. **Double-cliquez** sur `lancer_interface_graphique.bat`
3. L'application s'ouvre dans une nouvelle fenêtre

#### Mac / Linux
1. Allez dans le dossier `MODULE_04/03_scripts`
2. Clic droit sur `lancer_interface_graphique.sh` > "Ouvrir avec" > "Terminal"
3. Ou dans le Terminal :
   ```bash
   cd chemin/vers/MODULE_04/03_scripts
   ./lancer_interface_graphique.sh
   ```

---

## 📝 Comment créer un CR Chantier

### Étape 1 : Remplir les informations générales

| Champ | Description | Obligatoire | Exemple |
|-------|-------------|-------------|---------|
| **Nom du projet** | Nom du chantier | ✅ Oui | "Construction Immeuble Résidentiel A" |
| **Date du CR** | Date d'aujourd'hui (pré-rempli) | ✅ Oui | 2025-11-28 |
| **Lot concerné** | Type de travaux | Non | "Gros œuvre", "CVC", "Électricité" |
| **Participants** | Liste séparée par virgules | ✅ Oui | "Jean Dupont (MOE), Marie Martin (Entreprise)" |
| **Météo** | Conditions météo | Non | "Ensoleillé, 18°C" |
| **Rédacteur** | Votre nom | Non | "Jean Dupont" |
| **Documents consultés** | Plans, CCTP, etc. | Non | "Planning S+8, Plan MEP L2" |

### Étape 2 : Avancement des travaux

Remplissez les zones de texte suivantes (une tâche par ligne) :

- **Tâches prévues** : Ce qui devait être fait
  ```
  Coulage dalle niveau 2
  Pose menuiseries extérieures
  Contrôle étanchéité
  ```

- **Tâches réalisées** : Ce qui a été fait
  ```
  Coulage dalle niveau 2 effectué (100%)
  Ferraillage niveau 3 terminé
  ```

- **Écarts constatés** : Les problèmes ou retards
  ```
  Retard livraison menuiseries (2 jours)
  Main d'œuvre insuffisante zone B
  ```

### Étape 3 : Ajouter des points remarquables

Cliquez sur **"+ Ajouter un point"** pour chaque observation, problème ou amélioration :

| Champ | Description | Exemple |
|-------|-------------|---------|
| **Identifiant** | Code du point (auto-généré) | P-001, NC-042 |
| **Type** | Nature du point | Non-conformité, Point d'attention, Observation |
| **Gravité** | Niveau d'importance | Critique, Majeure, Mineure, Significative |
| **Description** | Détails du point | "Manchon sans collier coupe-feu zone cage A" |
| **Liens** | Références (photos, plans) | "Photo_001.jpg, Plan_MEP_L2#A12" |

**Codes couleur dans le document final :**
- 🔴 **Critique** : Rouge
- 🟠 **Majeure** : Orange
- 🟡 **Mineure** : Jaune

### Étape 4 : Ajouter des actions à mener

Cliquez sur **"+ Ajouter une action"** pour chaque action de suivi :

| Champ | Description | Exemple |
|-------|-------------|---------|
| **Qui** | Responsable | "Entreprise XYZ", "MOE", "Bureau de contrôle" |
| **Quoi** | Action à réaliser | "Poser collier CF et refaire PV" |
| **Quand** | Échéance | "2025-12-01", "J+3", "S+1" |
| **Critère de succès** | Comment vérifier | "PV essais validé", "Visa MOE obtenu" |

### Étape 5 : Générer le document

1. Cliquez sur le bouton **"🚀 Générer le CR .docx"**
2. Attendez quelques secondes (un message de chargement s'affiche)
3. Le document Word (.docx) est automatiquement téléchargé
4. Ouvrez-le avec Microsoft Word, LibreOffice ou Google Docs

---

## 🎨 Ce que contient le document généré

Le document Word créé contient automatiquement :

1. **Page de garde** avec titre, projet et date
2. **Tableau des informations générales** (participants, météo, etc.)
3. **Section Avancement** avec :
   - Tâches prévues
   - Tâches réalisées (en vert ✅)
   - Écarts (en orange ⚠️)
4. **Points remarquables** avec code couleur par gravité
5. **Photos** (si fichiers disponibles)
6. **Tableau des actions** avec colonnes Qui/Quoi/Quand/Critère
7. **Pied de page** avec date de génération

**Mise en forme professionnelle incluse :**
- Titres et sous-titres formatés
- Tableaux avec style professionnel
- Couleurs selon la gravité
- Logo et en-tête (modifiable dans le template)

---

## ❓ Questions fréquentes (FAQ)

### Je n'ai jamais utilisé Python, c'est compliqué ?

**Non !** Vous n'avez pas besoin de connaître Python. Il suffit de :
1. L'installer une fois (5 minutes)
2. Double-cliquer sur le fichier de lancement
3. Remplir le formulaire

### L'application ne se lance pas

**Vérifiez :**
1. Python est bien installé : ouvrez un Terminal et tapez `python --version` (ou `python3 --version`)
2. Vous avez bien coché "Add Python to PATH" lors de l'installation (Windows)
3. Les scripts de lancement sont dans le bon dossier

**Si problème persiste :**
- Relancez l'installation de Python
- Ou contactez votre support IT

### Erreur "No module named 'docx'" ou "No module named 'flask'"

**Solution automatique :**
Les scripts de lancement installent automatiquement les dépendances.

**Solution manuelle :**
Ouvrez un Terminal et tapez :
```bash
pip install python-docx flask
```

### Le document généré est vide ou mal formaté

**Vérifiez :**
- Vous avez bien rempli les champs obligatoires (*)
- Les participants sont séparés par des virgules
- Les tâches sont sur des lignes séparées (pas de virgules)

### Comment ajouter un logo ou personnaliser le document ?

**Deux options :**

1. **Modifier après génération** : Ouvrez le .docx dans Word et ajoutez votre logo
2. **Modifier le template** (avancé) : Voir la documentation technique

### Puis-je utiliser l'application sans connexion internet ?

**Oui !** Après la première installation, l'application fonctionne 100% hors ligne.

### Comment partager l'application avec mes collègues ?

**Réseau local (Application Web uniquement) :**
1. Lancez l'application web
2. Notez l'adresse IP de votre ordinateur (ex: 192.168.1.50)
3. Vos collègues vont sur `http://VOTRE_IP:5000`

**Ou donnez-leur le dossier et le guide d'installation.**

### Les documents sont-ils sauvegardés ?

**Non**, le document est téléchargé directement sur votre ordinateur.
Vous devez l'enregistrer dans votre système de fichiers habituel.

### Puis-je modifier le document généré ?

**Oui !** C'est un fichier Word (.docx) normal que vous pouvez :
- Ouvrir dans Word, LibreOffice, Google Docs
- Modifier, copier, partager
- Exporter en PDF

---

## 📞 Besoin d'aide ?

### Documentation technique

Pour les utilisateurs avancés ou l'IT :
- Guide complet : `MODULE_04/05_docs/generation_docx.md`
- README : `MODULE_04/README_DOCX.md`

### Support

- **Email** : support@stone-sea.example.com (à adapter)
- **Documentation** : Voir dossier `MODULE_04/05_docs/`
- **Issues GitHub** : Pour signaler un bug

---

## 🎓 Tutoriel vidéo (à créer)

### Vidéo 1 : Installation (5 min)
- Installation de Python
- Premier lancement
- Vérification

### Vidéo 2 : Créer son premier CR (10 min)
- Remplir le formulaire
- Ajouter des points et actions
- Générer le document

### Vidéo 3 : Trucs et astuces (5 min)
- Raccourcis
- Personnalisation
- Résolution de problèmes courants

---

## ✅ Checklist : Première utilisation

- [ ] Python est installé
- [ ] J'ai téléchargé le dossier MODULE_04
- [ ] J'ai double-cliqué sur le fichier de lancement
- [ ] L'application s'est ouverte (web ou bureau)
- [ ] J'ai rempli un formulaire de test
- [ ] J'ai généré mon premier CR
- [ ] Le document Word s'est ouvert correctement

**Si tous les points sont cochés : Félicitations ! 🎉**

---

## 🔄 Mises à jour

Pour obtenir les nouvelles versions :
1. Téléchargez le nouveau dossier MODULE_04
2. Remplacez l'ancien
3. Relancez l'application (l'installation se fait automatiquement)

---

**Document créé pour Stone-Sea - MODULE_04**
**Version 1.0 - Guide Utilisateur Non Technique**
**Dernière mise à jour : 2025-11-28**
