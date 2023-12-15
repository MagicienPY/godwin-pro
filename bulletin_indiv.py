from tkinter import *
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import pymysql
from tkinter import messagebox
class bul_indiv:
    def __init__(self):
        pass
        def rechercher_etudiant():
            # Connexion à la base de données
            conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
            cursor = conn.cursor()

            # Demande de saisie du matricule de l'étudiant
            mat_etudiant = matricule_entry.get()

            # Requête SQL pour récupérer les informations de l'étudiant
            etudiant_query = '''
            SELECT mat_etudiant, nom_etu
            FROM etudiant
            WHERE mat_etudiant = %s
            '''
            # Exécution de la requête pour récupérer les informations de l'étudiant
            cursor.execute(etudiant_query, (mat_etudiant,))
            etudiant = cursor.fetchone()

            if etudiant:
                # Affichage des informations de l'étudiant trouvé
                nom_etudiant_label.config(text=f"Nom de l'étudiant : {etudiant[1]}")

                # Génération et impression du bulletin de l'étudiant
                generer_bulletin(etudiant[0], etudiant[1])

                resultat_label.config(text="Le bulletin a été généré et imprimé avec succès.")
            else:
                resultat_label.config(text="Aucun étudiant trouvé avec ce matricule.")

            # Fermeture de la connexion à la base de données
            conn.close()

        def generer_bulletin(mat_etudiant, nom_etudiant):
            # Connexion à la base de données
            conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
            cursor = conn.cursor()

            # Requête SQL pour récupérer les données du bulletin de l'étudiant
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
            elements.append(Paragraph("Nom de l'étudiant : " + nom_etudiant, style_heading))
            elements.append(Spacer(1, 20))

            # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
            cursor.execute(bulletin_query, (mat_etudiant,))
            bulletin_data = cursor.fetchall()

            # Création du tableau pour afficher les données du bulletin
            bulletin_table_data = [['Semestre', 'Matière', 'Coefficient', 'Moyenne', 'Ordre de mérite', 'Classe']]

            # Variables pour calculer la note finale
            total_coef = 0
            total_moyenne = 0

            for row in bulletin_data:
                semestre = row[0]
                matiere = row[1]
                coef_matiere = row[2]
                moyenne = row[6]
                ordre_merite = row[7]
                classe = row[8]

                # Calcul de la moyenne pondérée
                moyenne_ponderee = moyenne * coef_matiere
                total_coef += coef_matiere
                total_moyenne += moyenne_ponderee

                bulletin_table_data.append([semestre, matiere, coef_matiere, moyenne, ordre_merite, classe])

            # Calcul de la note finale
            note_finale = total_moyenne / total_coef
            
            # Ajout de la ligne de la note finale dans le tableau
            bulletin_table_data.append(['', 'Note finale', total_coef, '', '', '', note_finale])

            # Création du tableau avec les données du bulletin
            bulletin_table = Table(bulletin_table_data)

            # Style du tableau
            style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            # Appliquer le style au tableau
            bulletin_table.setStyle(style)

            # Ajouter le tableau au document PDF
            elements.append(bulletin_table)
            try:
                # Génération du document PDF
                doc.build(elements)
                messagebox.showinfo("cool","bulletin imprimer avec succes  dans    \n ib/")
            except:
                messagebox.showinfo("attention","un erreur contacter un administrateur svp !")
            # Fermeture de la connexion à la base de données
            conn.close()

        # Interface graphique avec tkinter
        root = Tk()
        root.title("Générateur de bulletin")
        root.geometry("400x200")

        matricule_label = Label(root, text="Matricule de l'étudiant:")
        matricule_label.pack()

        matricule_entry = Entry(root)
        matricule_entry.pack()

        rechercher_button = Button(root, text="Rechercher", command=rechercher_etudiant)
        rechercher_button.pack()

        nom_etudiant_label = Label(root, text="")
        nom_etudiant_label.pack()

        resultat_label = Label(root, text="")
        resultat_label.pack()

      #  root.mainloop()



