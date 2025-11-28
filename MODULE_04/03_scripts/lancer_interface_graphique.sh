#!/bin/bash
# Lancement de l'interface graphique pour générer des CR
# Double-cliquez sur ce fichier pour démarrer (ou ./lancer_interface_graphique.sh)

echo ""
echo "========================================"
echo "  Générateur de CR Chantier - Stone-Sea"
echo "  Interface Graphique"
echo "========================================"
echo ""

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "[ERREUR] Python 3 n'est pas installé"
    echo ""
    echo "Installez Python 3:"
    echo "  - Ubuntu/Debian: sudo apt install python3 python3-pip python3-tk"
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

# Vérification de tkinter
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "[ERREUR] Tkinter n'est pas installé"
    echo "  - Ubuntu/Debian: sudo apt install python3-tk"
    echo "  - MacOS: Inclus avec Python 3"
    exit 1
fi

# Lancement de l'interface graphique
echo "Lancement de l'interface graphique..."
echo ""

cd "$(dirname "$0")"
python3 gui_cr_generator.py
