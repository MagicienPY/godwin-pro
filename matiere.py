#from importation import *
from tkinter import *
import tkinter.messagebox as msgbox
import customtkinter as ctk
import tkinter.ttk as ttk
import aspose.pdf as pdf
from fenetre import *
from ajouterEl import *

class Matier:
    

    def __init__(self):
        pass
    def acceuil2(self):
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

        acceuil2 = ctk.CTk()
        acceuil2.title("MYSCOLAR")
        acceuil2.geometry("1000x900")
#frame pricipale
        haut_frame = ctk.CTkFrame(master=acceuil2,fg_color="light gray",border_width=10,border_color="dark blue")
        haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

        droit_frame = ctk.CTkFrame(master=acceuil2,fg_color="dark gray")
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

        gauche_frame = ctk.CTkFrame(master=acceuil2,fg_color="dark gray",width=700)
        gauche_frame.pack(side="left",fill="both",expand=False)
#fin frame pricipale
#frame interne
        frame = ctk.CTkFrame(master=haut_frame,fg_color="Dodgerblue2")
        frame.pack(side="top", fill= "both", expand = True) 
        button = ctk.CTkButton(master=frame, text="light/black",command=mode)
        button.pack(side="right")
        letitre = ctk.CTkLabel(master=frame,text = "MYSCOLAR",font=("arial",40) )
        letitre.pack(side="top",fill="x",expand=False)



        frame1 = ctk.CTkFrame(master=gauche_frame,fg_color="medium spring green")
        frame1.pack(side="top", fill= "both", expand = True) 
        
       

        frame3 = ctk.CTkFrame(master=gauche_frame,fg_color="orange")
        frame3.pack(side="bottom", fill= "both", expand = True) 



        frame2 = ctk.CTkFrame(master=haut_frame,fg_color="medium spring green")
        frame2.pack(side="bottom", fill= "both", expand = True) 

        def pdf ():
            # Créer un nouveau document PDF
            doc = pdf.Document()  

            # Ajouter une page
            page = doc.Pages.Add()

            # Récupérer le contexte graphique de la page  
            gfx = pdf.Graphics(page)

            # Imprimer du texte
            gfx.DrawString("Bonjour je suis le magicien", pdf.Font(pdf.FontFamily.HELVETICA, 20), pdf.Brushes.Black, 100, 100)

            # Imprimer des données issues d'une variable
            nom = "Marc"
            gfx.DrawString(nom, pdf.Font(pdf.FontFamily.HELVETICA, 20), pdf.Brushes.Black, 100, 150) 

            # Imprimer une liste
            liste = ["Item 1", "Item 2", "Item 3"]
            for i, item in enumerate(liste):
                gfx.DrawString(item, pdf.Font(pdf.FontFamily.HELVETICA, 12), pdf.Brushes.Black, 100, 200+i*20)

            # Enregistrer le document
            doc.Save("document.pdf")
##################################################################
        
        a = "2019-2020"
        o1 = ttk.Combobox(frame2, values=[a, a, a, a])
        o1.pack (side="left", fill= "x", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
        l1 = ctk.CTkLabel(master=frame2,text = "date",font=("arial",14) )
        l1.pack(side="left",fill="y",expand=False)

##################################################################
        ac = "1"
        o = ttk.Combobox(frame2, values=[ac, ac, ac, ac])
        o.pack (side="left", fill= "y", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
        l = ctk.CTkLabel(master=frame2,text = "trimestres",font=("arial",14) )
        l.pack(side="left",fill="y",expand=False)
#####################################################################
        b = "premier"

        o2 = ttk.Combobox(frame2, values=[b, b, b, b])
        o2.pack (side="left", fill= "y", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
        l2 = ctk.CTkLabel(master=frame2,text = "classe",font=("arial",14) )
        l2.pack(side="left",fill="y",expand=False)


##################################################################



#########################**********************

##################################################################
        
        a = "2019-2020"
        o1 = ttk.Combobox(frame2, values=[a, a, a, a])
        o1.pack (side="left", fill= "x", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
        l1 = ctk.CTkLabel(master=frame2,text = "date",font=("arial",14) )
        l1.pack(side="left",fill="y",expand=False)

##################################################################
        ac = "1"
        o = ttk.Combobox(frame2, values=[ac, ac, ac, ac])
        o.pack (side="left", fill= "y", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
        l = ctk.CTkLabel(master=frame2,text = "trimestres",font=("arial",14) )
        l.pack(side="left",fill="y",expand=False)
#####################################################################
        b = "premier"

        o2 = ttk.Combobox(frame2, values=[b, b, b, b])
        o2.pack (side="left", fill= "y", expand = False)

        def print_file () :                     # voir le chapitre sur les événements
            print(o.get())
        l2 = ctk.CTkLabel(master=frame2,text = "classe",font=("arial",14) )
        l2.pack(side="left",fill="y",expand=False)


##################################################################

        bu = bul()
        
        button2 = ctk.CTkButton(master=frame1, text="bulletin",command=bu.fen)
        button2.pack(side="top", fill= "x", expand = False) 
##################################################################
        button12 = ctk.CTkButton(master=frame1, text="afficher",command=mode)
        button12.pack(side="top", fill= "x", expand = False)
#####################################################################
        button13 = ctk.CTkButton(master=frame1, text="imprimer",command=pdf)
        button13.pack(side="top", fill= "x", expand = False)
######################################################################

#fin frame interne


   #bare de menu
        aj = ajouterEl()
        menub = Menu(acceuil2)
        filemenu = Menu(menub,tearoff=0)
        menub.add_cascade(label="fichier", menu=filemenu)
        filemenu.add_command(label="nouveaux eleve",command=lambda: aj.ajoue())
        filemenu.add_command(label="classe",command=lambda: Vue.attentetaches(self))
        filemenu.add_command(label="enseignant",command=lambda: g1.permission)
        filemenu.add_command(label="matieres",command=lambda: Vue.taches(self))
        filemenu.add_command(label="tables de moyennes",command=lambda: Vue.attentetaches(self))
        filemenu.add_command(label="calculatrice",command=lambda: g1.permission)
        filemenu.add_separator()
        filemenu.add_command(label="sortir", command=acceuil2.destroy)
        

        #+
        filemenu2 = Menu(menub,tearoff=0)
        menub.add_cascade(label="fiche de note", menu=filemenu2)
        filemenu2.add_command(label="par ordre de merite/classe",command=lambda: g1.actualiser)
        filemenu2.add_command(label="resultat de fin An",command=lambda: g1.actualiser)
        filemenu2.add_command(label="stats",command=lambda: g1.actualiser)
        filemenu2.add_separator()
        filemenu2.add_command(label="relevé de note / trim", command=acceuil2.quit)
        

        #+
        filemenu3 = Menu(menub,tearoff=0)
        menub.add_cascade(label="attestation", menu=filemenu3)

        #+
        filemenu4 = Menu(menub,tearoff=0)
        menub.add_cascade(label="parametre", menu=filemenu4)

        #+
        filemenu5 = Menu(menub,tearoff=0)
        menub.add_cascade(label="sauvegarde", menu=filemenu5)

        acceuil2.config(menu=menub)
    #fin menu


        table = ttk.Treeview(droit_frame,columns=(1,2,3,4), height=20, show= "headings")
        table.pack(fill="both",pady=10,padx=10)
        table.heading(1,text = "Libelle")
        table.heading(2,text = "coefficien")
        table.heading(3,text = "id matiere")
        table.heading(4,text = "*****")
        

        #colonnes
        table.column(1,width=20)
        table.column(2,width=70)
        table.column(3,width=70)
        table.column(4,width=70)
        
        
        import pymysql

        con = pymysql.connect(user='root', password ='',database = 'myscolar')
        cursor = con.cursor()
#Matiere.Libelle, Matiere_trimestre.Coefficient
        query = 'select  Matiere.Libelle, Matiere_Trimestre.Coefficient ,Matiere.Id_matiere from Matiere inner join Matiere_Trimestre on Matiere.Id_matiere = Matiere_Trimestre.Id_matiere ;'
        #query2 = 'select * from Matiere '
        r = cursor.execute(query)

        for ligne in cursor:
            table.insert('',END, value= ligne)

        con.close()



##fin tableau

        table2 = ctk.CTkTabview(master=droit_frame)
        table2.pack(fill="both",pady=10,padx=10)


    #champ frame gauche
        chama = ctk.CTkEntry(master=frame1, placeholder_text="matricule",font=("time_new_roman",10))
        chama.pack(pady=20)
        chama1 = ctk.CTkEntry(master= frame1, placeholder_text="matricule",font=("time_new_roman",10))
        chama1.pack(pady=10)

        chama2 = ctk.CTkEntry(master=frame1, placeholder_text="matricule",font=("time_new_roman",10))
        chama2.pack(pady=10)
        chama3 = ctk.CTkEntry(master= frame1, placeholder_text="matricule",font=("time_new_roman",10),width=100,height=100)
        chama3.pack(pady=20)

        button2 = ctk.CTkButton(master=frame1, text="valider",command=mode)
        button2.pack(pady=10)








        #acceuil2.mainloop()

#ri = Vueri()

#ri.acceuil2()

        


   