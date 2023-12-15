import tkinter as tk
from tkinter import filedialog
import shutil
import os
import mysql.connector

class AjouterUser:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="g_note"
        )

        self.window = tk.Tk()
        self.window.title("Ajout d'utilisateur")

        self.label_nom = tk.Label(self.window, text="Nom:")
        self.label_nom.pack()
        self.entry_nom = tk.Entry(self.window)
        self.entry_nom.pack()

        self.label_prenom = tk.Label(self.window, text="Prénom:")
        self.label_prenom.pack()
        self.entry_prenom = tk.Entry(self.window)
        self.entry_prenom.pack()

        self.label_username = tk.Label(self.window, text="Nom d'utilisateur:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.window)
        self.entry_username.pack()

        self.label_password = tk.Label(self.window, text="Mot de passe:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.pack()

        self.label_tof = tk.Label(self.window, text="Chemin de la photo:")
        self.label_tof.pack()
        self.entry_tof = tk.Entry(self.window)
        self.entry_tof.pack()

        self.label_role = tk.Label(self.window, text="Rôle:")
        self.label_role.pack()
        self.entry_role = tk.Entry(self.window)
        self.entry_role.pack()

        self.button_select_image = tk.Button(self.window, text="Sélectionner une image", command=self.selectionner_image)
        self.button_select_image.pack()

        self.button_ajouter = tk.Button(self.window, text="Ajouter", command=self.ajouter_utilisateur)
        self.button_ajouter.pack()

        self.label_message = tk.Label(self.window, text="")
        self.label_message.pack()

        self.window.mainloop()

        self.conn.close()

    def selectionner_image(self):
        # Ouvrir la boîte de dialogue pour sélectionner une image
        filename = filedialog.askopenfilename(initialdir="/", title="Sélectionner une image", filetypes=(("Fichiers images", "*.jpg;*.jpeg;*.png"), ("Tous les fichiers", "*.*")))
        
        # Afficher le chemin de l'image sélectionnée dans le champ de saisie
        self.entry_tof.delete(0, tk.END)
        self.entry_tof.insert(0, filename)

    def ajouter_utilisateur(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        tof = self.entry_tof.get()
        role = self.entry_role.get()

        if not all([nom, prenom, username, password, tof, role]):
            self.label_message.config(text="Veuillez remplir tous les champs", fg="red")
            return

        if not os.path.isfile(tof):
            self.label_message.config(text="Le fichier image n'existe pas", fg="red")
            return

        # Copier l'image dans le dossier "photo_user"
        image_basename = os.path.basename(tof)
        destination_path = os.path.join("photo_user", image_basename)
        
        try:
            shutil.copy2(tof, destination_path)
        except Exception as e:
            self.label_message.config(text=str(e), fg="red")
            return

        cursor = self.conn.cursor()

        sql = "INSERT INTO utilisateur (nom, prenom, username, password, role_id,tof) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, username, password, role, destination_path)

        try:
            cursor.execute(sql, values)
            self.conn.commit()
            self.label_message.config(text="Utilisateur ajouté avec succès", fg="green")
        except Exception as e:
            self.label_message.config(text=str(e), fg="red")

        cursor.close()


# Utilisation de la classe AjouterUser
#ajouter_user = AjouterUser()


import tkinter as tk
from tkinter import filedialog
import shutil
import os
import mysql.connector

class AjouterUser2:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="g_note"
        )

        self.window = tk.Tk()
        self.window.title("Ajout d'utilisateur")

        self.label_nom = tk.Label(self.window, text="Nom:")
        self.label_nom.pack()
        self.entry_nom = tk.Entry(self.window)
        self.entry_nom.pack()

        self.label_prenom = tk.Label(self.window, text="Prénom:")
        self.label_prenom.pack()
        self.entry_prenom = tk.Entry(self.window)
        self.entry_prenom.pack()

        self.label_username = tk.Label(self.window, text="Nom d'utilisateur:")
        self.label_username.pack()
        self.entry_username = tk.Entry(self.window)
        self.entry_username.pack()

        self.label_password = tk.Label(self.window, text="Mot de passe:")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.window, show="*")
        self.entry_password.pack()

        self.label_tof = tk.Label(self.window, text="Chemin de la photo:")
        self.label_tof.pack()
        self.entry_tof = tk.Entry(self.window)
        self.entry_tof.pack()

        self.label_role = tk.Label(self.window, text="Rôle:")
        self.label_role.pack()
        self.combo_role = tk.Combobox(self.window, state="readonly")
        self.combo_role.pack()

        self.button_select_image = tk.Button(self.window, text="Sélectionner une image", command=self.selectionner_image)
        self.button_select_image.pack()

        self.button_ajouter = tk.Button(self.window, text="Ajouter", command=self.ajouter_utilisateur)
        self.button_ajouter.pack()

        self.label_message = tk.Label(self.window, text="")
        self.label_message.pack()

        self.charger_roles()

        self.window.mainloop()

        self.conn.close()

    def charger_roles(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nom_role FROM role")
        roles = cursor.fetchall()
        cursor.close()

        # Remplir la liste des rôles dans la combobox
        self.combo_role["values"] = [role[1] for role in roles]
        self.combo_role.current(0)  # Sélectionner le premier rôle par défaut

    def selectionner_image(self):
        # Ouvrir la boîte de dialogue pour sélectionner une image
        filename = filedialog.askopenfilename(initialdir="/", title="Sélectionner une image", filetypes=(("Fichiers images", "*.jpg;*.jpeg;*.png"), ("Tous les fichiers", "*.*")))
        
        # Afficher le chemin de l'image sélectionnée dans le champ de saisie
        self.entry_tof.delete(0, tk.END)
        self.entry_tof.insert(0, filename)

    def ajouter_utilisateur(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        tof = self.entry_tof.get()
        role = self.combo_role.get()

        if not all([nom, prenom, username, password, tof, role]):
            self.label_message.config(text="Veuillez remplir tous les champs", fg="red")
            return

        if not os.path.isfile(tof):
            self.label_message.config(text="Le fichier image n'existe pas", fg="red")
            return

        # Copier l'image dans le dossier "photo_user"
        image_basename = os.path.basename(tof)
        destination_path = os.path.join("photo_user", image_basename)
        
        try:
            shutil.copy2(tof, destination_path)
        except Exception as e:
            self.label_message.config(text=str(e), fg="red")
            return

        cursor = self.conn.cursor()

        # Récupérer l'ID du rôle sélectionné
        cursor.execute("SELECT id FROM role WHERE nom_role = %s", (role,))
        role_id = cursor.fetchone()

        if not role_id:
            self.label_message.config(text="Le rôle sélectionné est invalide", fg="red")
            return

        sql = "INSERT INTO utilisateur (nom, prenom, username, password, tof, id_role) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, username, password, destination_path, role_id[0])

        try:
            cursor.execute(sql, values)
            self.conn.commit()
            self.label_message.config(text="Utilisateur ajouté avec succès", fg="green")
        except Exception as e:
            self.label_message.config(text=str(e), fg="red")

        cursor.close()


# Utilisation de la classe AjouterUser
#ajouter_user = AjouterUser2()