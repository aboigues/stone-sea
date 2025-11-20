# Glossaire IA

## 🤖 Introduction

Ce glossaire explique les principaux termes liés à l'intelligence artificielle utilisés dans Stone-Sea, dans un langage simple et accessible.

---

## A

### Agent IA
Programme intelligent capable d'accomplir des tâches de manière autonome.
**Dans Stone-Sea** : Claude ou ChatGPT agissent comme des agents IA pour analyser des documents.

### Algorithme
Suite d'instructions qu'un programme suit pour accomplir une tâche.
**Analogie** : Comme une recette de cuisine, étape par étape.

### API (Application Programming Interface)
Interface qui permet à deux programmes de communiquer entre eux.
**Exemple** : Stone-Sea pourrait utiliser l'API de Claude pour automatiser des analyses.

---

## B

### Biais
Tendance systématique de l'IA à favoriser certains types de réponses.
**Exemple** : Une IA entraînée principalement sur des données européennes pourrait avoir un biais vers les normes européennes.

---

## C

### ChatGPT
Outil d'IA générative développé par OpenAI.
**Usage** : Peut être utilisé pour les wrappers Stone-Sea (alternative à Claude).

### Claude
Outil d'IA générative développé par Anthropic.
**Usage** : Recommandé pour Stone-Sea grâce à sa bonne compréhension des documents techniques.

### Contexte
Informations fournies à l'IA pour qu'elle comprenne votre demande.
**Exemple** : "Je suis chef de chantier" = contexte qui aide l'IA à adapter sa réponse.

---

## D

### Dataset (jeu de données)
Ensemble de données utilisées pour entraîner une IA.
**Exemple** : Claude a été entraîné sur des milliards de textes (livres, articles, sites web).

---

## E

### Embedding
Représentation numérique d'un mot ou d'une phrase que l'IA peut traiter.
**Note** : Concept technique, pas besoin de le maîtriser pour utiliser Stone-Sea.

### Entraînement (Training)
Processus par lequel l'IA "apprend" à partir de données.
**Exemple** : Claude a été entraîné sur des milliards de textes pendant des mois.

### Extrapolation
Quand l'IA déduit ou interprète au-delà des informations fournies.
**Exemple dangereux** : Document dit "Béton C25/30" → IA déduit "donc il faut des adjuvants" (pas dans le document !).

---

## F

### Fine-tuning
Affinage d'un modèle IA pour une tâche spécifique.
**Note** : Stone-Sea utilise des wrappers plutôt que du fine-tuning.

---

## G

### GPT (Generative Pre-trained Transformer)
Architecture de modèle IA utilisée par ChatGPT et d'autres outils.
**Note** : Détail technique, pas essentiel pour utiliser Stone-Sea.

---

## H

### Hallucination
Quand l'IA invente des informations qui semblent vraies mais qui sont fausses.
**Exemple dangereux** : L'IA invente "NF DTU 40.29 (édition 2025)" qui n'existe pas.

---

## I

### IA (Intelligence Artificielle)
Programme capable de réaliser des tâches nécessitant normalement l'intelligence humaine.
**Dans Stone-Sea** : Claude ou ChatGPT analysent des documents BTP.

### IA générative
IA capable de créer du contenu (texte, images, etc.).
**Exemple** : Claude génère des analyses de documents.

### Interface
Écran par lequel vous interagissez avec l'IA.
**Exemple** : La page web de Claude où vous tapez vos messages.

---

## L

### LLM (Large Language Model)
Grand modèle de langage comme Claude ou ChatGPT.
**Analogie** : Un "étudiant" qui a lu des milliards de documents et peut répondre à vos questions.

---

## M

### Modèle
Le "cerveau" de l'IA, entraîné sur des données.
**Exemple** : Claude Sonnet, GPT-4.

---

## P

### Paramètre
Variable interne du modèle IA (en milliards).
**Exemple** : GPT-4 a ~1 trillion de paramètres.
**Note** : Plus il y a de paramètres, plus le modèle est puissant (mais aussi coûteux).

### Prompt
Texte que vous écrivez pour donner des instructions à l'IA.
**Exemple** : "Analyse ce CCTP et liste les matériaux prescrits".

### Prompt engineering
Art de formuler des prompts efficaces pour obtenir de bons résultats.
**Dans Stone-Sea** : Les wrappers sont du prompt engineering avancé.

---

## R

### RAG (Retrieval-Augmented Generation)
Technique où l'IA cherche d'abord dans une base de documents avant de répondre.
**Note** : Technique avancée, Stone-Sea utilise des wrappers simples à la place.

### Réponse
Texte généré par l'IA suite à votre prompt.
**Exemple** : L'analyse d'un CCTP produite par Claude.

---

## S

### Session / Conversation
Échange complet entre vous et l'IA (plusieurs messages).
**Conseil** : Créez une nouvelle session pour chaque nouveau document à analyser.

---

## T

### Token
Unité de texte traitée par l'IA (environ 4 caractères).
**Exemple** : "Bonjour" = environ 2 tokens.
**Importance** : Les IA ont des limites en nombre de tokens (ex: 100 000 tokens max).

### Température
Paramètre contrôlant la créativité de l'IA (0 = déterministe, 1 = créatif).
**Dans Stone-Sea** : On préfère une température basse (0-0,3) pour la précision.

---

## V

### Validation
Vérification par un humain des résultats de l'IA.
**Important** : TOUJOURS valider les résultats critiques (conformité, sécurité).

---

## W

### Wrapper
Ensemble d'instructions strictes qui encadrent l'IA.
**Dans Stone-Sea** : Les 8 wrappers permettent d'utiliser l'IA de manière sûre et fiable.

---

## Comparaison : Termes courants

| Terme IA | Équivalent simple | Exemple |
|----------|-------------------|---------|
| **Prompt** | Instruction, demande | "Analyse ce document" |
| **Réponse** | Ce que l'IA répond | L'analyse du document |
| **Hallucination** | Invention, erreur | Fausse norme inventée |
| **Wrapper** | Mode d'emploi strict | Instructions pour encadrer l'IA |
| **Token** | Morceau de texte | Environ 4 caractères |
| **Session** | Conversation | Tous vos messages avec l'IA |
| **Modèle** | Le "cerveau" de l'IA | Claude Sonnet, GPT-4 |

---

## Outils IA mentionnés dans Stone-Sea

### Claude (Anthropic)
**Type** : IA générative de texte
**Site** : https://claude.ai
**Usage** : Recommandé pour Stone-Sea
**Versions** :
- Claude gratuit (limité)
- Claude Pro (20 €/mois, illimité)

### ChatGPT (OpenAI)
**Type** : IA générative de texte
**Site** : https://chat.openai.com
**Usage** : Alternative valide pour Stone-Sea
**Versions** :
- ChatGPT gratuit (GPT-3.5)
- ChatGPT Plus (20 $/mois, GPT-4)

---

## Acronymes courants

| Acronyme | Signification |
|----------|---------------|
| **AI** | Artificial Intelligence (Intelligence Artificielle) |
| **API** | Application Programming Interface |
| **GPT** | Generative Pre-trained Transformer |
| **IA** | Intelligence Artificielle |
| **LLM** | Large Language Model |
| **NLP** | Natural Language Processing (Traitement du langage naturel) |
| **RAG** | Retrieval-Augmented Generation |

---

**💡 Astuce** : Gardez ce glossaire à portée de main pendant votre apprentissage !
