#!/usr/bin/env python3
"""
Script d'anonymisation pour documents BTP
Conforme RGPD et secret des affaires
"""
import re
import sys
import json
import yaml
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime


class AnonymizerBTP:
    """Anonymiseur de documents BTP avec patterns spécialisés"""

    def __init__(self, rules_path: str = None):
        """
        Initialise l'anonymiseur avec les règles de configuration

        Args:
            rules_path: Chemin vers le fichier de règles YAML (optionnel)
        """
        self.rules = self._load_rules(rules_path) if rules_path else {}
        self.stats = {
            'total_redactions': 0,
            'by_category': {}
        }

        # Patterns d'anonymisation par catégorie
        self.patterns = {
            'plaques': [
                r'\b[0-9]{2}\s?[A-Z]{2}\s?[0-9]{3}\b',  # AA-123-BB
                r'\b[A-Z]{2}[-\s]?\d{3}[-\s]?[A-Z]{2}\b'  # Format ancien
            ],
            'dates': [
                r'\b\d{2}/\d{2}/\d{4}\b',  # JJ/MM/AAAA
                r'\b\d{4}-\d{2}-\d{2}\b'   # AAAA-MM-JJ
            ],
            'emails': [
                r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            ],
            'telephones': [
                r'\b(?:0|\+33)[1-9](?:\s?\d{2}){4}\b',  # 06 12 34 56 78
                r'\b0[1-9](?:\d{2}){4}\b'                # 0612345678
            ],
            'siret_siren': [
                r'\b\d{14}\b',  # SIRET (14 chiffres)
                r'\b\d{9}\b'    # SIREN (9 chiffres) - peut être trop général
            ],
            'montants': [
                r'(?i)(?:montant|prix|coût|budget)\s*:?\s*\d+[\s\d]*(?:€|EUR|euros?)',
                r'\d+[\s\d]*\s*(?:€|EUR)\s*(?:HT|TTC)',
                r'\b\d{1,3}(?:\s?\d{3})*(?:[,.]\d{2})?\s*€\b'
            ],
            'num_marche': [
                r'(?i)(?:marché|contrat|commande|affaire)\s*(?:n°|numero|#)\s*[A-Z0-9/-]+',
                r'\bMAR-\d{4}-\d+\b',
                r'\bCONT-\d{4}-\d+\b'
            ],
            'pii_noms': [
                r'(?i)(?:nom|prénom|prenom)\s*:?\s*[A-Z][a-zéèêëàâäôöûüç-]+(?:\s+[A-Z][a-zéèêëàâäôöûüç-]+)*',
                r'(?i)(?:m\.|mme|mlle|mr|monsieur|madame)\s+[A-Z][a-zéèêëàâäôöûüç-]+(?:\s+[A-Z][a-zéèêëàâäôöûüç-]+)*'
            ],
            'pii_general': [
                r'(?i)(?:email|tél|téléphone|tel|telephone|mobile)\s*:?\s*.+?(?=\n|$)',
                r'(?i)adresse\s*:?\s*.+?(?=\n|$)'
            ],
            'iban': [
                r'\b[A-Z]{2}\d{2}\s?(?:\d{4}\s?){4,7}\d{1,4}\b'
            ],
            'secu_sociale': [
                r'\b[12]\s?\d{2}\s?\d{2}\s?\d{2}\s?\d{3}\s?\d{3}\s?\d{2}\b'
            ]
        }

        # Règles de remplacement par catégorie
        self.replacements = {
            'plaques': '[PLAQUE-XXX]',
            'dates': '[DATE]',
            'emails': '[EMAIL]',
            'telephones': '[TEL]',
            'siret_siren': '[SIRET]',
            'montants': '[MONTANT]',
            'num_marche': '[MARCHE-XXX]',
            'pii_noms': '[NOM]',
            'pii_general': '[INFO-PERSONNELLE]',
            'iban': '[IBAN]',
            'secu_sociale': '[NUM-SECU]'
        }

    def _load_rules(self, rules_path: str) -> dict:
        """Charge les règles depuis un fichier YAML"""
        try:
            with open(rules_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Avertissement: impossible de charger les règles {rules_path}: {e}")
            return {}

    def anonymize_text(self, text: str, categories: List[str] = None) -> Tuple[str, Dict]:
        """
        Anonymise le texte selon les catégories spécifiées

        Args:
            text: Texte à anonymiser
            categories: Liste des catégories à appliquer (None = toutes)

        Returns:
            Tuple (texte anonymisé, statistiques)
        """
        result = text
        self.stats = {'total_redactions': 0, 'by_category': {}}

        # Détermine les catégories à appliquer
        categories_to_apply = categories if categories else self.patterns.keys()

        for category in categories_to_apply:
            if category not in self.patterns:
                continue

            patterns = self.patterns[category]
            replacement = self.replacements.get(category, '[ANON]')
            category_count = 0

            for pattern in patterns:
                matches = re.findall(pattern, result, re.MULTILINE)
                count = len(matches)
                if count > 0:
                    result = re.sub(pattern, replacement, result, flags=re.MULTILINE)
                    category_count += count

            if category_count > 0:
                self.stats['by_category'][category] = category_count
                self.stats['total_redactions'] += category_count

        return result, self.stats

    def anonymize_file(self, input_path: str, output_path: str,
                       categories: List[str] = None,
                       generate_report: bool = True) -> Dict:
        """
        Anonymise un fichier et génère optionnellement un rapport

        Args:
            input_path: Chemin du fichier source
            output_path: Chemin du fichier anonymisé
            categories: Catégories à appliquer (None = toutes)
            generate_report: Génère un rapport JSON des anonymisations

        Returns:
            Statistiques d'anonymisation
        """
        # Lecture du fichier source
        input_file = Path(input_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Fichier introuvable: {input_path}")

        text = input_file.read_text(encoding='utf-8', errors='ignore')

        # Anonymisation
        anonymized_text, stats = self.anonymize_text(text, categories)

        # Écriture du fichier anonymisé
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(anonymized_text, encoding='utf-8')

        # Génération du rapport
        if generate_report:
            report = {
                'timestamp': datetime.now().isoformat(),
                'input_file': str(input_path),
                'output_file': str(output_path),
                'statistics': stats,
                'categories_applied': list(categories) if categories else list(self.patterns.keys())
            }
            report_path = output_file.with_suffix('.anonymization_report.json')
            with open(report_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            print(f"✓ Rapport d'anonymisation: {report_path}")

        return stats

    def print_stats(self, stats: Dict):
        """Affiche les statistiques d'anonymisation"""
        print(f"\n{'='*60}")
        print(f"RAPPORT D'ANONYMISATION")
        print(f"{'='*60}")
        print(f"Total de redactions: {stats['total_redactions']}")

        if stats['by_category']:
            print(f"\nDétail par catégorie:")
            for category, count in sorted(stats['by_category'].items()):
                print(f"  - {category:20s}: {count:4d} occurrence(s)")
        else:
            print("\n✓ Aucune donnée sensible détectée")
        print(f"{'='*60}\n")


def main():
    """Point d'entrée principal"""
    if len(sys.argv) < 3:
        print("Usage: python anonymize.py <input_file> <output_file> [rules.yaml]")
        print("\nExemple:")
        print("  python anonymize.py document.md document_anon.md")
        print("  python anonymize.py document.md document_anon.md anonymisation_rules.yaml")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    rules_path = sys.argv[3] if len(sys.argv) > 3 else None

    # Initialisation de l'anonymiseur
    anonymizer = AnonymizerBTP(rules_path)

    # Anonymisation
    print(f"Anonymisation de: {input_path}")
    try:
        stats = anonymizer.anonymize_file(input_path, output_path, generate_report=True)
        anonymizer.print_stats(stats)
        print(f"✓ Fichier anonymisé créé: {output_path}")
    except Exception as e:
        print(f"✗ Erreur lors de l'anonymisation: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
