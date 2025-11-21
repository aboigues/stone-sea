#!/usr/bin/env python3
"""
Script de vérification post-anonymisation
Détecte les fuites potentielles de données sensibles
Conforme RGPD et secret des affaires
"""
import re
import sys
import json
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime


class AnonymizationVerifier:
    """Vérificateur de données sensibles résiduelles"""

    def __init__(self):
        """Initialise le vérificateur avec les patterns de détection"""

        # Patterns de détection (plus stricts que l'anonymisation)
        self.detection_patterns = {
            'emails': {
                'pattern': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
                'severity': 'HIGH',
                'category': 'RGPD - Données personnelles'
            },
            'telephones_fr': {
                'pattern': r'\b(?:0|\+33)[1-9](?:\s?\d{2}){4}\b',
                'severity': 'HIGH',
                'category': 'RGPD - Données personnelles'
            },
            'telephones_compact': {
                'pattern': r'\b0[1-9]\d{8}\b',
                'severity': 'HIGH',
                'category': 'RGPD - Données personnelles'
            },
            'siret': {
                'pattern': r'\b\d{14}\b',
                'severity': 'MEDIUM',
                'category': 'Secret des affaires'
            },
            'iban': {
                'pattern': r'\b[A-Z]{2}\d{2}\s?(?:\d{4}\s?){4,7}\d{1,4}\b',
                'severity': 'HIGH',
                'category': 'RGPD - Données bancaires'
            },
            'secu_sociale': {
                'pattern': r'\b[12]\s?\d{2}\s?\d{2}\s?\d{2}\s?\d{3}\s?\d{3}\s?\d{2}\b',
                'severity': 'HIGH',
                'category': 'RGPD - Données de santé'
            },
            'prix_euros': {
                'pattern': r'\b\d{1,3}(?:\s?\d{3})+(?:[,.]\d{2})?\s*€\b',
                'severity': 'MEDIUM',
                'category': 'Secret des affaires - Prix'
            },
            'montants_contexte': {
                'pattern': r'(?i)(?:montant|prix|coût|budget)\s*:?\s*\d+[\s\d]*(?:€|EUR)',
                'severity': 'HIGH',
                'category': 'Secret des affaires - Montants'
            },
            'noms_propres': {
                'pattern': r'(?i)(?:m\.|mme|mlle|mr|monsieur|madame)\s+[A-Z][a-zéèêëàâäôöûüç]{2,}',
                'severity': 'MEDIUM',
                'category': 'RGPD - Identité'
            },
            'plaques_immat': {
                'pattern': r'\b[A-Z]{2}[-\s]?\d{3}[-\s]?[A-Z]{2}\b',
                'severity': 'LOW',
                'category': 'RGPD - Véhicules'
            }
        }

        # Patterns à ignorer (références techniques légitimes)
        self.whitelist_patterns = [
            r'NF DTU.*',
            r'EN \d+.*',
            r'AT \d{2}-\d+',
            r'DTU \d+\.\d+',
            r'C\d+/\d+',
            r'ISO \d+',
            r'AFNOR.*'
        ]

        self.findings = []

    def is_whitelisted(self, text: str, context: str) -> bool:
        """
        Vérifie si le texte correspond à un pattern autorisé

        Args:
            text: Texte détecté
            context: Contexte (ligne complète)

        Returns:
            True si le texte est dans la whitelist
        """
        for pattern in self.whitelist_patterns:
            if re.search(pattern, context, re.IGNORECASE):
                return True
        return False

    def verify_file(self, file_path: str) -> Tuple[bool, List[Dict]]:
        """
        Vérifie un fichier pour détecter des données sensibles

        Args:
            file_path: Chemin du fichier à vérifier

        Returns:
            Tuple (is_clean, findings_list)
        """
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"Fichier introuvable: {file_path}")

        content = file.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')

        self.findings = []

        for line_num, line in enumerate(lines, 1):
            for detection_name, detection_info in self.detection_patterns.items():
                pattern = detection_info['pattern']
                matches = re.finditer(pattern, line, re.MULTILINE | re.IGNORECASE)

                for match in matches:
                    matched_text = match.group()

                    # Vérifie la whitelist
                    if self.is_whitelisted(matched_text, line):
                        continue

                    # Ajoute le finding
                    finding = {
                        'type': detection_name,
                        'category': detection_info['category'],
                        'severity': detection_info['severity'],
                        'line_number': line_num,
                        'matched_text': matched_text,
                        'context': line.strip()[:100]  # Limite à 100 caractères
                    }
                    self.findings.append(finding)

        is_clean = len(self.findings) == 0
        return is_clean, self.findings

    def generate_report(self, file_path: str, is_clean: bool,
                       findings: List[Dict], output_format: str = 'json') -> str:
        """
        Génère un rapport de vérification

        Args:
            file_path: Fichier vérifié
            is_clean: Résultat global
            findings: Liste des détections
            output_format: Format de sortie (json, text)

        Returns:
            Chemin du fichier de rapport
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'file_path': str(file_path),
            'is_clean': is_clean,
            'total_findings': len(findings),
            'findings': findings,
            'severity_summary': self._get_severity_summary(findings)
        }

        # Sauvegarde JSON
        report_path = Path(file_path).with_suffix('.verification_report.json')
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Génère aussi un rapport texte
        text_report_path = Path(file_path).with_suffix('.verification_report.txt')
        with open(text_report_path, 'w', encoding='utf-8') as f:
            f.write(self._format_text_report(report))

        return str(report_path)

    def _get_severity_summary(self, findings: List[Dict]) -> Dict:
        """Compte les findings par niveau de sévérité"""
        summary = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
        for finding in findings:
            severity = finding.get('severity', 'MEDIUM')
            summary[severity] = summary.get(severity, 0) + 1
        return summary

    def _format_text_report(self, report: Dict) -> str:
        """Formate le rapport en texte lisible"""
        lines = []
        lines.append("=" * 70)
        lines.append("RAPPORT DE VÉRIFICATION D'ANONYMISATION")
        lines.append("=" * 70)
        lines.append(f"Fichier: {report['file_path']}")
        lines.append(f"Date: {report['timestamp']}")
        lines.append(f"Statut: {'✓ CONFORME' if report['is_clean'] else '✗ NON-CONFORME'}")
        lines.append(f"Total détections: {report['total_findings']}")
        lines.append("")

        if report['total_findings'] > 0:
            summary = report['severity_summary']
            lines.append("Résumé par sévérité:")
            lines.append(f"  - HAUTE:   {summary.get('HIGH', 0)}")
            lines.append(f"  - MOYENNE: {summary.get('MEDIUM', 0)}")
            lines.append(f"  - BASSE:   {summary.get('LOW', 0)}")
            lines.append("")
            lines.append("-" * 70)
            lines.append("DÉTAIL DES DÉTECTIONS")
            lines.append("-" * 70)

            for i, finding in enumerate(report['findings'], 1):
                lines.append(f"\n[{i}] {finding['type'].upper()}")
                lines.append(f"    Catégorie: {finding['category']}")
                lines.append(f"    Sévérité:  {finding['severity']}")
                lines.append(f"    Ligne:     {finding['line_number']}")
                lines.append(f"    Détecté:   {finding['matched_text']}")
                lines.append(f"    Contexte:  {finding['context']}")
        else:
            lines.append("✓ Aucune donnée sensible détectée")

        lines.append("")
        lines.append("=" * 70)
        return "\n".join(lines)

    def print_findings(self, findings: List[Dict]):
        """Affiche les findings dans la console"""
        if not findings:
            print("\n✓ Aucune donnée sensible détectée - Document conforme")
            return

        print(f"\n✗ {len(findings)} donnée(s) sensible(s) détectée(s):\n")

        # Groupe par sévérité
        by_severity = {'HIGH': [], 'MEDIUM': [], 'LOW': []}
        for finding in findings:
            severity = finding.get('severity', 'MEDIUM')
            by_severity[severity].append(finding)

        for severity in ['HIGH', 'MEDIUM', 'LOW']:
            items = by_severity[severity]
            if not items:
                continue

            symbol = '⚠️' if severity == 'HIGH' else '⚡' if severity == 'MEDIUM' else 'ℹ️'
            print(f"{symbol} Sévérité {severity}: {len(items)} détection(s)")

            for finding in items[:5]:  # Limite à 5 par sévérité
                print(f"  Ligne {finding['line_number']:4d} | {finding['type']:20s} | {finding['matched_text']}")

            if len(items) > 5:
                print(f"  ... et {len(items) - 5} autre(s)")
            print()


def main():
    """Point d'entrée principal"""
    if len(sys.argv) < 2:
        print("Usage: python verify_anonymization.py <file_path>")
        print("\nExemple:")
        print("  python verify_anonymization.py document_anonymise.md")
        sys.exit(1)

    file_path = sys.argv[1]

    # Vérification
    verifier = AnonymizationVerifier()
    print(f"Vérification de: {file_path}")
    print("-" * 60)

    try:
        is_clean, findings = verifier.verify_file(file_path)

        # Affiche les résultats
        verifier.print_findings(findings)

        # Génère le rapport
        report_path = verifier.generate_report(file_path, is_clean, findings)
        print(f"✓ Rapport généré: {report_path}")
        print(f"✓ Rapport texte: {Path(report_path).with_suffix('.txt')}")

        # Code de sortie
        sys.exit(0 if is_clean else 1)

    except Exception as e:
        print(f"✗ Erreur lors de la vérification: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
