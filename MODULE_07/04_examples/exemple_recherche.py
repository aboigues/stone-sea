#!/usr/bin/env python3
"""
Exemples d'utilisation du client API BDNB
=========================================

Ce script démontre différentes façons d'utiliser le client API BDNB
pour récupérer des informations sur les bâtiments.

Auteur: Stone-Sea
Date: 2025-11-21
"""

import sys
import os
import json
from datetime import datetime

# Ajout du chemin des scripts au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '03_scripts'))

from bdnb_api_client import BDNBAPIClient


def exemple_recherche_adresse():
    """Exemple 1: Recherche de bâtiments par adresse."""
    print("\n" + "="*70)
    print("EXEMPLE 1: Recherche par adresse")
    print("="*70)

    client = BDNBAPIClient()

    # Recherche d'une adresse à Paris
    address = "10 rue de Rivoli, Paris"
    print(f"\n🔍 Recherche de l'adresse: {address}")

    try:
        results = client.search_by_address(address, limit=5)

        print(f"\n✅ {len(results)} résultat(s) trouvé(s)\n")

        for i, building in enumerate(results, 1):
            print(f"Bâtiment #{i}:")
            print(f"  - ID: {building.get('batiment_id', 'N/A')}")
            print(f"  - Adresse: {building.get('adresse', {}).get('voie', 'N/A')}")
            print(f"  - Année construction: {building.get('annee_construction', 'N/A')}")
            print(f"  - DPE: {building.get('dpe_classe', 'N/A')}")
            print()

        # Export en JSON
        output_file = "recherche_adresse.json"
        client.export_to_json(results, output_file)

    except Exception as e:
        print(f"❌ Erreur: {e}")


def exemple_recherche_proximite():
    """Exemple 2: Recherche de bâtiments autour de coordonnées GPS."""
    print("\n" + "="*70)
    print("EXEMPLE 2: Recherche par coordonnées GPS")
    print("="*70)

    client = BDNBAPIClient()

    # Coordonnées de la Tour Eiffel
    lat = 48.8584
    lon = 2.2945
    radius = 500  # 500 mètres

    print(f"\n🔍 Recherche autour de ({lat}, {lon}) dans un rayon de {radius}m")

    try:
        results = client.search_by_coordinates(lat, lon, radius_m=radius, limit=10)

        print(f"\n✅ {len(results)} bâtiment(s) trouvé(s)\n")

        for i, building in enumerate(results, 1):
            coords = building.get('geolocalisation', {})
            print(f"Bâtiment #{i}:")
            print(f"  - ID: {building.get('batiment_id', 'N/A')}")
            print(f"  - Position: ({coords.get('latitude', 'N/A')}, {coords.get('longitude', 'N/A')})")
            print(f"  - Usage: {building.get('usage_principal', 'N/A')}")
            print()

        # Export en JSON
        output_file = "recherche_proximite.json"
        client.export_to_json(results, output_file)

    except Exception as e:
        print(f"❌ Erreur: {e}")


def exemple_performance_energetique():
    """Exemple 3: Récupération de la performance énergétique d'un bâtiment."""
    print("\n" + "="*70)
    print("EXEMPLE 3: Performance énergétique d'un bâtiment")
    print("="*70)

    client = BDNBAPIClient()

    # ID d'exemple (à remplacer par un vrai ID)
    building_id = "BDNB00001234"

    print(f"\n🔍 Récupération des données énergétiques du bâtiment: {building_id}")

    try:
        energy_data = client.get_energy_performance(building_id)

        print("\n✅ Données énergétiques:\n")
        print(f"  - ID Bâtiment: {energy_data.get('building_id')}")
        print(f"  - Classe DPE: {energy_data.get('dpe_classe', 'N/A')}")
        print(f"  - Consommation: {energy_data.get('dpe_energie', 'N/A')} kWh/m²/an")
        print(f"  - Classe GES: {energy_data.get('ges_classe', 'N/A')}")
        print(f"  - Émission GES: {energy_data.get('ges_emission', 'N/A')} kgCO2/m²/an")
        print(f"  - Année construction: {energy_data.get('annee_construction', 'N/A')}")
        print(f"  - Surface habitable: {energy_data.get('surface_habitable', 'N/A')} m²")

        # Export en JSON
        output_file = "performance_energetique.json"
        client.export_to_json(energy_data, output_file)

    except Exception as e:
        print(f"❌ Erreur: {e}")


def exemple_analyse_lot():
    """Exemple 4: Analyse énergétique d'un lot de bâtiments."""
    print("\n" + "="*70)
    print("EXEMPLE 4: Analyse énergétique d'un lot de bâtiments")
    print("="*70)

    client = BDNBAPIClient()

    # Recherche dans une zone
    address = "Rue du Faubourg Saint-Antoine, Paris"
    print(f"\n🔍 Recherche de bâtiments à: {address}")

    try:
        buildings = client.search_by_address(address, limit=20)
        print(f"\n✅ {len(buildings)} bâtiment(s) trouvé(s)")

        # Analyse statistique
        dpe_stats = {}
        total_surface = 0
        nb_with_dpe = 0

        for building in buildings:
            dpe_classe = building.get('dpe_classe', 'N/A')
            if dpe_classe != 'N/A':
                dpe_stats[dpe_classe] = dpe_stats.get(dpe_classe, 0) + 1
                nb_with_dpe += 1

            surface = building.get('surface_habitable', 0)
            if surface:
                total_surface += surface

        print("\n📊 Statistiques énergétiques:")
        print(f"  - Nombre de bâtiments avec DPE: {nb_with_dpe}/{len(buildings)}")
        print(f"  - Surface totale: {total_surface:.0f} m²")
        print(f"\n  Distribution des classes DPE:")

        for classe in sorted(dpe_stats.keys()):
            count = dpe_stats[classe]
            percentage = (count / nb_with_dpe * 100) if nb_with_dpe > 0 else 0
            print(f"    Classe {classe}: {count} ({percentage:.1f}%)")

        # Export du rapport
        rapport = {
            'zone': address,
            'date_analyse': datetime.now().isoformat(),
            'nombre_batiments': len(buildings),
            'nombre_avec_dpe': nb_with_dpe,
            'surface_totale_m2': total_surface,
            'distribution_dpe': dpe_stats,
            'batiments': buildings
        }

        output_file = "analyse_lot.json"
        client.export_to_json(rapport, output_file)

    except Exception as e:
        print(f"❌ Erreur: {e}")


def main():
    """Fonction principale pour exécuter tous les exemples."""
    print("\n" + "="*70)
    print(" Exemples d'utilisation du client API BDNB ".center(70, "="))
    print("="*70)

    print("\n⚠️  NOTE IMPORTANTE:")
    print("Ces exemples utilisent des endpoints et des données fictifs.")
    print("L'API réelle de la BDNB peut avoir une structure différente.")
    print("Consultez la documentation officielle: https://bdnb.io/")

    # Affichage du menu
    print("\n📋 Choisissez un exemple:")
    print("  1. Recherche par adresse")
    print("  2. Recherche par coordonnées GPS")
    print("  3. Performance énergétique d'un bâtiment")
    print("  4. Analyse énergétique d'un lot de bâtiments")
    print("  5. Exécuter tous les exemples")
    print("  0. Quitter")

    try:
        choice = input("\n👉 Votre choix: ").strip()

        if choice == '1':
            exemple_recherche_adresse()
        elif choice == '2':
            exemple_recherche_proximite()
        elif choice == '3':
            exemple_performance_energetique()
        elif choice == '4':
            exemple_analyse_lot()
        elif choice == '5':
            exemple_recherche_adresse()
            exemple_recherche_proximite()
            exemple_performance_energetique()
            exemple_analyse_lot()
        elif choice == '0':
            print("\n👋 Au revoir !")
            return
        else:
            print("\n❌ Choix invalide")
            return

        print("\n" + "="*70)
        print("✅ Exemples terminés avec succès")
        print("="*70 + "\n")

    except KeyboardInterrupt:
        print("\n\n⚠️  Interruption par l'utilisateur")
        sys.exit(0)


if __name__ == '__main__':
    main()
