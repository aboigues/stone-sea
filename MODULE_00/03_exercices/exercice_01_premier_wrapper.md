# Exercice pratique : Votre premier wrapper

## 🎯 Objectif

Dans cet exercice, vous allez **utiliser votre premier wrapper** pour analyser un extrait de CCTP.

**Durée estimée** : 30 minutes

**Ce que vous allez apprendre** :
- Comment copier-coller un wrapper dans Claude
- Comment insérer un document à analyser
- Comment interpréter le résultat
- Comment vérifier que l'analyse est correcte

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :
- ✅ Un compte Claude (ou ChatGPT) actif
- ✅ Accès au MODULE_01/wrappers_markdown/ de Stone-Sea
- ✅ 30 minutes de temps disponible

---

## 📝 Étape 1 : Ouvrir le Wrapper 1

### 1.1 Localiser le fichier

Le Wrapper 1 se trouve dans :
```
MODULE_01/wrappers_markdown/wrapper1_contexte_limite.md
```

### 1.2 Ouvrir le fichier

Ouvrez ce fichier avec un éditeur de texte (Bloc-notes, VS Code, etc.).

### 1.3 Sélectionner tout le contenu

- **Windows** : Ctrl+A puis Ctrl+C
- **Mac** : Cmd+A puis Cmd+C

Le contenu complet du Wrapper 1 est maintenant copié dans votre presse-papiers.

---

## 🤖 Étape 2 : Préparer Claude

### 2.1 Ouvrir Claude

Allez sur https://claude.ai et connectez-vous.

### 2.2 Démarrer une nouvelle conversation

Cliquez sur le bouton "+" pour démarrer une nouvelle conversation.

**Conseil** : Donnez un nom à votre conversation (ex: "Exercice MODULE_00 - Wrapper 1")

### 2.3 Coller le Wrapper 1

Dans la zone de saisie de Claude, collez le contenu du Wrapper 1 :
- **Windows** : Ctrl+V
- **Mac** : Cmd+V

**⚠️ N'envoyez PAS encore !** Nous devons d'abord insérer le document à analyser.

---

## 📄 Étape 3 : Insérer le document à analyser

### 3.1 Le document d'exemple

Nous allons analyser cet extrait de CCTP :

```
ARTICLE 5.3 - COUVERTURE EN TUILES TERRE CUITE

5.3.1 Tuiles
Type : Tuiles plates petit moule 16x27 cm
Matériau : Terre cuite, aspect vieilli
Coloris : Rouge nuancé
Référence : IMERYS Tradition ou équivalent

5.3.2 Support
Liteaux sapin classe 2, section 40x40 mm
Espacement : 13,5 cm (pureau)
Fixation sur chevrons : 2 pointes inox par liteau

5.3.3 Mise en œuvre
Selon NF DTU 40.21
Pente minimale : 45%
Tuiles de rive : scellées au mortier bâtard
Fixation mécanique : 1 tuile sur 5

5.3.4 Accessoires
Chatières : 1 pour 15 m² de couverture
Closoir de faîtage : universel ventilé
Crochets inox pour tuiles de rive
```

### 3.2 Trouver la zone d'insertion

Dans le Wrapper 1 que vous avez collé dans Claude, cherchez cette ligne :

```
<<<COLLER ICI L'EXTRAIT>>>
```

### 3.3 Remplacer par le document

Supprimez la ligne `<<<COLLER ICI L'EXTRAIT>>>` et remplacez-la par le document d'exemple ci-dessus.

**Votre message complet dans Claude devrait maintenant contenir** :
1. Le texte complet du Wrapper 1
2. Avec le document d'exemple à la place de `<<<COLLER ICI L'EXTRAIT>>>`

---

## 🚀 Étape 4 : Lancer l'analyse

### 4.1 Envoyer

Cliquez sur le bouton "Envoyer" (ou appuyez sur Entrée).

### 4.2 Patienter

Claude va analyser le document. Cela prend généralement 10-30 secondes.

### 4.3 Lire la réponse

Claude devrait vous fournir une analyse structurée du document.

---

## ✅ Étape 5 : Vérifier le résultat

### 5.1 Ce que vous devez vérifier

Claude devrait vous avoir fourni :

#### ✅ 1. La structure du document
Quelque chose comme :
```
Article 5.3 - Couverture en tuiles terre cuite
  - 5.3.1 Tuiles
  - 5.3.2 Support
  - 5.3.3 Mise en œuvre
  - 5.3.4 Accessoires
```

#### ✅ 2. Un résumé factuel
Par exemple :
- Type de couverture : Tuiles plates terre cuite 16x27 cm
- Support : Liteaux sapin 40x40 mm
- Pente : 45% minimum
- Norme : NF DTU 40.21

#### ✅ 3. Les limites identifiées
Claude devrait signaler :
- ❌ Édition du NF DTU 40.21 non précisée (quelle version ?)
- ❌ Pas de quantités mentionnées
- ❌ "Équivalent" non défini (critères d'équivalence ?)
- ❌ Délais non mentionnés

#### ✅ 4. Les ambiguïtés
Claude devrait mentionner :
- 🤔 "Aspect vieilli" : définition contractuelle à préciser
- 🤔 "Mortier bâtard" : dosage non précisé
- 🤔 "Rouge nuancé" : tolérance de nuance ?

### 5.2 Questions à vous poser

**Question 1** : Claude a-t-il inventé des informations qui ne sont pas dans le document ?
- Si OUI → ❌ Le wrapper n'a pas été respecté
- Si NON → ✅ Parfait !

**Question 2** : Claude a-t-il bien signalé l'absence d'édition pour le DTU 40.21 ?
- Si OUI → ✅ Excellent !
- Si NON → ⚠️ C'est une limite importante qui devrait être mentionnée

**Question 3** : Claude a-t-il essayé d'interpréter ou de déduire des choses ?
- Si OUI → ❌ Le wrapper demande de ne PAS interpréter
- Si NON → ✅ Parfait !

---

## 🔍 Étape 6 : Analyse critique

### Comparaison document source vs analyse de Claude

Prenez 5 minutes pour comparer ligne par ligne :

| Ce qui est dans le document | Ce que Claude a dit | Correct ? |
|-----------------------------|---------------------|-----------|
| "Tuiles plates petit moule 16x27" | "Tuiles 16x27 cm" | ✅ Oui |
| "Selon NF DTU 40.21" | "NF DTU 40.21" | ✅ Oui |
| (pas d'édition mentionnée) | "Édition non précisée" | ✅ Oui, c'est signalé |
| "Pente minimale : 45%" | "Pente 45% minimum" | ✅ Oui |

**Si tous les points sont corrects** : Bravo ! Claude a bien appliqué le Wrapper 1. 🎉

**Si certains points sont incorrects** : Pas de panique, relancez l'analyse en précisant :
```
Tu as fait quelques erreurs. Peux-tu réanalyser en respectant strictement ces règles :
- Ne rien inventer
- Ne rien interpréter
- Citer uniquement ce qui figure dans le document
```

---

## 💡 Étape 7 : Aller plus loin

### Exercice bonus 1 : Tester avec un autre document

Essayez maintenant d'analyser cet extrait différent :

```
ARTICLE 7.2 - CHAPE FLOTTANTE

Isolation phonique : Panneaux laine de roche 40 mm, CP2
Chape ciment : Dosage 350 kg/m³, épaisseur 50 mm
Finition : Talochée mécanique, planéité P3
Joints de fractionnement : Tous les 36 m²
```

**Questions** :
- Claude détecte-t-il les sources manquantes (quel DTU ? Quelle norme pour la laine de roche ?) ?
- Claude signale-t-il que les quantités ne sont pas mentionnées ?

### Exercice bonus 2 : Comparer Wrapper 1 vs sans wrapper

Testez la différence :

**Test 1 (SANS wrapper)** :
```
Analyse cet extrait de CCTP :

[Collez le document de l'exercice]
```

**Test 2 (AVEC Wrapper 1)** :
```
[Collez le Wrapper 1 complet avec le document]
```

**Observez la différence** :
- Sans wrapper : Claude risque d'ajouter des informations, d'interpréter
- Avec wrapper : Claude se limite au document et signale les manques

**Vous voyez l'intérêt du wrapper ?** 🎯

---

## 📊 Auto-évaluation

### Quiz : Avez-vous bien compris ?

**Question 1** : Où doit-on remplacer `<<<COLLER ICI L'EXTRAIT>>>` ?
<details>
<summary>Voir la réponse</summary>
✅ Dans le texte du wrapper, à l'endroit où cette mention apparaît, on remplace par le document à analyser.
</details>

**Question 2** : Si Claude invente une norme qui n'est pas dans le document, que faut-il faire ?
<details>
<summary>Voir la réponse</summary>
✅ Lui rappeler de respecter le wrapper et de ne citer que ce qui figure dans le document. C'est une hallucination qu'il faut corriger.
</details>

**Question 3** : Pourquoi est-il important que Claude signale que l'édition du DTU n'est pas précisée ?
<details>
<summary>Voir la réponse</summary>
✅ Parce que les exigences peuvent changer d'une édition à l'autre. Sans l'édition, on ne sait pas quelle version appliquer, c'est une source manquante critique.
</details>

**Question 4** : Peut-on faire confiance à 100% à l'analyse de Claude sans vérification ?
<details>
<summary>Voir la réponse</summary>
❌ NON ! Même avec un wrapper, il faut toujours vérifier les résultats, surtout pour des décisions critiques.
</details>

---

## 🎯 Points clés à retenir

- 📋 On copie-colle le **wrapper complet** dans Claude
- 📝 On remplace `<<<COLLER ICI L'EXTRAIT>>>` par le **document à analyser**
- ✅ On vérifie que Claude **ne dépasse pas** ce qui est dans le document
- 🔍 On contrôle que les **sources manquantes** sont bien signalées
- 🛡️ Le wrapper **encadre** l'IA pour éviter les hallucinations et extrapolations

---

## ✅ Checklist de fin d'exercice

Avant de passer à la suite, vérifiez que :

- [ ] Vous avez réussi à copier-coller le Wrapper 1 dans Claude
- [ ] Vous avez inséré le document à analyser
- [ ] Claude vous a fourni une analyse structurée
- [ ] Vous avez vérifié que l'analyse est correcte
- [ ] Vous comprenez l'intérêt du wrapper (éviter les extrapolations)
- [ ] Vous avez testé au moins un exercice bonus

**Si tous les points sont cochés : Bravo ! Vous maîtrisez votre premier wrapper !** 🎉

---

## ➡️ Prochaine étape

Maintenant que vous avez pratiqué avec le Wrapper 1, vérifions vos connaissances globales !

👉 **Section 7** : [Quiz de vérification](quiz_verification.md)

---

**Excellent travail ! Vous avez franchi l'étape la plus importante !** 🚀
