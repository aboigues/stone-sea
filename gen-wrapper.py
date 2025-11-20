import os
from datetime import datetime
from textwrap import dedent

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

def wrapper_1() -> str:
    return dedent("""
    # Wrapper 1 — Contexte limité (BTP)

    Objet
    - Limiter strictement l'analyse à l'extrait fourni sans extrapolation.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    Analyse UNIQUEMENT la structure et le contenu de l'extrait fourni ci-dessous.
    NE FAIS AUCUNE HYPOTHÈSE en dehors des sources.
    Tâches:
    - Liste la structure (titres, sections, numéros).
    - Résume en 5 points factuels maximum.
    - Liste les limites et informations manquantes.
    - Signale toute ambiguïté ou incohérence interne.
    Contraintes:
    - Pas de contenu hors source.
    - Pas d'interprétation normative: cite exactement les références visibles (ex: NF DTU 40.21, édition et date si présentes).
    Format de sortie:
    - Sections: Structure / Résumé / Limites / Ambiguïtés.
    Source à analyser:
    <<<COLLER ICI L’EXTRAIT>>>
    ```
    """)

def wrapper_2() -> str:
    return dedent("""
    # Wrapper 2 — Sources obligatoires et datation

    Objet
    - Exiger la présence de sources jointes et la datation/édition des références citées.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    Ne t'appuie QUE sur les documents joints.
    Si une norme, un guide ou un chiffre n'est pas présent dans les pièces: réponds "source manquante".
    Pour chaque référence citée, fournis: titre exact, numéro, édition/version et date (jj/mm/aaaa) si disponibles.
    Tâches:
    - Réponds uniquement avec des éléments présents dans les pièces.
    - Ajoute une table "Références citées" (numéro / titre / édition / date / page).
    - Liste "Sources manquantes" s'il en existe.
    Contraintes:
    - Aucune recherche externe.
    - Aucune paraphrase non vérifiable.
    Format:
    - Réponse
    - Références citées (table)
    - Sources manquantes
    - Hypothèses: aucune
    Pièces:
    <<<INSÉRER ICI LA LISTE DES FICHIERS OU EXTRAITS>>>
    ```
    """)

def wrapper_3() -> str:
    return dedent("""
    # Wrapper 3 — Sortie vérifiable (2 colonnes)

    Objet
    - Produire des propositions contrôlables avec les vérifications nécessaires.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    Produis un tableau à 2 colonnes:
    - Proposition
    - Vérifications nécessaires (référence, page, mesure, interlocuteur)
    Ajoute un paragraphe "Points d'incertitude".
    Contraintes:
    - Chaque proposition doit pointer vers une preuve dans les pièces (ex: NF DTU XX, page Y).
    - Si la preuve est absente: indiquer "source manquante".
    Format:
    | Proposition | Vérifications nécessaires |
    Points d'incertitude:
    - ...
    Sources utilisées: lister précisément les fichiers/pages.
    ```
    """)

def wrapper_4() -> str:
    return dedent("""
    # Wrapper 4 — Données sensibles (refus/alerte)

    Objet
    - Empêcher la fuite d'informations personnelles, de prix ou d'identifiants contractuels.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    Avant de répondre, effectue un contrôle "Données sensibles".
    Si le texte contient:
      - Données personnelles non minimisées (noms, emails, téléphones),
      - Prix, montants, taux non publics,
      - N° marché, contrat, série, immatriculation,
    ALORS: refuse et alerte en listant les éléments à anonymiser et la règle appliquée (RGPD, secret des affaires).
    Sinon: poursuis la tâche demandée.
    Format:
    - Contrôle données sensibles: OK / Refus + liste
    - Réponse (si OK)
    Conseils d’anonymisation:
    - Remplacer noms par [Rôle-Init.], montants par [Classe de prix], identifiants par [ID-XXX].
    ```
    """)

def wrapper_5() -> str:
    return dedent("""
    # Wrapper 5 — Double raisonnement + matrice avantages/risques

    Objet
    - Comparer deux options contradictoires et conclure par une recommandation conditionnelle.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    Tâches:
    - Propose 2 options contradictoires (Option A / Option B) pour le sujet demandé.
    - Dresse une matrice Avantages / Risques / Coûts / Délais / Conformité (DTU/RE2020/contrat).
    - Propose des critères de décision (seuils) et une recommandation conditionnelle.
    Contraintes:
    - Appui sur sources jointes uniquement; citer pages/paragraphes.
    Format:
    Option A:
    - ...
    Option B:
    - ...
    Matrice comparée (table)
    Recommandation conditionnelle:
    - Si [critère], choisir A, sinon B.
    Hypothèses et sources: lister fichier/page.
    ```
    """)

def wrapper_6() -> str:
    return dedent("""
    # Wrapper 6 — Journal des sources (traçabilité)

    Objet
    - Journaliser exactement ce qui a été utilisé et ce qui ne l’a pas été.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    En fin de réponse, fournis un "Journal des sources" avec 2 listes:
    1) Fichiers/sections utilisés (avec pages/chapitres précis).
    2) Fichiers/sections disponibles non utilisés (pour transparence).
    Interdiction d'inventer des sources.
    Format:
    - Réponse
    - Journal des sources:
      - Utilisés: fichier, section, page
      - Non utilisés: fichier, section
    ```
    """)

def wrapper_7() -> str:
    return dedent("""
    # Wrapper 7 — Traçabilité, citations et horodatage

    Objet
    - Assurer un fil d’audit: numérotation des citations, horodatage, empreinte des pièces si disponible.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    Exige:
    - Citations numérotées [1], [2]... placées après les phrases concernées.
    - Pour chaque citation: fichier, section, page, édition/date.
    - Horodatage de la réponse: jj/mm/aaaa HH:MM (heure locale).
    - Si une empreinte (hash) de la pièce est fournie, l’inclure.
    Format:
    - Réponse avec citations [n].
    - Liste des citations:
      [n] fichier — section — page — édition/date — (hash si fourni)
    - Horodatage:
    ```
    """)

def wrapper_8() -> str:
    return dedent("""
    # Wrapper 8 — Contrôle normatif (DTU/Eurocodes) avec édition/date

    Objet
    - Encadrer les vérifications de conformité aux normes métiers.

    Prompt modèle
    ```
    Tu es un assistant BTP.
    But: contrôler un point d'exécution par rapport aux référentiels fournis.
    Règles:
    - Citer pour chaque exigence: numéro de norme (ex: NF DTU 40.21), titre, édition, date et paragraphe.
    - Si l’édition/date n’apparaît pas dans les pièces: marquer "édition/date manquante".
    - Ne jamais substituer une norme non fournie.
    Tâches:
    - Lister exigences applicables.
    - Vérifier la conformité de l'élément étudié.
    - Émettre des écarts classés Majeur / Mineur / Observation.
    Format:
    Exigences (table): Référence | Paragraphe | Intitulé | Édition/Date | Preuve (page)
    Constat de conformité (table): Exigence | Conformité (Oui/Non/NA) | Écart | Action
    Sources: fichiers/pages exacts.
    ```
    """)

def readme(now: str) -> str:
    return dedent(f"""
    # Pack de 8 wrappers IA — BTP (Markdown)
    Généré automatiquement le {now}.

    Contenu
    - Wrapper 1 — Contexte limité
    - Wrapper 2 — Sources obligatoires et datation
    - Wrapper 3 — Sortie vérifiable (2 colonnes)
    - Wrapper 4 — Données sensibles (refus/alerte)
    - Wrapper 5 — Double raisonnement + matrice avantages/risques
    - Wrapper 6 — Journal des sources (traçabilité)
    - Wrapper 7 — Traçabilité, citations et horodatage
    - Wrapper 8 — Contrôle normatif (DTU/Eurocodes)

    Utilisation
    - Copiez-collez le contenu de chaque fichier .md dans votre outil IA.
    - Remplacez les zones <<<...>>> par vos pièces (extraits, listes de fichiers, pages).
    - Exigez toujours l’édition et la date des normes citées (NF DTU, Eurocodes, NF EN, guides).

    Bonnes pratiques
    - Cloisonnez par chantier/lot (RBAC).
    - Activez MFA/SSO et DLP côté outil.
    - Interdisez toute extrapolation hors sources.
    """)

def main():
    out_dir = "wrappers_markdown"
    ensure_dir(out_dir)

    files = {
        "wrapper1_contexte_limite.md": wrapper_1(),
        "wrapper2_sources_obligatoires.md": wrapper_2(),
        "wrapper3_sortie_verifiable.md": wrapper_3(),
        "wrapper4_donnees_sensibles.md": wrapper_4(),
        "wrapper5_double_raisonnement.md": wrapper_5(),
        "wrapper6_journal_sources.md": wrapper_6(),
        "wrapper7_tracabilite_citations.md": wrapper_7(),
        "wrapper8_controle_normatif_dtu.md": wrapper_8(),
        "README.md": readme(datetime.now().strftime("%d/%m/%Y %H:%M"))
    }

    for name, content in files.items():
        write_file(os.path.join(out_dir, name), content)

    print("Fichiers créés dans:", out_dir)
    for name in files:
        print("-", name)

if __name__ == "__main__":
    main()


