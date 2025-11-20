# FAQ - Questions fréquentes

## 📚 Questions générales sur Stone-Sea

### Qu'est-ce que Stone-Sea ?

Stone-Sea est un système complet pour gérer la conformité et la documentation dans le BTP en utilisant l'IA de manière sécurisée.

**Composants principaux** :
- 8 wrappers IA pour encadrer les analyses
- Schémas JSON pour structurer les données
- Scripts Python pour automatiser certaines tâches
- Prompts spécialisés pour le BTP

---

### À qui s'adresse Stone-Sea ?

**Tous les professionnels du BTP** :
- Chefs de chantier
- Conducteurs de travaux
- Ingénieurs d'études
- Contrôleurs techniques
- Maîtres d'œuvre
- Assistants administratifs

**Pas besoin d'être développeur !** Le MODULE_00 est conçu pour les débutants.

---

### Stone-Sea est-il gratuit ?

**Le projet Stone-Sea lui-même** : Oui (selon la licence)

**Les outils IA** (Claude, ChatGPT) :
- Versions gratuites disponibles (limitées)
- Versions payantes : 20 €/mois environ

---

## 🤖 Questions sur l'IA

### Ai-je besoin d'un compte Claude ou ChatGPT ?

**Oui**, vous avez besoin d'au moins un compte :
- **Recommandé** : Claude (https://claude.ai)
- **Alternative** : ChatGPT (https://chat.openai.com)

Les deux ont des versions gratuites pour commencer.

---

### Claude ou ChatGPT, lequel choisir ?

**Pour Stone-Sea, nous recommandons Claude** :
- Meilleure compréhension des documents techniques
- Meilleure gestion des longs documents
- Meilleur respect des instructions (wrappers)

**Mais ChatGPT fonctionne aussi !**

---

### L'IA peut-elle remplacer un expert BTP ?

**Non, absolument pas !**

L'IA est un **outil d'assistance**, pas un expert autonome :
- ✅ Elle peut analyser, extraire, comparer
- ❌ Elle ne peut pas valider de manière définitive
- ❌ Elle ne peut pas prendre de décisions critiques

**Un expert humain doit toujours valider les résultats.**

---

### L'IA fait-elle des erreurs ?

**Oui, l'IA peut faire des erreurs** :
- Hallucinations (inventer des informations)
- Extrapolations (déduire au-delà du document)
- Erreurs de compréhension

**C'est pour cela que les wrappers sont essentiels** : ils réduisent drastiquement ces risques.

---

### Comment éviter que l'IA invente des normes ?

**Utilisez les wrappers Stone-Sea !**

Les wrappers forcent l'IA à :
- Citer ses sources précisément
- Signaler ce qu'elle ne sait pas
- Ne pas extrapoler

**Et toujours vérifier** les normes citées dans les documents officiels.

---

## 🛡️ Questions sur les wrappers

### Qu'est-ce qu'un wrapper exactement ?

Un **wrapper**, c'est un **mode d'emploi très strict** qu'on donne à l'IA.

**Analogie** : C'est comme donner des consignes très précises à un stagiaire pour qu'il travaille correctement.

---

### Dois-je utiliser les 8 wrappers à chaque fois ?

**Non !** Vous utilisez le(s) wrapper(s) adapté(s) à votre besoin :

- Analyse simple → Wrapper 1
- Vérification normes → Wrapper 2 + Wrapper 8
- Rapport officiel → Wrapper 7 + Wrapper 6
- Document avec prix → Wrapper 4 en premier

**Vous pouvez combiner plusieurs wrappers.**

---

### Où trouver les wrappers ?

Les wrappers sont dans :
```
MODULE_01/wrappers_markdown/
```

**8 fichiers** :
- `wrapper1_contexte_limite.md`
- `wrapper2_sources_obligatoires.md`
- `wrapper3_sortie_verifiable.md`
- `wrapper4_donnees_sensibles.md`
- `wrapper5_double_raisonnement.md`
- `wrapper6_journal_sources.md`
- `wrapper7_tracabilite_citations.md`
- `wrapper8_controle_normatif_dtu.md`

---

### Comment utiliser un wrapper ?

**Étapes simples** :
1. Ouvrez le fichier `.md` du wrapper
2. Copiez tout le contenu
3. Collez dans Claude (ou ChatGPT)
4. Remplacez `<<<COLLER ICI...>>>` par votre document
5. Envoyez !

**Voir l'exercice pratique** : `MODULE_00/03_exercices/exercice_01_premier_wrapper.md`

---

### Puis-je modifier les wrappers ?

**Oui, mais avec prudence !**

Les wrappers ont été conçus pour la sécurité. Si vous les modifiez :
- Testez bien les modifications
- Documentez vos changements
- Vérifiez que l'IA ne "dérive" pas

**Pour débuter, utilisez-les tels quels.**

---

## 📄 Questions sur les documents BTP

### Je ne connais pas les normes BTP, puis-je quand même utiliser Stone-Sea ?

**Oui !** Le MODULE_00 explique les bases.

Pour aller plus loin :
- Consultez le [Guide documents BTP](../02_guides/guide_documents_btp.md)
- Consultez le [Glossaire BTP](glossaire_btp.md)
- Pratiquez avec des exemples simples

---

### Où trouver les DTU et normes ?

**Sources officielles** :
- Site AFNOR : https://www.afnor.org
- Boutique CSTB : https://www.boutique.cstb.fr
- Abonnement normes en entreprise

**Attention** : Les normes sont payantes (sauf si votre entreprise a un abonnement).

---

### Comment savoir quelle édition d'un DTU utiliser ?

**Règle générale** : Utilisez l'édition **en vigueur à la date du marché**.

**Si un CCTP dit** : "Selon NF DTU 21 (mars 2021)"
→ Utilisez cette édition précise, pas une autre

**Si aucune édition n'est précisée** :
→ C'est une source manquante à signaler !

---

## 🔒 Questions sur la sécurité et RGPD

### Puis-je envoyer n'importe quel document à l'IA ?

**Non !** Soyez prudent avec :
- Données personnelles (noms, adresses, tél, emails)
- Prix et montants contractuels
- Informations confidentielles

**Utilisez le Wrapper 4** (données sensibles) en premier.

**Mieux** : Anonymisez les documents avant.

---

### Comment anonymiser un document ?

**Méthode manuelle** :
- Remplacer les noms par [ANONYMISÉ] ou [MO-001], [ENT-001]
- Supprimer les prix
- Supprimer les coordonnées

**Wrapper 4** peut détecter ces données et vous alerter.

---

### L'IA garde-t-elle mes documents en mémoire ?

**Cela dépend de l'outil** :

**Claude** :
- Les conversations sont gardées dans votre historique
- Vous pouvez les supprimer
- Claude ne réutilise pas vos données pour s'entraîner (selon leur politique)

**ChatGPT** :
- Similaire, avec options de désactivation de l'historique
- Vérifiez les paramètres de confidentialité

**⚠️ En cas de doute** : N'envoyez jamais de données vraiment sensibles.

---

## 💻 Questions techniques

### Dois-je installer un logiciel ?

**Pour le MODULE_00 et MODULE_01** : Non !
- Tout se fait via le navigateur web (Claude ou ChatGPT)

**Pour les modules avancés** (04, 05, 06) : Oui
- Python 3.8+ requis
- Bibliothèques Python (selon le module)

---

### Je ne suis pas développeur, puis-je utiliser Stone-Sea ?

**Oui !** Pour les wrappers (MODULE_01), aucune compétence en développement n'est nécessaire.

**Vous devez juste savoir** :
- Copier-coller du texte
- Utiliser un navigateur web
- Lire et comprendre des documents BTP

---

### Puis-je utiliser Stone-Sea sur mobile ?

**Pour les wrappers** : Oui, mais c'est moins pratique
- Claude et ChatGPT ont des apps mobiles
- Mais les longs documents sont difficiles à manipuler

**Recommandation** : Utilisez un ordinateur pour plus de confort.

---

## 🎓 Questions sur la formation

### Combien de temps faut-il pour maîtriser les wrappers ?

**MODULE_00** : 2 heures (bases)
**MODULE_01** : 4 heures (pratique des 8 wrappers)
**Pratique régulière** : 2-4 semaines pour être à l'aise

**Total** : Environ 1 mois pour une maîtrise complète.

---

### Puis-je faire les modules dans le désordre ?

**Non, il faut suivre l'ordre** :
1. MODULE_00 (obligatoire pour débuter)
2. MODULE_01 (obligatoire pour les wrappers)
3. Modules 02, 04, 05, 06 (au choix selon vos besoins)

---

### J'ai raté le quiz, que faire ?

**Pas de panique !**
- Relisez les sections où vous avez des difficultés
- Consultez les glossaires
- Refaites le quiz
- Demandez de l'aide si besoin

**L'apprentissage prend du temps, c'est normal !**

---

### Où trouver de l'aide si je suis bloqué ?

**Ressources MODULE_00** :
- [Glossaire BTP](glossaire_btp.md)
- [Glossaire IA](glossaire_ia.md)
- [Guide de dépannage](depannage.md)

**Autres** :
- Demandez à un collègue qui connaît Stone-Sea
- Consultez les README des modules
- Relisez les guides du MODULE_00

---

## 🚀 Questions sur l'utilisation en production

### Puis-je utiliser Stone-Sea sur mes vrais projets ?

**Oui, mais avec prudence** :

**Recommandations** :
1. Maîtrisez d'abord les wrappers sur des exemples
2. Testez sur des documents non critiques
3. Vérifiez toujours les résultats
4. Faites valider par un expert

**Ne jamais** :
- Utiliser l'IA seule pour des décisions de sécurité
- Faire confiance aveuglément aux résultats
- Traiter des données sensibles sans anonymisation

---

### Comment mesurer les gains de temps ?

**Méthode simple** :
1. Notez le temps pour faire une tâche manuellement (ex: analyser un CCTP)
2. Notez le temps avec Stone-Sea + validation
3. Comparez

**Gains typiques** :
- Extraction d'infos : 50-70% de temps gagné
- Comparaison documents : 60-80% de temps gagné
- Structuration données : 70-90% de temps gagné

**Attention** : Temps de validation humaine à inclure !

---

### Puis-je former mes collègues ?

**Oui, absolument !**

**Méthode recommandée** :
1. Vous maîtrisez d'abord MODULE_00 et MODULE_01
2. Vous testez sur vos propres projets
3. Vous formez un premier collègue
4. Vous formez progressivement l'équipe

**Utilisez le MODULE_00 comme support de formation !**

---

## ❓ Autres questions

### Cette FAQ sera mise à jour ?

Cette FAQ est un document de base du MODULE_00.

Pour les mises à jour et questions plus avancées :
- Consultez les README des autres modules
- Consultez la documentation officielle de Stone-Sea

---

### Qui a créé Stone-Sea ?

Stone-Sea est un projet open-source pour le secteur BTP.

**Pour plus d'infos** : Consultez le `README.md` à la racine du projet.

---

### Comment contribuer à Stone-Sea ?

Si vous souhaitez contribuer (retours d'expérience, améliorations, bugs) :
- Consultez le README principal
- Contactez les mainteneurs du projet
- Partagez vos retours d'expérience

---

**💡 Votre question n'est pas dans cette FAQ ?**

Consultez le [Guide de dépannage](depannage.md) ou demandez à un collègue / formateur !
