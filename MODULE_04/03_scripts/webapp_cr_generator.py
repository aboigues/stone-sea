#!/usr/bin/env python3
# webapp_cr_generator.py
# Application web Flask pour générer des CR .docx sans compétences techniques

import os
import json
import sys
from datetime import datetime
from flask import Flask, render_template_string, request, send_file, jsonify
from werkzeug.utils import secure_filename
import tempfile
import shutil

# Importe le générateur
try:
    from cr_json_to_docx import generate_programmatic, generate_from_template, find_default_template
except ImportError:
    print("[ERREUR] Impossible d'importer cr_json_to_docx.py")
    print("Assurez-vous que le fichier est dans le même dossier.")
    sys.exit(1)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()

# Détecte le template par défaut
DEFAULT_TEMPLATE = find_default_template()

# Template HTML avec formulaire
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Générateur de CR Chantier - Stone-Sea</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #004687 0%, #00679e 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            font-size: 28px;
            margin-bottom: 10px;
        }
        .header p {
            opacity: 0.9;
            font-size: 14px;
        }
        .content {
            padding: 40px;
        }
        .section {
            margin-bottom: 30px;
        }
        .section h2 {
            color: #004687;
            font-size: 18px;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f0f0f0;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
            font-size: 14px;
        }
        label .required {
            color: #e74c3c;
        }
        label .hint {
            color: #7f8c8d;
            font-weight: 400;
            font-size: 12px;
            font-style: italic;
        }
        input[type="text"],
        input[type="date"],
        textarea,
        select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
            font-family: inherit;
        }
        input[type="text"]:focus,
        input[type="date"]:focus,
        textarea:focus,
        select:focus {
            outline: none;
            border-color: #004687;
        }
        textarea {
            resize: vertical;
            min-height: 80px;
        }
        .points-container,
        .actions-container {
            border: 2px dashed #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            background: #f9f9f9;
        }
        .point-item,
        .action-item {
            background: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            border-left: 4px solid #004687;
        }
        .point-item:last-child,
        .action-item:last-child {
            margin-bottom: 0;
        }
        .add-btn {
            background: #27ae60;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            margin-top: 10px;
            transition: background 0.3s;
        }
        .add-btn:hover {
            background: #229954;
        }
        .remove-btn {
            background: #e74c3c;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            float: right;
            transition: background 0.3s;
        }
        .remove-btn:hover {
            background: #c0392b;
        }
        .submit-btn {
            background: linear-gradient(135deg, #004687 0%, #00679e 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            width: 100%;
            transition: transform 0.2s;
        }
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,70,135,0.3);
        }
        .submit-btn:disabled {
            background: #95a5a6;
            cursor: not-allowed;
            transform: none;
        }
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
        }
        .loading.active {
            display: block;
        }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #004687;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .success {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 1px solid #c3e6cb;
            display: none;
        }
        .success.active {
            display: block;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 1px solid #f5c6cb;
            display: none;
        }
        .error.active {
            display: block;
        }
        .info-box {
            background: #e8f4f8;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #004687;
        }
        .info-box h3 {
            color: #004687;
            margin-bottom: 10px;
            font-size: 16px;
        }
        .info-box ul {
            margin-left: 20px;
            color: #333;
        }
        .info-box li {
            margin-bottom: 5px;
        }
        .row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        @media (max-width: 768px) {
            .row {
                grid-template-columns: 1fr;
            }
            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏗️ Générateur de CR Chantier</h1>
            <p>Stone-Sea MODULE_04 - Génération automatique de documents .docx</p>
        </div>

        <div class="content">
            <div class="info-box">
                <h3>📝 Instructions</h3>
                <ul>
                    <li>Remplissez les informations du chantier</li>
                    <li>Ajoutez les points remarquables et actions nécessaires</li>
                    <li>Cliquez sur "Générer le CR" pour créer votre document Word</li>
                    <li>Les champs marqués <span style="color: #e74c3c;">*</span> sont obligatoires</li>
                </ul>
            </div>

            <div id="success-message" class="success"></div>
            <div id="error-message" class="error"></div>

            <form id="cr-form">
                <!-- Section Informations générales -->
                <div class="section">
                    <h2>1. Informations générales</h2>

                    <div class="form-group">
                        <label>Nom du projet <span class="required">*</span></label>
                        <input type="text" name="projet" required placeholder="Ex: Construction Immeuble Résidentiel A">
                    </div>

                    <div class="row">
                        <div class="form-group">
                            <label>Date du CR <span class="required">*</span></label>
                            <input type="date" name="date" required>
                        </div>
                        <div class="form-group">
                            <label>Lot concerné</label>
                            <input type="text" name="lot" placeholder="Ex: Gros œuvre, CVC, Plomberie...">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Participants <span class="required">*</span> <span class="hint">(séparés par des virgules)</span></label>
                        <input type="text" name="participants" required placeholder="Ex: Jean Dupont (MOE), Marie Martin (Entreprise), Pierre Durand (MOA)">
                    </div>

                    <div class="row">
                        <div class="form-group">
                            <label>Météo</label>
                            <input type="text" name="meteo" placeholder="Ex: Ensoleillé, 18°C">
                        </div>
                        <div class="form-group">
                            <label>Rédacteur</label>
                            <input type="text" name="redacteur" placeholder="Nom du rédacteur">
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Documents consultés <span class="hint">(séparés par des virgules)</span></label>
                        <input type="text" name="documents_consultes" placeholder="Ex: Planning S+8, Plan MEP L2, CCTP Lot 04">
                    </div>
                </div>

                <!-- Section Avancement -->
                <div class="section">
                    <h2>2. Avancement des travaux</h2>

                    <div class="form-group">
                        <label>Tâches prévues <span class="hint">(une par ligne)</span></label>
                        <textarea name="taches_prevues" rows="3" placeholder="Ex:&#10;Coulage dalle niveau 2&#10;Pose menuiseries extérieures&#10;Contrôle étanchéité"></textarea>
                    </div>

                    <div class="form-group">
                        <label>Tâches réalisées <span class="hint">(une par ligne)</span></label>
                        <textarea name="taches_realisees" rows="3" placeholder="Ex:&#10;Coulage dalle niveau 2 effectué (100%)&#10;Ferraillage niveau 3 terminé"></textarea>
                    </div>

                    <div class="form-group">
                        <label>Écarts constatés <span class="hint">(une par ligne)</span></label>
                        <textarea name="ecarts" rows="3" placeholder="Ex:&#10;Retard livraison menuiseries (2 jours)&#10;Main d'œuvre insuffisante zone B"></textarea>
                    </div>
                </div>

                <!-- Section Points remarquables -->
                <div class="section">
                    <h2>3. Points remarquables</h2>

                    <div class="points-container" id="points-container">
                        <div class="point-item" data-index="0">
                            <button type="button" class="remove-btn" onclick="removePoint(0)">Supprimer</button>
                            <div class="form-group">
                                <label>Identifiant</label>
                                <input type="text" name="point_id_0" placeholder="Ex: NC-001, P-01">
                            </div>
                            <div class="row">
                                <div class="form-group">
                                    <label>Type</label>
                                    <select name="point_type_0">
                                        <option value="NC">Non-conformité</option>
                                        <option value="point_attention">Point d'attention</option>
                                        <option value="observation">Observation</option>
                                        <option value="amelioration">Amélioration</option>
                                    </select>
                                </div>
                                <div class="form-group">
                                    <label>Gravité</label>
                                    <select name="point_gravite_0">
                                        <option value="critique">Critique</option>
                                        <option value="majeure">Majeure</option>
                                        <option value="mineure">Mineure</option>
                                        <option value="significative">Significative</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group">
                                <label>Description</label>
                                <textarea name="point_description_0" rows="2" placeholder="Description détaillée du point"></textarea>
                            </div>
                            <div class="form-group">
                                <label>Liens <span class="hint">(références, photos, plans - séparés par virgules)</span></label>
                                <input type="text" name="point_liens_0" placeholder="Ex: Photo_001.jpg, Plan_MEP_L2#A12">
                            </div>
                        </div>
                    </div>
                    <button type="button" class="add-btn" onclick="addPoint()">+ Ajouter un point</button>
                </div>

                <!-- Section Actions -->
                <div class="section">
                    <h2>4. Actions à mener</h2>

                    <div class="actions-container" id="actions-container">
                        <div class="action-item" data-index="0">
                            <button type="button" class="remove-btn" onclick="removeAction(0)">Supprimer</button>
                            <div class="row">
                                <div class="form-group">
                                    <label>Qui (responsable)</label>
                                    <input type="text" name="action_qui_0" placeholder="Ex: Entreprise XYZ, MOE">
                                </div>
                                <div class="form-group">
                                    <label>Quand (échéance)</label>
                                    <input type="text" name="action_quand_0" placeholder="Ex: 2025-12-01, J+3, S+1">
                                </div>
                            </div>
                            <div class="form-group">
                                <label>Quoi (action à réaliser)</label>
                                <textarea name="action_quoi_0" rows="2" placeholder="Description de l'action à mener"></textarea>
                            </div>
                            <div class="form-group">
                                <label>Critère de succès</label>
                                <input type="text" name="action_critere_0" placeholder="Ex: PV essais validé, Visa MOE">
                            </div>
                        </div>
                    </div>
                    <button type="button" class="add-btn" onclick="addAction()">+ Ajouter une action</button>
                </div>

                <!-- Section Options de génération -->
                <div class="section">
                    <h2>5. Options de génération</h2>

                    <div class="form-group">
                        <label>
                            <input type="checkbox" name="use_template" id="use_template" value="1" """ + ("checked" if DEFAULT_TEMPLATE else "") + """>
                            Utiliser un template .docx
                        </label>
                    </div>

                    <div class="info-box" id="template-info" style="margin-top: 10px;">
                        """ + (f"<p>📄 Template détecté: <strong>{os.path.basename(DEFAULT_TEMPLATE)}</strong></p>" if DEFAULT_TEMPLATE else "<p>⚠️ Aucun template détecté - génération programmatique par défaut</p>") + """
                        <p style="margin-top: 8px; font-size: 12px; color: #666;">
                            <strong>Mode template :</strong> Remplit un modèle Word prédéfini<br>
                            <strong>Mode programmatique :</strong> Génère un document avec mise en forme avancée (couleurs, tableaux dynamiques)
                        </p>
                    </div>
                </div>

                <!-- Bouton de soumission -->
                <div class="section">
                    <button type="submit" class="submit-btn" id="submit-btn">
                        🚀 Générer le CR .docx
                    </button>
                </div>

                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p style="margin-top: 15px; color: #666;">Génération du document en cours...</p>
                </div>
            </form>
        </div>
    </div>

    <script>
        let pointIndex = 1;
        let actionIndex = 1;

        function addPoint() {
            const container = document.getElementById('points-container');
            const newPoint = document.createElement('div');
            newPoint.className = 'point-item';
            newPoint.setAttribute('data-index', pointIndex);
            newPoint.innerHTML = `
                <button type="button" class="remove-btn" onclick="removePoint(${pointIndex})">Supprimer</button>
                <div class="form-group">
                    <label>Identifiant</label>
                    <input type="text" name="point_id_${pointIndex}" placeholder="Ex: NC-001, P-01">
                </div>
                <div class="row">
                    <div class="form-group">
                        <label>Type</label>
                        <select name="point_type_${pointIndex}">
                            <option value="NC">Non-conformité</option>
                            <option value="point_attention">Point d'attention</option>
                            <option value="observation">Observation</option>
                            <option value="amelioration">Amélioration</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Gravité</label>
                        <select name="point_gravite_${pointIndex}">
                            <option value="critique">Critique</option>
                            <option value="majeure">Majeure</option>
                            <option value="mineure">Mineure</option>
                            <option value="significative">Significative</option>
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea name="point_description_${pointIndex}" rows="2" placeholder="Description détaillée du point"></textarea>
                </div>
                <div class="form-group">
                    <label>Liens <span class="hint">(références, photos, plans - séparés par virgules)</span></label>
                    <input type="text" name="point_liens_${pointIndex}" placeholder="Ex: Photo_001.jpg, Plan_MEP_L2#A12">
                </div>
            `;
            container.appendChild(newPoint);
            pointIndex++;
        }

        function removePoint(index) {
            const point = document.querySelector(`[data-index="${index}"].point-item`);
            if (point && document.querySelectorAll('.point-item').length > 1) {
                point.remove();
            } else {
                alert('Vous devez garder au moins un point remarquable.');
            }
        }

        function addAction() {
            const container = document.getElementById('actions-container');
            const newAction = document.createElement('div');
            newAction.className = 'action-item';
            newAction.setAttribute('data-index', actionIndex);
            newAction.innerHTML = `
                <button type="button" class="remove-btn" onclick="removeAction(${actionIndex})">Supprimer</button>
                <div class="row">
                    <div class="form-group">
                        <label>Qui (responsable)</label>
                        <input type="text" name="action_qui_${actionIndex}" placeholder="Ex: Entreprise XYZ, MOE">
                    </div>
                    <div class="form-group">
                        <label>Quand (échéance)</label>
                        <input type="text" name="action_quand_${actionIndex}" placeholder="Ex: 2025-12-01, J+3, S+1">
                    </div>
                </div>
                <div class="form-group">
                    <label>Quoi (action à réaliser)</label>
                    <textarea name="action_quoi_${actionIndex}" rows="2" placeholder="Description de l'action à mener"></textarea>
                </div>
                <div class="form-group">
                    <label>Critère de succès</label>
                    <input type="text" name="action_critere_${actionIndex}" placeholder="Ex: PV essais validé, Visa MOE">
                </div>
            `;
            container.appendChild(newAction);
            actionIndex++;
        }

        function removeAction(index) {
            const action = document.querySelector(`[data-index="${index}"].action-item`);
            if (action && document.querySelectorAll('.action-item').length > 1) {
                action.remove();
            } else {
                alert('Vous devez garder au moins une action.');
            }
        }

        function showMessage(type, message) {
            const successEl = document.getElementById('success-message');
            const errorEl = document.getElementById('error-message');

            if (type === 'success') {
                successEl.textContent = message;
                successEl.classList.add('active');
                errorEl.classList.remove('active');
            } else {
                errorEl.textContent = message;
                errorEl.classList.add('active');
                successEl.classList.remove('active');
            }

            // Scroll vers le haut
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        document.getElementById('cr-form').addEventListener('submit', async function(e) {
            e.preventDefault();

            const submitBtn = document.getElementById('submit-btn');
            const loading = document.getElementById('loading');

            submitBtn.disabled = true;
            loading.classList.add('active');

            const formData = new FormData(this);

            try {
                const response = await fetch('/generate', {
                    method: 'POST',
                    body: formData
                });

                if (response.ok) {
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = `CR_Chantier_${formData.get('date') || 'document'}.docx`;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(a);

                    showMessage('success', '✅ Document généré avec succès ! Le téléchargement va démarrer...');
                } else {
                    const error = await response.text();
                    showMessage('error', '❌ Erreur lors de la génération : ' + error);
                }
            } catch (error) {
                showMessage('error', '❌ Erreur réseau : ' + error.message);
            } finally {
                submitBtn.disabled = false;
                loading.classList.remove('active');
            }
        });

        // Initialise la date d'aujourd'hui
        document.querySelector('input[name="date"]').valueAsDate = new Date();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Page d'accueil avec le formulaire."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/generate', methods=['POST'])
def generate():
    """Génère le document .docx à partir du formulaire."""
    try:
        # Récupère les données du formulaire
        form_data = request.form

        # Construit le JSON CR
        cr_data = {
            "meta": {
                "projet": form_data.get('projet', ''),
                "date": form_data.get('date', ''),
                "lot": form_data.get('lot', ''),
                "participants": [p.strip() for p in form_data.get('participants', '').split(',') if p.strip()],
                "meteo": form_data.get('meteo', ''),
                "redacteur": form_data.get('redacteur', ''),
                "documents_consultes": [d.strip() for d in form_data.get('documents_consultes', '').split(',') if d.strip()]
            },
            "avancement": {
                "taches_prevues": [t.strip() for t in form_data.get('taches_prevues', '').split('\n') if t.strip()],
                "taches_realisees": [t.strip() for t in form_data.get('taches_realisees', '').split('\n') if t.strip()],
                "ecarts": [e.strip() for e in form_data.get('ecarts', '').split('\n') if e.strip()]
            },
            "points": [],
            "photos": [],
            "actions": []
        }

        # Collecte les points
        i = 0
        while f'point_id_{i}' in form_data or f'point_description_{i}' in form_data:
            point_id = form_data.get(f'point_id_{i}', f'P-{i+1:03d}')
            description = form_data.get(f'point_description_{i}', '')

            if description:  # Seulement si une description est fournie
                liens = [l.strip() for l in form_data.get(f'point_liens_{i}', '').split(',') if l.strip()]
                cr_data["points"].append({
                    "id": point_id,
                    "type": form_data.get(f'point_type_{i}', 'observation'),
                    "gravite": form_data.get(f'point_gravite_{i}', 'mineure'),
                    "description": description,
                    "liens": liens
                })
            i += 1

        # Collecte les actions
        i = 0
        while f'action_qui_{i}' in form_data or f'action_quoi_{i}' in form_data:
            qui = form_data.get(f'action_qui_{i}', '')
            quoi = form_data.get(f'action_quoi_{i}', '')

            if qui and quoi:  # Seulement si qui et quoi sont remplis
                cr_data["actions"].append({
                    "qui": qui,
                    "quoi": quoi,
                    "quand": form_data.get(f'action_quand_{i}', ''),
                    "critere_succes": form_data.get(f'action_critere_{i}', '')
                })
            i += 1

        # Génère le document selon le mode choisi
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], f'CR_{datetime.now().strftime("%Y%m%d_%H%M%S")}.docx')

        use_template = form_data.get('use_template') == '1'

        if use_template and DEFAULT_TEMPLATE:
            # Mode template
            generate_from_template(cr_data, DEFAULT_TEMPLATE, output_path)
        else:
            # Mode programmatique
            generate_programmatic(cr_data, output_path)

        # Envoie le fichier
        return send_file(
            output_path,
            as_attachment=True,
            download_name=f'CR_Chantier_{cr_data["meta"]["date"]}.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

    except Exception as e:
        return str(e), 500

def main():
    print("="*70)
    print("  APPLICATION WEB - Générateur de CR Chantier")
    print("  Stone-Sea MODULE_04")
    print("="*70)
    print()
    print("✅ Serveur web démarré !")
    print()
    print("📱 Ouvrez votre navigateur et allez sur :")
    print()
    print("   👉  http://localhost:5000")
    print()
    print("💡 Instructions :")
    print("   1. Remplissez le formulaire dans le navigateur")
    print("   2. Cliquez sur 'Générer le CR'")
    print("   3. Le document .docx sera téléchargé automatiquement")
    print()
    print("⛔ Pour arrêter le serveur : Ctrl+C")
    print("="*70)
    print()

    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()
