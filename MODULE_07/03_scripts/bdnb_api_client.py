#!/usr/bin/env python3
"""
Client API pour la Base de Données Nationale des Bâtiments (BDNB)
=================================================================

Ce module permet d'interroger l'API Open de la BDNB du CSTB pour récupérer
des informations sur les bâtiments français.

API Documentation: https://bdnb.io/
Data Portal: https://www.data.gouv.fr/datasets/base-de-donnees-nationale-des-batiments/

Auteur: Stone-Sea
Date: 2025-11-21
"""

import json
import sys
import urllib.request
import urllib.parse
import urllib.error
from typing import Dict, List, Optional, Any
from datetime import datetime


class BDNBAPIClient:
    """Client pour interroger l'API Open de la BDNB."""

    def __init__(self, api_base_url: str = "https://bdnb.io/api/v1"):
        """
        Initialise le client API BDNB.

        Args:
            api_base_url: URL de base de l'API BDNB (par défaut: API Open)
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.session_start = datetime.now().isoformat()

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Effectue une requête HTTP GET vers l'API.

        Args:
            endpoint: Endpoint de l'API (ex: "/buildings")
            params: Paramètres de requête optionnels

        Returns:
            Réponse JSON désérialisée

        Raises:
            Exception: En cas d'erreur HTTP ou de parsing JSON
        """
        url = f"{self.api_base_url}{endpoint}"

        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"

        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = response.read()
                return json.loads(data.decode('utf-8'))
        except urllib.error.HTTPError as e:
            raise Exception(f"Erreur HTTP {e.code}: {e.reason}")
        except urllib.error.URLError as e:
            raise Exception(f"Erreur de connexion: {e.reason}")
        except json.JSONDecodeError as e:
            raise Exception(f"Erreur de parsing JSON: {e}")

    def search_by_address(self, address: str, limit: int = 10) -> List[Dict]:
        """
        Recherche des bâtiments par adresse.

        Args:
            address: Adresse à rechercher (ex: "10 rue de Rivoli, Paris")
            limit: Nombre maximum de résultats (par défaut: 10)

        Returns:
            Liste de bâtiments correspondants
        """
        params = {
            'address': address,
            'limit': limit
        }

        # Note: L'endpoint exact peut varier selon la version de l'API
        # Cette implémentation est un exemple et devra être adaptée
        # selon la documentation officielle de l'API BDNB
        return self._make_request('/buildings/search', params)

    def get_building_by_id(self, building_id: str) -> Dict:
        """
        Récupère les informations détaillées d'un bâtiment par son ID.

        Args:
            building_id: Identifiant du bâtiment (batiment_id ou rnb_id)

        Returns:
            Informations détaillées du bâtiment
        """
        return self._make_request(f'/buildings/{building_id}')

    def search_by_coordinates(self, lat: float, lon: float,
                             radius_m: int = 100, limit: int = 10) -> List[Dict]:
        """
        Recherche des bâtiments autour de coordonnées GPS.

        Args:
            lat: Latitude (WGS84)
            lon: Longitude (WGS84)
            radius_m: Rayon de recherche en mètres (par défaut: 100m)
            limit: Nombre maximum de résultats (par défaut: 10)

        Returns:
            Liste de bâtiments dans le rayon spécifié
        """
        params = {
            'lat': lat,
            'lon': lon,
            'radius': radius_m,
            'limit': limit
        }
        return self._make_request('/buildings/nearby', params)

    def get_energy_performance(self, building_id: str) -> Dict:
        """
        Récupère les données de performance énergétique d'un bâtiment.

        Args:
            building_id: Identifiant du bâtiment

        Returns:
            Données énergétiques (DPE, étiquette, etc.)
        """
        building_data = self.get_building_by_id(building_id)

        # Extraction des données énergétiques pertinentes
        energy_data = {
            'building_id': building_id,
            'dpe_classe': building_data.get('dpe_classe'),
            'dpe_energie': building_data.get('dpe_energie'),
            'ges_classe': building_data.get('ges_classe'),
            'ges_emission': building_data.get('ges_emission'),
            'annee_construction': building_data.get('annee_construction'),
            'surface_habitable': building_data.get('surface_habitable'),
            'retrieved_at': datetime.now().isoformat()
        }

        return energy_data

    def export_to_json(self, data: Any, output_file: str):
        """
        Exporte les données au format JSON.

        Args:
            data: Données à exporter
            output_file: Chemin du fichier de sortie
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Données exportées vers: {output_file}")


def main():
    """Fonction principale pour utilisation en ligne de commande."""

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python bdnb_api_client.py search <address>")
        print("  python bdnb_api_client.py get <building_id>")
        print("  python bdnb_api_client.py nearby <lat> <lon> [radius_m]")
        print("")
        print("Exemples:")
        print("  python bdnb_api_client.py search '10 rue de Rivoli, Paris'")
        print("  python bdnb_api_client.py get 'BDNB00001234'")
        print("  python bdnb_api_client.py nearby 48.8566 2.3522 500")
        sys.exit(1)

    command = sys.argv[1]
    client = BDNBAPIClient()

    try:
        if command == 'search' and len(sys.argv) >= 3:
            address = sys.argv[2]
            results = client.search_by_address(address)
            print(json.dumps(results, indent=2, ensure_ascii=False))

        elif command == 'get' and len(sys.argv) >= 3:
            building_id = sys.argv[2]
            result = client.get_building_by_id(building_id)
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif command == 'nearby' and len(sys.argv) >= 4:
            lat = float(sys.argv[2])
            lon = float(sys.argv[3])
            radius = int(sys.argv[4]) if len(sys.argv) >= 5 else 100
            results = client.search_by_coordinates(lat, lon, radius)
            print(json.dumps(results, indent=2, ensure_ascii=False))

        else:
            print("❌ Commande invalide")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
