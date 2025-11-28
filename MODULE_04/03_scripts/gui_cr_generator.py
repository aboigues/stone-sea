#!/usr/bin/env python3
# gui_cr_generator.py
# Interface graphique (Tkinter) pour générer des CR .docx sans compétences techniques

import os
import sys
import json
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox, filedialog, scrolledtext
from tkinter.font import Font

# Importe le générateur
try:
    from cr_json_to_docx import generate_programmatic
except ImportError:
    print("[ERREUR] Impossible d'importer cr_json_to_docx.py")
    print("Assurez-vous que le fichier est dans le même dossier.")
    sys.exit(1)


class CRGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de CR Chantier - Stone-Sea")
        self.root.geometry("900x800")

        # Variables pour les listes dynamiques
        self.points = []
        self.actions = []

        # Configure le style
        self.setup_style()

        # Crée l'interface
        self.create_widgets()

        # Centre la fenêtre
        self.center_window()

    def setup_style(self):
        """Configure le style de l'interface."""
        style = ttk.Style()
        style.theme_use('clam')

        # Couleurs Stone-Sea
        self.color_primary = '#004687'
        self.color_secondary = '#00679e'
        self.color_success = '#27ae60'
        self.color_danger = '#e74c3c'

        # Configure les styles
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground=self.color_primary)
        style.configure('Section.TLabel', font=('Arial', 12, 'bold'), foreground=self.color_primary)
        style.configure('Primary.TButton', font=('Arial', 10, 'bold'))

    def center_window(self):
        """Centre la fenêtre sur l'écran."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        """Crée tous les widgets de l'interface."""
        # Frame principal avec scrollbar
        main_canvas = Canvas(self.root)
        scrollbar = Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk.Frame(main_canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )

        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)

        # Header
        header_frame = ttk.Frame(scrollable_frame, padding="20")
        header_frame.grid(row=0, column=0, sticky=(W, E))

        ttk.Label(
            header_frame,
            text="🏗️ Générateur de CR Chantier",
            style='Title.TLabel'
        ).grid(row=0, column=0, pady=(0, 5))

        ttk.Label(
            header_frame,
            text="Stone-Sea MODULE_04 - Génération automatique de documents .docx"
        ).grid(row=1, column=0)

        # Container principal
        container = ttk.Frame(scrollable_frame, padding="20")
        container.grid(row=1, column=0, sticky=(W, E, N, S))

        row_idx = 0

        # Section 1 : Informations générales
        ttk.Label(container, text="1. Informations générales", style='Section.TLabel').grid(
            row=row_idx, column=0, columnspan=2, sticky=W, pady=(10, 10)
        )
        row_idx += 1

        # Projet
        ttk.Label(container, text="Nom du projet *").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_projet = ttk.Entry(container, width=50)
        self.entry_projet.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Date et Lot
        ttk.Label(container, text="Date du CR *").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_date = ttk.Entry(container, width=50)
        self.entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_date.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        ttk.Label(container, text="Lot concerné").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_lot = ttk.Entry(container, width=50)
        self.entry_lot.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Participants
        ttk.Label(container, text="Participants * (séparés par virgules)").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_participants = ttk.Entry(container, width=50)
        self.entry_participants.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Météo
        ttk.Label(container, text="Météo").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_meteo = ttk.Entry(container, width=50)
        self.entry_meteo.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Rédacteur
        ttk.Label(container, text="Rédacteur").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_redacteur = ttk.Entry(container, width=50)
        self.entry_redacteur.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Documents consultés
        ttk.Label(container, text="Documents consultés (séparés par virgules)").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.entry_docs = ttk.Entry(container, width=50)
        self.entry_docs.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Section 2 : Avancement
        ttk.Separator(container, orient='horizontal').grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=20)
        row_idx += 1

        ttk.Label(container, text="2. Avancement des travaux", style='Section.TLabel').grid(
            row=row_idx, column=0, columnspan=2, sticky=W, pady=(10, 10)
        )
        row_idx += 1

        # Tâches prévues
        ttk.Label(container, text="Tâches prévues (une par ligne)").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.text_taches_prevues = scrolledtext.ScrolledText(container, width=50, height=4)
        self.text_taches_prevues.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Tâches réalisées
        ttk.Label(container, text="Tâches réalisées (une par ligne)").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.text_taches_realisees = scrolledtext.ScrolledText(container, width=50, height=4)
        self.text_taches_realisees.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Écarts
        ttk.Label(container, text="Écarts constatés (une par ligne)").grid(row=row_idx, column=0, sticky=W, pady=5)
        self.text_ecarts = scrolledtext.ScrolledText(container, width=50, height=4)
        self.text_ecarts.grid(row=row_idx, column=1, sticky=(W, E), pady=5)
        row_idx += 1

        # Section 3 : Points remarquables
        ttk.Separator(container, orient='horizontal').grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=20)
        row_idx += 1

        points_frame = ttk.Frame(container)
        points_frame.grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=10)

        ttk.Label(points_frame, text="3. Points remarquables", style='Section.TLabel').pack(side=LEFT)
        ttk.Button(points_frame, text="+ Ajouter un point", command=self.add_point_dialog).pack(side=RIGHT)
        row_idx += 1

        # Liste des points
        self.points_listbox = Listbox(container, height=5)
        self.points_listbox.grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=5)
        row_idx += 1

        points_buttons = ttk.Frame(container)
        points_buttons.grid(row=row_idx, column=0, columnspan=2, sticky=W, pady=5)
        ttk.Button(points_buttons, text="Supprimer", command=self.remove_point).pack(side=LEFT, padx=5)
        row_idx += 1

        # Section 4 : Actions
        ttk.Separator(container, orient='horizontal').grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=20)
        row_idx += 1

        actions_frame = ttk.Frame(container)
        actions_frame.grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=10)

        ttk.Label(actions_frame, text="4. Actions à mener", style='Section.TLabel').pack(side=LEFT)
        ttk.Button(actions_frame, text="+ Ajouter une action", command=self.add_action_dialog).pack(side=RIGHT)
        row_idx += 1

        # Liste des actions
        self.actions_listbox = Listbox(container, height=5)
        self.actions_listbox.grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=5)
        row_idx += 1

        actions_buttons = ttk.Frame(container)
        actions_buttons.grid(row=row_idx, column=0, columnspan=2, sticky=W, pady=5)
        ttk.Button(actions_buttons, text="Supprimer", command=self.remove_action).pack(side=LEFT, padx=5)
        row_idx += 1

        # Bouton de génération
        ttk.Separator(container, orient='horizontal').grid(row=row_idx, column=0, columnspan=2, sticky=(W, E), pady=20)
        row_idx += 1

        self.btn_generate = ttk.Button(
            container,
            text="🚀 Générer le CR .docx",
            command=self.generate_document,
            style='Primary.TButton'
        )
        self.btn_generate.grid(row=row_idx, column=0, columnspan=2, pady=20)

        # Configure grid weights
        container.columnconfigure(1, weight=1)

        # Pack canvas et scrollbar
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def add_point_dialog(self):
        """Ouvre une fenêtre pour ajouter un point remarquable."""
        dialog = Toplevel(self.root)
        dialog.title("Ajouter un point remarquable")
        dialog.geometry("500x400")

        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=BOTH, expand=True)

        # ID
        ttk.Label(frame, text="Identifiant:").grid(row=0, column=0, sticky=W, pady=5)
        entry_id = ttk.Entry(frame, width=40)
        entry_id.insert(0, f"P-{len(self.points)+1:03d}")
        entry_id.grid(row=0, column=1, sticky=(W, E), pady=5)

        # Type
        ttk.Label(frame, text="Type:").grid(row=1, column=0, sticky=W, pady=5)
        combo_type = ttk.Combobox(frame, width=37, values=["NC", "point_attention", "observation", "amelioration"])
        combo_type.set("NC")
        combo_type.grid(row=1, column=1, sticky=(W, E), pady=5)

        # Gravité
        ttk.Label(frame, text="Gravité:").grid(row=2, column=0, sticky=W, pady=5)
        combo_gravite = ttk.Combobox(frame, width=37, values=["critique", "majeure", "mineure", "significative"])
        combo_gravite.set("majeure")
        combo_gravite.grid(row=2, column=1, sticky=(W, E), pady=5)

        # Description
        ttk.Label(frame, text="Description:").grid(row=3, column=0, sticky=W, pady=5)
        text_desc = scrolledtext.ScrolledText(frame, width=40, height=6)
        text_desc.grid(row=3, column=1, sticky=(W, E), pady=5)

        # Liens
        ttk.Label(frame, text="Liens (séparés par virgules):").grid(row=4, column=0, sticky=W, pady=5)
        entry_liens = ttk.Entry(frame, width=40)
        entry_liens.grid(row=4, column=1, sticky=(W, E), pady=5)

        def save_point():
            point = {
                "id": entry_id.get(),
                "type": combo_type.get(),
                "gravite": combo_gravite.get(),
                "description": text_desc.get("1.0", END).strip(),
                "liens": [l.strip() for l in entry_liens.get().split(',') if l.strip()]
            }
            if point["description"]:
                self.points.append(point)
                self.update_points_listbox()
                dialog.destroy()
            else:
                messagebox.showwarning("Champ requis", "La description est obligatoire.")

        ttk.Button(frame, text="Ajouter", command=save_point).grid(row=5, column=0, columnspan=2, pady=20)
        frame.columnconfigure(1, weight=1)

    def add_action_dialog(self):
        """Ouvre une fenêtre pour ajouter une action."""
        dialog = Toplevel(self.root)
        dialog.title("Ajouter une action")
        dialog.geometry("500x350")

        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=BOTH, expand=True)

        # Qui
        ttk.Label(frame, text="Qui (responsable):").grid(row=0, column=0, sticky=W, pady=5)
        entry_qui = ttk.Entry(frame, width=40)
        entry_qui.grid(row=0, column=1, sticky=(W, E), pady=5)

        # Quand
        ttk.Label(frame, text="Quand (échéance):").grid(row=1, column=0, sticky=W, pady=5)
        entry_quand = ttk.Entry(frame, width=40)
        entry_quand.grid(row=1, column=1, sticky=(W, E), pady=5)

        # Quoi
        ttk.Label(frame, text="Quoi (action):").grid(row=2, column=0, sticky=W, pady=5)
        text_quoi = scrolledtext.ScrolledText(frame, width=40, height=5)
        text_quoi.grid(row=2, column=1, sticky=(W, E), pady=5)

        # Critère
        ttk.Label(frame, text="Critère de succès:").grid(row=3, column=0, sticky=W, pady=5)
        entry_critere = ttk.Entry(frame, width=40)
        entry_critere.grid(row=3, column=1, sticky=(W, E), pady=5)

        def save_action():
            action = {
                "qui": entry_qui.get(),
                "quand": entry_quand.get(),
                "quoi": text_quoi.get("1.0", END).strip(),
                "critere_succes": entry_critere.get()
            }
            if action["qui"] and action["quoi"]:
                self.actions.append(action)
                self.update_actions_listbox()
                dialog.destroy()
            else:
                messagebox.showwarning("Champs requis", "Le responsable et l'action sont obligatoires.")

        ttk.Button(frame, text="Ajouter", command=save_action).grid(row=4, column=0, columnspan=2, pady=20)
        frame.columnconfigure(1, weight=1)

    def remove_point(self):
        """Supprime le point sélectionné."""
        selection = self.points_listbox.curselection()
        if selection:
            index = selection[0]
            self.points.pop(index)
            self.update_points_listbox()

    def remove_action(self):
        """Supprime l'action sélectionnée."""
        selection = self.actions_listbox.curselection()
        if selection:
            index = selection[0]
            self.actions.pop(index)
            self.update_actions_listbox()

    def update_points_listbox(self):
        """Met à jour la liste des points."""
        self.points_listbox.delete(0, END)
        for point in self.points:
            self.points_listbox.insert(END, f"[{point['gravite']}] {point['id']} - {point['description'][:50]}")

    def update_actions_listbox(self):
        """Met à jour la liste des actions."""
        self.actions_listbox.delete(0, END)
        for action in self.actions:
            self.actions_listbox.insert(END, f"{action['qui']} → {action['quoi'][:50]} ({action['quand']})")

    def generate_document(self):
        """Génère le document .docx."""
        # Validation
        if not self.entry_projet.get():
            messagebox.showerror("Erreur", "Le nom du projet est obligatoire.")
            return

        if not self.entry_participants.get():
            messagebox.showerror("Erreur", "Les participants sont obligatoires.")
            return

        # Construit les données CR
        cr_data = {
            "meta": {
                "projet": self.entry_projet.get(),
                "date": self.entry_date.get(),
                "lot": self.entry_lot.get(),
                "participants": [p.strip() for p in self.entry_participants.get().split(',') if p.strip()],
                "meteo": self.entry_meteo.get(),
                "redacteur": self.entry_redacteur.get(),
                "documents_consultes": [d.strip() for d in self.entry_docs.get().split(',') if d.strip()]
            },
            "avancement": {
                "taches_prevues": [t.strip() for t in self.text_taches_prevues.get("1.0", END).split('\n') if t.strip()],
                "taches_realisees": [t.strip() for t in self.text_taches_realisees.get("1.0", END).split('\n') if t.strip()],
                "ecarts": [e.strip() for e in self.text_ecarts.get("1.0", END).split('\n') if e.strip()]
            },
            "points": self.points,
            "photos": [],
            "actions": self.actions
        }

        # Demande où sauvegarder
        output_path = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Documents Word", "*.docx")],
            initialfile=f"CR_Chantier_{cr_data['meta']['date']}.docx"
        )

        if not output_path:
            return

        try:
            # Génère le document
            generate_programmatic(cr_data, output_path)
            messagebox.showinfo("Succès", f"Document généré avec succès !\n\n{output_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la génération :\n{str(e)}")


def main():
    root = Tk()
    app = CRGeneratorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
