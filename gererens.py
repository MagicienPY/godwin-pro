import customtkinter as ctk
import mysql.connector
from subprocess import call
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from departement2 import *

import sqlite3
import pymysql
class ajouterES:
    def __init__(self):
        pass
    def ajoue (self):
        global essaie
        essaie = 0

        #dep = Vue()


        def fermer ():
            ajouterEl.destroy()
        def tentative ():
            global essaie
            essaie += 1
            lable1 = ctk.CTkLabel(master= ajouterEl, text = "nombre de tentative restante  "+str(essaie),bg_color="red")
            lable1.pack(padx= 1, pady= 0)

            
            #messagebox.showinfo("nombre de tentative restante",essaie)
            if essaie==3:
                messagebox.showinfo("Attention","vous n'avez plus d'autre tentative !")
                ajouterEl.destroy()
        def conn1():
        # mysqldb = mysql.connector.connect(host="localhost", user="root", password="",database="gestage")
        # mycursor = mysqldb.cursor()
            con = pymysql.connect(user='root', password ='',database = 'myscolar')
            cursor = con.cursor()
            print("connecté avec succes")
            codeax = chama.get()
            passax = chama2.get()
            choix2 = choix.get()


            command="use myscolar"
            cursor.execute(command)
            print("nous utilisons AUTH")
            admin = "Admin"
            query = 'select * from Compte where Nom_utilisateur = %s and Mot_de_passe = %s and Type =%s;'
            query2 = 'select * from Compte where Nom_utilisateur = %s and Mot_de_passe = %s;'
        # query2 = 'select * from administrateur where matricule = %s;'
            
            
            
            print("la valeur du choix",choix2)
            if choix2 > 0:
                r2 = cursor.execute(query,(codeax,passax,admin))
                data2 = cursor.fetchall()
                if data2 == None:
                    messagebox.showinfo("desole"," nous ne pravenons pas a vous connecter")
                    tentative()
                if data2:
                    messagebox.showinfo("cool","connecté en tant que admin")
                    print(choix2)
                    ajouterEl.destroy()

                    ri = Vueri()

                    ri.acceuil()
            else:
                r = cursor.execute(query2,(codeax,passax))
            
                data1 = cursor.fetchall()
                if data1 ==None:
                # print(codeax)
                    #print(passax)
                    messagebox.showinfo("desole"," nous ne pravenons pas a vous connecter")
                    tentative()
                if data1:
                    messagebox.showinfo("cool","connecté en tant que stagiaire")
                    ajouterEl.destroy()
                    stag.evenement()


        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")


        ajouterEl = ctk.CTk()
        ajouterEl.title("MYSCOLAR")
        ajouterEl.geometry("900x700")

        #une frame au centre

        frame = ctk.CTkFrame(master= ajouterEl)
        frame.pack(padx = 220, pady = 60, fill= "both", expand = True) 

        frame3 = ctk.CTkFrame(master= ajouterEl,width=200,height=300)
        frame3.place(x = 0, y = 60) 


        #label

        lable = ctk.CTkLabel(master= frame, text = "Ajoue d'Eleve")
        lable.pack(padx= 12, pady= 10)




        chama = ctk.CTkEntry(master=  frame, placeholder_text="nom")
        chama.pack(padx= 12)

        chama = ctk.CTkEntry(master=  frame, placeholder_text="prenom")
        chama.pack(padx= 12)


        chama = ctk.CTkEntry(master=  frame, placeholder_text="classe")
        chama.pack(padx= 12)

        chama2 = ctk.CTkEntry(master=  frame, placeholder_text="mot de passe")
        chama2.pack(pady= 12)


        button = ctk.CTkButton(master=frame, text="Ajouter",command=conn1)
        button.pack(padx=10, pady=12)

        button = ctk.CTkButton(master=frame3, text="Annuler",command=fermer)
        button.pack(padx=10, pady=12)

        #ajouterEl.mainloop()