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

    # Requête SQL pour récupérer les données du bulletin de chaque étudiant
    bulletin_query = '''
    SELECT 
        note.semestre, 
        matiere.nom_matiere, 
        matiere.coef_matiere,
        note.note_cc,
        cote.cote_cc,
        note.note_sn,
        cote.cote_sn,
        etudiant.mat_etudiant, 
        etudiant.nom_etu, 
        note.type_note, 
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
        classe.nom_classe, etudiant.mat_etudiant, note.semestre
    '''

    # Liste pour contenir les éléments du document PDF
    elements = []

    # Liste pour stocker les moyennes finales de chaque étudiant
    moyennes_finales = []

    # Génération du bulletin individuel pour chaque étudiant
    for student in students:
        mat_etudiant = student[0]
        nom_etudiant = student[1]

        # Exécution de la requête pour récupérer les données du bulletin de l'étudiant
        cursor.execute(bulletin_query, (mat_etudiant,))
        results = cursor.fetchall()

        # Calcul de la moyenne finale de l'étudiant
        somme_notes_ponderees = 0
        somme_coefficients = 1

        for result in results:
            coef_matiere = result[2]
            note_cc = result[3]
            cote_cc = result[4]
            note_sn = result[5]
            cote_sn = result[6]

            somme_notes_ponderees += (note_cc * cote_cc + note_sn * cote_sn) * coef_matiere
            somme_coefficients += coef_matiere
            
            moyenne_finale = somme_notes_ponderees / somme_coefficients
            moyennes_finales.append(moyenne_finale)

            print(moyenne_finale)

        # ... Code pour la génération du bulletin ...

    # Imprimer les moyennes finales de chaque étudiant
    for i, student in enumerate(students):
        mat_etudiant = student[0]
        moyenne_finale = moyennes_finales[i]
        print(f"Étudiant : {student[1]}, Matricule : {student[0]}, Moyenne finale : {moyennes_finales[i]}")
        insert_query = "INSERT INTO moyennes_finales (mat_etudiant, moyenne_finale) VALUES (%s, %s)"
        cursor.execute(insert_query, (mat_etudiant, moyenne_finale))
        conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()

# Appel de la fonction pour afficher les bulletins des étudiants
afficher_bulletin()