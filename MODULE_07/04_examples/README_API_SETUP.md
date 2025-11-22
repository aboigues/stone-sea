# Configuration de l'API BDNB - Guide de démarrage

## ⚠️ Information importante

Le client API fourni dans `bdnb_api_client.py` est un **template/exemple** qui doit être adapté avec les endpoints réels de l'API BDNB.

## 🔑 Accès à l'API BDNB

### Tiers d'API disponibles

La BDNB propose 3 niveaux d'accès :

| Tier | Authentification | Requêtes/mois | Requêtes/min | Coût |
|------|------------------|---------------|--------------|------|
| **API Open** | ❌ Aucune | 10 000 | 120/IP | Gratuit |
| **API Open Plus** | ✅ Token | 1 000 000 | 1 200/IP | Sur demande |
| **API Expert** | ✅ Token | 10 000 000 | 1 200/IP | Sur demande |

### Étapes pour démarrer

#### 1. Accéder au portail API
```
https://api-portail.bdnb.io/
```

#### 2. Créer un compte (pour Open Plus et Expert)
- S'inscrire sur le portail
- Demander une clé API
- Attendre la validation

#### 3. Consulter la documentation des endpoints
Une fois connecté au portail, vous aurez accès à :
- La liste complète des endpoints
- Les exemples de requêtes
- Les schémas de réponse
- Les limites de débit

## 🔧 Configuration du client

### 1. Mettre à jour l'URL de base

Dans `bdnb_api_client.py`, ligne ~25 :

```python
def __init__(self, api_base_url: str = "https://api-portail.bdnb.io/v1"):
    # Remplacer par l'URL réelle du portail
    self.api_base_url = api_base_url.rstrip('/')
```

### 2. Ajouter l'authentification (pour Open Plus/Expert)

```python
class BDNBAPIClient:
    def __init__(self, api_base_url: str = "https://api-portail.bdnb.io/v1",
                 api_key: Optional[str] = None):
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        url = f"{self.api_base_url}{endpoint}"

        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"

        # Créer la requête avec authentification
        req = urllib.request.Request(url)

        # Ajouter le header d'authentification si une clé API est fournie
        if self.api_key:
            req.add_header('Authorization', f'Bearer {self.api_key}')
            # ou selon la doc: req.add_header('X-Gravitee-Api-Key', self.api_key)

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                return json.loads(data.decode('utf-8'))
        except urllib.error.HTTPError as e:
            raise Exception(f"Erreur HTTP {e.code}: {e.reason}")
```

### 3. Mettre à jour les endpoints

Consulter la documentation du portail pour les vrais endpoints, par exemple :

```python
# Exemple d'endpoints possibles (à vérifier dans la doc officielle)
def search_by_address(self, address: str, limit: int = 10) -> List[Dict]:
    params = {
        'address': address,
        'limit': limit
    }
    return self._make_request('/buildings/search', params)

def get_building_by_id(self, building_id: str) -> Dict:
    # Peut être /buildings/{id} ou /batiments/{id}
    return self._make_request(f'/buildings/{building_id}')
```

## 📚 Ressources officielles

### Documentation BDNB
- **Portail API** : https://api-portail.bdnb.io/
- **Site officiel** : https://bdnb.io/
- **Documentation services** : https://bdnb.io/services/services_api/
- **Schéma de données** : https://bdnb.io/schema/latest/

### Open Data
- **Data.gouv.fr** : https://www.data.gouv.fr/datasets/base-de-donnees-nationale-des-batiments/
- **GitLab BDNB** : https://gitlab.com/BDNB/base_nationale_batiment

### Support
- **Contact CSTB** : Via le formulaire sur bdnb.io
- **Issues GitLab** : https://gitlab.com/BDNB/base_nationale_batiment/-/issues

## 🧪 Tests de connexion

### Test sans clé API (API Open)

```python
from bdnb_api_client import BDNBAPIClient

# Initialiser le client (API Open)
client = BDNBAPIClient(api_base_url="https://api-portail.bdnb.io/v1")

# Tester une requête simple
try:
    result = client.search_by_address("10 rue de Rivoli, Paris", limit=5)
    print("✅ Connexion réussie")
    print(result)
except Exception as e:
    print(f"❌ Erreur: {e}")
```

### Test avec clé API (Open Plus/Expert)

```python
import os

# Clé API depuis variable d'environnement (recommandé)
api_key = os.environ.get('BDNB_API_KEY')

client = BDNBAPIClient(
    api_base_url="https://api-portail.bdnb.io/v1",
    api_key=api_key
)

try:
    result = client.search_by_address("10 rue de Rivoli, Paris", limit=5)
    print("✅ Connexion avec authentification réussie")
except Exception as e:
    print(f"❌ Erreur: {e}")
```

## 🔒 Sécurité

### Ne jamais committer de clés API

```bash
# .gitignore
*.env
.env.local
bdnb_config_local.json
*_api_key.txt
```

### Utiliser des variables d'environnement

```bash
# .env
BDNB_API_KEY=votre_cle_api_ici
BDNB_API_URL=https://api-portail.bdnb.io/v1
```

```python
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

client = BDNBAPIClient(
    api_base_url=os.getenv('BDNB_API_URL'),
    api_key=os.getenv('BDNB_API_KEY')
)
```

## 📊 Alternative : Utiliser les fichiers téléchargeables

Si l'API n'est pas adaptée à votre cas d'usage, la BDNB propose des téléchargements complets :

### Formats disponibles
- **GeoPackage (GPKG)** : Format géospatial
- **CSV** : Format tabulaire
- **Dump PostgreSQL** : Base de données complète

### Téléchargement
```bash
# Via data.gouv.fr
wget https://www.data.gouv.fr/fr/datasets/r/[resource-id]/download

# Ou via le site BDNB
# https://bdnb.io/ > Télécharger les données
```

### Importation locale
```python
import pandas as pd
import geopandas as gpd

# CSV
df = pd.read_csv('bdnb_open_data.csv')

# GeoPackage
gdf = gpd.read_file('bdnb_open_data.gpkg')

# Filtrer par département, commune, etc.
paris = gdf[gdf['code_insee'].str.startswith('75')]
```

## 🆘 Besoin d'aide ?

1. **Documentation insuffisante** → Contactez le support BDNB via le site
2. **Erreurs d'API** → Vérifiez les issues sur GitLab
3. **Questions techniques** → Utilisez le forum de discussion sur le portail
4. **Demande de fonctionnalité** → Ouvrez une issue sur GitLab

---

**Dernière mise à jour** : 2025-11-21
**Version du module** : 1.0
