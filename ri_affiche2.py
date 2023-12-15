from importation import *
from tkinter import *
import tkinter.messagebox as msgbox
import customtkinter as ctk
from datetime import date, datetime
import time
class Vueri:
    

    def __init__(self):
        pass
    def acceuil(self):
        def mode ():
            if (ctk.get_appearance_mode() == "Light"):
                ctk.set_appearance_mode("Dark")
            else:
                ctk.set_appearance_mode("Light")
            
        #ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Light")
        #customtkinter.set_appearance_mode("Dark")
        #ctk.set_appearance_mode("System")  # macOS only

        print(ctk.get_appearance_mode())

        root = ctk.CTk()
        root.title("GestnOTE")
        root.geometry("1000x500")
#frame pricipale
        haut_frame = ctk.CTkFrame(master=root,fg_color="light gray",border_width=10,border_color="dark blue")
        haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

        droit_frame = ctk.CTkFrame(master=root,fg_color="dark gray",corner_radius=15)
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

        gauche_frame = ctk.CTkFrame(master=root,fg_color="dark gray",width=700)
        gauche_frame.pack(side="left",fill="both",expand=False)
#fin frame pricipale
#frame interne
        frame = ctk.CTkFrame(master=haut_frame,fg_color="orange")
        frame.pack(side="top", fill= "both", expand = True) 
        button = ctk.CTkButton(master=frame, text="light/black",command=mode)
        button.pack(side="right")
        
        letitre = ctk.CTkLabel(master=frame,text = "GESTION DE NOTES",font=("arial",40) )
        letitre.pack(side="top",fill="x",expand=False)

        frame1 = ctk.CTkFrame(master=gauche_frame,fg_color="light green")
        frame1.pack(side="top", fill= "both", expand = True) 

        frame3 = ctk.CTkFrame(master=gauche_frame,fg_color="orange")
        frame3.pack(side="bottom", fill= "both", expand = True) 

        frame2 = ctk.CTkFrame(master=gauche_frame,fg_color="dark blue")
        frame2.pack(side="bottom", fill= "both", expand = True) 

        


#fin frame interne


   #bare de menu

        menub = Menu(root)
        filemenu = Menu(menub,tearoff=0)
        filemenu.add_command(label="nouvelles demandes",command=lambda: Vue.taches(self))
        filemenu.add_command(label="demande attentes",command=lambda: Vue.attentetaches(self))
        filemenu.add_command(label="demande validé",command=lambda: g1.permission)

        filemenu.add_separator()

        filemenu.add_command(label="sortir", command=root.quit)
        menub.add_cascade(label="nouveaux", menu=filemenu)

        #+
        filemenu2 = Menu(menub,tearoff=0)
        filemenu2.add_command(label="demandes migrés",command=lambda: g1.actualiser)
        filemenu2.add_command(label="demandes recu",command=lambda: g1.actualiser)
        

        filemenu2.add_separator()

        filemenu2.add_command(label="creer permissions", command=root.quit)
        menub.add_cascade(label="transfert", menu=filemenu2)

        root.config(menu=menub)
    #fin menu
##tableu
        table = ttk.Treeview(droit_frame,columns=(1,2,3,4), height=20, show= "headings")
        table.pack(fill="both",pady=10,padx=10)
        table.heading(1,text = "id")
        table.heading(2,text = "Niveau")
        table.heading(3,text = "section")
        table.heading(4,text = "date")
        

        #colonnes
        table.column(1,width=20)
        table.column(2,width=70)
        table.column(3,width=70)
        table.column(4,width=70)
        
        import pymysql

        con = pymysql.connect(user='root', password ='',database = 'gestion_note')
        cursor = con.cursor()

        query = 'select * from Classe;'

        r = cursor.execute(query)

        for ligne in cursor:
            table.insert('',END, value= ligne)

        con.close()



##fin tableau

        table2 = ctk.CTkTabview(master=droit_frame)
        table2.pack(fill="both",pady=10,padx=10)

        

    #champ frame gauche
        def ins():
            con = pymysql.connect(user='root', password ='',database = 'gestion_note')
            cursor = con.cursor()

            query = 'select * from Classe;'
            matri =  chama.get()
            niv =  chama1.get()
            sec =  chama2.get()
            r = cursor.execute(query)

            maintenant = datetime.now()
            ctime = maintenant.strftime("%H:%M:%S")

            jour = date.today()
            nday = jour.strftime("%y-%m-%d")

            print(ctime)
            query2 = 'INSERT INTO  Classe (Id_classe,Niveau,Section) VALUES  (%s, %s, %s);'
            cursor.execute(query2,(matri,niv,sec))
            
            print(nday)

        chama = ctk.CTkEntry(master=frame1, placeholder_text="id",font=("time_new_roman",10))
        chama.pack(pady=20)
        chama1 = ctk.CTkEntry(master= frame1, placeholder_text="Niveau",font=("time_new_roman",10))
        chama1.pack(pady=10)

        chama2 = ctk.CTkEntry(master=frame1, placeholder_text="Section",font=("time_new_roman",10))
        chama2.pack(pady=10)
        

        button2 = ctk.CTkButton(master=frame1, text="ajouter",command=ins)
        button2.pack(pady=10)

        button3 = ctk.CTkButton(master=frame1, text="supprimer",command=ins)
        button3.pack(pady=12)

        button4 = ctk.CTkButton(master=frame1, text="modifier",command=ins)
        button4.pack(pady=14)

        root.mainloop()



        


   