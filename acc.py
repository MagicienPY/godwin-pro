import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import pymysql
# Configuration de la base de données


# Fonction pour vérifier les informations d'identification de l'utilisateur
def authenticate_user():
    con = pymysql.connect(user='root', password ='',database = 'g_note')
    cursor = con.cursor()
    username = entry_username.get()
    password = entry_password.get()

    # Requête SQL pour vérifier les informations d'identification
    query = """
            SELECT r.nom_role 
            FROM role r
            inner JOIN utilisateur u ON u.role_id = r.id
            WHERE u.nom = %s AND u.password = %s
            """
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()
    print(result)

    if result is not None:
        role = result[0]
        if role == "admin":
            # Rediriger vers la page d'administration
            messagebox.showinfo("Connexion réussie", "Bienvenue, Admin!")
        elif role == "chef_departement":
            # Rediriger vers la page du chef de département
            messagebox.showinfo("Connexion réussie", "Bienvenue, Chef de département!")
        elif role == "agent":
            # Rediriger vers la page de l'agent
            messagebox.showinfo("Connexion réussie", "Bienvenue, Agent!")
    else:
        # Afficher un message d'erreur si les informations d'identification sont incorrectes
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

# Page d'authentification
window = tk.Tk()
window.title("Gestion de notes - Authentification")
window.configure(bg="#f0f0f0")  # Couleur de fond

# Style pour les widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))

# Création des widgets
label_username = ttk.Label(window, text="Nom d'utilisateur :", background="#f0f0f0")
label_username.pack(pady=10)

entry_username = ttk.Entry(window)
entry_username.pack(pady=5)

label_password = ttk.Label(window, text="Mot de passe :", background="#f0f0f0")
label_password.pack()

entry_password = ttk.Entry(window, show="*")
entry_password.pack(pady=10)

button_login = ttk.Button(window, text="Se connecter", command=authenticate_user)
button_login.pack(pady=10)

# Centrer la fenêtre sur l'écran
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.mainloop()