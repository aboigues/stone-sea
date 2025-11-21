# MODULE_07 : Intégration BDNB (Base de Données Nationale des Bâtiments)

## 📋 Vue d'ensemble

Le MODULE_07 permet d'interroger et d'exploiter les données de la **Base de Données Nationale des Bâtiments (BDNB)** développée par le CSTB. Ce référentiel open data contient des informations sur **32 millions de bâtiments** français avec plus de **170 caractéristiques** accessibles librement.

## 🎯 Objectifs

- Récupérer des données de bâtiments existants via l'API Open de la BDNB
- Enrichir les projets BTP avec des informations réglementaires et techniques
- Analyser la performance énergétique des bâtiments
- Évaluer l'exposition aux risques naturels
- Produire des statistiques territoriales

## 🏗️ Structure du module

```
MODULE_07/
├── 01_schemas/                      # Schémas JSON
│   ├── batiment_bdnb.schema.json   # Schéma d'un bâtiment BDNB
│   └── recherche_bdnb.schema.json  # Schéma de résultats de recherche
├── 02_config/                       # Configuration
│   └── bdnb_config.json            # Paramètres API et métadonnées
├── 03_scripts/                      # Scripts Python
│   └── bdnb_api_client.py          # Client API BDNB
├── 04_examples/                     # Exemples d'utilisation
│   └── exemple_recherche.py        # Exemples de recherche et analyse
└── 05_docs/                         # Documentation
    └── README.md                    # Ce fichier
```

## 🚀 Installation et prérequis

### Prérequis
- Python 3.8 ou supérieur
- Aucune dépendance externe (utilise uniquement la bibliothèque standard Python)
- Connexion Internet pour accéder à l'API BDNB

### Installation
Aucune installation spécifique requise. Le module utilise uniquement les bibliothèques standard Python (`json`, `urllib`, `datetime`).

## 📖 Utilisation

### 1. Client API de base

#### Recherche par adresse
```bash
python MODULE_07/03_scripts/bdnb_api_client.py search "10 rue de Rivoli, Paris"
```

#### Récupération d'un bâtiment par ID
```bash
python MODULE_07/03_scripts/bdnb_api_client.py get "BDNB00001234"
```

#### Recherche par coordonnées GPS
```bash
python MODULE_07/03_scripts/bdnb_api_client.py nearby 48.8566 2.3522 500
```

### 2. Utilisation en Python

```python
from bdnb_api_client import BDNBAPIClient

# Initialisation du client
client = BDNBAPIClient()

# Recherche par adresse
results = client.search_by_address("10 rue de Rivoli, Paris", limit=10)

# Récupération des données énergétiques
energy_data = client.get_energy_performance("BDNB00001234")

# Recherche autour de coordonnées
nearby_buildings = client.search_by_coordinates(
    lat=48.8584,
    lon=2.2945,
    radius_m=500,
    limit=20
)

# Export en JSON
client.export_to_json(results, "batiments.json")
```

### 3. Exemples complets

Exécutez le script d'exemples interactif :
```bash
python MODULE_07/04_examples/exemple_recherche.py
```

Ce script propose 4 cas d'usage :
1. **Recherche par adresse** - Trouver des bâtiments à partir d'une adresse
2. **Recherche GPS** - Trouver des bâtiments autour de coordonnées
3. **Performance énergétique** - Analyser le DPE d'un bâtiment
4. **Analyse de lot** - Statistiques sur un groupe de bâtiments

## 📊 Données disponibles

### Informations générales
- Identifiant unique (batiment_id, rnb_id)
- Adresse complète (numéro, voie, code postal, commune, code INSEE)
- Géolocalisation (latitude, longitude, précision)
- Caractéristiques (année construction, nb niveaux, nb logements, surfaces)

### Performance énergétique (DPE)
- Classe énergétique (A à G)
- Consommation (kWh/m²/an)
- Classe GES (A à G)
- Émission GES (kgCO2/m²/an)

### Systèmes techniques
- Type de chauffage
- Eau chaude sanitaire
- Refroidissement
- Ventilation
- Énergies renouvelables

### Exposition aux risques
- Risque d'inondation
- Zone de sismicité
- Potentiel radon

## 🔗 Intégration avec les autres modules Stone-Sea

### MODULE_04 : Production documentaire
- **Enrichissement DQE** : Récupérer les caractéristiques d'un bâtiment existant pour enrichir le DQE
- **CCTP** : Intégrer les données du bâtiment existant dans le CCTP de rénovation

### MODULE_05 : Conformité normative
- **Contrôle RT/RE** : Vérifier la conformité énergétique du bâtiment existant
- **Exigences** : Adapter les exigences selon les caractéristiques du bâtiment

### MODULE_06 : Plan d'essais
- **Historique** : Consulter l'historique des contrôles et essais du bâtiment
- **Planification** : Adapter le plan d'essais selon les caractéristiques existantes

## 🎯 Cas d'usage BTP

### 1. Rénovation énergétique
```python
# Analyser un bâtiment avant travaux de rénovation
building = client.get_building_by_id("BDNB00001234")
energy_data = client.get_energy_performance("BDNB00001234")

# Déterminer les travaux nécessaires selon le DPE actuel
if energy_data['dpe_classe'] in ['F', 'G']:
    print("Rénovation lourde recommandée")
```

### 2. Diagnostic avant travaux
```python
# Rechercher tous les bâtiments d'une copropriété
buildings = client.search_by_address("Résidence Les Jardins, Lyon", limit=50)

# Analyser les risques
for building in buildings:
    if building.get('risques', {}).get('inondation') == 'fort':
        print(f"⚠️ Bâtiment {building['batiment_id']} en zone inondable")
```

### 3. Étude de marché territorial
```python
# Analyser la qualité énergétique d'un quartier
results = client.search_by_coordinates(48.8566, 2.3522, radius_m=1000, limit=100)

dpe_distribution = {}
for building in results:
    dpe = building.get('dpe_classe', 'N/A')
    dpe_distribution[dpe] = dpe_distribution.get(dpe, 0) + 1

print("Distribution des DPE dans le quartier:", dpe_distribution)
```

## 📚 Ressources et références

### Sources officielles BDNB
- **Portail BDNB** : https://bdnb.io/
- **Data.gouv.fr** : https://www.data.gouv.fr/datasets/base-de-donnees-nationale-des-batiments/
- **GitLab** : https://gitlab.com/BDNB/base_nationale_batiment
- **CSTB** : https://www.cstb.fr/bases-donnees/base-donnees-nationale-batiments

### Documentation
- Documentation API : https://bdnb.io/documentation
- Webinaires CSTB : https://formations.cstb.fr/

### Licence
Les données BDNB sont diffusées sous **Licence Ouverte v2.0 (Etalab)** :
- Libre réutilisation (commerciale ou non)
- Attribution obligatoire : "BDNB - CSTB"
- Licence : https://www.etalab.gouv.fr/licence-ouverte-open-licence/

## ⚠️ Notes importantes

### Limitations techniques
- L'API Open a des limites de débit (rate limiting)
- Certaines données détaillées nécessitent l'API Open+ ou Expert
- La géolocalisation peut avoir différents niveaux de précision

### Données et confidentialité
- Les données BDNB sont publiques et open data
- Aucune donnée personnelle n'est contenue dans la BDNB
- Respecter les conditions d'utilisation de la Licence Ouverte

### Mise à jour
- La BDNB est mise à jour **3 fois par an**
- Vérifier la date de récupération des données (`retrieved_at`)
- Les DPE peuvent être obsolètes si le bâtiment a été rénové

## 🔧 Développement et contribution

### Structure des schémas JSON
Les schémas JSON sont conçus pour être compatibles avec les autres modules Stone-Sea :
- Validation automatique des données
- Traçabilité (horodatage, source, licence)
- Interopérabilité avec les modules existants

### Extension du client API
Pour ajouter de nouveaux endpoints ou fonctionnalités :
1. Modifier `bdnb_api_client.py`
2. Ajouter les méthodes dans la classe `BDNBAPIClient`
3. Mettre à jour les schémas JSON si nécessaire
4. Ajouter des exemples dans `exemple_recherche.py`

## 📞 Support et questions

### API BDNB
Pour les questions sur l'API BDNB :
- Consulter la documentation officielle : https://bdnb.io/documentation
- Contacter le CSTB : https://www.cstb.fr/contact

### Module Stone-Sea
Pour les questions sur ce module :
- Consulter le README principal du projet Stone-Sea
- Ouvrir une issue sur le dépôt du projet

---

**Version** : 1.0
**Dernière mise à jour** : 2025-11-21
**Auteur** : Stone-Sea
**Licence module** : [À définir selon le projet Stone-Sea]
