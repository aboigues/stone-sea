#!/usr/bin/env python3
# demo_generation_docx.py
# Script de démonstration de la génération de documents .docx

import os
import sys
import subprocess

def print_separator():
    print("\n" + "="*70)

def run_command(cmd, description):
    """Exécute une commande et affiche le résultat."""
    print(f"\n🔹 {description}")
    print(f"   Commande: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {result.stdout.strip()}")
            return True
        else:
            print(f"   ❌ Erreur: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False

def check_dependencies():
    """Vérifie que python-docx est installé."""
    print("🔍 Vérification des dépendances...")
    try:
        import docx
        print("   ✅ python-docx installé")
        return True
    except ImportError:
        print("   ❌ python-docx non installé")
        print("\n   Installation nécessaire:")
        print("   pip install python-docx")
        return False

def main():
    print_separator()
    print("   DÉMONSTRATION - Génération de documents .docx")
    print("   Stone-Sea MODULE_04")
    print_separator()

    # Vérifie les dépendances
    if not check_dependencies():
        print("\n⚠️  Installation requise avant de continuer.")
        sys.exit(1)

    # Chemins
    script_dir = os.path.dirname(os.path.abspath(__file__))
    modeles_dir = os.path.join(script_dir, "../04_modeles")
    examples_dir = os.path.join(script_dir, "../06_examples")
    output_dir = os.path.join(script_dir, "../07_output_docx")

    # Crée le dossier de sortie si nécessaire
    os.makedirs(output_dir, exist_ok=True)

    # Fichiers
    template_file = os.path.join(modeles_dir, "cr_template.docx")
    example_json = os.path.join(examples_dir, "cr_exemple.json")
    output_template_based = os.path.join(output_dir, "cr_avec_template.docx")
    output_programmatic = os.path.join(output_dir, "cr_programmatique.docx")

    print("\n📁 Configuration:")
    print(f"   Scripts:   {script_dir}")
    print(f"   Modèles:   {modeles_dir}")
    print(f"   Exemples:  {examples_dir}")
    print(f"   Sortie:    {output_dir}")

    print_separator()
    print("ÉTAPE 1 : Création du template .docx")
    print_separator()

    success = run_command(
        f"cd '{script_dir}' && python create_cr_template.py '{template_file}'",
        "Génération du template CR avec marqueurs {{variable}}"
    )

    if not success:
        print("\n⚠️  Impossible de créer le template. Vérifiez l'installation.")
        sys.exit(1)

    print_separator()
    print("ÉTAPE 2 : Génération avec TEMPLATE (méthode 1)")
    print_separator()

    success = run_command(
        f"cd '{script_dir}' && python cr_json_to_docx.py '{example_json}' '{output_template_based}' --template '{template_file}'",
        "Génération du CR en remplissant le template"
    )

    print_separator()
    print("ÉTAPE 3 : Génération PROGRAMMATIQUE (méthode 2)")
    print_separator()

    success = run_command(
        f"cd '{script_dir}' && python cr_json_to_docx.py '{example_json}' '{output_programmatic}'",
        "Génération du CR de manière programmatique (avec mise en forme avancée)"
    )

    print_separator()
    print("RÉSULTATS")
    print_separator()

    print("\n📄 Fichiers générés:")

    files_to_check = [
        (template_file, "Template .docx avec marqueurs"),
        (output_template_based, "CR généré avec template"),
        (output_programmatic, "CR généré programmatiquement")
    ]

    for filepath, description in files_to_check:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"   ✅ {description}")
            print(f"      Fichier: {filepath}")
            print(f"      Taille:  {size:,} octets")
        else:
            print(f"   ❌ {description} - NON CRÉÉ")

    print_separator()
    print("COMPARAISON DES MÉTHODES")
    print_separator()

    print("""
┌─────────────────────────┬──────────────────────┬──────────────────────┐
│ Critère                 │ Méthode Template     │ Méthode Program.     │
├─────────────────────────┼──────────────────────┼──────────────────────┤
│ Facilité d'utilisation  │ ⭐⭐⭐⭐⭐           │ ⭐⭐⭐              │
│ Flexibilité             │ ⭐⭐                 │ ⭐⭐⭐⭐⭐           │
│ Mise en forme avancée   │ ⭐⭐                 │ ⭐⭐⭐⭐⭐           │
│ Tableaux dynamiques     │ ⭐                   │ ⭐⭐⭐⭐⭐           │
│ Images                  │ ❌                   │ ✅                   │
│ Couleurs conditionnelles│ ❌                   │ ✅                   │
│ Maintenance             │ ⭐⭐⭐⭐⭐           │ ⭐⭐⭐              │
└─────────────────────────┴──────────────────────┴──────────────────────┘

💡 Recommandations:
   • Documents simples, structure fixe → Méthode TEMPLATE
   • Documents complexes, tableaux dynamiques → Méthode PROGRAMMATIQUE
   • Avec photos/images → Méthode PROGRAMMATIQUE
   • Mise en forme conditionnelle → Méthode PROGRAMMATIQUE
    """)

    print_separator()
    print("PROCHAINES ÉTAPES")
    print_separator()

    print("""
1. Ouvrir les documents générés dans Word/LibreOffice :
   - {0}
   - {1}

2. Comparer les deux méthodes

3. Adapter à vos besoins:
   - Modifier le template dans Word
   - Personnaliser le script programmatique

4. Intégrer dans votre workflow:
   - Validation JSON
   - Génération batch
   - Archivage automatique

📚 Documentation complète:
   MODULE_04/05_docs/generation_docx.md
    """.format(output_template_based, output_programmatic))

    print_separator()
    print("✅ Démonstration terminée avec succès!")
    print_separator()

if __name__ == "__main__":
    main()
