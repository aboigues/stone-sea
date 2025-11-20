# Introduction aux wrappers IA

## 🛡️ Qu'est-ce qu'un wrapper ?

### Définition simple

Un **wrapper** (enveloppe en français), c'est un ensemble d'**instructions strictes** qu'on donne à l'IA pour encadrer son travail.

**Analogie simple** :
Imaginez que l'IA est un stagiaire très intelligent mais inexpérimenté.

- **Sans wrapper** : Vous lui donnez un dossier et vous dites "Fais quelque chose avec ça"
  → Résultat imprévisible, risque d'erreurs

- **Avec wrapper** : Vous lui donnez des instructions précises :
  - "Analyse uniquement ce document"
  - "Ne déduis rien qui n'est pas écrit"
  - "Cite toutes tes sources avec page et article"
  - "Signale ce que tu ne sais pas"
  → Résultat prévisible, fiable et vérifiable

---

## ❓ Pourquoi encadrer l'IA dans le BTP ?

### Les enjeux spécifiques du BTP

Dans le BTP, les erreurs peuvent avoir des conséquences graves :

**Sécurité** 🔴
- Un calcul faux → Risque d'effondrement
- Une norme mal appliquée → Ouvrage non conforme

**Juridique** ⚖️
- Une erreur dans un rapport → Litige, responsabilité engagée
- Une non-conformité non détectée → Contentieux coûteux

**Financier** 💰
- Une reprise d'ouvrage → Coûts supplémentaires importants
- Un retard de chantier → Pénalités

**Réputation** 📉
- Défaut de qualité → Perte de marchés futurs

### Ce que les wrappers apportent

Les wrappers permettent de :

✅ **Éliminer les hallucinations**
- L'IA ne peut pas inventer de fausses normes
- Chaque affirmation doit avoir une source

✅ **Empêcher les extrapolations**
- L'IA se limite strictement au contenu fourni
- Elle signale ce qu'elle ne sait pas

✅ **Protéger les données sensibles**
- Détection automatique des données RGPD
- Alerte sur les prix et montants

✅ **Garantir la traçabilité**
- Journal complet des sources utilisées
- Citations numérotées précises

✅ **Produire des sorties vérifiables**
- Tableaux source / conclusion
- Format structuré facile à contrôler

---

## 📦 Les 8 wrappers de Stone-Sea

Stone-Sea propose **8 wrappers** différents, chacun adapté à un cas d'usage spécifique.

### Vue d'ensemble

| N° | Nom | Usage principal | Quand l'utiliser ? |
|----|-----|-----------------|-------------------|
| **1** | Contexte limité | Analyser sans extrapolation | Lecture d'un extrait isolé |
| **2** | Sources obligatoires | Exiger références datées | Analyse avec normes |
| **3** | Sortie vérifiable | Tableau 2 colonnes | Vérification point par point |
| **4** | Données sensibles | Détecter/bloquer RGPD/prix | Avant toute analyse |
| **5** | Double raisonnement | Matrice avantages/risques | Choix techniques |
| **6** | Journal des sources | Traçabilité complète | Audit, expertise |
| **7** | Citations numérotées | Références précises | Rapports officiels |
| **8** | Contrôle normatif | Conformité DTU/Eurocodes | Contrôle qualité |

---

## 📋 Détail des wrappers

### Wrapper 1 : Contexte limité

**Objectif** : Analyser un document **sans rien ajouter** qui n'y figure pas.

**Principe** :
- Lire uniquement ce qui est écrit
- Ne pas déduire ou interpréter
- Signaler les limites et ambiguïtés

**Cas d'usage** :
- Comprendre un extrait de CCTP isolé
- Analyser une clause sans contexte complet

**Ce que l'IA doit faire** :
✅ Résumer factuellement
✅ Identifier la structure
✅ Signaler les sources manquantes
✅ Signaler les ambiguïtés

**Ce que l'IA ne doit PAS faire** :
❌ Interpréter
❌ Ajouter des informations externes
❌ Déduire des implications

---

### Wrapper 2 : Sources obligatoires

**Objectif** : S'assurer que chaque référence est **datée et précise**.

**Principe** :
- Chaque norme citée doit avoir une édition et une date
- Chaque affirmation doit avoir une source
- Signaler les sources manquantes

**Cas d'usage** :
- Vérifier qu'un CCTP cite bien les normes avec éditions
- S'assurer de la traçabilité des références

**Ce que l'IA doit produire** :
✅ Table des références avec éditions et dates
✅ Liste des sources manquantes
✅ Localisation précise (page, article)

**Exemple de sortie** :

| Référence | Titre | Édition | Date | Page |
|-----------|-------|---------|------|------|
| NF DTU 21 | Ouvrages en béton | - | mars 2021 | Art. 3.1 |

---

### Wrapper 3 : Sortie vérifiable (2 colonnes)

**Objectif** : Produire un tableau où chaque conclusion est **reliée à sa source**.

**Principe** :
- Colonne 1 : Citation exacte du document source
- Colonne 2 : Affirmation ou conclusion
- Permet de vérifier ligne par ligne

**Cas d'usage** :
- Vérifier un PV d'essai
- Contrôler qu'une analyse est bien fondée

**Exemple de sortie** :

| Source (verbatim) | Conclusion |
|-------------------|------------|
| "Classe prescrite : C25/30" | Résistance mini = 30 MPa |
| "Éprouvette 1 : 32,5 MPa" | Conforme (> 30 MPa) |

---

### Wrapper 4 : Données sensibles

**Objectif** : **Détecter et bloquer** les données personnelles et confidentielles.

**Principe** :
- Scanner le document à la recherche de données RGPD
- Détecter les prix, montants, données contractuelles
- Refuser le traitement ou proposer l'anonymisation

**Cas d'usage** :
- **TOUJOURS en premier** avant toute analyse
- Traitement de documents commerciaux
- Anonymisation de rapports

**Types de données détectées** :
- Noms et prénoms
- Adresses postales
- Téléphones et emails
- Prix et montants
- Numéros de contrats
- Plaques d'immatriculation

**Exemple de sortie** :

```
⚠️ ALERTE DONNÉES SENSIBLES
- Nom : Jean DURAND
- Téléphone : 06 12 34 56 78
- Prix : 12 500 € HT

⛔ REFUS DE TRAITEMENT
Veuillez anonymiser le document avant analyse.
```

---

### Wrapper 5 : Double raisonnement + matrice avantages/risques

**Objectif** : Analyser les **pour et contre** d'une solution technique.

**Principe** :
- Présenter les avantages ET les risques
- Matrice de décision structurée
- Pas de conclusion imposée

**Cas d'usage** :
- Choisir entre deux solutions techniques
- Analyser les risques d'un procédé
- Aide à la décision

**Exemple de sortie** :

| Critère | Avantages | Risques | Score |
|---------|-----------|---------|-------|
| Coût | Économique (85€/m²) | Prix volatil pétrole | 7/10 |
| Durabilité | Bonne si protégé | Sensible UV/chocs | 6/10 |
| Feu | - | Inflammable (classe E) | 4/10 |

---

### Wrapper 6 : Journal des sources

**Objectif** : Tracer **toutes les sources** utilisées lors d'une analyse.

**Principe** :
- Journal chronologique des documents consultés
- Hash SHA-256 pour vérifier l'intégrité
- Horodatage de chaque accès

**Cas d'usage** :
- Audit de conformité
- Expertise judiciaire
- Traçabilité complète

**Exemple de sortie** :

| ID | Type | Nom | Version | Horodatage | Hash |
|----|------|-----|---------|------------|------|
| S001 | PDF | CCTP_v2.3.pdf | v2.3 | 2024-11-20 10:15 | a3f5... |
| S002 | PDF | DTU_20.1.pdf | mars 2020 | 2024-11-20 10:17 | b8e2... |

---

### Wrapper 7 : Citations numérotées

**Objectif** : Référencer **précisément** chaque affirmation.

**Principe** :
- Chaque affirmation a une citation [1], [2], etc.
- Liste des sources en fin de document
- Citation exacte (verbatim)

**Cas d'usage** :
- Rapports d'expertise
- Documents officiels
- Contrôle qualité

**Exemple de sortie** :

**Texte** :
"Les menuiseries doivent comporter 4 fixations par montant pour les fenêtres de hauteur > 1,50 m [1]."

**Sources** :
[1] NF DTU 36.5, Section 6.2.3, Octobre 2010

---

### Wrapper 8 : Contrôle normatif DTU/Eurocodes

**Objectif** : Vérifier la **conformité** par rapport aux référentiels.

**Principe** :
- Tableau des exigences normatives
- Comparaison avec le constat terrain
- Détection des écarts et non-conformités

**Cas d'usage** :
- Contrôle qualité chantier
- Vérification CCTP vs normes
- Validation de mise en œuvre

**Exemple de sortie** :

| Exigence | Conformité | Valeur constatée | Écart | Gravité |
|----------|------------|------------------|-------|---------|
| Épaisseur ≥ 5 cm | ✅ Oui | 5,5 cm | - | - |
| Recouvrement treillis | ❌ Non | 1 maille + 15 cm | -1 maille, -5 cm | MAJEUR |

---

## 🔄 Comment choisir le bon wrapper ?

### Arbre de décision rapide

```
Votre document contient-il des données personnelles ou des prix ?
├─ OUI → Commencez par le Wrapper 4
└─ NON → Continuez

Devez-vous produire un rapport d'expertise opposable ?
├─ OUI → Wrapper 7 + Wrapper 6
└─ NON → Continuez

Devez-vous vérifier la conformité aux normes ?
├─ OUI → Wrapper 8
└─ NON → Continuez

Devez-vous comparer plusieurs solutions ?
├─ OUI → Wrapper 5
└─ NON → Continuez

Voulez-vous simplement comprendre un document ?
├─ OUI → Wrapper 1
└─ Autre cas → Wrapper 2 ou 3
```

---

## 🔗 Combinaisons de wrappers

Souvent, vous utiliserez **plusieurs wrappers** successivement :

### Exemple : Contrôle de conformité CCTP

**Étape 1** : Wrapper 4 (détection données sensibles)
→ Anonymiser si nécessaire

**Étape 2** : Wrapper 1 (compréhension du CCTP)
→ Identifier les exigences

**Étape 3** : Wrapper 2 (vérification des sources)
→ S'assurer que les normes sont datées

**Étape 4** : Wrapper 8 (contrôle normatif)
→ Comparer avec les DTU applicables

**Étape 5** : Wrapper 7 + Wrapper 6 (rapport final)
→ Produire un rapport traçable

---

## 💡 Points clés à retenir

- 🛡️ Un **wrapper** encadre l'IA avec des instructions strictes
- 📦 Stone-Sea propose **8 wrappers** pour 8 cas d'usage différents
- 🔒 Les wrappers **éliminent les risques** de l'IA (hallucinations, extrapolations)
- ✅ Chaque wrapper produit une **sortie structurée** et vérifiable
- 🔗 On peut **combiner plusieurs wrappers** pour une analyse complète
- 🎯 Le Wrapper 4 (données sensibles) doit être utilisé **en premier**

---

## ✅ Quiz rapide de compréhension

### Question 1
Qu'est-ce qu'un wrapper ?
<details>
<summary>Voir la réponse</summary>
✅ Un ensemble d'instructions strictes qui encadrent le travail de l'IA pour la rendre fiable et sécurisée.
</details>

### Question 2
Quel wrapper faut-il utiliser si un document contient des prix ?
<details>
<summary>Voir la réponse</summary>
✅ Le Wrapper 4 (Données sensibles), en premier, avant toute autre analyse.
</details>

### Question 3
Quel wrapper utiliser pour produire un rapport d'expertise ?
<details>
<summary>Voir la réponse</summary>
✅ Le Wrapper 7 (Citations numérotées) + le Wrapper 6 (Journal des sources) pour la traçabilité complète.
</details>

### Question 4
Peut-on utiliser plusieurs wrappers successivement ?
<details>
<summary>Voir la réponse</summary>
✅ OUI, c'est même recommandé ! On combine souvent plusieurs wrappers pour une analyse complète.
</details>

---

## ➡️ Prochaine étape

Maintenant que vous comprenez ce que sont les wrappers, passons à la pratique !

👉 **Section 5** : [Premiers pas avec un outil IA](guide_premiers_pas.md)

---

**Excellent ! Vous êtes prêt(e) à utiliser les wrappers !** 🚀
