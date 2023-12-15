from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
import pymysql
from tkinter import messagebox
from reportlab.platypus import PageBreak
class imprimer_t_b:
    def __init__(self):
        pass
    def afficher_bulletin(self):
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

        # Requête SQL pour récupérer les rangs des étudiants
        ranks_query = '''
        SELECT mat_etudiant, ordre_merite, moyenne 
        FROM ( SELECT etudiant.mat_etudiant,
        RANK() OVER (ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite,
            (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) AS moyenne 
            FROM matiere 
            LEFT JOIN note ON note.id_matiere = matiere.id_matiere 
            LEFT JOIN cote ON cote.id_cote = note.id_cote 
            LEFT JOIN etudiant ON etudiant.id_etudiant = note.id_etudiant WHERE note.type_note IN ("cc", "sn", "examen") GROUP BY etudiant.mat_etudiant ) AS ranks
        '''

        # Exécution de la requête pour récupérer les rangs des étudiants
        cursor.execute(ranks_query)
        ranks = cursor.fetchall()

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
            matiere
        LEFT JOIN
            note ON note.id_matiere = matiere.id_matiere
        LEFT JOIN 
            cote ON cote.id_cote = note.id_cote 
        LEFT JOIN 
            etudiant ON etudiant.id_etudiant = note.id_etudiant 
        LEFT JOIN
            classe ON etudiant.id_classe = classe.id_classe
        WHERE 
            note.type_note IN ("cc", "sn", "examen") 
            AND etudiant.mat_etudiant = %s
        GROUP BY 
            etudiant.mat_etudiant, note.semestre, matiere.nom_matiere, matiere.coef_matiere, classe.nom_classe
        ORDER BY 
            classe.nom_classe, etudiant.mat_etudiant, note.semestre, moyenne DESC
        '''

        # Liste pour contenir les éléments du document PDF
        elements = []

        # Génération du bulletin individuel pour chaque étudiant
        for student in students:
            mat_etudiant = student[0]
            nom_etudiant = student[1]

            # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
            cursor.execute(bulletin_query, (mat_etudiant,))
            results = cursor.fetchall()

            # Recherche du rang de l'étudiant
            rank = next((r[1] for r in ranks if r[0] == mat_etudiant), None)
            moyen1 = next((r[2] for r in ranks if r[0] == mat_etudiant), None)

            # Création du tableau contenant les données du bulletin
            data = [['Semestre', 'Matière', 'Coefficient', 'Type de note', 'Moyenne', 'Rang','moyenne']]

            for result in results:
                semestre = result[0]
                nom_matiere = result[1]
                coef_matiere = result[2]
                type_note = result[5]
                moyenne = result[6]
                rang = result[7]
                nom_classe = result[8]
            # moyp = result[9]

                data.append([semestre, nom_matiere, coef_matiere, type_note, moyenne, rang])
            styles = getSampleStyleSheet()

            logo = Image("logo/godwin.jpg", width=200, height=100)
            elements.append(logo)

            title = Paragraph("Grand Bulletin - Classement par classe et par ordre de mérite", styles["Title"])
            elements.append(title)

            # Création du titre du bulletin
            title = f'NOM: {nom_etudiant}\n'
            title2 = f'Matricule : {mat_etudiant}\n'
            title3 = f'Classe : {nom_classe}\n'
            title4 = f'Moyenne: {moyen1}\n'
            title5 = f'Rang : {rank if rank else "-"}'

            # Ajout du titre au document
            elements.append(Paragraph(title, styles["Title"]))
            elements.append(Paragraph(title2, styles["Title"]))
            elements.append(Paragraph(title3, styles["Title"]))
            elements.append(Paragraph(title4, styles["Title"]))
            elements.append(Paragraph(title5, styles["Title"]))

            # Création du tableau
            table = Table(data)

            # Modification du style du tableau
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ]))

            # Ajout du tableau au document
            elements.append(table)
            elements.append(Spacer(1, 20))
            elements.append(Paragraph("Administration. ____________________________________________________________________________________________  Parents.", styles["Normal"]))


            # Ajout d'un saut de page entre chaque bulletin
            elements.append(PageBreak())

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()
        try:
            # Création du document PDF
            doc = SimpleDocTemplate("i/bulletins.pdf", pagesize=landscape(letter))

            # Ajout des éléments au document
            doc.build(elements)
            messagebox.showinfo("Enregistrement réussie", "vous pouvez retouver le fichier dans le dossier i/bulletins.pdf merci !")
        except:
            messagebox.showinfo("oups", "un probleme est survenus")

# Appel de la fonction pour afficher les bulletins
#afficher_bulletin()
        