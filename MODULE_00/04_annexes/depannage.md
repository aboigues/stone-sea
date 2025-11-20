# Guide de dépannage

## 🔧 Introduction

Ce guide vous aide à résoudre les problèmes courants rencontrés lors de l'utilisation de Stone-Sea et des wrappers IA.

---

## 🤖 Problèmes avec Claude / ChatGPT

### Je ne parviens pas à créer un compte

**Symptômes** :
- Le site refuse mon inscription
- Je ne reçois pas l'email de confirmation

**Solutions** :

**1. Vérifiez votre email**
- Vérifiez les spams / courriers indésirables
- Attendez quelques minutes (parfois l'email est retardé)

**2. Essayez un autre email**
- Utilisez un email professionnel
- Évitez les emails temporaires

**3. Vérifiez votre connexion**
- Essayez avec un autre navigateur
- Désactivez temporairement le VPN si vous en avez un

**4. Essayez l'autre outil**
- Si Claude ne fonctionne pas → Essayez ChatGPT
- Si ChatGPT ne fonctionne pas → Essayez Claude

---

### Claude refuse mon message

**Symptômes** :
- Message d'erreur : "I can't help with that"
- Claude ne veut pas traiter le document

**Causes possibles** :

**1. Détection de contenu sensible**
Claude a détecté des données personnelles ou confidentielles.

**Solution** :
- Anonymisez votre document avant (remplacez noms, adresses, prix)
- Utilisez le Wrapper 4 pour détecter ces données d'abord

**2. Document trop long**
Le document dépasse la limite de tokens.

**Solution** :
- Découpez le document en plusieurs parties
- Traitez section par section

**3. Demande ambiguë**
Claude ne comprend pas ce que vous voulez.

**Solution** :
- Reformulez votre demande plus clairement
- Utilisez un wrapper complet (ne modifiez pas le wrapper)

---

### L'IA ne respecte pas le wrapper

**Symptômes** :
- L'IA invente des informations
- L'IA extrapole au-delà du document
- L'IA ne cite pas ses sources

**Solutions** :

**1. Vérifiez que vous avez copié le wrapper complet**
- Ne prenez pas juste un extrait
- Copiez tout le fichier `.md` du wrapper

**2. Vérifiez que vous avez bien inséré le document**
- Remplacez `<<<COLLER ICI L'EXTRAIT>>>` par votre document
- N'oubliez pas cette étape !

**3. Relancez avec un rappel**
```
Tu n'as pas respecté le wrapper. Recommence en suivant STRICTEMENT les instructions :
- Ne rien inventer
- Ne pas extrapoler
- Citer toutes les sources
- Signaler les sources manquantes
```

**4. Démarrez une nouvelle conversation**
Parfois, l'IA "dérive" dans une longue conversation. Recommencez à zéro.

---

### L'IA répond en anglais

**Symptômes** :
- La réponse est en anglais alors que le wrapper est en français

**Solution** :
```
Merci, mais peux-tu répondre en français s'il te plaît ?
```

Ou ajoutez au début du wrapper :
```
IMPORTANT : Réponds UNIQUEMENT en français.
```

---

## 📄 Problèmes avec les documents

### Mon document est trop long pour Claude

**Symptômes** :
- Message d'erreur : "Too long"
- Claude refuse le document

**Solutions** :

**1. Découpez le document**
Traitez par sections :
- Section 1 : Articles 1-3
- Section 2 : Articles 4-6
- Etc.

**2. Extrayez uniquement les parties pertinentes**
Ne collez pas tout le CCTP de 200 pages, juste la section à analyser.

**3. Utilisez Claude Pro**
Claude Pro a une limite plus élevée que la version gratuite.

---

### Le copier-coller ne fonctionne pas

**Symptômes** :
- Le texte ne se colle pas
- Le formatage est cassé

**Solutions** :

**1. Utilisez Ctrl+C / Ctrl+V (ou Cmd+C / Cmd+V sur Mac)**
Évitez le clic droit → Copier

**2. Essayez un autre navigateur**
Chrome, Firefox, Safari, Edge

**3. Copiez depuis un fichier texte simple**
- Ouvrez le `.md` avec Bloc-notes (Windows) ou TextEdit (Mac)
- Copiez depuis là

---

### Mon PDF ne s'ouvre pas

**Symptômes** :
- Impossible d'ouvrir le fichier PDF du wrapper ou du guide

**Solutions** :

**1. Installez un lecteur PDF**
- Adobe Acrobat Reader (gratuit)
- Ou utilisez votre navigateur web

**2. Le fichier n'est pas un PDF**
Les wrappers sont en `.md` (Markdown), pas en PDF.

**3. Ouvrez avec un éditeur de texte**
- Bloc-notes (Windows)
- TextEdit (Mac)
- VS Code
- Tout éditeur de texte fonctionne

---

## 🛡️ Problèmes avec les wrappers

### Je ne trouve pas les fichiers des wrappers

**Symptômes** :
- Je ne sais pas où sont les fichiers `.md`

**Solution** :

**Emplacement** :
```
stone-sea/
  MODULE_01/
    wrappers_markdown/
      wrapper1_contexte_limite.md
      wrapper2_sources_obligatoires.md
      wrapper3_sortie_verifiable.md
      wrapper4_donnees_sensibles.md
      wrapper5_double_raisonnement.md
      wrapper6_journal_sources.md
      wrapper7_tracabilite_citations.md
      wrapper8_controle_normatif_dtu.md
      README.md
```

**Si vous ne les trouvez pas** :
- Vérifiez que vous avez bien téléchargé tout le projet Stone-Sea
- Recherchez "wrapper1" dans l'explorateur de fichiers

---

### Le wrapper donne un résultat bizarre

**Symptômes** :
- Le résultat ne correspond pas à ce que j'attends
- L'IA semble confuse

**Causes et solutions** :

**1. Vous avez modifié le wrapper**
→ Utilisez le wrapper original tel quel

**2. Le document inséré n'est pas au bon endroit**
→ Vérifiez que vous avez remplacé `<<<COLLER ICI...>>>` correctement

**3. Le document est mal formaté**
→ Assurez-vous que le texte est lisible (pas d'images, pas de tableaux cassés)

**4. La demande est ambiguë**
→ Ajoutez des précisions dans votre message

---

### Quel wrapper choisir ?

**Symptômes** :
- Je ne sais pas quel wrapper utiliser

**Solution** : Consultez l'arbre de décision

```
Document avec prix/noms ?
  ├─ OUI → Wrapper 4 en premier
  └─ NON → Suite

Rapport officiel ?
  ├─ OUI → Wrapper 7 + 6
  └─ NON → Suite

Contrôle conformité ?
  ├─ OUI → Wrapper 8
  └─ NON → Suite

Comparaison de solutions ?
  ├─ OUI → Wrapper 5
  └─ NON → Suite

Analyse simple ?
  └─ OUI → Wrapper 1
```

**Voir aussi** : [Guide des wrappers](../02_guides/guide_wrappers.md)

---

## 🎓 Problèmes de compréhension

### Je ne comprends pas un concept

**Symptômes** :
- Un terme n'est pas clair
- Un concept semble flou

**Solutions** :

**1. Consultez les glossaires**
- [Glossaire BTP](glossaire_btp.md) - Termes du BTP
- [Glossaire IA](glossaire_ia.md) - Termes de l'IA

**2. Relisez la section concernée**
Prenez votre temps, relisez plusieurs fois si nécessaire.

**3. Faites une pause**
Parfois, une pause de quelques heures aide à mieux assimiler.

**4. Demandez de l'aide**
- Collègue
- Formateur
- Responsable de formation

---

### Le quiz est trop difficile

**Symptômes** :
- Je n'arrive pas à obtenir 7/10 au quiz

**Solutions** :

**1. Relisez les guides**
Concentrez-vous sur les sections correspondant à vos erreurs.

**2. Refaites les exercices pratiques**
La pratique aide à mieux comprendre.

**3. Prenez votre temps**
Il n'y a pas d'urgence. Apprenez à votre rythme.

**4. Consultez la FAQ**
[FAQ](faq.md) - Questions fréquentes

---

## 💻 Problèmes techniques

### Mon ordinateur est trop lent

**Symptômes** :
- Claude met longtemps à répondre
- L'interface rame

**Solutions** :

**1. Fermez les autres onglets**
Gardez uniquement Claude ouvert.

**2. Vérifiez votre connexion Internet**
Claude a besoin d'une bonne connexion.

**3. Essayez un autre navigateur**
Chrome est généralement le plus rapide.

**4. Redémarrez votre ordinateur**
Parfois, un simple redémarrage suffit.

---

### Je ne peux pas copier-coller

**Symptômes** :
- Ctrl+C / Ctrl+V ne fonctionnent pas

**Solutions** :

**1. Vérifiez votre clavier**
- Windows : Ctrl+C (copier), Ctrl+V (coller)
- Mac : Cmd+C (copier), Cmd+V (coller)

**2. Essayez le clic droit**
Clic droit → Copier / Coller

**3. Redémarrez le navigateur**

---

## 📊 Problèmes de résultats

### Les résultats de l'IA semblent faux

**Symptômes** :
- L'IA cite une norme qui n'existe pas
- Les chiffres semblent incorrects

**⚠️ C'est peut-être une hallucination !**

**Solutions** :

**1. Vérifiez dans les documents sources**
- Consultez le DTU original
- Vérifiez sur le site AFNOR
- Demandez à un expert

**2. Utilisez les wrappers**
Les wrappers réduisent les hallucinations, mais ne les éliminent pas à 100%.

**3. Ne faites JAMAIS confiance aveuglément**
Vérifiez toujours les informations critiques.

---

### L'IA ne détecte pas une erreur évidente

**Symptômes** :
- Il y a clairement une erreur dans le document
- L'IA ne la signale pas

**Explication** :
L'IA peut "louper" des erreurs, surtout si :
- L'erreur est subtile
- Elle nécessite du contexte externe
- Elle nécessite un calcul complexe

**Solution** :
L'IA est un **assistant**, pas un **vérificateur parfait**.
→ La validation humaine reste indispensable !

---

## 🔐 Problèmes de sécurité

### J'ai envoyé un document confidentiel par erreur

**Symptômes** :
- J'ai oublié d'anonymiser
- Le document contenait des données sensibles

**Actions immédiates** :

**1. Supprimez la conversation**
Dans Claude : Supprimez l'historique de cette conversation.

**2. Informez votre responsable**
Selon votre politique de sécurité, informez qui de droit.

**3. Pour l'avenir**
Utilisez TOUJOURS le Wrapper 4 en premier !

---

### Je ne sais pas si mon document contient des données RGPD

**Solution** :

**Utilisez le Wrapper 4** : Il détecte automatiquement :
- Noms et prénoms
- Adresses
- Téléphones
- Emails
- Prix et montants
- Numéros de contrats

**Règle de prudence** :
En cas de doute, anonymisez !

---

## 📞 Où trouver de l'aide supplémentaire ?

### Ressources internes MODULE_00

- [FAQ](faq.md) - Questions fréquentes
- [Glossaire BTP](glossaire_btp.md)
- [Glossaire IA](glossaire_ia.md)
- [Guides](../02_guides/) - Tous les guides du MODULE_00

### Documentation Stone-Sea

- `README.md` - À la racine du projet
- `MODULE_01/wrappers_markdown/README.md`
- READMEs des autres modules

### Aide humaine

- Demandez à un collègue
- Contactez votre formateur
- Contactez le support de votre entreprise

---

## 🆘 Problème non résolu ?

Si votre problème n'est pas dans ce guide :

**1. Décrivez précisément le problème**
- Que vouliez-vous faire ?
- Qu'avez-vous fait exactement ?
- Quel est le résultat obtenu ?
- Quel est le résultat attendu ?

**2. Prenez des captures d'écran**
Cela aide beaucoup à comprendre le problème.

**3. Demandez de l'aide**
- À un collègue
- À un formateur
- Au support

---

**💡 La plupart des problèmes ont une solution simple !**

**Ne restez pas bloqué(e), demandez de l'aide !** 🚀
