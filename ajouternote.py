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
class ajouterNote:
    def __init__(self):
        pass
    def ajoue (self):
        global essaie
        essaie = 0

        #dep = Vue()


        def fermer ():
            ajouterEl.destroy()
        
        def creationn():
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                #print("connecté avec succes")
                iden = id_note.get()
                valeur_n = valeur_note.get()
                type_n = type_note.get()
                ann_s = annee_scolaire.get()
                sem = semestre.get()
                poids_n = poids_note.get()
                id_etu =  id_etudiant.get()
                id_ma = id_matiere.get()
                id_ens = id_enseignat.get()
                not_c =  note_cc.get()
                not_s = note_sn.get()
                id_c = id_cote.get()
                data =  []
                #data.append(iden, valeur_n, type_n, ann_s, sem, poids_n, id_etu, id_ma, id_ens, not_c, not_s, id_cn)
                #for i in range (len(data)):
                 #   #print(data[i])
                #print(iden, valeur_n, type_n, ann_s, sem, poids_n, id_etu, id_ma, id_ens, not_c, not_s, id_c)
                command="use g_note"
                cursor.execute(command)
                sql = "INSERT INTO note (id_note, valeur_note, type_note , annee_scolaire, semestre, poids_note, id_etudiant, id_matiere, id_enseignant, note_cc, note_sn, id_cote) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s)"
                cursor.execute(sql, (iden, valeur_n, type_n, ann_s, sem, poids_n, id_etu, id_ma, id_ens, not_c, not_s, id_c))
                con.commit()
                messagebox.showinfo(" cool ", "enregistrement reussit !!")
                ajouterEl.destroy()
            except:
                messagebox.showinfo("attention", "un soucis veuillez verifier vos informations")



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

        #frame4 = ctk.CTkFrame(master= ajouterEl,width=200,height=300)
        #frame4.pack(side="rigth",fill="both",expand=False)
        droit_frame = ctk.CTkFrame(master=ajouterEl,fg_color="dark gray")
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)


        #label
        #print("ajoue de note")
        lable = ctk.CTkLabel(master= frame, text = "Ajoue de Notes")
        lable.pack(padx= 12, pady= 10)




        id_note = ctk.CTkEntry(master=  frame, placeholder_text=" id note")
        id_note.pack(padx= 12)

        valeur_note = ctk.CTkEntry(master=  frame, placeholder_text="valeur du cc")
        valeur_note.pack(padx= 12)


        type_note = ctk.CTkEntry(master=  frame, placeholder_text="type de note")
        type_note.pack(padx= 12)

        annee_scolaire = ctk.CTkEntry(master=  frame, placeholder_text="anné scolaire")
        annee_scolaire.pack(pady= 12)

        semestre = ctk.CTkEntry(master=  frame, placeholder_text="semestres ")
        semestre.pack(padx= 12)

        poids_note = ctk.CTkEntry(master=  frame, placeholder_text="poids ")
        poids_note.pack(padx= 12)

        id_etudiant = ctk.CTkEntry(master=  frame, placeholder_text="id etudiant")
        id_etudiant.pack(padx= 12)


        id_matiere = ctk.CTkEntry(master=  frame, placeholder_text="id matiere")
        id_matiere.pack(padx= 12)

        id_enseignat = ctk.CTkEntry(master=  frame, placeholder_text="id enseignat")
        id_enseignat.pack(pady= 12)

        note_cc = ctk.CTkEntry(master=  frame, placeholder_text="note cc")
        note_cc.pack(padx= 12)


        note_sn = ctk.CTkEntry(master=  frame, placeholder_text="note sn")
        note_sn.pack(padx= 12)

        id_cote = ctk.CTkEntry(master=  frame, placeholder_text="id cote")
        id_cote.pack(pady= 12)


        button = ctk.CTkButton(master=frame, text="Ajouter",command=creationn)
        button.pack(padx=10, pady=12)

        button = ctk.CTkButton(master=frame3, text="Annuler",command=fermer)
        button.pack(padx=10, pady=12)

        table26 = ttk.Treeview(droit_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12), height=20, show= "headings")
        table26.pack(fill="both",pady=10,padx=10)
        table26.heading(1,text = "****")
        table26.heading(2,text = "")
        table26.heading(3,text = "")
        table26.heading(4,text = "")
            
            

            #colonnes
        table26.column(1,width=20)
        table26.column(2,width=70)
        table26.column(3,width=70)
        table26.column(4,width=70)
        table26.column(5,width=20)
        table26.column(6,width=70)
        table26.column(7,width=70)
        table26.column(8,width=70)
        table26.column(9,width=20)
        table26.column(10,width=70)
        table26.column(11,width=70)
        table26.column(12,width=70)
            
            
        import pymysql

        con76 = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con76.cursor()

        query = 'select * from note;'

        r = cursor.execute(query)

        for ligne in cursor:
            table26.insert('',END, value= ligne)


        ajouterEl.mainloop()