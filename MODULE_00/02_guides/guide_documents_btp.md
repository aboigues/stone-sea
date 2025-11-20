# Les documents BTP pour les non-initiés

## 📄 Introduction

Dans le secteur du BTP, on manipule beaucoup de documents techniques. Si vous débutez ou si vous n'êtes pas familier avec tous ces acronymes (CCTP, DTU, PV, DQE...), ce guide est fait pour vous !

**Objectif** : Comprendre les principaux types de documents que vous allez rencontrer dans Stone-Sea.

---

## 🏗️ Les documents de projet

### 1. CCTP - Cahier des Clauses Techniques Particulières

#### Qu'est-ce que c'est ?

Le **CCTP** est le document qui décrit **comment** réaliser les travaux sur un projet précis.

**Analogie simple** :
C'est comme la recette de cuisine détaillée pour construire un bâtiment spécifique.

#### Que contient un CCTP ?

- **Matériaux** à utiliser (ex: béton C25/30, tuiles terre cuite)
- **Normes** à respecter (ex: NF DTU 21, NF DTU 40.21)
- **Méthodes** de mise en œuvre (ex: pose collée, fixation mécanique)
- **Performances** attendues (ex: résistance thermique R≥4,0)
- **Exigences** spécifiques au chantier

#### Exemple concret (extrait)

```
ARTICLE 3.2 - DALLE BÉTON REZ-DE-CHAUSSÉE

Béton : Classe C25/30, exposition XC1
Épaisseur : 15 cm minimum
Armatures : Treillis soudé ST25C, mailles 150x150 mm
Mise en œuvre : Selon NF DTU 21 (mars 2021)
Finition : Talochée mécanique
```

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea peut :
- Analyser un CCTP pour en extraire les exigences
- Comparer un CCTP avec les normes (contrôle de conformité)
- Vérifier qu'un CCTP est complet (détecter les sources manquantes)

---

### 2. DPGF / DQE - Décomposition du Prix Global et Forfaitaire

#### Qu'est-ce que c'est ?

Le **DPGF** (ou **DQE**) est le document qui liste **tous les postes de travaux** avec leurs quantités et leurs prix.

**Analogie simple** :
C'est comme le ticket de caisse détaillé d'un supermarché, mais pour un chantier.

#### Que contient un DPGF ?

- **Numéro de poste** (ex: 1.2.3)
- **Désignation** (ex: "Terrassement en déblai")
- **Unité** (ex: m³, m², m, unité)
- **Quantité** (ex: 250 m³)
- **Prix unitaire** (ex: 35,00 € HT)
- **Prix total** (ex: 8 750,00 € HT)

#### Exemple concret

| N° | Désignation | Unité | Qté | PU HT | Total HT |
|----|-------------|-------|-----|-------|----------|
| 1.1 | Installation de chantier | Ens | 1 | 3 500 € | 3 500 € |
| 2.1 | Terrassement général | m³ | 250 | 35 € | 8 750 € |
| 2.2 | Fondations semelles | ml | 85 | 180 € | 15 300 € |
| ... | ... | ... | ... | ... | ... |

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea peut :
- Convertir un DQE au format CSV en format JSON structuré
- Vérifier la cohérence d'un DQE (unités, calculs)
- Extraire les quantités pour planifier les essais

---

### 3. CR - Compte-Rendu de chantier

#### Qu'est-ce que c'est ?

Le **CR** est le document qui décrit ce qui s'est passé sur le chantier lors d'une réunion ou d'une visite.

**Analogie simple** :
C'est comme le compte-rendu d'une réunion de travail, mais pour un chantier.

#### Que contient un CR ?

- **Date** et **participants**
- **Avancement** des travaux
- **Problèmes** rencontrés
- **Décisions** prises
- **Actions** à mener (qui fait quoi pour quand)
- **Points en attente**

#### Exemple concret (extrait)

```
COMPTE-RENDU DE CHANTIER
Chantier : Résidence Les Pins
Date : 15/11/2024
Participants : MOE, Entreprise, Contrôleur

1. AVANCEMENT
- Dalle RDC coulée le 12/11
- Voiles R+1 en cours de coffrage

2. PROBLÈMES
- Livraison béton retardée de 2h
- Treillis soudé non conforme (maille 200x200 au lieu de 150x150)

3. DÉCISIONS
- Reprise du treillis non conforme
- Nouvelle livraison prévue le 18/11

4. ACTIONS
- Entreprise : Commander treillis conforme (avant 16/11)
- MOE : Valider le nouveau planning (avant 17/11)
```

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea peut :
- Structurer un CR en format JSON
- Extraire les décisions et actions
- Exporter un CR JSON en Markdown ou PDF

---

## 📚 Les documents normatifs

### 4. DTU - Documents Techniques Unifiés

#### Qu'est-ce que c'est ?

Les **DTU** sont des normes françaises qui décrivent les **règles de l'art** pour réaliser des ouvrages dans le BTP.

**Analogie simple** :
Les DTU, c'est le "code de la route" du BTP. Ce sont les règles à respecter obligatoirement.

#### Exemples de DTU courants

| DTU | Domaine |
|-----|---------|
| **NF DTU 20.1** | Maçonnerie (murs en blocs, briques) |
| **NF DTU 21** | Ouvrages en béton (dalles, poutres, poteaux) |
| **NF DTU 26.2** | Chapes et dalles à base de liants hydrauliques |
| **NF DTU 36.5** | Fenêtres et portes extérieures |
| **NF DTU 40.11** | Couverture en ardoises |
| **NF DTU 40.21** | Couverture en tuiles de terre cuite |
| **NF DTU 40.29** | Couverture en ardoise naturelle |
| **NF DTU 45.1** | Isolation thermique des circuits de plomberie |
| **NF DTU 60.5** | Canalisations en cuivre |
| **NF DTU 65.x** | Chauffage, ventilation, climatisation |

#### Structure d'un DTU

Un DTU contient généralement :
- **Partie 1-1** : Cahier des clauses techniques types (CCT)
- **Partie 1-2** : Critères généraux de choix des matériaux (CGM)
- **Partie 2** : Cahier des clauses administratives spéciales types (CCS)

#### Éditions et dates

**⚠️ IMPORTANT** : Un DTU a plusieurs éditions dans le temps.

**Exemple** :
- NF DTU 21 (octobre 1993) ← ancienne version
- NF DTU 21 (mars 2021) ← version actuelle

**Attention** : Les exigences peuvent changer d'une édition à l'autre !

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea utilise les DTU pour :
- Contrôler la conformité d'un CCTP
- Vérifier qu'un ouvrage respecte les règles de l'art
- Détecter les non-conformités

---

### 5. Eurocodes

#### Qu'est-ce que c'est ?

Les **Eurocodes** sont des normes européennes pour le **calcul des structures**.

**Analogie simple** :
Les DTU disent "comment faire", les Eurocodes disent "comment calculer pour que ça tienne".

#### Exemples d'Eurocodes courants

| Eurocode | Domaine |
|----------|---------|
| **EN 1990** | Bases de calcul des structures |
| **EN 1991** | Actions sur les structures (charges) |
| **EN 1992** | Calcul des structures en béton |
| **EN 1993** | Calcul des structures en acier |
| **EN 1994** | Calcul des structures mixtes acier-béton |
| **EN 1995** | Calcul des structures en bois |
| **EN 1996** | Calcul des ouvrages en maçonnerie |
| **EN 1997** | Calcul géotechnique (fondations) |

#### Annexes Nationales (AN)

En France, les Eurocodes sont complétés par des **Annexes Nationales** qui précisent les valeurs à utiliser en France.

**Exemple** :
- EN 206 : Béton - Spécification, performance, production
- EN 206/CN : Annexe Nationale française

---

### 6. Normes produits (NF EN)

#### Qu'est-ce que c'est ?

Les **normes produits** définissent les caractéristiques que doivent avoir les matériaux.

**Exemples** :
- **NF EN 12350-2** : Essai d'affaissement du béton
- **NF EN 13318** : Chapes - Caractéristiques et exigences
- **NF EN 197-1** : Ciments - Composition, spécifications

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea peut vérifier que les produits prescrits ou utilisés respectent les normes applicables.

---

## 🧪 Les documents de contrôle

### 7. PV - Procès-Verbal d'essai

#### Qu'est-ce que c'est ?

Un **PV d'essai** est un document produit par un laboratoire qui atteste des résultats d'un essai (béton, étanchéité, etc.).

**Analogie simple** :
C'est comme un bulletin d'analyse médicale, mais pour des matériaux de construction.

#### Que contient un PV ?

- **Identification** du chantier
- **Date** de prélèvement
- **Nature** de l'essai (ex: résistance béton à 28 jours)
- **Résultats** mesurés (ex: 32,5 MPa)
- **Normes** appliquées (ex: NF EN 12350-2)
- **Conclusion** (conforme / non conforme)
- **Accréditation** du laboratoire (ex: COFRAC)

#### Exemple concret

```
PV D'ESSAI N° 2024-BET-0156
Laboratoire QUALIBAT - Accréditation COFRAC n°1-2345

Chantier : Résidence Les Érables
Date prélèvement : 10/11/2024
Classe prescrite : C25/30

Essai de résistance à 28 jours (NF EN 12350-2)
- Éprouvette 1 : 32,5 MPa
- Éprouvette 2 : 31,8 MPa
- Éprouvette 3 : 33,1 MPa
Moyenne : 32,5 MPa

Conclusion : CONFORME (> 30 MPa)
```

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea peut :
- Vérifier qu'un PV est conforme aux exigences du CCTP
- Extraire les résultats pour alimenter un tableau de bord
- Détecter les PV non conformes

---

### 8. Plan de contrôle

#### Qu'est-ce que c'est ?

Le **plan de contrôle** liste tous les essais et contrôles à réaliser sur un chantier.

**Analogie simple** :
C'est comme un planning de révisions médicales, mais pour un chantier.

#### Que contient un plan de contrôle ?

- **Type d'essai** (ex: résistance béton, étanchéité)
- **Référence normative** (ex: NF EN 206/CN)
- **Fréquence** (ex: 1 essai par 150 m³ de béton)
- **Critère d'acceptation** (ex: résistance ≥ 30 MPa)
- **Responsable** du contrôle

#### Exemple concret

| Essai | Norme | Fréquence | Critère | Responsable |
|-------|-------|-----------|---------|-------------|
| Résistance béton | NF EN 206/CN | 1 / 150 m³ | ≥ 30 MPa | Laboratoire |
| Étanchéité | NF DTU 43.1 | 100% surfaces | Pas de fuite | Contrôleur |
| Planéité dalle | NF DTU 26.2 | 1 / 100 m² | ≤ 5 mm/2m | MOE |

#### À quoi ça sert dans Stone-Sea ?

Stone-Sea peut :
- Générer automatiquement un plan de contrôle à partir d'un CCTP
- Planifier les essais selon les quantités
- Suivre l'avancement des contrôles

---

## 📊 Tableau récapitulatif

| Document | Rôle | Exemple d'info | Qui le crée ? |
|----------|------|----------------|---------------|
| **CCTP** | Définit comment réaliser les travaux | "Béton C25/30 selon NF DTU 21" | Maître d'œuvre |
| **DQE/DPGF** | Liste les quantités et prix | "250 m³ de terrassement à 35€" | Maître d'œuvre |
| **CR** | Trace l'avancement du chantier | "Dalle coulée le 12/11, conforme" | Maître d'œuvre |
| **DTU** | Norme de mise en œuvre | "Épaisseur mini 5 cm pour dalle" | AFNOR |
| **Eurocode** | Norme de calcul | "Résistance béton selon EN 1992" | CEN |
| **PV** | Atteste d'un résultat d'essai | "Résistance : 32,5 MPa - Conforme" | Laboratoire |
| **Plan de contrôle** | Programme les essais | "1 essai béton par 150 m³" | Contrôleur / MOE |

---

## 🔗 Relations entre les documents

```
CCTP (prescrit)
  ↓
DTU / Eurocodes (normes à respecter)
  ↓
Plan de contrôle (essais à réaliser)
  ↓
PV d'essai (résultats mesurés)
  ↓
CR de chantier (trace de conformité)
```

**Exemple de chaîne complète** :
1. Le **CCTP** prescrit : "Béton C25/30 selon NF DTU 21"
2. Le **DTU 21** exige : "Résistance ≥ 30 MPa à 28 jours"
3. Le **plan de contrôle** prévoit : "1 essai par 150 m³"
4. Le **PV** atteste : "Résistance mesurée : 32,5 MPa - CONFORME"
5. Le **CR** note : "Dalle RDC conforme selon PV n°2024-BET-0156"

---

## 💡 Points clés à retenir

- 📄 Le **CCTP** dit "quoi et comment" faire
- 💰 Le **DQE** liste les quantités et prix
- 📝 Le **CR** trace ce qui se passe sur le chantier
- 📚 Les **DTU** sont les règles de l'art (obligatoires)
- 🧮 Les **Eurocodes** servent aux calculs de structure
- 🧪 Les **PV** attestent des résultats d'essai
- ✅ Le **plan de contrôle** organise les essais

---

## ✅ Quiz rapide de compréhension

### Question 1
À quoi sert un CCTP ?
<details>
<summary>Voir la réponse</summary>
✅ Le CCTP décrit comment réaliser les travaux sur un projet spécifique (matériaux, normes, méthodes).
</details>

### Question 2
Quelle est la différence entre un DTU et un Eurocode ?
<details>
<summary>Voir la réponse</summary>
✅ Le DTU dit "comment faire" (mise en œuvre), l'Eurocode dit "comment calculer" (dimensionnement des structures).
</details>

### Question 3
Pourquoi est-il important de connaître l'édition d'un DTU ?
<details>
<summary>Voir la réponse</summary>
✅ Parce que les exigences peuvent changer d'une édition à l'autre. Il faut toujours utiliser la bonne version.
</details>

### Question 4
Qu'est-ce qu'un PV d'essai ?
<details>
<summary>Voir la réponse</summary>
✅ C'est un document de laboratoire qui atteste des résultats d'un essai (ex: résistance béton).
</details>

---

## ➡️ Prochaine étape

Maintenant que vous connaissez les principaux documents du BTP, découvrons les wrappers IA !

👉 **Section 4** : [Introduction aux wrappers IA](guide_wrappers.md)

---

**Bravo ! Vous maîtrisez maintenant le vocabulaire du BTP !** 🎉
