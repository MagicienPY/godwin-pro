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
    doc = SimpleDocTemplate("grand_bulletin2.pdf", pagesize=landscape(letter))

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

    # Création du tableau pour afficher les données du grand bulletin
    grand_bulletin_table_data = [['Matricule', 'Nom', 'Classe', 'Moyenne']]

    for row in grand_bulletin_data:
        mat_etudiant = row[0]
        nom_etudiant = row[1]
        nom_classe = row[2]
        moyenne = row[3]

        grand_bulletin_table_data.append([mat_etudiant, nom_etudiant, nom_classe, moyenne])

    # Création du tableau avec les données du grand bulletin
    grand_bulletin_table = Table(grand_bulletin_table_data)

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
    grand_bulletin_table.setStyle(style)

    # Ajouter le tableau au document PDF
    elements.append(grand_bulletin_table)

    elements.append(Spacer(1, 20))

    # Exécution de la requête pour récupérer les données du classement des classes
    cursor.execute(classement_query)
    classement_data = cursor.fetchall()

    # Création du tableau pour afficher le classement des classes
    classement_table_data = [['Classe', 'Moyenne de la classe']]

    for row in classement_data:
        nom_classe = row[0]
        moyenne_classe = row[1]

        classement_table_data.append([nom_classe, moyenne_classe])

    # Création du tableau avec les données du classement des classes
    classement_table = Table(classement_table_data)

    # Style du tableau
    style_classement = TableStyle([
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
    classement_table.setStyle(style_classement)

    # Ajouter le tableau au document PDF
    elements.append(classement_table)

    # Génération du document PDF
    doc.build(elements)

    # Fermeture de la connexion à la base de données
    conn.close()

# Interface graphique avec tkinter
root = Tk()
root.title("Générateur de grand bulletin")
root.geometry("400x200")

generer_button = Button(root, text="Générer le grand bulletin", command=generer_grand_bulletin)
generer_button.pack()

root.mainloop()