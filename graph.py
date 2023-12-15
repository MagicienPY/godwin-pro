import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Configuration de la base de données
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='g_note')
cursor = cnx.cursor()

# Définition des fonctions de sauvegarde et d'annulation
def save_data():
    # Récupération des valeurs des entrées
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    lieu_naissance = entry_lieu_naissance.get()
    adresse = entry_adresse.get()
    code_postal = entry_code_postal.get()
    ville = entry_ville.get()
    pays = entry_pays.get()
    telephone = entry_telephone.get()
    email = entry_email.get()

    # Insertion des données dans la table etudiant
    cursor.execute("INSERT INTO etudiant (nom_etu, prenom_etu, daten_etu, lieun_etu, adress_etu, tel_etu) VALUES (%s, %s, %s, %s, %s, %s)", (nom, prenom, date_naissance, lieu_naissance, adresse, telephone))
    cnx.commit()

    # Récupération de l'id de l'étudiant inséré
    cursor.execute("SELECT LAST_INSERT_ID()")
    id_etudiant = cursor.fetchone()[0]

    # Insertion des données dans la table classe
    # Ici, vous devrez récupérer le niveau de la classe à partir d'une entrée ou d'une liste déroulante
    niveau_classe = 1  # Exemple : niveau 1
    cursor.execute("INSERT INTO classe (nom_classe, niveau_classe) VALUES (%s, %s)", (nom_classe, niveau_classe))
    cnx.commit()

    # Récupération de l'id de la classe insérée
    cursor.execute("SELECT LAST_INSERT_ID()")
    id_classe = cursor.fetchone()[0]

    # Insertion des données dans la table etudiant_classe
    cursor.execute("INSERT INTO etudiant_classe (id_etudiant, id_classe) VALUES (%s, %s)", (id_etudiant, id_classe))
    cnx.commit()

    # Affichage d'un message de confirmation
    tk.messagebox.showinfo("Sauvegarde réussie", "Les données ont été enregistrées avec succès.")

def cancel_data():
    # Annulation de la saisie
    entry_nom.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_date_naissance.delete(0, tk.END)
    entry_lieu_naissance.delete(0, tk.END)
    entry_adresse.delete(0, tk.END)
    entry_code_postal.delete(0, tk.END)
    entry_ville.delete(0, tk.END)
    entry_pays.delete(0, tk.END)
    entry_telephone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

    # Affichage d'un message d'information
    tk.messagebox.showinfo("Annulation", "La saisie a été annulée.")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Gestionnaire de notes")
window.geometry("800x600")

# Création d'un frame pour la grille
frame = ttk.Frame(window)
frame.pack()

# Création des labels et des entrées
label_nom = ttk.Label(frame, text="Nom :")
label_prenom = ttk.Label(frame, text="Prénom :")
label_date_naissance = ttk.Label(frame, text="Date de naissance :")
label_lieu_naissance = ttk.Label(frame, text="Lieu de naissance :")
label_adresse = ttk.Label(frame, text="Adresse :")
label_code_postal = ttk.Label(frame, text="Code postal :")
label_ville = ttk.Label(frame, text="Ville :")
label_pays = ttk.Label(frame, text="Pays :")
label_telephone = ttk.Label(frame, text="Téléphone :")
label_email = ttk.Label(frame, text="Email :")

entry_nom = ttk.Entry(frame)
entry_prenom = ttk.Entry(frame)
entry_date_naissance = ttk.Entry(frame)
entry_lieu_naissance = ttk.Entry(frame)
entry_adresse = ttk.Entry(frame)
entry_code_postal = ttk.Entry(frame)
entry_ville = ttk.Entry(frame)
entry_pays = ttk.Entry(frame)
entry_telephone = ttk.Entry(frame)
entry_email = ttk.Entry(frame)

# Création des boutons
button_save = ttk.Button(frame, text="Enregistrer", command=save_data)
button_cancel = ttk.Button(frame, text="Annuler", command=cancel_data)

# Placement des labels et des entrées dans la grille
label_nom.grid(row=0, column=0, padx=5, pady=5)
entry_nom.grid(row=0, column=1, padx=5, pady=5)
label_prenom.grid(row=1, column=0, padx=5, pady=5)
entry_prenom.grid(row=1, column=1, padx=5, pady=5)
label_date_naissance.grid(row=2, column=0, padx=5, pady=5)
entry_date_naissance.grid(row=2, column=1, padx=5, pady=5)
label_lieu_naissance.grid(row=3, column=0, padx=5, pady=5)
entry_lieu_naissance.grid(row=3, column=1, padx=5, pady=5)
label_adresse.grid(row=4, column=0, padx=5, pady=5)
entry_adresse.grid(row=4, column=1, padx=5, pady=5)
label_code_postal.grid(row=5, column=0, padx=5, pady=5)
entry_code_postal.grid(row=5, column=1, padx=5, pady=5)
label_ville.grid(row=6, column=0, padx=5, pady=5)
entry_ville.grid(row=6, column=1, padx=5, pady=5)
label_pays.grid(row=7, column=0, padx=5, pady=5)
entry_pays.grid(row=7, column=1, padx=5, pady=5)
label_telephone.grid(row=8, column=0, padx=5, pady=5)
entry_telephone.grid(row=8, column=1, padx=5, pady=5)
label_email.grid(row=9, column=0, padx=5, pady=5)
entry_email.grid(row=9, column=1, padx=5, pady=5)

# Placement des boutons dans la grille
button_save.grid(row=10, column=0, padx=5, pady=5)
button_cancel.grid(row=10, column=1, padx=5, pady=5)

# Lancement de la boucle principale
window.mainloop()

# Fermeture de la connexion à la base de données
cursor.close()
cnx.close()