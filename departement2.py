#from importation import *
from tkinter import *
import tkinter.messagebox as msgbox
import customtkinter as ctk
import tkinter.ttk as ttk
import aspose.pdf as pdf
from fenetre import *
from ajouterEl import *
from ajouternote import *
from matiere import *
from fonctions import *
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, LongTable, TableStyle
from reportlab.platypus.tables import Table
import pymysql
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
from taux_par_classe import *
from calc import *
from table_moyen import *
from table_moyen2 import bul
from bulletin_indiv import *
from bon_grand_b import *
from ajouterUSER import *
from br import *

class Vueri:
    

    def __init__(self):
        pass
    def acceuil(self,nom, matricule,passe, role):
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

        ##print(ctk.get_appearance_mode())

        acceuil = ctk.CTk()
        acceuil.title("GODWIN")
        acceuil.geometry("1000x900")
        #print(nom, matricule, passe , role)
#frame pricipale
        haut_frame = ctk.CTkFrame(master=acceuil,fg_color="light gray",border_width=10,border_color="dark blue")
        haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

        droit_frame = ctk.CTkFrame(master=acceuil,fg_color="dark gray")
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

        gauche_frame = ctk.CTkFrame(master=acceuil,fg_color="dark gray",width=700)
        gauche_frame.pack(side="left",fill="both",expand=False)
#fin frame pricipale
#frame interne
        def open_modules():
            pass
            # Code pour ouvrir la page de gestion des modules
            #print("Ouvrir la page de gestion des modules")
        
            # Afficher le tableau des modules

        def open_bilan():
            # Code pour ouvrir la page de gestion des matières
            
            #print("Ouvrir la page de bilan")
            window = tk.Toplevel()
            window.title("bilan et bulettin")

            haut_frame = ctk.CTkFrame(master=window,fg_color="light gray",border_width=10,border_color="dark blue")
            haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

            droit_frame = ctk.CTkFrame(master=window,fg_color="dark gray")
            droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

            gauche_frame = ctk.CTkFrame(master=window,fg_color="dark gray",width=700)
            gauche_frame.pack(side="left",fill="both",expand=False)
    #fin frame pricipale

            ##################################################################
            chama7 = ctk.CTkEntry(master=gauche_frame, placeholder_text="identifiant",font=("time_new_roman",10))
            chama7.pack(side="top", fill= "x", expand = False) 
            chama8 = ctk.CTkEntry(master= gauche_frame, placeholder_text="nom",font=("time_new_roman",10))
            chama8.pack(side="top", fill= "x", expand = False) 

            chama9 = ctk.CTkEntry(master=gauche_frame, placeholder_text="id_module",font=("time_new_roman",10))
            chama9.pack(side="top", fill= "x", expand = False) 

            chama10 = ctk.CTkEntry(master=gauche_frame, placeholder_text="coeficiant",font=("time_new_roman",10))
            chama10.pack(side="top", fill= "x", expand = False) 
            image_pil = Image.open("logo/godwin.jpg")

            # Définir la nouvelle taille souhaitée
            nouvelle_taille = (100, 100)

            # Redimensionner l'image
            image_redimensionnee = image_pil.resize(nouvelle_taille)

            # Convertir l'image PIL en un objet Tkinter
            image_tk = ImageTk.PhotoImage(image_redimensionnee)

            # Créer un widget Label pour afficher l'image redimensionnée
            profile_photo_label = ttk.Label(haut_frame, image=image_tk)
            profile_photo_label.image = image_tk
            profile_photo_label.pack()

            iden = chama7.get()
            nom = chama8.get()
            id_module = chama9.get()
            coef = chama10.get()
            def actualiser2 ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    # Supprimer tous les éléments existants dans la table
                    
                    table2.delete(*table2.get_children())
                        # Récupérer les données depuis la base de données
                    cursor = con.cursor()
                    
                    cursor.execute("SELECT * FROM matiere")
                    data = cursor.fetchall()
                    #print("ok1")
                    
                        # Insérer les données dans le tableau
                    for row in data:
                        table2.insert("", "end", values=row)

                   # messagebox.showinfo("actualisé","page a ete actualisé!")

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
        ###############################

            def ajouterMatier ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama7.get()
                    nom = chama8.get()
                    id_module = chama9.get()
                    coef = chama10.get()
                    
                    actualiser2()
                
                    sql = "INSERT INTO matiere (id_matiere, nom_matiere, id_module, coef_matiere) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (iden, nom, id_module, coef))
                        
                    con.commit()
                    actualiser2()
                    con.close()

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def supprimerMatier():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama7.get()
                    
                    actualiser2()
                    

                    sql = "DELETE FROM matiere WHERE id_matiere = %s"
                    cursor.execute(sql, (iden))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def modifierMatier ():
                try:

                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                # f = fonc()
                    iden = chama7.get()
                    nom = chama8.get()
                    id_module = chama9.get()
                    coef = chama10.get()
                    actualiser2()
                    
                    # 696354742 BA2B ############################################

                    sql = "UPDATE matiere SET nom_matiere = %s, coef_matiere = %s, id_module = %s WHERE id_matiere = %s"
                    cursor.execute(sql, (nom, coef,id_module, iden ))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
           
           
            button2 = ctk.CTkButton(master=gauche_frame, text="ajouter",command=ajouterMatier)
            button2.pack(side="top", fill= "x", expand = False) 
    ##################################################################
            button12 = ctk.CTkButton(master=gauche_frame, text="modifier",command=modifierMatier)
            button12.pack(side="top", fill= "x", expand = False)
    #####################################################################
            button13 = ctk.CTkButton(master=gauche_frame, text="supprimer",command=supprimerMatier)
            button13.pack(side="top", fill= "x", expand = False)


            table2 = ttk.Treeview(droit_frame,columns=(1,2,3,4), height=20, show= "headings")
            table2.pack(fill="both",pady=10,padx=10)
            table2.heading(1,text = "identifiant")
            table2.heading(2,text = "Nom matiere")
            table2.heading(3,text = "id_module")
            table2.heading(4,text = "coef")
            
            

            #colonnes
            table2.column(1,width=20)
            table2.column(2,width=70)
            table2.column(3,width=70)
            table2.column(4,width=70)
            
            
            import pymysql

            con76 = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con76.cursor()

            query = 'select * from matiere;'

            r = cursor.execute(query)

            for ligne in cursor:
                table2.insert('',END, value= ligne)

        

            con76.close()

        def open_matieres():
            # Code pour ouvrir la page de gestion des matières
            
            #print("Ouvrir la page de gestion des matières")
            window = tk.Toplevel()
            window.title("gestion de matiere")

            haut_frame = ctk.CTkFrame(master=window,fg_color="light gray",border_width=10,border_color="dark blue")
            haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

            droit_frame = ctk.CTkFrame(master=window,fg_color="dark gray")
            droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

            gauche_frame = ctk.CTkFrame(master=window,fg_color="dark gray",width=700)
            gauche_frame.pack(side="left",fill="both",expand=False)
    #fin frame pricipale

            ##################################################################
            chama7 = ctk.CTkEntry(master=gauche_frame, placeholder_text="identifiant",font=("time_new_roman",10))
            chama7.pack(side="top", fill= "x", expand = False) 
            chama8 = ctk.CTkEntry(master= gauche_frame, placeholder_text="nom",font=("time_new_roman",10))
            chama8.pack(side="top", fill= "x", expand = False) 

            chama9 = ctk.CTkEntry(master=gauche_frame, placeholder_text="id_module",font=("time_new_roman",10))
            chama9.pack(side="top", fill= "x", expand = False) 

            chama10 = ctk.CTkEntry(master=gauche_frame, placeholder_text="coeficiant",font=("time_new_roman",10))
            chama10.pack(side="top", fill= "x", expand = False) 

            image_pil = Image.open("logo/godwin.jpg")

            # Définir la nouvelle taille souhaitée
            nouvelle_taille = (100, 100)

            # Redimensionner l'image
            image_redimensionnee = image_pil.resize(nouvelle_taille)

            # Convertir l'image PIL en un objet Tkinter
            image_tk = ImageTk.PhotoImage(image_redimensionnee)

            # Créer un widget Label pour afficher l'image redimensionnée
            profile_photo_label = ttk.Label(haut_frame, image=image_tk)
            profile_photo_label.image = image_tk
            profile_photo_label.pack()

            iden = chama7.get()
            nom = chama8.get()
            id_module = chama9.get()
            coef = chama10.get()
            def actualiser2 ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    # Supprimer tous les éléments existants dans la table
                    
                    table2.delete(*table2.get_children())
                        # Récupérer les données depuis la base de données
                    cursor = con.cursor()
                    
                    cursor.execute("SELECT * FROM matiere")
                    data = cursor.fetchall()
                    #print("ok1")
                    
                        # Insérer les données dans le tableau
                    for row in data:
                        table2.insert("", "end", values=row)

                   # messagebox.showinfo("actualisé","page a ete actualisé!")

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
        ###############################

            def ajouterMatier ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama7.get()
                    nom = chama8.get()
                    id_module = chama9.get()
                    coef = chama10.get()
                    
                    actualiser2()
                
                    sql = "INSERT INTO matiere (id_matiere, nom_matiere, id_module, coef_matiere) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (iden, nom, id_module, coef))
                        
                    con.commit()
                    actualiser2()
                    con.close()

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def supprimerMatier():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama7.get()
                    
                    actualiser2()
                    

                    sql = "DELETE FROM matiere WHERE id_matiere = %s"
                    cursor.execute(sql, (iden))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def modifierMatier ():
                try:

                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                # f = fonc()
                    iden = chama7.get()
                    nom = chama8.get()
                    id_module = chama9.get()
                    coef = chama10.get()
                    actualiser2()
                    
                    # 696354742 BA2B ############################################

                    sql = "UPDATE matiere SET nom_matiere = %s, coef_matiere = %s, id_module = %s WHERE id_matiere = %s"
                    cursor.execute(sql, (nom, coef,id_module, iden ))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
           
           
            button2 = ctk.CTkButton(master=gauche_frame, text="ajouter",command=ajouterMatier)
            button2.pack(side="top", fill= "x", expand = False) 
    ##################################################################
            button12 = ctk.CTkButton(master=gauche_frame, text="modifier",command=modifierMatier)
            button12.pack(side="top", fill= "x", expand = False)
    #####################################################################
            button13 = ctk.CTkButton(master=gauche_frame, text="supprimer",command=supprimerMatier)
            button13.pack(side="top", fill= "x", expand = False)


            table2 = ttk.Treeview(droit_frame,columns=(1,2,3,4), height=20, show= "headings")
            table2.pack(fill="both",pady=10,padx=10)
            table2.heading(1,text = "identifiant")
            table2.heading(2,text = "Nom matiere")
            table2.heading(3,text = "id_module")
            table2.heading(4,text = "coef")
            
            

            #colonnes
            table2.column(1,width=20)
            table2.column(2,width=70)
            table2.column(3,width=70)
            table2.column(4,width=70)
            
            
            import pymysql

            con76 = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con76.cursor()

            query = 'select * from matiere;'

            r = cursor.execute(query)

            for ligne in cursor:
                table2.insert('',END, value= ligne)

        

            con76.close()

        def openordre():
            # Code pour ouvrir la page de gestion des matières
            
            #print("Ouvrir la page de de resultat")
            window = tk.Toplevel()
            window.title("ordre par classe")

            haut_frame = ctk.CTkFrame(master=window,fg_color="light gray",border_width=10,border_color="dark blue")
            haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

            droit_frame = ctk.CTkFrame(master=window,fg_color="dark gray")
            droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

            gauche_frame = ctk.CTkFrame(master=window,fg_color="dark gray",width=700)
            gauche_frame.pack(side="left",fill="both",expand=False)
    #fin frame pricipale

            ##################################################################
            chama71 = ctk.CTkEntry(master=gauche_frame, placeholder_text="matricule etudiant",font=("time_new_roman",10))
            chama71.pack(side="top", fill= "x", expand = False) 
            
            image_pil = Image.open("logo/godwin.jpg")

            # Définir la nouvelle taille souhaitée
            nouvelle_taille = (100, 100)

            # Redimensionner l'image
            image_redimensionnee = image_pil.resize(nouvelle_taille)

            # Convertir l'image PIL en un objet Tkinter
            image_tk = ImageTk.PhotoImage(image_redimensionnee)

            # Créer un widget Label pour afficher l'image redimensionnée
            profile_photo_label = ttk.Label(haut_frame, image=image_tk)
            profile_photo_label.image = image_tk
            profile_photo_label.pack()

            iden = chama71.get()
           
            def actualiser22 ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    # Supprimer tous les éléments existants dans la table
                    
                    tableresultat.delete(*tableresultat.get_children())
                        # Récupérer les données depuis la base de données
                    cursor = con.cursor()
                    
                    cursor.execute("SELECT note.semestre, matiere.nom_matiere, note.note_cc, note.note_sn, matiere.coef_matiere ,(note.note_cc*cote.cote_cc) + (note.note_sn* cote.cote_sn), etudiant.mat_etudiant, etudiant.nom_etu, note.type_note from cote INNER JOIN note on cote.id_cote = note.id_cote INNER JOIN matiere on note.id_matiere = matiere.id_matiere INNER JOIN etudiant on etudiant.id_etudiant = note.id_etudiant order by ((note.note_cc*cote.cote_cc) + (note.note_sn* cote.cote_sn)) desc;")
                    data = cursor.fetchall()
                    #print("ok1")
                    
                        # Insérer les données dans le tableau
                    for row in data:
                        tableresultat.insert("", "end", values=row)

                   # messagebox.showinfo("actualisé","page a ete actualisé!")

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme de d'actualisation")
        ###############################
            def recherche ():
                iden = chama71.get()
                
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    # Supprimer tous les éléments existants dans la table
                   # actualiser2()
                    tableresultat.delete(*tableresultat.get_children())
                    
                    #print("hey")
                        # Récupérer les données depuis la base de données
                    cursor = con.cursor()
                    #print("valeur du champ * ",iden)
                    sql1 = cursor.execute("SELECT note.semestre, matiere.nom_matiere, note.note_cc, note.note_sn, matiere.coef_matiere ,(note.note_cc*cote.cote_cc) + (note.note_sn* cote.cote_sn), etudiant.mat_etudiant, etudiant.nom_etu , note.type_note from cote INNER JOIN note on cote.id_cote = note.id_cote INNER JOIN matiere on note.id_matiere = matiere.id_matiere INNER JOIN etudiant on etudiant.id_etudiant = note.id_etudiant WHERE etudiant.mat_etudiant = %s order by (note.note_cc*cote.cote_cc) + (note.note_sn* cote.cote_sn);",(iden))
                   # cursor.execute(sql1, (iden))
                    data = cursor.fetchall()
                    #print("ok1")
                    
                        # Insérer les données dans le tableau
                    for row in data:
                        tableresultat.insert("", "end", values=row)

                   # messagebox.showinfo("actualisé","page a ete actualisé!")
                  #  actualiser22()

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme dans  le recherche")
        ###############################

            def ajouterMatier ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama7.get()
                    nom = chama8.get()
                    id_module = chama9.get()
                    coef = chama10.get()
                    
                    actualiser2()
                
                    sql = "INSERT INTO matiere (id_matiere, nom_matiere, id_module, coef_matiere) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (iden, nom, id_module, coef))
                        
                    con.commit()
                    actualiser2()
                    con.close()

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def afficher_bulletin():
                
                # Connexion à la base de données
                conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
                cursor = conn.cursor()

                # Requête SQL pour récupérer les informations des étudiants
                students_query = '''
                SELECT DISTINCT etudiant.mat_etudiant, etudiant.nom_etu
                FROM etudiant
                '''

                # Exécution de la requête pour récupérer les informations des étudiants
                cursor.execute(students_query)
                students = cursor.fetchall()

                # Requête SQL pour récupérer les données du bulletin de chaque étudiant
                bulletin_query = '''
               SELECT 
                    note.semestre, 
                    matiere.nom_matiere, 
                    matiere.coef_matiere,
                    etudiant.mat_etudiant, 
                    etudiant.nom_etu, 
                    note.type_note, 
                    (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) AS moyenne, 
                    RANK() OVER (PARTITION BY etudiant.mat_etudiant, note.semestre ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite,
                    classe.nom_classe
                FROM 
                    cote 
                INNER JOIN 
                    note ON cote.id_cote = note.id_cote 
                INNER JOIN 
                    matiere ON note.id_matiere = matiere.id_matiere 
                INNER JOIN 
                    etudiant ON etudiant.id_etudiant = note.id_etudiant 
                INNER JOIN
                    classe ON etudiant.id_classe = classe.id_classe
                WHERE 
                    note.type_note IN ("cc", "sn", "examen") 
                    AND etudiant.mat_etudiant = %s
                GROUP BY 
                    etudiant.mat_etudiant, note.semestre, matiere.nom_matiere, matiere.coef_matiere, classe.nom_classe
                ORDER BY 
                    classe.nom_classe, etudiant.mat_etudiant, note.semestre, moyenne DESC
                '''

                # Génération du bulletin individuel pour chaque étudiant
                for student in students:
                    mat_etudiant = student[0]
                    nom_etudiant = student[1]

                    # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
                    cursor.execute(bulletin_query, (mat_etudiant,))
                    results = cursor.fetchall()

                    # Création du document PDF en format paysage
                    doc = SimpleDocTemplate(f"ib/{mat_etudiant}.pdf", pagesize=landscape(letter))

                    # Liste pour contenir les éléments du document PDF
                    elements = []

                    # Style des paragraphes
                    styles = getSampleStyleSheet()
                    style_title = styles['Title']
                    style_heading = styles['Heading1']
                    style_body = styles['BodyText']

                    # Informations de l'étudiant
                    title = Paragraph("Bulletin GODWIN", style_title)
                    elements.append(title)

                    elements.append(Spacer(1, 20))
                    elements.append(Paragraph("INSTITU DE FORMATIN PROFESIONNELLE GODWIN", style_heading))
                    elements.append(Spacer(1, 20))
                    student_info = f"Nom de l'étudiant: {nom_etudiant}<br/>" \
                                f"Matricule de l'étudiant: {mat_etudiant}"
                    student_info = Paragraph(student_info, style_body)
                    elements.append(student_info)

                    elements.append(Spacer(1, 20))
                    elements.append(Paragraph("Détails du bulletin:", style_heading))

                    # Contenu du tableau
                    data = [
                        ["Semestre", "Liste des matières", "Somme des coefficients", "Moyenne", "Ordre de mérite"],
                    ]

                    for result in results:
                        semestre = result[0]
                        liste_matiere = result[1]
                        somme_coefficients = result[2]
                        moyenne = result[6]
                        ordre_merite = result[7]

                        data.append([semestre, liste_matiere, somme_coefficients, moyenne, ordre_merite])

                    # Création du tableau avec le style
                    table = Table(data)
                    style = TableStyle([
                        ('BACKGROUND', (0, 0),(-1, 0), colors.cyan),  # Couleur cyan pour les titres
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 14),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ])
                    table.setStyle(style)

                    # Ajout du tableau aux éléments du document
                    elements.append(table)

                    # Ajout du nom de l'établissement et de la signature
                    elements.append(Spacer(1, 20))

                    elements.append(Paragraph("Notez bien que les notes suivante sont les notes obtenus grace a vos note dans les differents controlesfais en classe", style_body))
                    elements.append(Spacer(1, 20))
                    elements.append(Paragraph("INSTITU DE FORMATIN PROFESIONNELLE GODWIN", style_heading))
                    elements.append(Paragraph("Etablissement: GODWIN", style_body))
                    elements.append(Paragraph("Application de gestion: GODWIN_manager", style_body))
                    elements.append(Paragraph("signature admin:", style_heading))
                    elements.append(Paragraph("signature parents:", style_heading))

                    # Génération du document PDF
                    doc.build(elements)

                # Fermeture de la connexion à la base de données
                conn.close()
            
            def imprimer_rs ():
                conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
                cursor = conn.cursor()                
                # Requête SQL pour récupérer les informations des étudiants
                students_query = '''
                SELECT DISTINCT etudiant.mat_etudiant, etudiant.nom_etu, etudiant.tof
                FROM etudiant
                '''

                # Exécution de la requête pour récupérer les informations des étudiants
                cursor.execute(students_query)
                students = cursor.fetchall()

                # Liste pour contenir les éléments de tous les bulletins
                all_bulletin_elements = []

                # Génération du bulletin individuel pour chaque étudiant
                for student in students:
                    mat_etudiant = student[0]
                    nom_etudiant = student[1]

                    # Requête SQL pour récupérer les données du bulletin de l'étudiant regroupées par semestre
                    bulletin_query = f'''
                    SELECT 
                        note.semestre, 
                        matiere.nom_matiere, 
                        matiere.coef_matiere,
                        etudiant.mat_etudiant, 
                        etudiant.nom_etu, 
                        note.type_note, 
                        (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) AS moyenne, 
                        RANK() OVER (PARTITION BY etudiant.mat_etudiant, note.semestre ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite
                    FROM 
                        cote 
                    INNER JOIN 
                        note ON cote.id_cote = note.id_cote 
                    INNER JOIN 
                        matiere ON note.id_matiere = matiere.id_matiere 
                    INNER JOIN 
                        etudiant ON etudiant.id_etudiant = note.id_etudiant 
                    WHERE 
                        note.type_note IN ("cc", "sn", "examen") 
                        AND etudiant.mat_etudiant = "{mat_etudiant}"
                    GROUP BY 
                        etudiant.mat_etudiant, note.semestre, matiere.nom_matiere, matiere.coef_matiere
                    ORDER BY 
                        note.semestre, moyenne DESC
                    '''

                    # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
                    cursor.execute(bulletin_query)
                    results = cursor.fetchall()

                    # Liste pour contenir les éléments du bulletin de l'étudiant
                    elements = []

                    # Style des paragraphes
                    styles = getSampleStyleSheet()
                    style_title = styles['Title']
                    style_heading = styles['Heading1']
                    style_body = styles['BodyText']

                    # Informations de l'étudiant
                    title = Paragraph("INSTITUT DE FORMATION PROFESSIONNELLE GODWIN", style_title)
                    elements.append(title)

                    title = Paragraph("Bulletin de notes", style_title)
                    elements.append(title)

                    elements.append(Spacer(1, 20))
                    student_info = f"Nom de l'étudiant: {nom_etudiant}<br/>" \
                                f"Matricule de l'étudiant: {mat_etudiant}"
                    student_info = Paragraph(student_info, style_body)
                    elements.append(student_info)

                    elements.append(Spacer(1, 20))
                    elements.append(Paragraph("Détails du bulletin:", style_heading))

                    # Contenu du tableau
                    data = [
                        ["Semestre", "Liste des matières", "Somme des coefficients", "Moyenne", "Ordre de mérite"],
                    ]

                    for result in results:
                        semestre = result[0]
                        liste_matiere = result[1]
                        somme_coefficients = result[2]
                        moyenne = result[6]
                        ordre_merite = result[7]

                        data.append([semestre, liste_matiere, somme_coefficients, moyenne, ordre_merite])

                    # Création du tableau avec le style
                    table = Table(data)
                    style = TableStyle([
                        ('BACKGROUND', (0, 0),(-1, 0), colors.cyan),  # Couleur cyan pour les titres
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 14),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ])
                    table.setStyle(style)

                    elements.append(table)
                    elements.append(Spacer(1, 20))
                    elements.append(Paragraph("signature admin:...............", style_body))
                    elements.append(Paragraph("\nsignature parent:............", style_body))

                    # Ajout des éléments du bulletin de l'étudiant à la liste des bulletins généraux
                    all_bulletin_elements.extend(elements)

                # Fermeture de la connexion à la base de données
                cursor.close()
                conn.close()

                # Création du document PDF avec tous les bulletins
                doc = SimpleDocTemplate("tb/bulletin_general.pdf", pagesize=landscape(letter))
                doc.build(all_bulletin_elements)
            
            def bul2():
                b = bul()
                b.afficher_bulletin()

           # b = bul()
            #b.afficher_bulletin()
            button2 = ctk.CTkButton(master=gauche_frame, text="imprimer bulletin",command=afficher_bulletin)
            button2.pack(side="top", fill= "x", expand = False) 
    ##################################################################
            button22 = ctk.CTkButton(master=gauche_frame, text="bulletin avec logo",command=bul2)
            button22.pack(side="top", fill= "x", expand = False) 
    ##################################################################
          
    #####################################################################
            button13 = ctk.CTkButton(master=gauche_frame, text="imprimer bulletin generale",command=imprimer_rs)
            button13.pack(side="top", fill= "x", expand = False)

            button14 = ctk.CTkButton(master=gauche_frame, text="Chercher",command=recherche)
            button14.pack(side="top", fill= "x", expand = False)

            button15 = ctk.CTkButton(master=gauche_frame, text="actualiser",command=actualiser22)
            button15.pack(side="top", fill= "x", expand = False)


            tableresultat = ttk.Treeview(droit_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13), height=20, show="headings")
            tableresultat.pack(fill="both", pady=10, padx=10)
            tableresultat.heading(1, text="semestre")
            tableresultat.heading(2, text="nombre_matiere")
            tableresultat.heading(3, text="liste_matiere")
            tableresultat.heading(4, text="somme_coefficients")
            tableresultat.heading(5, text="liste_note_cc")
            tableresultat.heading(6, text="liste_note_sn")
            tableresultat.heading(7, text="mat_etudiant")
            tableresultat.heading(8, text="nom_etu")
            tableresultat.heading(9, text="type_note")
            tableresultat.heading(10, text="moyenne")
            tableresultat.heading(11, text="rang")

            # Définition des largeurs des colonnes
            tableresultat.column(1, width=20)
            tableresultat.column(2, width=70)
            tableresultat.column(3, width=70)
            tableresultat.column(4, width=70)
            tableresultat.column(5, width=20)
            tableresultat.column(6, width=70)
            tableresultat.column(7, width=70)
            tableresultat.column(8, width=70)
            tableresultat.column(9, width=20)
            tableresultat.column(10, width=70)
            tableresultat.column(11, width=70)
            tableresultat.column(12, width=20)
            tableresultat.column(13, width=20)

            # Connexion à la base de données
            con76 = pymysql.connect(user='root', password='', database='g_note')
            cursor = con76.cursor()

            # Exécution de la requête SQL
            query = """SELECT 
    note.semestre, 
    COUNT(DISTINCT CASE WHEN note.type_note = "examen" THEN matiere.id_matiere END) as nombre_matiere, 
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN matiere.nom_matiere END) as liste_matiere, 
    SUM(CASE WHEN note.type_note = "examen" THEN matiere.coef_matiere END) as somme_coefficients,
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN note.note_cc END) as liste_note_cc, 
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN note.note_sn END) as liste_note_sn, 
    etudiant.mat_etudiant, 
    etudiant.nom_etu, 
    note.type_note, 
    (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) AS moyenne, 
    RANK() OVER (ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite,  
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN matiere.coef_matiere END) as coef
    
FROM 
    cote 
INNER JOIN 
    note ON cote.id_cote = note.id_cote 
INNER JOIN 
    matiere ON note.id_matiere = matiere.id_matiere 
INNER JOIN 
    etudiant ON etudiant.id_etudiant = note.id_etudiant 
WHERE 
    note.type_note IN ("cc", "sn", "examen") 
GROUP BY 
    etudiant.mat_etudiant 
ORDER BY 
    moyenne DESC;"""

            cursor.execute(query)

            # Parcours des résultats et insertion dans le tableau
            for ligne in cursor:
                tableresultat.insert('', 'end', values=ligne)

            # Fermeture de la connexion à la base de données
            con76.close()

                        

            
            # Afficher le tableau des matières

        def open_classes():
            # Code pour ouvrir la page de gestion des matières
            #print("Ouvrir la page de gestion des classes")
            window = tk.Toplevel()
            window.title("gestion de classe")

            haut_frame = ctk.CTkFrame(master=window,fg_color="light gray",border_width=10,border_color="dark blue")
            haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

            droit_frame = ctk.CTkFrame(master=window,fg_color="dark gray")
            droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

            gauche_frame = ctk.CTkFrame(master=window,fg_color="dark gray",width=700)
            gauche_frame.pack(side="left",fill="both",expand=False)
    #fin frame pricipale

            ##################################################################
            chama0 = ctk.CTkEntry(master=gauche_frame, placeholder_text="identifiant",font=("time_new_roman",10))
            chama0.pack(side="top", fill= "x", expand = False) 
            chama4 = ctk.CTkEntry(master= gauche_frame, placeholder_text="nom",font=("time_new_roman",10))
            chama4.pack(side="top", fill= "x", expand = False) 

            chama5 = ctk.CTkEntry(master=gauche_frame, placeholder_text="niveau",font=("time_new_roman",10))
            chama5.pack(side="top", fill= "x", expand = False) 
            image_pil = Image.open("logo/godwin.jpg")

            # Définir la nouvelle taille souhaitée
            nouvelle_taille = (100, 100)

            # Redimensionner l'image
            image_redimensionnee = image_pil.resize(nouvelle_taille)

            # Convertir l'image PIL en un objet Tkinter
            image_tk = ImageTk.PhotoImage(image_redimensionnee)

            # Créer un widget Label pour afficher l'image redimensionnée
            profile_photo_label = ttk.Label(haut_frame, image=image_tk)
            profile_photo_label.image = image_tk
            profile_photo_label.pack()


         

            def actualiser2 ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    # Supprimer tous les éléments existants dans la table
                    
                    table3.delete(*table3.get_children())
                        # Récupérer les données depuis la base de données
                    cursor = con.cursor()
                    
                    cursor.execute("SELECT * FROM classe")
                    data = cursor.fetchall()
                    #print("ok1")
                    
                        # Insérer les données dans le tableau
                    for row in data:
                        table3.insert("", "end", values=row)

                   # messagebox.showinfo("actualisé","page a ete actualisé!")

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
        ###############################

            def ajouterclasse ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama0.get()
                    nom = chama4.get()
                    niveau = chama5.get()
                    
                    actualiser2()
                
                    sql = "INSERT INTO classe (id_classe, nom_classe, niveau_classe) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (iden, nom, niveau))
                        
                    con.commit()
                    actualiser2()
                    con.close()

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def supprimerClasse():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama0.get()
                    
                    actualiser2()
                    

                    sql = "DELETE FROM classe WHERE id_classe = %s"
                    cursor.execute(sql, (iden))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def modifierclasse ():
                try:

                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                # f = fonc()
                    iden = chama0.get()
                    nom = chama4.get()
                    niveau = chama5.get()
                    actualiser2()
                    
                    # 696354742 BA2B ############################################

                    sql = "UPDATE classe SET nom_classe = %s, niveau_classe = %s WHERE id_classe = %s"
                    cursor.execute(sql, (nom, niveau, iden))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
           
            #sql = "UPDATE matiere SET nom_matiere = %s, coef_matiere = %s, id_module = %s WHERE id_matiere = %s"     bout.ajouterMatier(iden,nom, id_module , coef)       bout.modifierMatier(nom ,coef,id_module, iden )   bout.supprimerMatier(iden)
            button2 = ctk.CTkButton(master=gauche_frame, text="ajouter",command=ajouterclasse)
            button2.pack(side="top", fill= "x", expand = False) 
    ##################################################################
            button12 = ctk.CTkButton(master=gauche_frame, text="modifier",command=modifierclasse)
            button12.pack(side="top", fill= "x", expand = False)
    #####################################################################
            button13 = ctk.CTkButton(master=gauche_frame, text="supprimer",command=supprimerClasse)
            button13.pack(side="top", fill= "x", expand = False)


            table3 = ttk.Treeview(droit_frame,columns=(1,2,3,4,5), height=20, show= "headings")
            table3.pack(fill="both",pady=10,padx=10)
            table3.heading(1,text = "identifiant classe")
            table3.heading(2,text = "Nom classe")
            table3.heading(3,text = "niveau")
            table3.heading(4,text = "------")
            
            

            #colonnes
            table3.column(1,width=20)
            table3.column(2,width=70)
            table3.column(3,width=70)
            table3.column(4,width=70)
            table3.column(5,width=70)
            
            
            import pymysql

            con76 = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con76.cursor()

            query = 'select * from classe;'

            r = cursor.execute(query)

            for ligne in cursor:
                table3.insert('',END, value= ligne)

        

            con76.close()


        def open_specialites():
            # Code pour ouvrir la page de gestion des matières
            #print("Ouvrir la page de gestion des specialité")
            window = tk.Toplevel()
            window.title("gestion de specialité")

            haut_frame = ctk.CTkFrame(master=window,fg_color="light gray",border_width=10,border_color="dark blue")
            haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

            droit_frame = ctk.CTkFrame(master=window,fg_color="dark gray")
            droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

            gauche_frame = ctk.CTkFrame(master=window,fg_color="dark gray",width=700)
            gauche_frame.pack(side="left",fill="both",expand=False)
    #fin frame pricipale

            ##################################################################
            chama23 = ctk.CTkEntry(master=gauche_frame, placeholder_text="identifiant",font=("time_new_roman",10))
            chama23.pack(side="top", fill= "x", expand = False) 
            chama24 = ctk.CTkEntry(master= gauche_frame, placeholder_text="nom",font=("time_new_roman",10))
            chama24.pack(side="top", fill= "x", expand = False) 

            chama25 = ctk.CTkEntry(master=gauche_frame, placeholder_text="Code du cours",font=("time_new_roman",10))
            chama25.pack(side="top", fill= "x", expand = False) 

            chama26 = ctk.CTkEntry(master=gauche_frame, placeholder_text="nombre credits",font=("time_new_roman",10))
            chama26.pack(side="top", fill= "x", expand = False) 
            image_pil = Image.open("logo/godwin.jpg")

            # Définir la nouvelle taille souhaitée
            nouvelle_taille = (100, 100)

            # Redimensionner l'image
            image_redimensionnee = image_pil.resize(nouvelle_taille)

            # Convertir l'image PIL en un objet Tkinter
            image_tk = ImageTk.PhotoImage(image_redimensionnee)

            # Créer un widget Label pour afficher l'image redimensionnée
            profile_photo_label = ttk.Label(haut_frame, image=image_tk)
            profile_photo_label.image = image_tk
            profile_photo_label.pack()

            iden = chama23.get()
            nom = chama24.get()
            code_cours = chama25.get()
            credit = chama26.get()

            def actualiser2 ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    # Supprimer tous les éléments existants dans la table
                    
                    table4.delete(*table4.get_children())
                        # Récupérer les données depuis la base de données
                    cursor = con.cursor()
                    
                    cursor.execute("SELECT * FROM cours")
                    data = cursor.fetchall()
                    #print("ok1")
                    
                        # Insérer les données dans le tableau
                    for row in data:
                        table4.insert("", "end", values=row)

                   # messagebox.showinfo("actualisé","page a ete actualisé!")

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
        ###############################

            def ajoutercours ():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama23.get()
                    nom = chama24.get()
                    code_cours = chama25.get()
                    credit = chama26.get()
                    
                    actualiser2()
                
                    sql = "INSERT INTO cours (id_cours, nom_cours,code_cours, nb_credits) VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, (iden, nom, code_cours, credit))
                        
                    con.commit()
                    actualiser2()
                    con.close()

                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def supprimerCours():
                try:
                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama23.get()
                    nom = chama24.get()
                    code_cours = chama25.get()
                    credit = chama26.get()
                    
                    actualiser2()
                    

                    sql = "DELETE FROM cours WHERE id_cours = %s"
                    cursor.execute(sql, (iden))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
            def modifiercours ():
                try:

                    con = pymysql.connect(user='root', password ='',database = 'g_note')
                    cursor = con.cursor()
                    iden = chama23.get()
                    nom = chama24.get()
                    code_cours = chama25.get()
                    credit = chama26.get()
                #
                    # 696354742 BA2B ############################################

                    sql = "UPDATE cours SET nom_cours = %s, code_cours = %s, nb_credits = %s WHERE id_cours = %s"
                    cursor.execute(sql, (nom, code_cours, credit, iden))
                    con.commit()
                    actualiser2()
                    con.close()
                except:
                    messagebox.showinfo("Attention","il semble avoir un probleme")
           
           
            bout = fonc()
            #sql = "UPDATE matiere SET nom_matiere = %s, coef_matiere = %s, id_module = %s WHERE id_matiere = %s"
            button2 = ctk.CTkButton(master=gauche_frame, text="ajouter",command=ajoutercours)
            button2.pack(side="top", fill= "x", expand = False) 
    ##################################################################
            button12 = ctk.CTkButton(master=gauche_frame, text="modifier",command=modifiercours)
            button12.pack(side="top", fill= "x", expand = False)
    #####################################################################
            button13 = ctk.CTkButton(master=gauche_frame, text="supprimer",command=supprimerCours)
            button13.pack(side="top", fill= "x", expand = False)


            table4 = ttk.Treeview(droit_frame,columns=(1,2,3,4), height=20, show= "headings")
            table4.pack(fill="both",pady=10,padx=10)
            table4.heading(1,text = "identifiant cours")
            table4.heading(2,text = "libellé")
            table4.heading(3,text = "codes cours")
            table4.heading(4,text = "nombre redits")
            
            

            #colonnes
            table4.column(1,width=20)
            table4.column(2,width=70)
            table4.column(3,width=70)
            table4.column(4,width=70)
            
            
            import pymysql

            con76 = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con76.cursor()

            query = 'select * from cours;'

            r = cursor.execute(query)

            for ligne in cursor:
                table4.insert('',END, value= ligne)

        

            con76.close()

            
            # Afficher le tableau des matières

            # Code pour ouvrir la page de gestion des spécialités
            #print("Ouvrir la page de gestion des spécialités")
            # Afficher le tableau des spécialités

        def get_classes_from_database():
            # Fonction pour récupérer les données des classes depuis une base de données MySQL
            conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')  # Remplacez les informations de connexion par celles de votre base de données
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM classe")
            classes = cursor.fetchall()
            conn.close()
            return classes

        def display_table(title, data):
            # Fonction pour afficher un tableau avec un titre et des données
            window = tk.Toplevel()
            window.title(title)

            table = ttk.Treeview(window)
            table["columns"] = tuple(range(len(data[0])))

            for col in table["columns"]:
                table.heading(col, text=col)

            for row in data:
                table.insert("", "end", values=tuple(row))

            table.pack()
        frame = ctk.CTkFrame(master=haut_frame,fg_color="Dodgerblue2")
        frame.pack(side="top", fill= "both", expand = True) 
        button = ctk.CTkButton(master=frame, text="gerer classe",command=open_classes)
        button.pack(side="right")
        button = ctk.CTkButton(master=frame, text="gerer specialite",command=open_specialites)
        button.pack(side="right")
        button = ctk.CTkButton(master=frame, text="gerer matiere",command=open_matieres)
        button.pack(side="right")
        button = ctk.CTkButton(master=frame, text="light/black",command=mode)
        button.pack(side="right")
        button = ctk.CTkButton(master=frame, text="actualiser",command=mode)
        button.pack(side="right")
        
        letitre = ctk.CTkLabel(master=frame,text = ("GODWIN",role, matricule),font=("arial",40) )
        letitre.pack(side="top",fill="x",expand=False)

        prof = ctk.CTkLabel(master=frame,text = (role, matricule),font=("arial",20) )
        #prof.pack(side="top",fill="x",expand=False)
        prof1 = ctk.CTkLabel(master=frame,text = nom,font=("arial",15) )
        prof1.pack(side="top",fill="x",expand=False)
## img  
        from PIL import Image, ImageTk
        import tkinter as tk
        import tkinter.ttk as ttk
                        # Ouvrir l'image avec PIL
        image_pil = Image.open("logo/godwin.jpg")

        # Définir la nouvelle taille souhaitée
        nouvelle_taille = (50, 50)

        # Redimensionner l'image
        image_redimensionnee = image_pil.resize(nouvelle_taille)

        # Convertir l'image PIL en un objet Tkinter
        image_tk = ImageTk.PhotoImage(image_redimensionnee)

        # Créer un widget Label pour afficher l'image redimensionnée
        profile_photo_label = ttk.Label(frame, image=image_tk)
        profile_photo_label.image = image_tk
        profile_photo_label.pack()
        import pymysql
        con5 = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con5.cursor()
###### fin img
        query5 = """
            SELECT r.nom_role ,u.nom, u.password, u.id, u.tof
            FROM role r
            inner JOIN utilisateur u ON u.role_id = r.id
            WHERE u.id = %s
                """
        values5 = (matricule)
        cursor.execute(query5, values5)
        result5 = cursor.fetchone()
        
        
        #print(result5[4])


        from PIL import Image, ImageTk
        import tkinter.ttk as ttk

        # Ouvrir l'image avec PIL
        image_pil = Image.open(f"photo_user/{result5[4]}")

        # Définir la nouvelle taille souhaitée
        nouvelle_taille = (50, 50)

        # Redimensionner l'image
        image_redimensionnee = image_pil.resize(nouvelle_taille)

        # Convertir l'image PIL en un objet Tkinter
        image_tk = ImageTk.PhotoImage(image_redimensionnee)

        # Créer un widget Label pour afficher l'image redimensionnée
        profile_photo_label = ttk.Label(frame, image=image_tk)
        profile_photo_label.image = image_tk
        profile_photo_label.pack()







        frame1 = ctk.CTkFrame(master=gauche_frame,fg_color="medium spring green")
        frame1.pack(side="top", fill= "both", expand = True) 
        
       

        frame3 = ctk.CTkFrame(master=gauche_frame,fg_color="orange")
        frame3.pack(side="bottom", fill= "both", expand = True) 



        



        #champ frame gauche
        chama = ctk.CTkEntry(master=frame1, placeholder_text="identifiant",font=("time_new_roman",10))
        chama.pack(side="top", fill= "x", expand = False) 
        chama1 = ctk.CTkEntry(master= frame1, placeholder_text="nom",font=("time_new_roman",10))
        chama1.pack(side="top", fill= "x", expand = False) 

        chama2 = ctk.CTkEntry(master=frame1, placeholder_text="coeficiant",font=("time_new_roman",10))
        chama2.pack(side="top", fill= "x", expand = False) 





     


   
#################################################################
# #
 


        def actualiser2 ():
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                # Supprimer tous les éléments existants dans la table
                
                table2.delete(*table2.get_children())
                    # Récupérer les données depuis la base de données
                cursor = con.cursor()
                
                cursor.execute("SELECT * FROM matiere")
                data = cursor.fetchall()
                #print("ok1")
                
                    # Insérer les données dans le tableau
                for row in data:
                    table2.insert("", "end", values=row)

                messagebox.showinfo("actualisé","page a ete actualisé!")

            except:
                messagebox.showinfo("Attention","il semble avoir un probleme")
    ###############################

############################################################
        def ajouter ():
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                actualiser1()
                iden = chama.get()
                nom = chama1.get()
                coef = chama2.get()

                sql = "INSERT INTO module (id_module,nom_module, coef_module) VALUES (%s, %s, %s)"
                cursor.execute(sql, (iden, nom, coef))
                
                con.commit()
                actualiser1()
                con.close()
            except:
                messagebox.showinfo("Attention","il semble avoir un probleme")


        def modifier ():
            try:
                    
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                actualiser1()
                iden = chama.get()
                nom = chama1.get()
                coef = chama2.get()

                sql = "UPDATE module SET nom_module =%s, coef_module  = %s WHERE id_module = %s"
                cursor.execute(sql, (nom, coef, iden))
                con.commit()
                actualiser1()
                con.close()
            except:
                messagebox.showinfo("Attention","il semble avoir un probleme")


        def supprimer ():
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                actualiser1()
                iden = chama.get()
                nom = chama1.get()
                coef = chama2.get()

                sql = "DELETE FROM module WHERE id_module = %s"
                cursor.execute(sql, (iden))
                con.commit()
                actualiser1()
                con.close()
            except:
                messagebox.showinfo("Attention","il semble avoir un probleme")

        def actualiser1 ():
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                # Supprimer tous les éléments existants dans la table
                table.delete(*table.get_children())

                # Récupérer les données depuis la base de données
                cursor = con.cursor()
                cursor.execute("SELECT * FROM module")
                data = cursor.fetchall()

                # Insérer les données dans le tableau
                for row in data:
                    table.insert("", "end", values=row)

                messagebox.showinfo("actualisé","page a ete actualisé!")
                window.destroy()
                open_matieres()

            except:
                messagebox.showinfo("Attention","il semble avoir un probleme")

        def stat():
            statistiques = Statistiques()
            statistiques.run()

        def calculatrice():
            calculatrice = Calculatrice()
            calculatrice.run()
#########################**********************
        def table_m():
            statistiques_classe = StatistiquesClasse()
##################################################################
        
      

##################################################################
       
#####################################################################
        


######
        button2 = ctk.CTkButton(master=frame1, text="ajouter",command=ajouter)
        button2.pack(side="top", fill= "x", expand = False) 
##################################################################
        button12 = ctk.CTkButton(master=frame1, text="modifier",command=modifier)
        button12.pack(side="top", fill= "x", expand = False)
#####################################################################
        button13 = ctk.CTkButton(master=frame1, text="supprimer",command=supprimer)
        button13.pack(side="top", fill= "x", expand = False)
######################################################################

#fin frame interne


   #bare de menu
        def aje():
            aj = ajouterEl()
            aj.ajoue()

        bj = ajouterNote()
        Vue = Matier()
        menub = Menu(acceuil)

        ajj = ajouterEl()
        
        def b_i ():
            monb = bul_indiv()
            monb.generer_bulletin()

        def g_b():
            generator = GrandBulletinGenerator()
            generator.generer_grand_bulletin()

        def indispo():
            messagebox.showinfo("désolé", "cette option n'est pas encore disponible")

        filemenu = Menu(menub,tearoff=0)
        menub.add_cascade(label="fichier", menu=filemenu)
        filemenu.add_command(label="Ajouter Etudiant",command=lambda: ajj.ajouet())
        filemenu.add_command(label="Ajouter note",command=lambda: bj.ajoue())
        filemenu.add_command(label="classe",command=open_classes)
        filemenu.add_command(label="enseignant",command=lambda: indispo)
        filemenu.add_command(label="matieres",command=open_matieres)
        filemenu.add_command(label="tables de moyennes",command= table_m)
        filemenu.add_command(label="grand bulletin",command= g_b)
        filemenu.add_command(label="bul individuel",command= b_i)
        filemenu.add_command(label="calculatrice",command=calculatrice)
        filemenu.add_separator()
        filemenu.add_command(label="sortir", command=acceuil.destroy)
        
        
        def runajouteruser():
            a = AjouterUser()

        av = imprimer_t_b()
        def avc():
            av.afficher_bulletin()
        filemenu2 = Menu(menub,tearoff=0)
        menub.add_cascade(label="fiche de note", menu=filemenu2)
        filemenu2.add_command(label="par ordre de merite/classe",command=openordre)
        filemenu2.add_command(label="resultat de fin An",command=open_bilan)
        filemenu2.add_command(label="imprimer tous bulletin",command=avc)
        filemenu2.add_command(label="stats",command= stat)
        filemenu2.add_separator()
        filemenu2.add_command(label="Ajouter utilisateur", command=runajouteruser)
        

        #+
        filemenu3 = Menu(menub,tearoff=0)
        menub.add_cascade(label="attestation", menu=filemenu3)
        filemenu3.add_command(label="att", command=indispo)
        

        #+
        filemenu4 = Menu(menub,tearoff=0)
        menub.add_cascade(label="parametre", menu=filemenu4)
        filemenu4.add_command(label="param", command=indispo)

        #+
        filemenu5 = Menu(menub,tearoff=0)
        menub.add_cascade(label="sauvegarde", menu=filemenu5)
        filemenu5.add_command(label="att", command=indispo)

        #+
        filemenu6 = Menu(menub,tearoff=0)
        menub.add_cascade(label="calculatrice", menu=filemenu6)
        filemenu6.add_command(label="calculatrice",command=calculatrice)

        acceuil.config(menu=menub)
    #fin menu


        table = ttk.Treeview(droit_frame,columns=(1,2,3,4), height=20, show= "headings")
        table.pack(fill="both",pady=10,padx=10)
        table.heading(1,text = "identifiant")
        table.heading(2,text = "Nom")
        table.heading(3,text = "coef")
        
        

        #colonnes
        table.column(1,width=20)
        table.column(2,width=70)
        table.column(3,width=70)
        table.column(4,width=70)
        
        
        import pymysql

        con6 = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con6.cursor()

        query = 'select * from module;'

        r = cursor.execute(query)

        for ligne in cursor:
            table.insert('',END, value= ligne)

       

        con6.close()
        


##fin tableau

        table2 = ctk.CTkTabview(master=droit_frame)
        table2.pack(fill="both",pady=10,padx=10)

        


    







        acceuil.mainloop()

#ri = Vueri()

#ri.acceuil()

        


   