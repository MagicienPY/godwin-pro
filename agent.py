#from importation import *
from tkinter import *
import tkinter.messagebox as msgbox
import customtkinter as ctk
import tkinter.ttk as ttk
import aspose.pdf as pdf
from fenetre import *
from ajouterEl import *
from matiere import *
import pymysql
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet



class agent:
    

    def __init__(self):
        pass
    def acceuil(self,nom, matricule, passe, role):
        def mode ():
            if (ctk.get_appearance_mode() == "Light"):
                ctk.set_appearance_mode("Dark")
            else:
                ctk.set_appearance_mode("Light")

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
                #print(id_ma)
                data =  []
                data2 = []
                
                #print(iden, valeur_n, type_n, ann_s, sem, poids_n, id_etu, id_ma, id_ens, not_c, not_s, id_c)
                command="use g_note"
                cursor.execute(command)
                sql = "INSERT INTO note (id_note, valeur_note, type_note , annee_scolaire, semestre, poids_note, id_etudiant, id_matiere, id_enseignant, note_cc, note_sn, id_cote) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s)"
                cursor.execute(sql, (iden, valeur_n, type_n, ann_s, sem, poids_n, id_etu, id_ma, id_ens, not_c, not_s, id_c))
                con.commit()
                messagebox.showinfo(" cool ", "enregistrement reussit !!")
               # ajouterEl.destroy()
                table.delete(*table.get_children())

                # Récupérer les données depuis la base de données
                cursor = con.cursor()
                cursor.execute("SELECT * FROM note")
                data = cursor.fetchall()

                # Insérer les données dans le tableau
                for row in data:
                    table.insert("", "end", values=row)

                messagebox.showinfo("actualisé","page a ete actualisé!")
                acceuil.destroy()
                con.close()
                
            except:
                messagebox.showinfo("attention", "un soucis veuillez verifier vos informations")

        def fermer():
            acceuil.destroy()
        def imprimer_rs ():
            conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
            cursor = conn.cursor()                
                # Requête SQL pour récupérer les informations des étudiants
            students_query = '''
                SELECT DISTINCT *
                FROM utilisateur
                '''

               #  Exécution de la requête pour récupérer les informations des étudiants
            cursor.execute(students_query)
            students = cursor.fetchone()

                # Liste pour contenir les éléments de tous les bulletins
            all_bulletin_elements = []
            rest_table = []

                # Génération du bulletin individuel pour chaque étudiant
            for student in students:
                mat_etudiant = matricule
                nom_etudiant = nom

                    # Requête SQL pour récupérer les données du bulletin de l'étudiant regroupées par semestre
                bulletin_query = '''select * from note'''

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
                title = Paragraph(" NOTES ", style_title)
                elements.append(title)

                elements.append(Spacer(1, 20))
                student_info = f"Nom de L'enseignant: {nom_etudiant}<br/>" \
                                f"Matricule de l'énseignant: {mat_etudiant}"
                student_info = Paragraph(student_info, style_body)
                elements.append(student_info)

                elements.append(Spacer(1, 20))
                elements.append(Paragraph("Détails du tableau:", style_heading))

                    # Contenu du tableau
                data = [
                        ["N°", "valeur", "examen", "iden etudiant", "id module","id enseigant","note cc","note sn"],
                    ]
                data2 = [
                        ["id enseigant","note cc","note sn"],
                    ]

                for result in results:
                    semestre = result[0]
                    liste_matiere = result[1]
                    somme_coefficients = result[2]
                    moyenne = result[6]
                    ordre_merite = result[7]
                    id_en=  result[8]
                    note_c = result[9]
                    note_s = result[10]

                    data.append([semestre, liste_matiere, somme_coefficients, moyenne, ordre_merite,id_en,note_c, note_s])
                    data2.append([id_en,note_c, note_s])

                    # Création du tableau avec le style
                table = Table(data)
                table1 = Table(data2)
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
                table1.setStyle(style)

                elements.append(table)
                elements.append(Spacer(1, 20))

               # elements.append(table1)
                #elements.append(Spacer(1, 20))

                    # Ajout des éléments du bulletin de l'étudiant à la liste des bulletins généraux
                all_bulletin_elements.extend(elements)
                rest_table.extend(elements)

                # Fermeture de la connexion à la base de données
            cursor.close()
            conn.close()

                # Création du document PDF avec tous les bulletins
            doc = SimpleDocTemplate("impression_enseignant/nouveau_document.pdf", pagesize=landscape(letter))
            doc.build(all_bulletin_elements)
            messagebox.showinfo("actualisé","document enregistré dans impression_enseignant/nouveau_document.pdf")
           
        def actualiser1 ():
            try:
                con = pymysql.connect(user='root', password ='',database = 'g_note')
                cursor = con.cursor()
                # Supprimer tous les éléments existants dans la table
                table.delete(*table.get_children())

                # Récupérer les données depuis la base de données
                cursor = con.cursor()
                cursor.execute("SELECT * FROM note")
                data = cursor.fetchall()

                # Insérer les données dans le tableau
                for row in data:
                    table.insert("", "end", values=row)

                messagebox.showinfo("actualisé","page a ete actualisé!")
                window.destroy()
                open_matieres()

            except:
                messagebox.showinfo("Attention","il semble avoir un probleme")
            
        #ctk.set_appearance_mode("light")
       # ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Light")
        #customtkinter.set_appearance_mode("Dark")
        #ctk.set_appearance_mode("System")  # macOS only

        #print(nom, matricule, passe, role)

        acceuil = ctk.CTk()
        acceuil.title("GODWIN Enseign...")
        acceuil.geometry("1000x1000")
#frame pricipale
        haut_frame = ctk.CTkFrame(master=acceuil,fg_color="light gray",border_width=10,border_color="dark blue")
        haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

        droit_frame = ctk.CTkFrame(master=acceuil,fg_color="dark gray")
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

        gauche_frame = ctk.CTkFrame(master=acceuil,fg_color="dark gray",width=700)
        gauche_frame.pack(side="left",fill="both",expand=False)

        # Définir la nouvelle taille souhaitée
        from PIL import Image, ImageTk
        import tkinter as tk
        from tkinter import ttk
        image_pil = Image.open("logo/godwin.jpg")
        nouvelle_taille = (100, 100)

            # Redimensionner l'image
        image_redimensionnee = image_pil.resize(nouvelle_taille)

        # Convertir l'image PIL en un objet Tkinter
        image_tk = ImageTk.PhotoImage(image_redimensionnee)

            # Créer un widget Label pour afficher l'image redimensionnée
        profile_photo_label = ttk.Label(haut_frame, image=image_tk)
        profile_photo_label.image = image_tk
        profile_photo_label.pack()
#fin frame pricipale
#frame interne
        frame = ctk.CTkFrame(master=haut_frame,fg_color="Dodgerblue2")
        frame.pack(side="top", fill= "both", expand = True) 

        button = ctk.CTkButton(master=frame, text="light/black",command=mode)
        button.pack(side="right")

        letitre = ctk.CTkLabel(master=frame,text = "GODWIN  Enseignant ",font=("arial",40) )
        letitre.pack(side="top",fill="x",expand=False)



        
        
       

        frame3 = ctk.CTkFrame(master=gauche_frame,fg_color="orange")
        frame3.pack(side="bottom", fill= "both", expand = True) 



       


        table = ttk.Treeview(droit_frame,columns=(1,2,3,4,5,6,7,8,9,10,11), height=20, show= "headings")
        table.pack(fill="both",pady=10,padx=10)
        table.heading(1,text = "id")
        
        

        #colonnes
        table.column(1,width=20)
        table.column(2,width=70)
        table.column(3,width=70)
        table.column(4,width=70)
        table.column(5,width=20)
        table.column(6,width=70)
        table.column(7,width=70)
        table.column(8,width=70)
        

        table.column(9,width=70)
        table.column(10,width=70)
        table.column(11,width=70)
        
        import pymysql

        con = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con.cursor()

        query = 'select * from note;'

        r = cursor.execute(query)

        for ligne in cursor:
            table.insert('',END, value= ligne)

       

        con.close()

   
        
        
       




        id_note = ctk.CTkEntry(master=  frame3, placeholder_text=" id note")
        id_note.pack(side="top", fill= "x", expand = False)

        valeur_note = ctk.CTkEntry(master=  frame3, placeholder_text="valeur du cc")
        valeur_note.pack(side="top", fill= "x", expand = False)


        type_note = ctk.CTkEntry(master=  frame3, placeholder_text="type de note")
        type_note.pack(side="top", fill= "x", expand = False)

        annee_scolaire = ctk.CTkEntry(master=  frame3, placeholder_text="anné scolaire")
        annee_scolaire.pack(side="top", fill= "x", expand = False)

        semestre = ctk.CTkEntry(master=  frame3, placeholder_text="semestres ")
        semestre.pack(side="top", fill= "x", expand = False)

        poids_note = ctk.CTkEntry(master=  frame3, placeholder_text="poids ")
        poids_note.pack(side="top", fill= "x", expand = False)

        id_etudiant = ctk.CTkEntry(master=  frame3, placeholder_text="id etudiant")
        id_etudiant.pack(side="top", fill= "x", expand = False)


        id_matiere = ctk.CTkEntry(master=  frame3, placeholder_text="id matiere")
        id_matiere.pack(side="top", fill= "x", expand = False)

        id_enseignat = ctk.CTkEntry(master=  frame3, placeholder_text="id enseignat")
        id_enseignat.pack(side="top", fill= "x", expand = False)

        note_cc = ctk.CTkEntry(master=  frame3, placeholder_text="note cc")
        note_cc.pack(side="top", fill= "x", expand = False)


        note_sn = ctk.CTkEntry(master=  frame3, placeholder_text="note sn")
        note_sn.pack(side="top", fill= "x", expand = False)

        id_cote = ctk.CTkEntry(master=  frame3, placeholder_text="id cote")
        id_cote.pack(side="top", fill= "x", expand = False)
        
        button13 = ctk.CTkButton(master=frame3, text="imprimer",command=imprimer_rs)
        button13.pack(side="top", fill= "x", expand = False)

        ##################################################################


        
        button2 = ctk.CTkButton(master=droit_frame, text="stats",command=mode)
        button2.pack(side="top", fill= "x", expand = False) 
##################################################################
        
        
######################################################################
        button1 = ctk.CTkButton(master=frame3, text="Ajouter",command=creationn)
        button1.pack(side="top", fill= "y", expand = False)

        button12 = ctk.CTkButton(master=frame3, text="modifier",command=mode)
        button12.pack(side="top", fill= "x", expand = False)

        button = ctk.CTkButton(master=frame3, text="Annuler",command=fermer)
        button.pack(side="top", fill= "y", expand = False)


#fin frame interne


   #bare de menu
        aj = ajouterEl()
        Vue = Matier()
        menub = Menu(acceuil)
        filemenu = Menu(menub,tearoff=0)
        menub.add_cascade(label="fichier", menu=filemenu)
        filemenu.add_command(label="classe",command=lambda: Vue.attentetaches(self))
        filemenu.add_command(label="tables de moyennes",command=lambda: Vue.attentetaches(self))
        filemenu.add_command(label="calculatrice",command=lambda: g1.permission)
        filemenu.add_separator()
        filemenu.add_command(label="sortir", command=acceuil.destroy)
        
        #+
        filemenu5 = Menu(menub,tearoff=0)
        menub.add_cascade(label="sauvegarde", menu=filemenu5)

        acceuil.config(menu=menub)
    #fin menu


        
       


##fin tableau

        table = ctk.CTkTabview(master=droit_frame)
        table.pack(fill="both",pady=10,padx=10)


    




        

        








        acceuil.mainloop()

#ri = Vueri()

#ri.acceuil()

        


   