import pymysql
from fpdf import FPDF

def imprimer_rs():
    # Connexion à la base de données
    con76 = pymysql.connect(user='root', password='', database='g_note')
    cursor = con76.cursor()

    # Exécution de la requête SQL
    query = """
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
    GROUP BY 
        etudiant.mat_etudiant 
    ORDER BY 
        moyenne DESC;
    """

    cursor.execute(query)

    # Récupération des résultats de la requête
    results = cursor.fetchall()

    # Création d'un document PDF en mode paysage
    pdf = FPDF(orientation="L")

    # Ajout d'une page au document
    pdf.add_page()

    # Ajout des titres au document
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(30, 10, txt="Semestre", border=1, align="L")
    pdf.cell(40, 10, txt="Nombre de matières", border=1, align="L")
    pdf.cell(60, 10, txt="Liste des matières", border=1, align="L")
    pdf.cell(40, 10, txt="Somme des coefficients", border=1, align="L")
    pdf.cell(40, 10, txt="Liste des notes CC", border=1, align="L")
    pdf.cell(40, 10, txt="Liste des notes SN", border=1, align="L")
    pdf.cell(30, 10, txt="Matricule étudiant", border=1, align="L")
    pdf.cell(40, 10, txt="Nom étudiant", border=1, align="L")
    pdf.cell(30, 10, txt="Type de note", border=1, align="L")
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for row in results:
        for item in row:
            pdf.cell(30, 10, txt=str(item), border=1, align="R")
        pdf.ln()

    # Sauvegarde du document PDF
    pdf.output("resultats1.pdf")

    # Fermeture de la connexion à la base de données
    cursor.close()
    con76.close()

# Appel de la fonction pour créer le document PDF
imprimer_rs()