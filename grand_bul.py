from tkinter import *
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import pymysql

def generer_grand_bulletin():
    # Connexion à la base de données
    conn = pymysql.connect(host='localhost', user='root', password='', db='g_note')
    cursor = conn.cursor()

    # Requête SQL pour récupérer les informations des classes
    classes_query = '''
    SELECT id_classe, nom_classe
    FROM classe
    '''
    # Exécution de la requête pour récupérer les informations des classes
    cursor.execute(classes_query)
    classes = cursor.fetchall()

    for classe in classes:
        id_classe = classe[0]
        nom_classe = classe[1]

        # Requête SQL pour récupérer les informations des étudiants de la classe
        etudiants_query = '''
        SELECT mat_etudiant, nom_etu
        FROM etudiant
        WHERE id_classe = %s
        '''
        # Exécution de la requête pour récupérer les informations des étudiants de la classe
        cursor.execute(etudiants_query, (id_classe,))
        etudiants = cursor.fetchall()

        for etudiant in etudiants:
            mat_etudiant = etudiant[0]
            nom_etudiant = etudiant[1]

            # Génération du bulletin de l'étudiant
            generer_bulletin(mat_etudiant, nom_etudiant, nom_classe)

    # Fermeture de la connexion à la base de données
    conn.close()

def generer_bulletin(mat_etudiant, nom_etudiant, nom_classe):
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
    doc = SimpleDocTemplate(f"ib/{nom_classe}/{mat_etudiant}.pdf", pagesize=landscape(letter))

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
    bulletin = cursor.fetchall()

    # Tableau pour afficher les résultats
    data = []

    # En-tête du tableau
    header = ["Semestre", "Matière", "Coefficient", "Type de note", "Moyenne", "Ordre de mérite"]
    data.append(header)

    # Remplissage du tableau avec les données du bulletin
    for row in bulletin:
        semestre = row[0]
        matiere = row[1]
        coef_matiere = row[2]
        type_note = row[5]
        moyenne = row[6]
        ordre_merite = row[7]

        data.append([semestre, matiere, coef_matiere, type_note, moyenne, ordre_merite])

    # Style du tableau
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    # Création du tableau
    table = Table(data)
    table.setStyle(table_style)

    # Ajout du tableau au document PDF
    elements.append(table)

    # Ajout des éléments au document PDF
    doc.build(elements)

    # Fermeture de la connexion à la base de données
    conn.close()

# Appel de la fonction pour générer les bulletins
generer_grand_bulletin()