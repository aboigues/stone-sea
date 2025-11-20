# Comprendre l'IA : les bases pour le BTP

## 🤖 Qu'est-ce que l'Intelligence Artificielle ?

### Définition simple

L'**Intelligence Artificielle** (IA) est un programme informatique capable de réaliser des tâches qui nécessitent normalement l'intelligence humaine.

**Ce que l'IA peut faire** :
- Comprendre du texte (comme lire un document)
- Répondre à des questions
- Analyser des informations
- Rédiger du texte
- Extraire des données

**Ce que l'IA ne peut PAS faire** :
- Comprendre vraiment ce qu'elle lit (elle ne "comprend" pas comme un humain)
- Avoir du jugement ou du bon sens
- Remplacer un expert humain
- Être 100% fiable sans supervision

---

## 🧠 Comment fonctionne l'IA générative ?

### Les modèles de langage

Les IA comme **Claude** ou **ChatGPT** sont ce qu'on appelle des **modèles de langage**.

**Analogie simple** :
Imaginez un étudiant qui a lu des millions de livres, de documents techniques, de sites web. Il a mémorisé des tonnes d'informations et de façons de formuler les choses.

Quand vous lui posez une question, il :
1. Analyse votre question
2. Cherche dans sa "mémoire" les informations pertinentes
3. Génère une réponse en assemblant ces informations

**Important** : L'IA ne "cherche" pas sur Internet en temps réel. Elle utilise ce qu'elle a appris pendant son entraînement.

### L'IA prédit le texte

En réalité, l'IA fonctionne en **prédisant le mot suivant** le plus probable.

**Exemple** :
- Vous écrivez : "Le béton doit avoir une résistance de..."
- L'IA prédit : "...25 MPa" ou "...30 MPa" (car ce sont des valeurs fréquentes dans ses données d'entraînement)

**Le problème** : Parfois, elle prédit quelque chose qui *semble* logique mais qui est **faux**.

---

## 💬 Les prompts : comment "parler" à l'IA

### Qu'est-ce qu'un prompt ?

Un **prompt**, c'est simplement le texte que vous écrivez pour donner des instructions à l'IA.

**Exemples de prompts** :
- "Résume ce document"
- "Quelles sont les normes applicables pour une dalle béton ?"
- "Analyse ce PV d'essai et dis-moi s'il est conforme"

### Bon prompt vs mauvais prompt

#### ❌ Mauvais prompt (trop vague)
```
Analyse ce document
```
**Problème** : L'IA ne sait pas ce que vous voulez exactement. Quelle analyse ? Sous quel angle ?

#### ✅ Bon prompt (précis)
```
Analyse ce CCTP couverture et liste :
1. Les matériaux prescrits
2. Les normes citées
3. Les exigences de mise en œuvre
4. Les sources manquantes (ex: éditions de normes non précisées)
```
**Avantage** : L'IA sait exactement quoi faire et comment structurer sa réponse.

### Les règles d'or d'un bon prompt

1. **Soyez précis** : Dites exactement ce que vous voulez
2. **Donnez du contexte** : Expliquez le contexte (ex: "Je suis chef de chantier et je dois...")
3. **Structurez** : Utilisez des listes numérotées ou à puces
4. **Donnez des exemples** : Montrez le format de réponse attendu
5. **Fixez des limites** : "N'extrapole pas", "Cite uniquement le document fourni"

---

## ⚠️ Les limites et risques de l'IA

### 1. Les hallucinations

**Définition** : L'IA invente des informations qui semblent vraies mais qui sont fausses.

#### Exemple réel dans le BTP

❌ **Prompt** : "Quelles sont les exigences du NF DTU 40.29 pour les pentes ?"

❌ **Réponse de l'IA** :
"Le NF DTU 40.29 (édition 2023) impose une pente minimale de 30% pour les couvertures en ardoise naturelle."

❌ **Problèmes** :
- L'édition 2023 n'existe peut-être pas
- La pente de 30% est peut-être fausse
- Aucune source précise (page, article)

✅ **Comment éviter** :
- Toujours vérifier dans le document source
- Exiger des citations précises (page, article)
- Utiliser les wrappers qui forcent les citations

### 2. Les extrapolations

**Définition** : L'IA déduit ou interprète au-delà de ce qui est écrit.

#### Exemple réel dans le BTP

📄 **Document fourni** :
```
Dalle béton C25/30, épaisseur 15 cm
```

❌ **Mauvaise réponse de l'IA** :
"Pour cette dalle, il faudra :
- Un treillis soudé ST25C
- Un film polyane 200µ
- Un joint de dilatation tous les 5 mètres"

❌ **Problème** : Le document ne mentionne rien de tout cela. L'IA a **extrapolé** en se basant sur des pratiques courantes.

✅ **Bonne réponse** :
"Le document mentionne uniquement :
- Classe béton : C25/30
- Épaisseur : 15 cm

Sources manquantes :
- Armatures non précisées
- Film polyane non mentionné
- Joints non spécifiés"

### 3. Les données sensibles

**Définition** : L'IA peut traiter et mémoriser des données confidentielles.

#### Types de données sensibles dans le BTP

**Données personnelles (RGPD)** :
- Noms et prénoms
- Adresses
- Numéros de téléphone
- Emails
- Plaques d'immatriculation

**Données commerciales** :
- Prix et montants
- Numéros de marchés
- Informations contractuelles

**Risques** :
- Fuite d'informations confidentielles
- Non-respect du RGPD (amende jusqu'à 20M€ ou 4% du CA)
- Perte d'avantage concurrentiel

✅ **Solution** : Le Wrapper 4 de Stone-Sea détecte et bloque automatiquement ces données.

### 4. Les versions obsolètes de normes

**Définition** : L'IA peut citer une ancienne version d'une norme.

#### Exemple réel

❌ **L'IA dit** : "Selon le NF DTU 21, l'épaisseur minimale est..."

❌ **Problème** :
- Quelle édition du DTU 21 ? (il y a eu plusieurs versions)
- Les exigences peuvent avoir changé entre deux éditions
- Risque d'appliquer une norme obsolète

✅ **Solution** : Toujours exiger l'édition ET la date (ex: NF DTU 21, mars 2021)

---

## 🎯 L'IA dans le BTP : cas d'usage concrets

### ✅ Ce que l'IA fait BIEN

#### 1. Extraction d'informations
**Tâche** : Extraire tous les matériaux mentionnés dans un CCTP de 200 pages
**Temps humain** : 2-3 heures
**Temps IA** : Quelques minutes
**Fiabilité** : Très bonne si bien encadrée

#### 2. Comparaison de documents
**Tâche** : Comparer un CCTP avec les exigences d'un DTU
**Temps humain** : 1 journée
**Temps IA** : 15-30 minutes
**Fiabilité** : Bonne pour détecter les manques, mais validation humaine requise

#### 3. Structuration de données
**Tâche** : Transformer un CR de chantier en format JSON structuré
**Temps humain** : 1-2 heures
**Temps IA** : Quelques minutes
**Fiabilité** : Très bonne

#### 4. Génération de rapports
**Tâche** : Créer un rapport de conformité avec citations
**Temps humain** : 2-3 heures
**Temps IA** : 20-30 minutes
**Fiabilité** : Bonne si les sources sont fournies

### ❌ Ce que l'IA fait MAL (ou ne doit pas faire)

#### 1. Calculs structurels
**❌ Ne pas faire** : Demander à l'IA de calculer des sections d'acier ou de béton
**Pourquoi** : Risque d'erreurs critiques, responsabilité légale

#### 2. Décisions critiques de sécurité
**❌ Ne pas faire** : Valider automatiquement des PV sans vérification humaine
**Pourquoi** : La sécurité ne peut pas reposer uniquement sur l'IA

#### 3. Interprétation juridique
**❌ Ne pas faire** : Demander à l'IA d'interpréter des clauses contractuelles
**Pourquoi** : Risque de malentendus et de litiges

#### 4. Validation finale
**❌ Ne pas faire** : Utiliser l'IA comme seule validation
**Pourquoi** : Un expert humain doit toujours valider les résultats critiques

---

## 🛡️ Les principes de sécurité

### Règle n°1 : Jamais d'IA seule sur les décisions critiques
Un expert humain doit **toujours** valider les résultats de l'IA pour :
- Validation de conformité
- Levée de réserves
- Choix techniques structurels
- Calculs de sécurité

### Règle n°2 : Toujours vérifier les sources
- Ne jamais accepter une affirmation sans source
- Vérifier que les sources existent vraiment
- Vérifier que les citations sont exactes

### Règle n°3 : Encadrer l'IA avec des wrappers
- Ne pas utiliser l'IA "en roue libre"
- Utiliser les wrappers appropriés
- Suivre les procédures définies

### Règle n°4 : Protéger les données sensibles
- Ne jamais envoyer de données personnelles
- Anonymiser les documents avant traitement
- Utiliser le Wrapper 4 systématiquement

---

## 📊 Tableau récapitulatif : IA Oui ou Non ?

| Tâche | IA seule | IA + Expert | Expert seul |
|-------|----------|-------------|-------------|
| Extraire des infos d'un CCTP | ✅ | ✅ | ✅ |
| Résumer un document | ✅ | ✅ | ✅ |
| Comparer CCTP vs normes | ❌ | ✅ | ✅ |
| Valider un PV d'essai | ❌ | ✅ | ✅ |
| Calculer une section d'acier | ❌ | ❌ | ✅ |
| Décision de levée de réserve | ❌ | ❌ | ✅ |
| Structurer des données | ✅ | ✅ | ✅ |
| Générer un rapport avec sources | ❌ | ✅ | ✅ |

**Légende** :
- ✅ Oui, c'est possible et sûr
- ❌ Non, dangereux ou non fiable

---

## 💡 Points clés à retenir

- 🤖 L'IA est un **outil puissant** mais **imparfait**
- 📝 Un bon **prompt** fait toute la différence
- ⚠️ Les risques principaux : **hallucinations**, **extrapolations**, **données sensibles**
- 🛡️ Les **wrappers** encadrent l'IA pour la rendre sûre
- 👤 Un **expert humain** doit toujours valider les décisions critiques
- 📚 Toujours exiger des **sources précises** (édition, date, page)

---

## ✅ Quiz rapide de compréhension

### Question 1
L'IA peut-elle inventer des informations qui semblent vraies ?
<details>
<summary>Voir la réponse</summary>
✅ OUI, c'est ce qu'on appelle une "hallucination". C'est pourquoi il faut toujours vérifier les sources.
</details>

### Question 2
Peut-on utiliser l'IA seule pour valider un PV d'essai béton ?
<details>
<summary>Voir la réponse</summary>
❌ NON, un expert humain doit toujours valider. L'IA peut aider, mais pas décider seule.
</details>

### Question 3
Qu'est-ce qu'un prompt ?
<details>
<summary>Voir la réponse</summary>
✅ C'est le texte que vous écrivez pour donner des instructions à l'IA.
</details>

### Question 4
Peut-on envoyer un devis avec des prix à une IA ?
<details>
<summary>Voir la réponse</summary>
❌ NON, ce sont des données sensibles. Il faut les anonymiser avant (ou utiliser le Wrapper 4 qui les détecte).
</details>

---

## ➡️ Prochaine étape

Maintenant que vous comprenez comment fonctionne l'IA et ses limites, découvrons les documents du BTP !

👉 **Section 3** : [Guide des documents BTP](guide_documents_btp.md)

---

**Bien joué ! Vous avez franchi une étape importante !** 🎉
