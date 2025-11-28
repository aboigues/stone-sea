#!/usr/bin/env python3
"""
Module de helpers pour faciliter la création de prompts combinant wrappers et sujets.

Usage:
    from prompt_builder import PromptBuilder

    builder = PromptBuilder()
    prompt = builder.wrapper(1).prompt("MODULE_04", "prompt_redaction_cctp").variables({
        "PROJET": "Résidence Les Acacias",
        "LOT": "Couverture"
    }).build()

    print(prompt)
"""

import os
from pathlib import Path
from typing import Dict, List, Optional


class PromptBuilder:
    """Builder pour créer des prompts en combinant wrappers, prompts et variables."""

    def __init__(self, base_dir: Optional[str] = None):
        """
        Initialise le builder.

        Args:
            base_dir: Répertoire racine du projet (détecté automatiquement si None)
        """
        if base_dir is None:
            base_dir = Path(__file__).parent
        self.base_dir = Path(base_dir)

        self._wrappers: List[str] = []
        self._prompts: List[str] = []
        self._variables: Dict[str, str] = {}
        self._separator = "\n\n---\n\n"

    def wrapper(self, *wrapper_ids: int) -> "PromptBuilder":
        """
        Ajoute un ou plusieurs wrappers au prompt.

        Args:
            *wrapper_ids: Numéros des wrappers (1-8)

        Returns:
            self pour chaînage

        Example:
            builder.wrapper(1, 2)  # Ajoute wrapper 1 et 2
        """
        for wid in wrapper_ids:
            if not 1 <= wid <= 8:
                raise ValueError(f"Wrapper ID doit être entre 1 et 8, reçu: {wid}")

            wrapper_path = self.base_dir / "MODULE_01" / "wrappers_markdown" / f"wrapper{wid}_*.md"
            # Cherche le fichier wrapper correspondant
            matches = list(self.base_dir.glob(f"MODULE_01/wrappers_markdown/wrapper{wid}_*.md"))

            if not matches:
                raise FileNotFoundError(f"Wrapper {wid} non trouvé dans MODULE_01/wrappers_markdown/")

            content = matches[0].read_text(encoding="utf-8")
            self._wrappers.append(content)

        return self

    def prompt(self, module: str, prompt_name: str) -> "PromptBuilder":
        """
        Ajoute un prompt spécifique depuis un module.

        Args:
            module: Nom du module (ex: "MODULE_04", "MODULE_05")
            prompt_name: Nom du fichier prompt sans extension (ex: "prompt_redaction_cctp")

        Returns:
            self pour chaînage

        Example:
            builder.prompt("MODULE_04", "prompt_redaction_cctp")
        """
        # Cherche le fichier dans différents sous-répertoires possibles
        search_dirs = ["02_prompts", "04_prompts", "prompts"]

        found = False
        for subdir in search_dirs:
            prompt_path = self.base_dir / module / subdir / f"{prompt_name}.md"
            if prompt_path.exists():
                content = prompt_path.read_text(encoding="utf-8")
                self._prompts.append(content)
                found = True
                break

        if not found:
            raise FileNotFoundError(
                f"Prompt '{prompt_name}.md' non trouvé dans {module}/ "
                f"(cherché dans: {', '.join(search_dirs)})"
            )

        return self

    def custom_prompt(self, prompt_text: str) -> "PromptBuilder":
        """
        Ajoute un prompt personnalisé directement.

        Args:
            prompt_text: Texte du prompt

        Returns:
            self pour chaînage
        """
        self._prompts.append(prompt_text)
        return self

    def variables(self, **vars: str) -> "PromptBuilder":
        """
        Définit les variables à remplacer dans le prompt.

        Args:
            **vars: Variables sous forme clé=valeur

        Returns:
            self pour chaînage

        Example:
            builder.variables(PROJET="Résidence X", LOT="Couverture")
        """
        self._variables.update(vars)
        return self

    def separator(self, sep: str) -> "PromptBuilder":
        """
        Définit le séparateur entre les sections (défaut: \n\n---\n\n).

        Args:
            sep: Chaîne de séparation

        Returns:
            self pour chaînage
        """
        self._separator = sep
        return self

    def build(self, replace_vars: bool = True) -> str:
        """
        Construit le prompt final.

        Args:
            replace_vars: Si True, remplace les variables {VAR} par leurs valeurs

        Returns:
            Prompt complet prêt à être copié
        """
        sections = []

        # Ajoute les wrappers
        if self._wrappers:
            sections.extend(self._wrappers)

        # Ajoute les prompts
        if self._prompts:
            sections.extend(self._prompts)

        # Combine tout
        result = self._separator.join(sections)

        # Remplace les variables
        if replace_vars and self._variables:
            for var_name, var_value in self._variables.items():
                result = result.replace(f"{{{var_name}}}", var_value)

        return result

    def save(self, output_path: str, replace_vars: bool = True) -> str:
        """
        Construit et sauvegarde le prompt dans un fichier.

        Args:
            output_path: Chemin du fichier de sortie
            replace_vars: Si True, remplace les variables

        Returns:
            Le prompt généré
        """
        prompt = self.build(replace_vars=replace_vars)
        Path(output_path).write_text(prompt, encoding="utf-8")
        return prompt

    def reset(self) -> "PromptBuilder":
        """Réinitialise le builder."""
        self._wrappers = []
        self._prompts = []
        self._variables = {}
        return self


# Fonctions helper raccourcies pour un usage rapide

def quick_prompt(wrapper_ids: List[int],
                 module: str,
                 prompt_name: str,
                 **variables) -> str:
    """
    Fonction raccourcie pour créer rapidement un prompt.

    Args:
        wrapper_ids: Liste des wrappers à utiliser (ex: [1, 2])
        module: Module source (ex: "MODULE_04")
        prompt_name: Nom du prompt (ex: "prompt_redaction_cctp")
        **variables: Variables à remplacer

    Returns:
        Prompt complet

    Example:
        prompt = quick_prompt(
            [1, 2],
            "MODULE_04",
            "prompt_redaction_cctp",
            PROJET="Résidence Les Acacias",
            LOT="Couverture"
        )
    """
    builder = PromptBuilder()
    builder.wrapper(*wrapper_ids)
    builder.prompt(module, prompt_name)
    builder.variables(**variables)
    return builder.build()


def list_wrappers(base_dir: Optional[str] = None) -> List[str]:
    """
    Liste tous les wrappers disponibles.

    Returns:
        Liste des chemins des wrappers
    """
    if base_dir is None:
        base_dir = Path(__file__).parent
    base_dir = Path(base_dir)

    wrapper_dir = base_dir / "MODULE_01" / "wrappers_markdown"
    if not wrapper_dir.exists():
        return []

    return sorted([f.name for f in wrapper_dir.glob("wrapper*.md")])


def list_prompts(module: str, base_dir: Optional[str] = None) -> List[str]:
    """
    Liste tous les prompts disponibles dans un module.

    Args:
        module: Nom du module (ex: "MODULE_04")

    Returns:
        Liste des noms de prompts
    """
    if base_dir is None:
        base_dir = Path(__file__).parent
    base_dir = Path(base_dir)

    results = []
    search_dirs = ["02_prompts", "04_prompts", "prompts"]

    for subdir in search_dirs:
        prompt_dir = base_dir / module / subdir
        if prompt_dir.exists():
            results.extend([f.stem for f in prompt_dir.glob("*.md")])

    return sorted(set(results))


def extract_variables(prompt_text: str) -> List[str]:
    """
    Extrait toutes les variables {VAR} présentes dans un prompt.

    Args:
        prompt_text: Texte du prompt

    Returns:
        Liste des noms de variables trouvées
    """
    import re
    matches = re.findall(r'\{([A-Z_][A-Z0-9_/]*)\}', prompt_text)
    return sorted(set(matches))


if __name__ == "__main__":
    # Exemple d'utilisation
    print("=== Exemple d'utilisation du PromptBuilder ===\n")

    print("1. Wrappers disponibles:")
    for w in list_wrappers():
        print(f"   - {w}")

    print("\n2. Prompts MODULE_04:")
    for p in list_prompts("MODULE_04"):
        print(f"   - {p}")

    print("\n3. Construction d'un prompt:")
    builder = PromptBuilder()
    prompt = builder.wrapper(1).prompt("MODULE_04", "prompt_redaction_cctp").variables(
        PROJET="Résidence Les Acacias",
        LOT="Couverture",
        LOTS="Couverture, Maçonnerie, Électricité"
    ).build()

    print(f"Taille du prompt généré: {len(prompt)} caractères")
    print(f"\nPremiers 500 caractères:\n{prompt[:500]}...")
