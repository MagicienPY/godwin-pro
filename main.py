import customtkinter as ctk
import mysql.connector
from subprocess import call
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from departement2 import *
from chefdep import *
from agent import *

import sqlite3
import pymysql

global essaie
essaie = 0

#dep = Vue()


class utilisateur:
    def __init__(self, nom , matricule, passe, role):
        self.nom = nom
        self.matricule = matricule
        self.passe = passe
        self.role = role

    def affichage (self):
        print (self.nom, self.matricule, self.passe, self.role)

    def get_nom(self):
        return self.nom

    def get_matricule(self):
        return self.matricule

    def get_passe(self):
        return self.passe

    def get_role(self):
        return self.role



def fermer ():
    authen.destroy()
def tentative ():
    global essaie
    essaie += 1
    lable1 = ctk.CTkLabel(master= authen, text = "nombre de tentative restante  "+str(essaie),bg_color="red")
    lable1.pack(padx= 1, pady= 0)

    
    #messagebox.showinfo("nombre de tentative restante",essaie)
    if essaie==3:
        messagebox.showinfo("Attention","vous n'avez plus d'autre tentative !")
        authen.destroy()
def authenticate_user():
    con = pymysql.connect(user='root', password ='',database = 'g_note')
    cursor = con.cursor()
    username = chama.get()
    password = chama2.get()

    # Requête SQL pour vérifier les informations d'identification
    query = """
            SELECT r.nom_role ,u.nom, u.password, u.id, u.tof
            FROM role r
            inner JOIN utilisateur u ON u.role_id = r.id
            WHERE u.nom = %s AND u.password = %s
            """
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()
    user = utilisateur(result[1], result[3],result[2], result[0])
    user.affichage()
    
    #print(result[0])

    if result is not None:
        role = result[0]
        if role == "admin":
            # Rediriger vers la page d'administration
            messagebox.showinfo("Connexion réussie", "Bienvenue, Admin!")
            authen.destroy()
            ri = Vueri()
            nom = user.get_nom()
            matricule = user.get_matricule()
            passe = user.get_passe()
            role = user.get_role()
            ri.acceuil(nom, matricule, passe, role)
        elif role == "chef_dep":
            # Rediriger vers la page du chef de département
            messagebox.showinfo("Connexion réussie", "Bienvenue, Chef de département!")
            authen.destroy()
            cp = chef_dep()
            ri = Vueri()
            nom = user.get_nom()
            matricule = user.get_matricule()
            passe = user.get_passe()
            role = user.get_role()
            cp.acceuil(nom, matricule, passe, role)
        elif role == "agent":
            # Rediriger vers la page de l'agent
            messagebox.showinfo("Connexion réussie", "Bienvenue, Chers enseignant !")
            authen.destroy()
            cp = agent()
            ri = Vueri()
            nom = user.get_nom()
            matricule = user.get_matricule()
            passe = user.get_passe()
            role = user.get_role()
            cp.acceuil(nom, matricule, passe, role)
    else:
        # Afficher un message d'erreur si les informations d'identification sont incorrectes
        messagebox.showinfo("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


authen = ctk.CTk()
authen.title("AUTH-SERCU")
authen.geometry("900x700")

#une frame au centre

frame = ctk.CTkFrame(master= authen)
frame.pack(padx = 220, pady = 60, fill= "both", expand = True) 

frame3 = ctk.CTkFrame(master= authen,width=200,height=300)
frame3.place(x = 0, y = 60) 


#label

lable = ctk.CTkLabel(master= frame, text = "se connecter")
lable.pack(padx= 12, pady= 10)

lable = ctk.CTkLabel(master= frame3, text = "   Bonjour et bienvenue sur AUTH SECUR    ", bg_color="cyan",height=65,width=70, text_color="black")
lable.pack(padx= 30, pady= 30)


chama = ctk.CTkEntry(master=  frame, placeholder_text="IDENTIFIANT", show= "+")
chama.pack(padx= 12)

chama2 = ctk.CTkEntry(master=  frame, placeholder_text="mot de passe", show="*-")
chama2.pack(pady= 12)


button = ctk.CTkButton(master=frame, text="connection",command=authenticate_user)
button.pack(padx=10, pady=12)

button = ctk.CTkButton(master=frame3, text="Annuler",command=fermer)
button.pack(padx=10, pady=12)

authen.mainloop()