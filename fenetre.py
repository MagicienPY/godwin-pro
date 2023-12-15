import customtkinter as ctk
import mysql.connector
from subprocess import call
from tkinter import messagebox
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sqlite3
import pymysql


class bul:
    global essaie
    essaie = 0

    #dep = Vue()
    def __init__(self):
        pass
    def fen(self):

        def fermer ():
            bulletin.destroy()
        def tentative ():
            global essaie
            essaie += 1
            lable1 = ctk.CTkLabel(master= bulletin, text = "nombre de tentative restante  "+str(essaie),bg_color="red")
            lable1.pack(padx= 1, pady= 0)

            
            #messagebox.showinfo("nombre de tentative restante",essaie)
            if essaie==3:
                messagebox.showinfo("Attention","vous n'avez plus d'autre tentative !")
                bulletin.destroy()


        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")


        bulletin = ctk.CTk()
        bulletin.title("MYSCOLAR")
        bulletin.geometry("1000x900")

        #une frame au centre

        frame = ctk.CTkFrame(master= bulletin)
        frame.pack(padx = 220, pady = 60, fill= "both", expand = True) 

        frame3 = ctk.CTkFrame(master= bulletin,width=200,height=300)
        frame3.place(x = 0, y = 60) 


        #label

        lable = ctk.CTkLabel(master= frame, text = "BULLETIN TRIMESTRIELLE")
        lable.pack(padx= 20, pady= 2)


        ##################################################################
        ac = "2022-2023"
        o = ttk.Combobox(frame, values=[ac, ac, ac, ac])
        o.pack (padx= 20, pady= 2, fill= "x", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
                print(o.get())
        l = ctk.CTkLabel(master=frame,text = "Anné sci",font=("arial",14) )
        l.pack(padx= 20, pady= 2,fill="x",expand=False)
        #####################################################################
        ##################################################################
        ac = "1"
        o = ttk.Combobox(frame, values=[ac, ac, ac, ac])
        o.pack (padx=20, pady=10, fill= "x", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
                print(o.get())
        l = ctk.CTkLabel(master=frame,text = "trimestres",font=("arial",14) )
        l.pack(padx=20, pady=10,fill="x",expand=False)
        #####################################################################



        ##################################################################
        ac2 = "premier"
        o = ttk.Combobox(frame, values=[ac2, ac, ac2, ac])
        o.pack (padx= 20, pady= 2, fill= "x", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
                print(o.get())
        l = ctk.CTkLabel(master=frame,text = "classe",font=("arial",14) )
        l.pack(padx= 20, pady= 2,fill="x",expand=False)
        #####################################################################
        ##################################################################
        ac = "1"
        o = ttk.Combobox(frame, values=[ac, ac, ac, ac])
        o.pack (padx=20, pady=10, fill= "x", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
                print(o.get())
        l = ctk.CTkLabel(master=frame,text = "matricul",font=("arial",14) )
        l.pack(padx=20, pady=10,fill="x",expand=False)
        #####################################################################

        #chama.pack(padx= 12)



        button = ctk.CTkButton(master=frame, text="imprimer",command=quit)
        button.pack(padx=20, pady=12)

        button = ctk.CTkButton(master=frame3, text="Annuler",command=bulletin.destroy)
        button.pack(padx=20, pady=12)

        bulletin.mainloop()