@echo off
REM Lancement de l'application web pour générer des CR
REM Double-cliquez sur ce fichier pour démarrer

echo.
echo ========================================
echo   Generateur de CR Chantier - Stone-Sea
echo ========================================
echo.
echo Demarrage de l'application web...
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

pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installation de Flask...
    pip install flask
)

REM Lancement de l'application
echo.
echo ========================================
echo   Application demarree !
echo ========================================
echo.
echo Ouvrez votre navigateur et allez sur:
echo.
echo    http://localhost:5000
echo.
echo Pour arreter l'application: Ctrl+C
echo ========================================
echo.

cd /d "%~dp0"
python webapp_cr_generator.py

pause
