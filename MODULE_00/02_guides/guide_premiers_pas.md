# Premiers pas avec un outil IA

## 🚀 Introduction

Maintenant que vous comprenez ce qu'est l'IA et les wrappers, il est temps de **pratiquer** !

Dans ce guide, vous allez :
1. Choisir un outil IA
2. Créer un compte
3. Comprendre l'interface
4. Écrire votre premier prompt

**Durée estimée** : 25 minutes

---

## 🤖 Choisir un outil IA

Pour utiliser les wrappers de Stone-Sea, vous avez besoin d'un outil d'IA générative.

### Les deux principales options

#### Option 1 : Claude (Anthropic)
**Recommandé pour Stone-Sea**

**Avantages** :
- ✅ Excellente compréhension des documents techniques
- ✅ Bonne gestion des longs documents
- ✅ Respect des instructions (wrappers)
- ✅ Interface claire et simple

**Versions disponibles** :
- **Claude gratuit** : Limité en nombre de messages par jour
- **Claude Pro** : 20 € /mois, messages illimités

**Site web** : https://claude.ai

#### Option 2 : ChatGPT (OpenAI)
**Alternative valide**

**Avantages** :
- ✅ Très populaire et documenté
- ✅ Bonne polyvalence
- ✅ Interface intuitive

**Versions disponibles** :
- **ChatGPT gratuit** : Modèle GPT-3.5, limité
- **ChatGPT Plus** : 20 $ /mois, accès GPT-4

**Site web** : https://chat.openai.com

### Notre recommandation

Pour ce module et pour Stone-Sea, nous recommandons **Claude**.

---

## 📝 Créer un compte Claude (guide pas à pas)

### Étape 1 : Aller sur le site

Ouvrez votre navigateur et allez sur : **https://claude.ai**

### Étape 2 : Cliquer sur "Sign Up" (S'inscrire)

Vous verrez un bouton "Sign Up" ou "S'inscrire" en haut à droite.

### Étape 3 : Choisir une méthode d'inscription

Vous avez plusieurs options :
- **Email** : Entrez votre adresse email professionnelle
- **Google** : Utilisez votre compte Google
- **Apple** : Utilisez votre compte Apple (si vous êtes sur Mac/iPhone)

**Conseil** : Utilisez votre email professionnel pour faciliter la gestion.

### Étape 4 : Vérifier votre email

Si vous vous inscrivez par email :
1. Vous recevrez un email de vérification
2. Cliquez sur le lien dans l'email
3. Confirmez votre inscription

### Étape 5 : Compléter votre profil (optionnel)

Claude peut vous demander quelques informations :
- Votre nom
- Votre utilisation prévue (sélectionnez "Professionnel")

### Étape 6 : Accepter les conditions d'utilisation

Lisez et acceptez les conditions d'utilisation.

**⚠️ Important** : Vérifiez la politique de confidentialité, notamment concernant les données que vous allez partager.

### Étape 7 : Vous êtes prêt !

Vous arrivez sur l'interface principale de Claude. Félicitations ! 🎉

---

## 🖥️ Comprendre l'interface de Claude

### Vue d'ensemble

L'interface de Claude est très simple :

```
┌─────────────────────────────────────────────────┐
│  [Claude logo]               [Historique] [+]   │ ← Barre de menu
├─────────────────────────────────────────────────┤
│                                                 │
│                                                 │
│          Zone de conversation                   │
│                                                 │
│     (Les messages s'affichent ici)              │
│                                                 │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌────────────────────────────────────────┐    │
│  │ Écrivez votre message ici...           │    │ ← Zone de saisie
│  └────────────────────────────────────────┘    │
│                                    [Envoyer →]  │
└─────────────────────────────────────────────────┘
```

### Les éléments clés

#### 1. Bouton "+" (Nouvelle conversation)
- Cliquez ici pour démarrer une nouvelle conversation
- Chaque conversation est indépendante

#### 2. Historique
- Liste de toutes vos conversations passées
- Vous pouvez reprendre une conversation en cours

#### 3. Zone de conversation
- C'est ici que les messages s'affichent
- Vos messages apparaissent à droite (ou avec votre nom)
- Les réponses de Claude apparaissent à gauche

#### 4. Zone de saisie
- C'est ici que vous écrivez vos prompts
- Vous pouvez écrire plusieurs lignes (utilisez Shift+Entrée)

#### 5. Bouton "Envoyer"
- Cliquez pour envoyer votre message
- Ou appuyez sur Entrée

### Fonctionnalités utiles

#### Copier du texte
Survolez un message de Claude, un bouton "Copier" apparaît.

#### Régénérer une réponse
Si la réponse ne vous convient pas, vous pouvez demander à Claude de régénérer (bouton qui apparaît sous le message).

#### Modifier votre message
Vous pouvez éditer un message déjà envoyé en cliquant dessus.

---

## ✍️ Écrire votre premier prompt

### Exercice guidé : Dire bonjour à Claude

**Objectif** : Vous familiariser avec l'interface.

#### Étape 1 : Cliquez dans la zone de saisie

Cliquez dans le champ "Écrivez votre message ici..."

#### Étape 2 : Tapez votre premier message

Écrivez :
```
Bonjour Claude ! Je suis un professionnel du BTP et je découvre comment utiliser l'IA dans mon travail. Peux-tu te présenter brièvement ?
```

#### Étape 3 : Envoyez

Cliquez sur "Envoyer" ou appuyez sur Entrée.

#### Étape 4 : Lisez la réponse

Claude va vous répondre et se présenter. Prenez le temps de lire sa réponse.

**Félicitations ! Vous venez d'envoyer votre premier prompt !** 🎉

---

## 🧪 Exercice : Votre premier prompt technique

Maintenant, essayons quelque chose de plus technique mais toujours simple.

### Consigne

Copiez-collez ce prompt dans Claude :

```
Je vais te donner un court extrait d'un document BTP. Analyse-le et dis-moi :
1. De quel type de document il s'agit (CCTP, PV, CR, etc.)
2. De quel sujet technique il parle
3. Si tu identifies des normes citées

Voici l'extrait :

"ARTICLE 3.2 - DALLE BÉTON
Béton : Classe C25/30, exposition XC1
Épaisseur : 15 cm minimum
Mise en œuvre : Selon NF DTU 21"
```

### Résultat attendu

Claude devrait vous répondre quelque chose comme :

```
1. Type de document : CCTP (Cahier des Clauses Techniques Particulières)

2. Sujet technique : Dalle en béton armé

3. Normes citées :
   - NF DTU 21 (mais l'édition/date n'est pas précisée)
   - Classe de béton selon NF EN 206 (implicite avec C25/30)
```

### Analysez la réponse

**Questions à vous poser** :
- Claude a-t-il bien identifié qu'il s'agit d'un CCTP ?
- A-t-il détecté que l'édition du DTU n'est pas précisée ?
- A-t-il répondu de manière structurée ?

**Si oui** : Excellent ! Claude a compris votre demande.
**Si non** : Ce n'est pas grave, reformulez votre question et réessayez.

---

## 💡 Bonnes pratiques pour vos prompts

### 1. Soyez précis

❌ **Mauvais** : "Analyse ce document"
✅ **Bon** : "Analyse ce CCTP et liste les matériaux prescrits"

### 2. Structurez votre demande

❌ **Mauvais** : "Dis-moi tout sur ce document"
✅ **Bon** :
```
Analyse ce document et indique-moi :
1. Le type de document
2. Les matériaux mentionnés
3. Les normes citées
4. Les sources manquantes
```

### 3. Donnez du contexte

❌ **Mauvais** : "C'est conforme ?"
✅ **Bon** : "Je suis chef de chantier. Ce PV d'essai béton indique 32,5 MPa pour une classe prescrite C25/30. Est-ce conforme ?"

### 4. Fixez des limites

❌ **Sans limites** : "Que faut-il pour une dalle béton ?"
✅ **Avec limites** : "D'après ce CCTP uniquement, quelles sont les exigences pour la dalle béton ? N'ajoute rien qui ne figure pas dans le document."

### 5. Demandez des exemples

❌ **Vague** : "Explique-moi les DTU"
✅ **Avec exemple** : "Explique-moi ce qu'est un DTU et donne-moi un exemple concret avec le DTU 21 (ouvrages en béton)"

---

## ⚠️ Erreurs fréquentes à éviter

### Erreur 1 : Prompts trop courts
**Problème** : L'IA ne comprend pas ce que vous voulez vraiment.
**Solution** : Détaillez votre demande.

### Erreur 2 : Oublier de fournir le document
**Problème** : Vous demandez d'analyser un document mais vous ne le fournissez pas.
**Solution** : Copiez-collez le contenu du document dans votre message.

### Erreur 3 : Accepter une réponse vague
**Problème** : Claude répond de manière générale sans source.
**Solution** : Redemandez en exigeant des sources précises.

### Erreur 4 : Ne pas vérifier
**Problème** : Vous acceptez la réponse de l'IA sans la vérifier.
**Solution** : Vérifiez toujours les informations critiques.

---

## 🎯 Exercice final : Conversation structurée

Essayez cette conversation complète avec Claude :

### Message 1
```
Bonjour Claude. Je vais utiliser les wrappers IA de Stone-Sea pour analyser des documents BTP. Avant de commencer, peux-tu me confirmer que tu comprends ces règles :

1. Tu ne dois jamais inventer de normes ou de chiffres
2. Tu dois toujours citer tes sources avec précision
3. Tu dois signaler quand une information n'est pas dans le document fourni
4. Tu dois détecter les données sensibles (prix, noms, etc.)

Confirme que tu as bien compris ces règles.
```

### Message 2 (après la réponse de Claude)
```
Parfait. Maintenant, je vais te donner un extrait de CCTP. Utilise le Wrapper 1 (contexte limité) pour l'analyser :

[Collez ici le Wrapper 1 depuis MODULE_01/wrappers_markdown/wrapper1_contexte_limite.md]

[Puis collez l'extrait à analyser]
```

### Message 3 (après l'analyse)
```
Merci. Maintenant, identifie les sources manquantes avec le Wrapper 2 (sources obligatoires).

[Collez ici le Wrapper 2]
```

**Vous voyez comment on enchaîne les wrappers ?** C'est exactement ce que vous ferez en production !

---

## 📌 Points clés à retenir

- 🤖 **Claude** est l'outil recommandé pour Stone-Sea
- ✍️ Un bon **prompt** est précis, structuré et contextualisé
- 🔗 L'interface de Claude est simple : zone de saisie en bas, conversation au milieu
- 📝 Vous pouvez (et devez !) **copier-coller les wrappers** dans Claude
- ✅ Vérifiez toujours les réponses de l'IA, surtout pour les informations critiques

---

## ✅ Checklist avant de passer à la pratique

Avant de faire l'exercice pratique du module suivant, vérifiez que :

- [ ] Vous avez créé un compte Claude (ou ChatGPT)
- [ ] Vous savez où se trouve la zone de saisie
- [ ] Vous avez testé d'envoyer un message
- [ ] Vous avez compris comment copier-coller du texte dans Claude
- [ ] Vous savez démarrer une nouvelle conversation

**Si tous les points sont cochés, vous êtes prêt(e) !** 🎉

---

## ➡️ Prochaine étape

Maintenant que vous savez utiliser un outil IA, passons à l'exercice pratique avec votre premier wrapper !

👉 **Section 6** : [Exercice pratique : Votre premier wrapper](../03_exercices/exercice_01_premier_wrapper.md)

---

**Bravo ! Vous maîtrisez maintenant les outils de base !** 🚀
