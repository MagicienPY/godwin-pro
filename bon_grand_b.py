from tkinter import *
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart
import pymysql
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from tkinter import messagebox

class GrandBulletinGenerator:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
        self.cursor = self.conn.cursor()

    def generer_grand_bulletin(self):
        grand_bulletin_query = '''
        SELECT 
            etudiant.mat_etudiant, 
            etudiant.nom_etu, 
            classe.nom_classe, 
            AVG((note.note_cc * cote.cote_cc * matiere.coef_matiere) + (note.note_sn * cote.cote_sn * matiere.coef_matiere)) / AVG(matiere.coef_matiere) AS moyenne
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
        GROUP BY 
            etudiant.mat_etudiant, etudiant.nom_etu, classe.nom_classe
        ORDER BY 
            classe.nom_classe ASC, moyenne DESC
        '''

        classement_query = '''
        SELECT 
            classe.nom_classe, 
            AVG((note.note_cc * cote.cote_cc * matiere.coef_matiere) + (note.note_sn * cote.cote_sn * matiere.coef_matiere)) / AVG(matiere.coef_matiere) AS moyenne_classe
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
        GROUP BY 
            classe.nom_classe
        ORDER BY 
            moyenne_classe DESC
        '''

        doc = SimpleDocTemplate("bul_generale/grand_bulletin.pdf", pagesize=landscape(letter))
        elements = []

        styles = getSampleStyleSheet()
        style_title = styles['Title']
        style_heading = styles['Heading1']
        style_body = styles['BodyText']
        logo = Image("logo/godwin.jpg", width=200, height=100)
        elements.append(logo)
        title = Paragraph("Grand Bulletin - Classement par classe et par ordre de mérite", style_title)
        elements.append(title)

        elements.append(Spacer(1, 20))

        self.cursor.execute(grand_bulletin_query)
        grand_bulletin_data = self.cursor.fetchall()

        grand_bulletin_table_data = [['Matricule', 'Nom', 'Classe', 'Moyenne']]
        grand_bulletin_table_data.extend(grand_bulletin_data)
        grand_bulletin_table = Table(grand_bulletin_table_data)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        grand_bulletin_table.setStyle(style)

        elements.append(grand_bulletin_table)

        elements.append(Spacer(1, 20))

        self.cursor.execute(classement_query)
        classement_data = self.cursor.fetchall()

        classes = []
        moyennes = []

        for row in classement_data:
            classes.append(row[0])

            moyennes.append(row[1])

        # Création du graphique à barres horizontales
        chart = Drawing(400, 200)
        data = [moyennes]
        bc = HorizontalBarChart()
        bc.x = 50
        bc.y = 50
        bc.height = 150
        bc.width = 300
        bc.data = data
        bc.categoryAxis.categoryNames = classes
        bc.valueAxis.valueMin = 0
        bc.valueAxis.valueMax = 20
        bc.valueAxis.valueStep = 1
        bc.bars[0].fillColor = colors.red
        bc.bars[1].fillColor = colors.orange
        bc.bars[2].fillColor = colors.yellow
        bc.bars[3].fillColor = colors.green
        bc.bars[4].fillColor = colors.blue
        bc.bars[5].fillColor = colors.indigo
        bc.bars[6].fillColor = colors.violet
        bc.bars[7].fillColor = colors.pink
        bc.bars[8].fillColor = colors.brown
        bc.bars[9].fillColor = colors.lightgrey  # Correction de la couleur ici
        chart.add(bc)

        elements.append(chart)

        doc.build(elements)
        messagebox.showinfo("cool ", " le document est situer   dans le dossier bul_general/  !")

        self.cursor.close()
        self.conn.close()

# Utilisation de la classe GrandBulletinGenerator
#generator = GrandBulletinGenerator()
#generator.generer_grand_bulletin()