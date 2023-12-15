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

    # Requête SQL pour récupérer les rangs des étudiants
    ranks_query = '''
    SELECT mat_etudiant, ordre_merite
    FROM (
        SELECT etudiant.mat_etudiant, RANK() OVER (ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite
        FROM matiere
        LEFT JOIN note ON note.id_matiere = matiere.id_matiere
        LEFT JOIN cote ON cote.id_cote = note.id_cote 
        LEFT JOIN etudiant ON etudiant.id_etudiant = note.id_etudiant 
        WHERE note.type_note IN ("cc", "sn", "examen")
        GROUP BY etudiant.mat_etudiant
    ) AS ranks
    '''

    # Exécution de la requête pour récupérer les rangs des étudiants
    cursor.execute(ranks_query)
    ranks = cursor.fetchall()

    # Liste pour contenir les éléments du document PDF
    elements = []
    bulletin_query = '''
        SELECT semestre, nom_matiere, coef_matiere, type_note, moyenne, rang, nom_classe
        FROM note
        JOIN matiere ON note.id_matiere = matiere.id_matiere
        JOIN etudiant ON note.id_etudiant = etudiant.id_etudiant
        JOIN classe ON etudiant.id_classe = classe.id_classe
        WHERE etudiant.mat_etudiant = %s
        '''
    # Génération du bulletin individuel pour chaque étudiant
    for student in students:
        mat_etudiant = student[0]
        nom_etudiant = student[1]

        # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
        cursor.execute(bulletin_query, (mat_etudiant,))
        results = cursor.fetchall()

        # Recherche du rang de l'étudiant
        rank = next((r[1] for r in ranks if r[0] == mat_etudiant), None)

        # Création du tableau contenant les données du bulletin
        data = [['Semestre', 'Matière', 'Coefficient', 'Type de note', 'Moyenne', 'Rang']]

        for result in results:
            semestre = result[0]
            nom_matiere = result[1]
            coef_matiere = result[2]
            type_note = result[5]
            moyenne = result[6]
            rang = result[7]
            nom_classe = result[8]

            data.append([semestre, nom_matiere, coef_matiere, type_note, moyenne, rang])
        styles = getSampleStyleSheet()
        # Création du titre du bulletin
        title = f'BULLETIN DE NOTES\n\nÉtudiant : {nom_etudiant}\nMatricule : {mat_etudiant}\nClasse : {nom_classe}\nRang : {rank if rank else "-"}'

        # Ajout du titre au document
        elements.append(Paragraph(title, styles["Title"]))

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

        # Ajout d'un saut de page après chaque bulletin individuel
        elements.append(PageBreak())

    # Création du document PDF
    doc = SimpleDocTemplate("i/bulletins.pdf", pagesize=letter)

    # Ajout des éléments au document
    doc.build(elements)

    # Fermeture de la connexion à la base de données
    cursor.close()
    conn.close()

# Appel de la fonction pour générer les bulletins
afficher_bulletin()