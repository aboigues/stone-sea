#!/bin/bash
# Lancement de l'application web pour générer des CR
# Double-cliquez sur ce fichier pour démarrer (ou ./lancer_application_web.sh)

echo ""
echo "========================================"
echo "  Générateur de CR Chantier - Stone-Sea"
echo "========================================"
echo ""
echo "Démarrage de l'application web..."
echo ""

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "[ERREUR] Python 3 n'est pas installé"
    echo ""
    echo "Installez Python 3:"
    echo "  - Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  - MacOS: brew install python3"
    echo ""
    exit 1
fi

# Installation des dépendances si nécessaire
echo "Vérification des dépendances..."

if ! python3 -c "import docx" &> /dev/null; then
    echo "Installation de python-docx..."
    pip3 install python-docx
fi

if ! python3 -c "import flask" &> /dev/null; then
    echo "Installation de Flask..."
    pip3 install flask
fi

# Lancement de l'application
echo ""
echo "========================================"
echo "  Application démarrée !"
echo "========================================"
echo ""
echo "Ouvrez votre navigateur et allez sur:"
echo ""
echo "   http://localhost:5000"
echo ""
echo "Pour arrêter l'application: Ctrl+C"
echo "========================================"
echo ""

cd "$(dirname "$0")"
python3 webapp_cr_generator.py
