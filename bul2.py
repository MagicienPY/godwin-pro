import pymysql
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# Connexion à la base de données
conn = pymysql.connect(host='192.168.43.154', user='root', password='', db='g_note')
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
SELECT 
    note.semestre, 
    COUNT(DISTINCT CASE WHEN note.type_note = "examen" THEN matiere.id_matiere END) as nombre_matiere, 
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN matiere.nom_matiere END) as liste_matiere, 
    SUM(CASE WHEN note.type_note = "examen" THEN matiere.coef_matiere END) as somme_coefficients,
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN note.note_cc END) as liste_note_cc, 
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN note.note_sn END) as liste_note_sn, 
    etudiant.mat_etudiant, 
    etudiant.nom_etu, 
    note.type_note, 
    (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) AS moyenne, 
    RANK() OVER (ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite,  
    GROUP_CONCAT(DISTINCT CASE WHEN note.type_note = "examen" THEN matiere.coef_matiere END) as coef
FROM 
    cote 
INNER JOIN 
    note ON cote.id_cote = note.id_cote 
INNER JOIN 
    matiere ON note.id_matiere = matiere.id_matiere 
INNER JOIN 
    etudiant ON etudiant.id_etudiant = note.id_etudiant 
WHERE 
    note.type_note IN ("cc", "sn", "examen") 
    AND etudiant.mat_etudiant = %s
GROUP BY 
    etudiant.mat_etudiant 
ORDER BY 
    moyenne DESC
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
        ["Semestre", "Nombre de matières", "Somme des coefficients", "Moyenne", "Ordre de mérite"],
    ]

    for result in results:
        semestre = result[0]
        nombre_matiere = result[1]
        somme_coefficients = result[3]
        moyenne = result[9]
        ordre_merite = result[10]
        row = [semestre, nombre_matiere, somme_coefficients, moyenne, ordre_merite]
        data.append(row)

    # Création du tableau
    table = Table(data)

    # Style du tableau
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Ajout du tableau aux éléments du document
    elements.append(table)

    # Génération du document PDF
    doc.build(elements)

# Fermeture de la connexion à la base de données
conn.close()