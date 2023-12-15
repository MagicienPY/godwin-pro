import pymysql
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

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
SELECT * FROM  note;
'''

# Génération du bulletin individuel pour chaque étudiant
for student in students:
    mat_etudiant = student[0]
    nom_etudiant = student[1]

    # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
    cursor.execute(bulletin_query, (mat_etudiant,))
    results = cursor.fetchall()

    # Création du document PDF en format paysage
    doc = SimpleDocTemplate(f"{mat_etudiant}.pdf", pagesize=landscape(letter))

    # Liste pour contenir les éléments du document PDF
    elements = []

    # Style des paragraphes
    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_heading = styles['Heading1']
    style_body = styles['BodyText']

    # Informations de l'étudiant
    title = Paragraph("Bulletin Universitaire", style_title)
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

    # Ajout du tableau aux éléments du document
    elements.append(table)

    # Ajout du nom de l'établissement et de la signature
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Etablissement: IAI-CAMEROUN", style_body))
    elements.append(Paragraph("Application de gestion: MYSCOLAR", style_body))

    # Génération du document PDF
    doc.build(elements)

# Fermeture de la connexion à la base de données
conn.close()