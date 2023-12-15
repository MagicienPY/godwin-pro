import customtkinter as ctk
import mysql.connector
from subprocess import call
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog

import sqlite3
import pymysql


class ajouterEl:
    def __init__(self):
        pass
    def ajouet(self):
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

                
        def browse_file():
            filename = filedialog.askopenfilename(initialdir = "/",title = "importer phhoto",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))  
            label_file_exp.configure(text=filename)
        def creatione():
        # mysqldb = mysql.connector.connect(host="192.168.43.154", user="root", password="",database="gestage")
        # mycursor = mysqldb.cursor()
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                #print("connecté avec succes")
                iden = id_etudiant.get()
                mat_e = mat_etudiant.get()
                cin_et = cin_etudiant.get()
                daten = daten_etu.get()
                lieun = lieun_etu.get()
                add = adress_etu.get()
                tel =  tel_etu.get()
                nom = nom_etu.get()
                prenom = prenom_etu.get()
                #photo = btn_browse.get()
                selected = selected_class.get()
                id_cl = int(selected.split(" - ")[1]) 
                #print("id --",id_cl)
                
                from PIL import Image
                import io

               # image = Image.open(label_file_exp.cget("text"))

                chemin_image = label_file_exp.cget("text")

                #print(chemin_image)
               
                #print(iden, mat_e, cin_et, daten, lieun, add, tel, nom, prenom, id_cl, chemin_image)
                #print(" c'est bon 1")
                command="use g_note"
                cursor.execute(command)
                sql = "INSERT INTO etudiant (id_etudiant, mat_etudiant, cin_etudiant, daten_etu, lieun_etu, adress_etu, tel_etu, nom_etu, prenom_etu, id_classe, tof) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
                #sql1 = "INSERT INTO note (id_note, valeur_note, type_note , annee_scolaire, semestre, poids_note, id_etudiant, id_matiere, id_enseignant, note_cc, note_sn, id_cote) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s)"
                cursor.execute(sql, (iden, mat_e, cin_et, daten, lieun, add, tel, nom, prenom, id_cl, chemin_image))
                
              #  cursor.execute(sql1, (NULL, NULL, NULL, NULL, NULL, NULL, id_etudiant, NULL, NULL, NULL, NULL, NULL))                

                con.commit()
                messagebox.showinfo(" cool ", " Enregistrement reussit !!")
                ajouterEl.destroy()
            except:
                messagebox.showinfo(" attention ", " un soucis veuillez verifier vos informations !")



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

        droit_frame = ctk.CTkFrame(master=ajouterEl,fg_color="dark gray")
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)


        #label
        #print("ajoue d'etudiant")
        lable = ctk.CTkLabel(master= frame, text = "Ajoue d'Etudiant")
        lable.pack(padx= 12, pady= 10)




        id_etudiant = ctk.CTkEntry(master=  frame, placeholder_text="identifiant")
        id_etudiant.pack(padx= 12)

        mat_etudiant = ctk.CTkEntry(master=  frame, placeholder_text="mat_etudiant")
        mat_etudiant.pack(padx= 12)


        cin_etudiant = ctk.CTkEntry(master=  frame, placeholder_text="cin_etudiant")
        cin_etudiant.pack(padx= 12)

        daten_etu = ctk.CTkEntry(master=  frame, placeholder_text="daten_etu")
        daten_etu.pack(pady= 12)

        lieun_etu = ctk.CTkEntry(master=  frame, placeholder_text="lieun_etu")
        lieun_etu.pack(padx= 12)

        adress_etu = ctk.CTkEntry(master=  frame, placeholder_text="adress_etu")
        adress_etu.pack(padx= 12)

        tel_etu = ctk.CTkEntry(master=  frame, placeholder_text="tel_etu")
        tel_etu.pack(padx= 12)


        nom_etu = ctk.CTkEntry(master=  frame, placeholder_text="nom_etu")
        nom_etu.pack(padx= 12)

        prenom_etu = ctk.CTkEntry(master=  frame, placeholder_text="prenom_etu")
        prenom_etu.pack(pady= 12)
        import pymysql
        con = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con.cursor()
        
        cursor.execute("SELECT id_classe, nom_classe FROM classe")
        classes = cursor.fetchall()

        # Liste des options
        options = []
        for id_classe, nom_classe in classes:
            options.append(f"{nom_classe} - {id_classe}")
         # Variable pour la sélection  
        selected_class = tk.StringVar() 
        class_list = tk.OptionMenu(frame, selected_class, options)
        class_list.pack()



        label_file = Label(frame, text="photo etufiant")
        label_file.pack()
        label_file_exp = Label(frame)
        label_file_exp.pack()
        btn_browse = Button(frame, text = "photo",command=browse_file)
        btn_browse.pack()

        button = ctk.CTkButton(master=frame, text="Ajouter",command=creatione)
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

        query = 'select * from etudiant;'

        r = cursor.execute(query)

        for ligne in cursor:
            table26.insert('',END, value= ligne)


        ajouterEl.mainloop()
