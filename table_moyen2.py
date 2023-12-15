from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
import pymysql
from tkinter import messagebox

class bul:
    def __init__(self):
        pass
    def afficher_bulletin(self):
        # Connexion à la base de données
        conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
        cursor = conn.cursor()

        # Requête SQL pour récupérer les informations des étudiants
        students_query = '''
        SELECT DISTINCT etudiant.mat_etudiant, etudiant.nom_etu,etudiant.tof
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
        liste = [""]
        # Génération du bulletin individuel pour chaque étudiant
        for student in students:
            mat_etudiant = student[0]
            nom_etudiant = student[1]
            tof1 = student[2]
            liste.append(tof1)
            #print(liste)

            # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
            cursor.execute(bulletin_query, (mat_etudiant,))
            results = cursor.fetchall()

            # Création du document PDF en format paysage
            doc = SimpleDocTemplate(f"iab/{mat_etudiant}.pdf", pagesize=landscape(letter))

            # Liste pour contenir les éléments du document PDF
            elements = []

            # Style des paragraphes
            styles = getSampleStyleSheet()
            style_title = styles['Title']
            style_heading = styles['Heading1']
            style_body = styles['BodyText']
            elements.append(Spacer(1, -30))
            # Ajout du logo de l'école
            logo = Image("C:/Users/magicien/Downloads/godwin-v2-main/logo/godwin.jpg", width=200, height=100)
            elements.append(logo)
            
            # Informations de l'étudiant
            title = Paragraph("Bulletin GODWIN", style_title)
            elements.append(title)

            elements.append(Spacer(1, 20))
            elements.append(Paragraph("INSTITUT DE FORMATION PROFESSIONNELLE GODWIN", style_heading))
            elements.append(Spacer(1, 20))
            student_info = f"Nom de l'étudiant: {nom_etudiant}<br/>" \
                        f"Matricule de l'étudiant: {mat_etudiant}"
            profil = Image(f"{tof1}", width=200, height=100)
            #elements.append(profil)
            student_info = Paragraph(student_info, style_body)
            elements.append(student_info)

            elements.append(Spacer(1, 10))
            elements.append(Paragraph("Détails du bulletin:", style_heading))

            
            

            # Contenu du tableau
            data = [
                ["Semestre", "Liste des matières", "Coefficient", "Moyenne", "Ordre de mérite"],
            ]

            for result in results:
                semestre = result[0]
                data.append([semestre, result[1], result[2], result[6], result[7]])

            data += [
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                        ["", "", "", "", ""],
                    ]

            # Création du tableau
            table = Table(data, colWidths=[80, 200, 100, 120, 120])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            elements.append(table)
            elements.append(Paragraph("signature admin:.........", style_heading))
            elements.append(Spacer(1, 20))
            elements.append(Paragraph("\nsignature admin:........", style_heading))

            # Génération du document PDF
            doc.build(elements)
            #messagebox.showinfo(" cool ","Bulletin generer avec succes  retrouvez le dans le dossier IAB")

        # Fermeture de la connexion à la base de données
        cursor.close()
        conn.close()


# Utilisation de la classe
b = bul()
b.afficher_bulletin()