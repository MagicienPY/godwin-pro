from tkinter import *
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart
import pymysql

def generer_grand_bulletin():
    # Connexion à la base de données
    conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
    cursor = conn.cursor()

    # Requête SQL pour récupérer les données des étudiants classés par classe, puis par ordre de mérite
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

    # Requête SQL pour récupérer le classement des classes par ordre de mérite
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

    # Création du document PDF en format paysage
    doc = SimpleDocTemplate("grand_bulletin.pdf", pagesize=landscape(letter))

    # Liste pour contenir les éléments du document PDF
    elements = []

    # Style des paragraphes
    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_heading = styles['Heading1']
    style_body = styles['BodyText']

    # Titre du grand bulletin
    title = Paragraph("Grand Bulletin - Classement par classe et par ordre de mérite", style_title)
    elements.append(title)

    elements.append(Spacer(1, 20))

    # Exécution de la requête pour récupérer les données du grand bulletin
    cursor.execute(grand_bulletin_query)
    grand_bulletin_data = cursor.fetchall()

    # Création de la table pour les données du grand bulletin
    grand_bulletin_table_data = [['Matricule', 'Nom', 'Classe', 'Moyenne']]
    grand_bulletin_table_data.extend(grand_bulletin_data)
    grand_bulletin_table = Table(grand_bulletin_table_data)

    # Style de la table du grand bulletin
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

    # Application du style à la table du grand bulletin
    grand_bulletin_table.setStyle(style)

    # Ajout de la table du grand bulletin aux éléments du document PDF
    elements.append(grand_bulletin_table)

    elements.append(Spacer(1, 20))

    # Exécution de la requête pour récupérer les données du classement des classes
    cursor.execute(classement_query)
    classement_data = cursor.fetchall()

    # Liste pour contenir les noms des classes et les moyennes de chaque classe
    classes = []
    moyennes = []

    # Remplissage des listes de noms de classes et de moyennes
    for row in classement_data:
        classes.append(row[0])
        moyennes.append(row[1])

    # Création du graphique à barres pour le classement des classes
    drawing = Drawing(400, 200)
    data = [moyennes]
    bc = HorizontalBarChart()
    bc.width = 300
    bc.height = 200
    bc.data = data
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = 20
    bc.valueAxis.valueStep = 2
    bc.categoryAxis.categoryNames = classes
    bc.bars[0].fillColor = colors.blue
    drawing.add(bc)

    # Ajout du graphique à barres aux éléments du document PDF
    elements.append(drawing)

    # Génération du document PDF
    doc.build(elements)

    # Fermeture de la connexion à la base de données
    conn.close()

    print("Le grand bulletin a été généré avec succès!")

# Appel de la fonction pour générer le grand bulletin
generer_grand_bulletin()