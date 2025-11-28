#!/usr/bin/env python3
"""
Script CLI interactif pour construire des prompts facilement.

Usage:
    python build_prompt.py
    python build_prompt.py --output mon_prompt.md
    python build_prompt.py --config config.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional

try:
    from prompt_builder import PromptBuilder, list_wrappers, list_prompts, extract_variables
except ImportError:
    print("❌ Erreur: impossible d'importer prompt_builder.py")
    print("Assurez-vous que le fichier prompt_builder.py est dans le même répertoire.")
    sys.exit(1)


def print_header(text: str):
    """Affiche un en-tête."""
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print('=' * 60)


def select_from_list(items: List[str], prompt: str, allow_multiple: bool = False) -> List[str]:
    """
    Affiche une liste d'items et demande à l'utilisateur d'en sélectionner.

    Args:
        items: Liste des items
        prompt: Message pour l'utilisateur
        allow_multiple: Si True, permet de sélectionner plusieurs items

    Returns:
        Liste des items sélectionnés
    """
    if not items:
        print("❌ Aucun item disponible.")
        return []

    print(f"\n{prompt}")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

    if allow_multiple:
        print("\n💡 Entrez les numéros séparés par des virgules (ex: 1,3,5)")
        print("   Ou appuyez sur Entrée pour passer")
    else:
        print("\n💡 Entrez le numéro de votre choix (ou 0 pour passer)")

    while True:
        try:
            user_input = input("Votre choix: ").strip()

            if not user_input or user_input == "0":
                return []

            if allow_multiple:
                indices = [int(x.strip()) - 1 for x in user_input.split(",")]
            else:
                indices = [int(user_input) - 1]

            # Vérifie que tous les indices sont valides
            if all(0 <= idx < len(items) for idx in indices):
                return [items[idx] for idx in indices]
            else:
                print("❌ Numéro(s) invalide(s). Réessayez.")
        except (ValueError, IndexError):
            print("❌ Entrée invalide. Réessayez.")


def select_wrappers() -> List[int]:
    """Demande à l'utilisateur de sélectionner des wrappers."""
    print_header("Sélection des Wrappers")

    wrappers = list_wrappers()
    if not wrappers:
        print("❌ Aucun wrapper trouvé dans MODULE_01/wrappers_markdown/")
        return []

    # Extrait les numéros des wrappers
    wrapper_descriptions = {
        1: "Contexte limité - Pas d'extrapolation",
        2: "Sources obligatoires - Datation/éditions",
        3: "Sortie vérifiable - Tables 2 colonnes",
        4: "Données sensibles - RGPD",
        5: "Double raisonnement - Matrice avantages/risques",
        6: "Journal des sources - Traçabilité complète",
        7: "Traçabilité citations - Citations numérotées",
        8: "Contrôle normatif - DTU/Eurocode"
    }

    items = []
    for i in range(1, 9):
        desc = wrapper_descriptions.get(i, "")
        items.append(f"Wrapper {i}: {desc}")

    selected = select_from_list(items, "Quels wrappers souhaitez-vous utiliser?", allow_multiple=True)

    # Extrait les numéros
    wrapper_ids = []
    for s in selected:
        num = int(s.split()[1].rstrip(":"))
        wrapper_ids.append(num)

    return wrapper_ids


def select_prompt() -> Optional[tuple]:
    """Demande à l'utilisateur de sélectionner un prompt."""
    print_header("Sélection du Prompt")

    # Liste les modules disponibles
    modules = ["MODULE_04", "MODULE_05", "MODULE_06", "MODULE_07"]
    print("\nModules disponibles:")
    for i, mod in enumerate(modules, 1):
        print(f"  {i}. {mod}")

    while True:
        try:
            choice = input("\nSélectionnez un module (1-4): ").strip()
            if not choice:
                return None
            module_idx = int(choice) - 1
            if 0 <= module_idx < len(modules):
                selected_module = modules[module_idx]
                break
            print("❌ Numéro invalide.")
        except ValueError:
            print("❌ Entrée invalide.")

    # Liste les prompts du module
    prompts = list_prompts(selected_module)
    if not prompts:
        print(f"❌ Aucun prompt trouvé dans {selected_module}")
        return None

    selected = select_from_list(prompts, f"\nPrompts disponibles dans {selected_module}:", allow_multiple=False)

    if not selected:
        return None

    return (selected_module, selected[0])


def input_variables(prompt_text: str) -> Dict[str, str]:
    """Demande à l'utilisateur de saisir les variables."""
    print_header("Variables du Prompt")

    variables = extract_variables(prompt_text)

    if not variables:
        print("✅ Aucune variable à remplir dans ce prompt.")
        return {}

    print(f"\n{len(variables)} variable(s) détectée(s):")
    for var in variables:
        print(f"  • {{{var}}}")

    print("\n💡 Entrez les valeurs pour chaque variable (ou laissez vide pour garder {VAR})")

    values = {}
    for var in variables:
        value = input(f"  {{{var}}}: ").strip()
        if value:
            values[var] = value

    return values


def save_config(config: Dict, path: str):
    """Sauvegarde une configuration en JSON."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"✅ Configuration sauvegardée dans {path}")


def load_config(path: str) -> Dict:
    """Charge une configuration depuis un fichier JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def interactive_mode(output_path: Optional[str] = None):
    """Mode interactif principal."""
    print_header("🏗️  Stone-Sea — Générateur de Prompts Interactif")

    print("\n👋 Bienvenue! Ce script va vous guider pour créer votre prompt.")

    # Sélection des wrappers
    wrapper_ids = select_wrappers()

    # Sélection du prompt
    prompt_info = select_prompt()

    if not prompt_info and not wrapper_ids:
        print("\n❌ Aucun wrapper ni prompt sélectionné. Abandon.")
        return

    # Construction du builder
    builder = PromptBuilder()

    if wrapper_ids:
        builder.wrapper(*wrapper_ids)
        print(f"\n✅ {len(wrapper_ids)} wrapper(s) ajouté(s): {wrapper_ids}")

    if prompt_info:
        module, prompt_name = prompt_info
        builder.prompt(module, prompt_name)
        print(f"✅ Prompt ajouté: {module}/{prompt_name}")

    # Aperçu et extraction des variables
    temp_prompt = builder.build(replace_vars=False)
    variables = input_variables(temp_prompt)

    if variables:
        builder.variables(**variables)

    # Construction finale
    print_header("Génération du Prompt")
    final_prompt = builder.build()

    print(f"\n✅ Prompt généré ({len(final_prompt)} caractères)")

    # Sauvegarde ou affichage
    if output_path:
        builder.save(output_path)
        print(f"✅ Prompt sauvegardé dans: {output_path}")
    else:
        save_choice = input("\nSauvegarder dans un fichier? (o/N): ").strip().lower()
        if save_choice == 'o':
            filename = input("Nom du fichier (ex: mon_prompt.md): ").strip()
            if filename:
                builder.save(filename)
                print(f"✅ Prompt sauvegardé dans: {filename}")
            else:
                print("❌ Nom de fichier vide, prompt non sauvegardé.")

    # Option de copie dans le presse-papier (si pyperclip disponible)
    try:
        import pyperclip
        copy_choice = input("\nCopier dans le presse-papier? (o/N): ").strip().lower()
        if copy_choice == 'o':
            pyperclip.copy(final_prompt)
            print("✅ Prompt copié dans le presse-papier!")
    except ImportError:
        print("\n💡 Astuce: installez pyperclip pour copier automatiquement (pip install pyperclip)")

    # Affiche un aperçu
    print("\n" + "─" * 60)
    print("APERÇU DU PROMPT (300 premiers caractères):")
    print("─" * 60)
    print(final_prompt[:300] + "...")
    print("─" * 60)

    # Option pour sauvegarder la config
    save_cfg = input("\nSauvegarder cette configuration pour réutilisation? (o/N): ").strip().lower()
    if save_cfg == 'o':
        cfg_name = input("Nom du fichier de config (ex: config.json): ").strip()
        if cfg_name:
            config = {
                "wrappers": wrapper_ids,
                "module": prompt_info[0] if prompt_info else None,
                "prompt": prompt_info[1] if prompt_info else None,
                "variables": variables
            }
            save_config(config, cfg_name)


def config_mode(config_path: str, output_path: Optional[str] = None):
    """Mode avec fichier de configuration."""
    print_header("Mode Configuration")

    if not Path(config_path).exists():
        print(f"❌ Fichier de configuration introuvable: {config_path}")
        return

    config = load_config(config_path)
    print(f"✅ Configuration chargée depuis: {config_path}")

    builder = PromptBuilder()

    # Wrappers
    if "wrappers" in config and config["wrappers"]:
        builder.wrapper(*config["wrappers"])
        print(f"✅ Wrappers: {config['wrappers']}")

    # Prompt
    if "module" in config and "prompt" in config:
        builder.prompt(config["module"], config["prompt"])
        print(f"✅ Prompt: {config['module']}/{config['prompt']}")

    # Variables
    if "variables" in config and config["variables"]:
        builder.variables(**config["variables"])
        print(f"✅ Variables: {len(config['variables'])} définies")

    # Génération
    final_prompt = builder.build()
    print(f"\n✅ Prompt généré ({len(final_prompt)} caractères)")

    if output_path:
        builder.save(output_path)
        print(f"✅ Sauvegardé dans: {output_path}")
    else:
        print("\n" + "─" * 60)
        print(final_prompt)
        print("─" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Générateur de prompts interactif pour Stone-Sea"
    )
    parser.add_argument(
        "--config", "-c",
        help="Fichier de configuration JSON"
    )
    parser.add_argument(
        "--output", "-o",
        help="Fichier de sortie pour le prompt généré"
    )

    args = parser.parse_args()

    try:
        if args.config:
            config_mode(args.config, args.output)
        else:
            interactive_mode(args.output)

        print("\n✅ Terminé!")

    except KeyboardInterrupt:
        print("\n\n⚠️  Interruption utilisateur. Au revoir!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
