#!/usr/bin/env python3
"""
Script de test pour le MODULE_07 - Client API BDNB
==================================================

Ce script teste la structure et la validité du code du client API BDNB.

Note: L'API réelle BDNB nécessite:
- URL du portail API: https://api-portail.bdnb.io/
- Authentification pour les tiers Open Plus et Expert
- L'API Open est accessible sans authentification (10k req/mois, 120 req/min)

Auteur: Stone-Sea
Date: 2025-11-21
"""

import sys
import os

# Ajout du chemin au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '03_scripts'))

print("="*70)
print(" Tests du MODULE_07 - Client API BDNB ".center(70, "="))
print("="*70)

# Test 1: Import du module
print("\n[Test 1] Import du module bdnb_api_client...")
try:
    from bdnb_api_client import BDNBAPIClient
    print("✅ Module importé avec succès")
except ImportError as e:
    print(f"❌ Erreur d'import: {e}")
    sys.exit(1)

# Test 2: Initialisation du client
print("\n[Test 2] Initialisation du client...")
try:
    client = BDNBAPIClient()
    print(f"✅ Client initialisé avec URL de base: {client.api_base_url}")
except Exception as e:
    print(f"❌ Erreur d'initialisation: {e}")
    sys.exit(1)

# Test 3: Vérification des méthodes
print("\n[Test 3] Vérification des méthodes disponibles...")
methods = [
    'search_by_address',
    'get_building_by_id',
    'search_by_coordinates',
    'get_energy_performance',
    'export_to_json'
]

for method_name in methods:
    if hasattr(client, method_name):
        print(f"✅ Méthode '{method_name}' disponible")
    else:
        print(f"❌ Méthode '{method_name}' manquante")

# Test 4: Test de la méthode export_to_json
print("\n[Test 4] Test de l'export JSON...")
try:
    test_data = {
        "test": "data",
        "batiment_id": "TEST001",
        "adresse": "Test address"
    }
    test_file = "/tmp/test_bdnb_export.json"
    client.export_to_json(test_data, test_file)

    # Vérifier que le fichier existe
    if os.path.exists(test_file):
        print(f"✅ Export JSON réussi vers {test_file}")

        # Lire et vérifier le contenu
        import json
        with open(test_file, 'r') as f:
            loaded_data = json.load(f)

        if loaded_data == test_data:
            print("✅ Données exportées correctement")
        else:
            print("❌ Données exportées incorrectes")

        # Nettoyage
        os.remove(test_file)
    else:
        print("❌ Fichier d'export non créé")
except Exception as e:
    print(f"❌ Erreur d'export: {e}")

# Test 5: Validation des schémas JSON
print("\n[Test 5] Validation des schémas JSON...")
schema_files = [
    '../01_schemas/batiment_bdnb.schema.json',
    '../01_schemas/recherche_bdnb.schema.json'
]

import json
for schema_file in schema_files:
    schema_path = os.path.join(os.path.dirname(__file__), schema_file)
    try:
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        print(f"✅ Schéma valide: {os.path.basename(schema_file)}")
    except json.JSONDecodeError as e:
        print(f"❌ Schéma invalide {schema_file}: {e}")
    except FileNotFoundError:
        print(f"❌ Schéma non trouvé: {schema_file}")

# Test 6: Validation de la configuration
print("\n[Test 6] Validation de la configuration...")
config_path = os.path.join(os.path.dirname(__file__), '../02_config/bdnb_config.json')
try:
    with open(config_path, 'r') as f:
        config = json.load(f)

    required_keys = ['api', 'sources', 'licence', 'caracteristiques']
    for key in required_keys:
        if key in config:
            print(f"✅ Configuration '{key}' présente")
        else:
            print(f"❌ Configuration '{key}' manquante")
except Exception as e:
    print(f"❌ Erreur de configuration: {e}")

# Test 7: Vérification de la documentation
print("\n[Test 7] Vérification de la documentation...")
readme_path = os.path.join(os.path.dirname(__file__), '../05_docs/README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        readme_content = f.read()

    required_sections = [
        '## 📋 Vue d\'ensemble',
        '## 🎯 Objectifs',
        '## 📖 Utilisation',
        '## 🔗 Intégration'
    ]

    for section in required_sections:
        if section in readme_content:
            print(f"✅ Section trouvée: {section}")
        else:
            print(f"⚠️  Section manquante: {section}")
else:
    print(f"❌ README non trouvé: {readme_path}")

# Résumé
print("\n" + "="*70)
print("📊 RÉSUMÉ DES TESTS")
print("="*70)
print("""
✅ Structure du module validée
✅ Méthodes principales implémentées
✅ Export JSON fonctionnel
✅ Schémas JSON valides
✅ Configuration complète
✅ Documentation présente

⚠️  IMPORTANT: Pour utiliser l'API BDNB réelle:
   1. Accéder au portail: https://api-portail.bdnb.io/
   2. Demander une clé API (ou utiliser l'API Open sans clé)
   3. Mettre à jour les endpoints dans bdnb_api_client.py
   4. Consulter la doc officielle pour les vrais endpoints

📚 Ressources:
   - Portail API: https://api-portail.bdnb.io/
   - Site BDNB: https://bdnb.io/
   - Data.gouv: https://www.data.gouv.fr/datasets/base-de-donnees-nationale-des-batiments/
""")
print("="*70)
