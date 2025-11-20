# TP MODULE 01 - Wrappers IA pour le BTP

**Formation pratique à l'utilisation des 8 wrappers IA**

---

## 📋 Informations générales

**Durée estimée** : 4 heures
**Niveau** : Débutant à intermédiaire
**Prérequis** :
- Connaissances de base du secteur BTP
- Familiarité avec les documents techniques (CCTP, DTU, PV)
- Accès à un outil IA (Claude, ChatGPT, etc.)
- Avoir lu le README.md du MODULE_01

**Objectifs pédagogiques** :
1. Maîtriser l'utilisation des 8 wrappers IA pour encadrer les interactions
2. Comprendre les enjeux de sécurité et de conformité dans l'usage de l'IA en BTP
3. Savoir choisir le wrapper approprié selon le contexte
4. Produire des analyses et contrôles conformes et traçables

---

## 📚 Partie 1 : Contexte et enjeux (15 min)

### 1.1 Pourquoi des wrappers IA ?

Dans le secteur BTP, l'utilisation de l'IA pour analyser des documents techniques, contrôler la conformité ou produire de la documentation présente des risques spécifiques :

- **Hallucinations** : L'IA peut inventer des normes, des chiffres ou des références inexistantes
- **Extrapolation** : L'IA peut déduire ou interpréter au-delà du contenu fourni
- **Données sensibles** : Prix, montants contractuels, données personnelles (RGPD)
- **Non-traçabilité** : Difficulté à retrouver les sources d'une affirmation
- **Non-conformité** : Risque d'erreurs normatives coûteuses

Les 8 wrappers permettent de **cadrer strictement** les interactions avec l'IA pour garantir :
- Fiabilité et vérifiabilité des résultats
- Conformité normative et contractuelle
- Traçabilité complète des sources
- Protection des données sensibles

### 1.2 Les 8 wrappers : vue d'ensemble

| Wrapper | Usage principal | Cas d'application |
|---------|-----------------|-------------------|
| **1 - Contexte limité** | Analyser un extrait sans extrapolation | Lecture de clause CCTP isolée |
| **2 - Sources obligatoires** | Exiger des références datées | Analyse de normes avec éditions |
| **3 - Sortie vérifiable** | Produire des tableaux à 2 colonnes | Comparaison source/conclusion |
| **4 - Données sensibles** | Détecter et bloquer les données RGPD | Anonymisation de documents |
| **5 - Double raisonnement** | Analyser avantages/risques | Choix techniques complexes |
| **6 - Journal des sources** | Tracer toutes les sources utilisées | Audit de conformité |
| **7 - Citations numérotées** | Référencer précisément les sources | Rapports d'expertise |
| **8 - Contrôle normatif** | Vérifier conformité DTU/Eurocodes | Contrôle qualité chantier |

---

## 🎯 Partie 2 : Exercices pratiques par wrapper

### Exercice 1 : Wrapper 1 - Contexte limité

**Objectif** : Limiter l'analyse à l'extrait fourni sans extrapolation

**Contexte** : Vous avez reçu un extrait d'un CCTP concernant la couverture d'un bâtiment. Vous devez l'analyser sans ajouter d'informations externes.

**Document fourni** :
```
ARTICLE 5.2 - COUVERTURE ZINC
La couverture sera réalisée en zinc naturel prépatiné, épaisseur 0,7 mm.
Mise en œuvre à joint debout, selon DTU 40.41.
Support : voligeage jointif en sapin 20 mm minimum.
Pente minimale : 7%.
```

**Consigne** :
1. Copiez le wrapper 1 dans votre outil IA
2. Remplacez `<<<COLLER ICI L'EXTRAIT>>>` par le document ci-dessus
3. Lancez l'analyse

**Questions à vous poser** :
- L'IA a-t-elle mentionné des informations absentes de l'extrait ?
- A-t-elle correctement identifié les limites (ex: pas de quantités, pas d'édition DTU) ?
- A-t-elle tenté d'interpréter ou d'ajouter des exigences non écrites ?

**Réponse attendue** :
L'IA devrait :
- Lister la structure (Article 5.2, 4 points techniques)
- Résumer factuellement (zinc 0,7mm, joint debout, voligeage 20mm, pente 7%)
- Signaler les **limites** : édition DTU non précisée, pas de quantités, pas de délais
- Signaler les **ambiguïtés** : "prépatiné" (définition contractuelle ?), "sapin" (qualité ?)

---

### Exercice 2 : Wrapper 2 - Sources obligatoires

**Objectif** : Exiger la présence de sources jointes et la datation/édition des références

**Contexte** : Un maître d'œuvre vous demande de vérifier si un CCTP mentionne bien les normes applicables pour la dalle béton.

**Documents fournis** :
```
CCTP - Article 3.1 Dalle béton rez-de-chaussée
Béton C25/30 XC1, granulométrie 0/20 mm.
Épaisseur : 15 cm minimum.
Armatures : treillis soudé ST25C (mailles 150x150).
Mise en œuvre selon NF DTU 21 (mars 2021).
Conformité béton : NF EN 206/CN.
```

**Consigne** :
1. Utilisez le wrapper 2
2. Insérez le document ci-dessus
3. Demandez : "Quelles sont les normes applicables à cette dalle béton ?"

**Questions** :
- L'IA a-t-elle produit une table "Références citées" ?
- Les éditions et dates sont-elles mentionnées ?
- L'IA a-t-elle signalé des sources manquantes ?

**Réponse attendue** :

**Références citées :**
| Référence | Titre | Édition/Version | Date | Page/Section |
|-----------|-------|-----------------|------|--------------|
| NF DTU 21 | Exécution des ouvrages en béton | - | mars 2021 | Article 3.1 |
| NF EN 206/CN | Béton - Spécification, performance... | - | - | Article 3.1 |

**Sources manquantes :**
- Édition précise de NF EN 206/CN non indiquée
- Norme pour treillis soudé (norme produit) non mentionnée
- Pas de référence pour mise en œuvre des armatures

---

### Exercice 3 : Wrapper 3 - Sortie vérifiable (2 colonnes)

**Objectif** : Produire des tableaux à 2 colonnes pour vérifier chaque affirmation

**Contexte** : Vous devez analyser un PV d'essai béton et vérifier que chaque conclusion est étayée par une donnée source.

**Document fourni** :
```
PV d'essai n°2024-BET-0042
Chantier : Résidence Les Pins
Date prélèvement : 15/10/2024
Classe prescrite : C25/30
Résultats à 28 jours :
- Éprouvette 1 : 32,5 MPa
- Éprouvette 2 : 31,8 MPa
- Éprouvette 3 : 33,1 MPa
Moyenne : 32,5 MPa
Écart-type : 0,65 MPa
Conformité : Conforme NF EN 206/CN
```

**Consigne** :
1. Utilisez le wrapper 3
2. Demandez : "Vérifier la conformité de ce PV d'essai béton"

**Réponse attendue** :

| Élément source (verbatim) | Affirmation / Conclusion |
|---------------------------|--------------------------|
| "Classe prescrite : C25/30" | Résistance minimale exigée = 30 MPa |
| "Éprouvette 1 : 32,5 MPa" | Essai 1 conforme (>30 MPa) |
| "Éprouvette 2 : 31,8 MPa" | Essai 2 conforme (>30 MPa) |
| "Éprouvette 3 : 33,1 MPa" | Essai 3 conforme (>30 MPa) |
| "Moyenne : 32,5 MPa" | Moyenne > 30 MPa : conforme |
| "Conformité : Conforme NF EN 206/CN" | Conclusion du laboratoire : conforme |

**Non vérifiable dans la source :**
- Critères détaillés de la norme NF EN 206/CN (non fournie)
- Conditions de conservation des éprouvettes
- Accréditation du laboratoire

---

### Exercice 4 : Wrapper 4 - Données sensibles

**Objectif** : Détecter et protéger les données sensibles (RGPD, prix, contrats)

**Contexte** : Vous devez analyser un extrait de marché de travaux pour en extraire les prestations, mais sans révéler les montants ni les données personnelles.

**Document fourni** :
```
MARCHÉ N° 2024-BTP-0156
Maître d'ouvrage : M. Jean DURAND, 12 rue des Lilas, 75012 Paris
Tel : 06 12 34 56 78 / Email : j.durand@email.com
Entreprise : SARL BATIPRO, RCS Paris 123 456 789

LOT 1 - Gros œuvre
- Terrassement général : 12 500 € HT
- Fondations semelles filantes : 28 000 € HT
- Élévation murs porteurs : 45 600 € HT

LOT 2 - Charpente
- Charpente traditionnelle sapin : 18 900 € HT
Total marché HT : 105 000 € HT
```

**Consigne** :
1. Utilisez le wrapper 4
2. Demandez : "Extraire la liste des prestations du marché"

**Réponse attendue** :

**⚠️ ALERTE DONNÉES SENSIBLES DÉTECTÉES**

**Données personnelles (RGPD) :**
- Nom : Jean DURAND
- Adresse : 12 rue des Lilas, 75012 Paris
- Téléphone : 06 12 34 56 78
- Email : j.durand@email.com

**Données contractuelles sensibles :**
- Prix unitaires et totaux
- Numéro de marché
- RCS entreprise

**⛔ REFUS DE TRAITEMENT**
Veuillez anonymiser le document avant toute analyse.

**Version anonymisée suggérée :**
```
MARCHÉ N° [ANONYMISÉ]
Maître d'ouvrage : [MO-001]
Entreprise : [ENT-001]

LOT 1 - Gros œuvre
- Terrassement général
- Fondations semelles filantes
- Élévation murs porteurs

LOT 2 - Charpente
- Charpente traditionnelle sapin
```

---

### Exercice 5 : Wrapper 5 - Double raisonnement + matrice

**Objectif** : Analyser les avantages et risques d'une solution technique

**Contexte** : Le bureau d'études propose deux solutions pour l'isolation thermique par l'extérieur (ITE) d'un bâtiment. Vous devez analyser les deux options.

**Document fourni** :
```
SOLUTION A - ITE Polystyrène expansé (PSE)
Épaisseur : 14 cm (R=4,0 m².K/W)
Finition : enduit mince organique
Coût estimatif : 85 €/m²
Délai de mise en œuvre : 6 semaines

SOLUTION B - ITE Laine de roche
Épaisseur : 16 cm (R=4,0 m².K/W)
Finition : enduit hydraulique
Coût estimatif : 105 €/m²
Délai de mise en œuvre : 8 semaines
```

**Consigne** :
1. Utilisez le wrapper 5
2. Demandez : "Analyser les avantages et risques de chaque solution ITE"

**Réponse attendue** :

**SOLUTION A - PSE**

| Critère | Avantages | Risques | Score |
|---------|-----------|---------|-------|
| Performance thermique | R=4,0 atteint | Pont thermique si pose non soignée | 7/10 |
| Coût | 85 €/m², le plus économique | Dépendance au pétrole (prix volatile) | 8/10 |
| Délai | 6 semaines | Conditions météo critiques | 7/10 |
| Durabilité | Bonne résistance si protégé | Sensible UV et chocs | 6/10 |
| Réaction au feu | Inflammable (Euroclasse E) | Nécessite coupures feu renforcées | 4/10 |

**SOLUTION B - Laine de roche**

| Critère | Avantages | Risques | Score |
|---------|-----------|---------|-------|
| Performance thermique | R=4,0 atteint, stable | Tassement si mal posé | 8/10 |
| Coût | Plus cher (+23%) | Coût global sur durée de vie OK | 6/10 |
| Délai | 8 semaines | Nécessite temps séchage enduit | 6/10 |
| Durabilité | Excellente, inerte | Doit rester sec | 9/10 |
| Réaction au feu | Incombustible (Euroclasse A1) | Aucun risque | 10/10 |

**RECOMMANDATION :**
Solution B (laine de roche) si :
- Bâtiment soumis à contraintes feu (ERP, IGH)
- Budget permet le surcoût
- Durabilité prioritaire

Solution A (PSE) si :
- Budget contraint
- Délai serré
- Bâtiment résidentiel standard

**SOURCES MANQUANTES pour décision finale :**
- Classement feu réglementaire du bâtiment
- Avis technique des systèmes proposés
- Cahier des charges maître d'ouvrage

---

### Exercice 6 : Wrapper 6 - Journal des sources

**Objectif** : Tracer toutes les sources utilisées pour un audit complet

**Contexte** : Vous réalisez un contrôle de conformité d'un CCTP. Vous devez produire un journal détaillé de toutes les sources consultées.

**Documents fournis** :
```
CCTP_Maconnerie_v2.3.pdf (pages 12-18)
NF_DTU_20.1_mars_2020_extraits.pdf (pages 5, 12, 28)
Plan_Facade_Sud_indice_B.dwg
CR_reunion_chantier_20241015.docx
```

**Consigne** :
1. Utilisez le wrapper 6
2. Simulez une analyse de conformité

**Réponse attendue** :

**JOURNAL DES SOURCES**

| ID | Type | Nom | Version/Date | Pages/Sections | Horodatage accès | Hash SHA-256 |
|----|------|-----|--------------|----------------|------------------|--------------|
| S001 | PDF | CCTP_Maconnerie_v2.3.pdf | v2.3 | 12-18 | 2024-11-20 10:15:23 | a3f5... |
| S002 | PDF | NF_DTU_20.1_mars_2020_extraits.pdf | mars 2020 | 5, 12, 28 | 2024-11-20 10:17:41 | b8e2... |
| S003 | DWG | Plan_Facade_Sud_indice_B.dwg | Indice B | - | 2024-11-20 10:22:10 | c1d9... |
| S004 | DOCX | CR_reunion_chantier_20241015.docx | 15/10/2024 | Tout | 2024-11-20 10:25:33 | d4a7... |

**CITATIONS PAR SOURCE :**
- S001 : Articles 2.1, 2.3, 4.5 (exigences maçonnerie)
- S002 : Paragraphes 5.2.1, 7.3.4, 12.1.2 (normes DTU)
- S003 : Dimensions façade Sud, niveaux
- S004 : Décisions sur mortier (page 2)

**TRAÇABILITÉ :**
- Analyse effectuée par : [VOTRE NOM]
- Date : 2024-11-20
- Outil IA : Claude 3.5 Sonnet
- Durée session : 00:15:28

---

### Exercice 7 : Wrapper 7 - Citations numérotées

**Objectif** : Référencer précisément chaque affirmation avec citation numérotée

**Contexte** : Vous rédigez un rapport d'expertise sur une non-conformité de menuiserie extérieure.

**Document fourni** :
```
NF DTU 36.5 - Mise en œuvre des fenêtres et portes extérieures (Octobre 2010)

Section 6.2.3 - Fixation des menuiseries
"Les menuiseries doivent être fixées au gros œuvre par des pattes métalliques
ou des équerres. Le nombre minimal de points de fixation est de :
- 3 par montant pour les fenêtres de hauteur ≤ 1,50 m
- 4 par montant pour les fenêtres de hauteur > 1,50 m
Les fixations doivent être réparties sur la hauteur, avec un point
obligatoire à 15 cm maximum des angles."

Section 6.3.1 - Étanchéité
"Un joint de calfeutrement périphérique doit être réalisé entre le dormant
et la maçonnerie. Ce joint doit être continu et d'épaisseur minimale 5 mm."
```

**Constat sur chantier** :
```
Fenêtre F12 (façade Ouest) : dimensions 1,35 m x 1,60 m
Fixations constatées : 2 pattes par montant vertical
Joint périphérique présent mais discontinu (absence sur traverse haute)
```

**Consigne** :
1. Utilisez le wrapper 7
2. Rédigez un constat de non-conformité avec citations numérotées

**Réponse attendue** :

**RAPPORT DE NON-CONFORMITÉ - Fenêtre F12**

**1. CONTEXTE**
Contrôle de la fenêtre F12 (façade Ouest), dimensions 1,35 m × 1,60 m (hauteur > 1,50 m).

**2. EXIGENCES NORMATIVES**

La NF DTU 36.5 (Octobre 2010) prescrit les exigences suivantes :

**[1]** "Les menuiseries doivent être fixées au gros œuvre par des pattes métalliques ou des équerres. Le nombre minimal de points de fixation est de : [...] - 4 par montant pour les fenêtres de hauteur > 1,50 m" (Section 6.2.3)

**[2]** "Les fixations doivent être réparties sur la hauteur, avec un point obligatoire à 15 cm maximum des angles." (Section 6.2.3)

**[3]** "Un joint de calfeutrement périphérique doit être réalisé entre le dormant et la maçonnerie. Ce joint doit être continu et d'épaisseur minimale 5 mm." (Section 6.3.1)

**3. CONSTATS**

| Exigence | Constat | Conformité | Gravité |
|----------|---------|------------|---------|
| Nombre de fixations [1] | 2 pattes/montant (au lieu de 4) | ❌ NON CONFORME | MAJEURE |
| Répartition fixations [2] | Non vérifié (points insuffisants) | ❌ NON CONFORME | MAJEURE |
| Joint périphérique continu [3] | Discontinu (absence traverse haute) | ❌ NON CONFORME | MAJEURE |

**4. ACTIONS REQUISES**

1. **Dépose et repose de la fenêtre F12** avec ajout de 2 fixations par montant [1]
2. **Vérification répartition** avec point à 15 cm max des angles [2]
3. **Reprise joint périphérique** sur toute la périphérie [3]
4. **Contrôle contradictoire** après reprise

**5. SOURCES**

- [1], [2] : NF DTU 36.5, Section 6.2.3 "Fixation des menuiseries", Octobre 2010
- [3] : NF DTU 36.5, Section 6.3.1 "Étanchéité", Octobre 2010

**Date du rapport** : 2024-11-20
**Contrôleur** : [VOTRE NOM]

---

### Exercice 8 : Wrapper 8 - Contrôle normatif DTU

**Objectif** : Vérifier la conformité d'un point d'exécution par rapport aux référentiels

**Contexte** : Contrôle d'une dalle de compression sur plancher collaborant.

**Documents fournis** :
```
NF DTU 21 - Exécution des ouvrages en béton (Mars 2021)
Section 9.4.2 - Dalles de compression sur bacs acier
"Épaisseur minimale de dalle : 5 cm au-dessus des ondes hautes du bac.
Béton : classe minimale C25/30.
Armatures : treillis soudé de section ≥ 0,6 cm²/m dans chaque direction.
Recouvrement treillis : 2 mailles + 20 cm minimum."

EN 1992-1-1 (Eurocode 2) - Section 9.3
"Enrobage minimal des armatures : 20 mm pour exposition XC1 (intérieur sec)."
```

**Constat chantier - Zone A2** :
```
Dalle réalisée : épaisseur 13 cm totale (bac 75 mm + dalle 55 mm sur ondes hautes)
Béton coulé : C30/37 XC1 selon BL
Armatures : treillis ST25C posé (5 cm² de section par nappe)
Recouvrement : 1 maille visible + environ 15 cm
Enrobage constaté : 18 mm (mesure au pachomètre)
```

**Consigne** :
1. Utilisez le wrapper 8
2. Produisez un tableau de contrôle normatif

**Réponse attendue** :

**CONTRÔLE NORMATIF - Dalle compression Zone A2**

**EXIGENCES APPLICABLES**

| Référence | Paragraphe | Intitulé | Édition/Date | Valeur prescrite |
|-----------|-----------|----------|--------------|------------------|
| NF DTU 21 | 9.4.2 | Épaisseur minimale | Mars 2021 | ≥ 5 cm au-dessus ondes hautes |
| NF DTU 21 | 9.4.2 | Classe béton | Mars 2021 | ≥ C25/30 |
| NF DTU 21 | 9.4.2 | Section armatures | Mars 2021 | ≥ 0,6 cm²/m chaque direction |
| NF DTU 21 | 9.4.2 | Recouvrement treillis | Mars 2021 | 2 mailles + 20 cm mini |
| EN 1992-1-1 | 9.3 | Enrobage XC1 | - | ≥ 20 mm |

**CONSTAT DE CONFORMITÉ**

| Exigence | Conformité | Valeur constatée | Écart | Gravité | Action |
|----------|------------|------------------|-------|---------|--------|
| Épaisseur dalle | ✅ Oui | 5,5 cm > 5 cm | - | - | - |
| Classe béton | ✅ Oui | C30/37 > C25/30 | - | - | - |
| Section armatures | ✅ Oui | 5 cm²/m > 0,6 cm²/m | - | - | - |
| Recouvrement | ❌ Non | 1 maille + 15 cm | -1 maille et -5 cm | **MAJEUR** | Reprise |
| Enrobage | ❌ Non | 18 mm | -2 mm | **MINEUR** | Dérogation ? |

**DÉCISIONS**

1. **Non-conformité MAJEURE** : Recouvrement treillis insuffisant
   - **Action** : Ajout d'armatures complémentaires si possible, ou note de calcul bureau d'études pour dérogation justifiée

2. **Non-conformité MINEURE** : Enrobage 18 mm au lieu de 20 mm
   - **Action** : Demander avis bureau d'études (classe XC1 peu agressive, écart faible)

**SOURCES**
- NF DTU 21 "Exécution des ouvrages en béton", Mars 2021, Section 9.4.2
- EN 1992-1-1 (Eurocode 2), Section 9.3
- Bordereau de livraison béton n° BL-2024-1042 (C30/37 XC1)
- Photos chantier 20241118 (enrobage, recouvrement)

---

## 🏆 Partie 3 : Évaluation finale (1h)

### Cas pratique intégré

**Contexte général** :
Vous êtes chef de chantier sur la construction d'un immeuble de logements. Le maître d'œuvre vous transmet un extrait de CCTP concernant la chape flottante des appartements, ainsi qu'un PV d'essai. Vous devez :
1. Analyser le CCTP
2. Contrôler la conformité du PV par rapport au CCTP et aux normes
3. Produire un rapport traçable

**Document 1 - Extrait CCTP** :
```
ARTICLE 8 - CHAPES FLOTTANTES
Lot : Revêtements de sols
Locaux : Appartements (séjours et chambres)

8.1 Isolation phonique
Sous-couche résiliente : panneaux laine de roche 40 mm, résistance au poinçonnement CP2.
Référence produit : ROCKWOOL Rockfloor Solid ou équivalent.
Performance acoustique : ΔLw ≥ 20 dB.

8.2 Chape de ravoirage
Type : chape ciment traditionnelle, dosage 350 kg/m³.
Épaisseur : 50 mm minimum.
Finition : talochée, planéité P3 (NF DTU 26.2, Avril 2008).
Joints de fractionnement : tous les 36 m² maximum.

8.3 Normes applicables
- NF DTU 26.2 - Chapes et dalles à base de liants hydrauliques (Avril 2008)
- NF DTU 52.1 - Revêtements de sol scellés
- Avis Technique du produit isolant
```

**Document 2 - PV d'essai chape** :
```
PROCES-VERBAL D'ESSAI N° 2024-CH-0089
Laboratoire QUALIBAT - Accréditation COFRAC n°1-2345

Chantier : Résidence Les Érables, Bâtiment B
Date prélèvement : 10/11/2024 (chape coulée le 28/10/2024)
Local : Appartement B204 (séjour)

Essai de résistance mécanique (NF EN 13318)
- Point 1 : 8,2 MPa
- Point 2 : 7,9 MPa
- Point 3 : 8,5 MPa
Moyenne : 8,2 MPa

Épaisseur constatée : 52 mm

Planéité mesurée (règle de 2m) :
- Défaut max sous règle : 4 mm
- Classement : P3 conforme NF DTU 26.2

Sous-couche isolante :
Produit identifié : ROCKWOOL Rockfloor Solid
Épaisseur constatée : 38 mm (2 points < 40 mm)
Pas d'Avis Technique fourni

Conclusion : Résistance mécanique conforme. Planéité P3 conforme.
Réserve : Épaisseur isolant non conforme par endroits.
```

### Questions de l'évaluation

**Question 1** (Wrapper 1 + 2) : Analysez l'extrait CCTP en listant les exigences et les sources manquantes. (15 points)

**Question 2** (Wrapper 3) : Créez un tableau à 2 colonnes comparant les prescriptions CCTP et les constats du PV. (15 points)

**Question 3** (Wrapper 7) : Rédigez un constat de réserve sur l'épaisseur de l'isolant avec citations numérotées. (20 points)

**Question 4** (Wrapper 8) : Produisez un tableau de contrôle normatif complet (exigences + conformité). (25 points)

**Question 5** (Wrapper 6) : Listez toutes les sources utilisées dans un journal de traçabilité. (10 points)

**Question 6** (Wrapper 5) : Proposez une matrice avantages/risques pour décider de l'action à mener (levée de réserve conditionnelle vs reprise totale). (15 points)

### Barème et critères d'évaluation

**Total : 100 points**

- **< 50 points** : Non acquis - Réviser les wrappers et refaire les exercices
- **50-69 points** : Partiellement acquis - Reprendre les wrappers en difficulté
- **70-84 points** : Acquis - Utilisation correcte des wrappers
- **85-100 points** : Maîtrisé - Prêt pour utilisation autonome en production

**Critères de qualité** :
- ✅ Respect strict du format du wrapper
- ✅ Aucune extrapolation hors sources
- ✅ Sources précisément référencées (édition, date, page)
- ✅ Tableaux structurés et complets
- ✅ Identification systématique des limites et sources manquantes
- ✅ Traçabilité complète

---

## 📖 Partie 4 : Ressources et bonnes pratiques

### 4.1 Quand utiliser quel wrapper ?

**Arbre de décision** :

```
Vous devez analyser un document BTP
│
├─ Le document contient-il des données personnelles ou des prix ?
│  └─ OUI → Wrapper 4 (Données sensibles) EN PREMIER
│
├─ Devez-vous produire un rapport d'expertise opposable ?
│  └─ OUI → Wrapper 7 (Citations numérotées) + Wrapper 6 (Journal sources)
│
├─ Devez-vous contrôler la conformité à des normes DTU/Eurocodes ?
│  └─ OUI → Wrapper 8 (Contrôle normatif)
│
├─ Devez-vous comparer deux solutions techniques ?
│  └─ OUI → Wrapper 5 (Double raisonnement + matrice)
│
├─ Voulez-vous simplement comprendre un extrait sans aller au-delà ?
│  └─ OUI → Wrapper 1 (Contexte limité)
│
├─ Avez-vous besoin de vérifier les éditions et dates de normes ?
│  └─ OUI → Wrapper 2 (Sources obligatoires)
│
└─ Voulez-vous une sortie facilement vérifiable ligne à ligne ?
   └─ OUI → Wrapper 3 (Sortie 2 colonnes)
```

### 4.2 Combinaisons de wrappers recommandées

**Cas 1 : Contrôle de conformité CCTP**
→ Wrapper 4 + Wrapper 2 + Wrapper 8 + Wrapper 6

**Cas 2 : Rapport d'expertise judiciaire**
→ Wrapper 7 + Wrapper 6 + Wrapper 3

**Cas 3 : Analyse technique pour arbitrage**
→ Wrapper 5 + Wrapper 2

**Cas 4 : Vérification simple de document**
→ Wrapper 1 + Wrapper 3

### 4.3 Erreurs fréquentes à éviter

❌ **Erreur 1** : Oublier de remplacer les `<<<...>>>`
→ ✅ Toujours insérer vos documents dans les zones prévues

❌ **Erreur 2** : Demander à l'IA d'interpréter sans sources
→ ✅ Exiger systématiquement "source manquante" si l'info n'est pas fournie

❌ **Erreur 3** : Accepter une norme sans édition ni date
→ ✅ Toujours exiger "NF DTU XX (mois année)" ou signaler l'absence

❌ **Erreur 4** : Ne pas vérifier les tableaux de sortie
→ ✅ Relire systématiquement chaque ligne source vs conclusion

❌ **Erreur 5** : Utiliser un seul wrapper alors que plusieurs sont nécessaires
→ ✅ Combiner les wrappers pour une analyse complète

### 4.4 Checklist avant de valider une analyse IA

Avant d'utiliser un résultat d'IA en production, vérifiez :

- [ ] Le wrapper approprié a été utilisé
- [ ] Toutes les sources sont citées avec édition et date
- [ ] Aucune extrapolation n'a été faite hors documents fournis
- [ ] Les données sensibles ont été détectées ou anonymisées
- [ ] Un journal de traçabilité a été produit (si requis)
- [ ] Les tableaux de sortie sont complets et cohérents
- [ ] Les limites et sources manquantes sont explicitement listées
- [ ] Une relecture humaine experte a validé les conclusions critiques

---

## 📝 Annexes

### Annexe A : Tableau récapitulatif des wrappers

| Wrapper | Objectif | Entrée | Sortie | Cas d'usage |
|---------|----------|--------|--------|-------------|
| **1** | Pas d'extrapolation | Extrait document | Structure + Résumé + Limites | Lecture isolée |
| **2** | Sources datées | Documents + Question | Réponse + Table références | Analyse normative |
| **3** | Vérifiabilité | Document | Tableau Source / Conclusion | Contrôle qualité |
| **4** | Protection RGPD | Document | Alerte + Refus ou Anonymisation | Données sensibles |
| **5** | Aide décision | Options techniques | Matrice Avantages/Risques | Arbitrage technique |
| **6** | Traçabilité | Documents multiples | Journal sources + Hash | Audit conformité |
| **7** | Citations précises | Documents | Texte avec [1], [2]... | Rapport expertise |
| **8** | Conformité normes | Élément + DTU/EC | Tables Exigences + Écarts | Contrôle chantier |

### Annexe B : Exemple de processus complet

**Objectif** : Contrôler la conformité d'un poste CCTP pour une couverture tuiles

**Étape 1** : Anonymisation (Wrapper 4)
→ Supprimer noms, adresses, montants du CCTP

**Étape 2** : Analyse du CCTP (Wrapper 1)
→ Comprendre la structure et identifier les exigences

**Étape 3** : Vérification des sources (Wrapper 2)
→ S'assurer que toutes les normes citées ont une édition et date

**Étape 4** : Contrôle normatif (Wrapper 8)
→ Comparer les prescriptions CCTP aux exigences DTU 40.21

**Étape 5** : Production du rapport (Wrapper 7 + Wrapper 6)
→ Rédiger le rapport avec citations numérotées et journal des sources

**Étape 6** : Validation humaine
→ Relecture experte et signature du rapport

### Annexe C : Ressources complémentaires

**Documentation Stone-Sea** :
- `README.md` du projet : Vue d'ensemble complète
- `MODULE_01/wrappers_markdown/README.md` : Instructions d'utilisation des wrappers
- Fichiers individuels des wrappers : `wrapper1_contexte_limite.md` à `wrapper8_controle_normatif_dtu.md`

**Normes BTP principales** :
- NF DTU 20.1 : Maçonnerie
- NF DTU 21 : Ouvrages en béton
- NF DTU 26.2 : Chapes et dalles
- NF DTU 40.xx : Couvertures
- NF DTU 60.x et 65.x : CVC et plomberie
- Eurocodes : EN 1990 à EN 1999

**Règlementation** :
- RGPD : Protection des données personnelles
- Code des marchés publics
- Normes ISO 9001, ISO 19650 (BIM)

---

## 🎓 Conclusion

Vous avez maintenant parcouru l'ensemble des 8 wrappers IA du MODULE_01 de Stone-Sea. Ces outils sont essentiels pour garantir :

✅ **Fiabilité** : Aucune hallucination, tout est vérifié dans les sources
✅ **Conformité** : Respect strict des normes DTU, Eurocodes et AT
✅ **Traçabilité** : Journal complet pour audits et contentieux
✅ **Sécurité** : Protection des données sensibles (RGPD, secret des affaires)

**Prochaines étapes** :
1. Pratiquer régulièrement avec des documents réels de vos chantiers
2. Combiner les wrappers selon les besoins
3. Former vos équipes à leur utilisation
4. Intégrer les wrappers dans vos processus qualité

**Rappel important** :
L'IA est un **assistant**, pas un **expert autonome**. La validation humaine par un professionnel qualifié reste **obligatoire** pour toute décision engageante (validation de conformité, levée de réserve, choix technique structurel).

---

**Formateur** : [À compléter]
**Date de création du TP** : 2024-11-20
**Version** : 1.0
**Contact** : [À compléter]
