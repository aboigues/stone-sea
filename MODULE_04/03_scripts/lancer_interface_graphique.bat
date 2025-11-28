@echo off
REM Lancement de l'interface graphique pour générer des CR
REM Double-cliquez sur ce fichier pour démarrer

echo.
echo ========================================
echo   Generateur de CR Chantier - Stone-Sea
echo   Interface Graphique
echo ========================================
echo.

REM Vérification de Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou pas dans le PATH
    echo.
    echo Telechargez Python sur: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Installation des dépendances si nécessaire
echo Verification des dependances...
pip show python-docx >nul 2>&1
if errorlevel 1 (
    echo Installation de python-docx...
    pip install python-docx
)

REM Lancement de l'interface graphique
echo Lancement de l'interface graphique...
echo.

cd /d "%~dp0"
python gui_cr_generator.py

pause
