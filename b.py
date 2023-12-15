from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
import pymysql
from reportlab.platypus import PageBreak

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

    # Requête SQL pour récupérer toutes les matières
    matieres_query = '''
    SELECT DISTINCT nom_matiere
    FROM matiere
    '''

    # Exécution de la requête pour récupérer toutes les matières
    cursor.execute(matieres_query)
    matieres = cursor.fetchall()

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

        # Création du document PDF en format paysage
        doc = SimpleDocTemplate(f"tout_les_buls/{mat_etudiant}.pdf", pagesize=landscape(letter))

        # Informations de l'étudiant
        styles = getSampleStyleSheet()
        style_title = styles['Title']
        style_heading = styles['Heading1']
        style_body = styles['BodyText']
         # Ajout du logo de l'école
        logo = Image("logo/godwin.jpg", width=100, height=100)
        elements.append(logo)
        title = Paragraph("Bulletin GODWIN", style_title)
        elements.append(title)

        elements.append(Spacer(1, 20))
        elements.append(Paragraph("INSTITUT DE FORMATION PROFESSIONNELLE GODWIN", style_heading))
        elements.append(Spacer(1, 20))
        student_info = f"Nom de l'étudiant: {nom_etudiant}<br/>" \
                    f"Matricule de l'étudiant: {mat_etudiant}"
        student_info = Paragraph(student_info, style_body)
        elements.append(student_info)

        elements.append(Spacer(1, 10))
        elements.append(Paragraph("Détails du bulletin:", style_heading))

       

        # Création du tableau des résultats
        # Création du tableau des résultats (suite)
        data = [['Semestre', 'Matière', 'Coefficient', 'Type de note', 'Moyenne', 'Ordre de mérite', 'Classe']]
        for result in results:
            semestre = result[0]
            nom_matiere = result[1]
            coef_matiere = result[2]
            type_note = result[5]
            moyenne = result[6]
            ordre_merite = result[7]
            nom_classe = result[8]

            row = [semestre, nom_matiere, coef_matiere, type_note, moyenne, ordre_merite, nom_classe]
            data.append(row)

        # Style du tableau
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        # Création du tableau
        table = Table(data)
        table.setStyle(table_style)

        elements.append(table)
        elements.append(Spacer(1, 10))
        elements.append(Paragraph("admin:", style_heading))
        elements.append(Spacer(5, 0))
        elements.append(Paragraph("Parents:", style_heading))

        # Ajout d'un saut de page après chaque bulletin
        elements.append(Spacer(1, 20))
        elements.append(PageBreak())

    # Génération du document PDF final
    doc.build(elements)

    # Fermeture de la connexion à la base de données
    cursor.close()
    conn.close()

# Appel de la fonction pour générer les bulletins
afficher_bulletin()