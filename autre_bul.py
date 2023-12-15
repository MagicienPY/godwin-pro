import pymysql
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import tkinter as tk

def generer_bulletin():
    mat_etudiant = mat_etudiant_entry.get()
    nom_etudiant = nom_etudiant_entry.get()

    # Connexion à la base de données
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="g_note"
    )

    # Création du curseur pour exécuter les requêtes SQL
    cursor = db.cursor()

    # Récupération de la classe de l'étudiant
    classe = classe_etudiant_entry.get()

    # Requête SQL pour récupérer les données de l'étudiant
    etudiant_query = '''
    SELECT 
        etudiant.nom_etu, 
        matiere.nom_matiere, 
        note.note_cc, 
        note.note_sn, 
        matiere.coef_matiere,
        (note.note_cc * matiere.coef_matiere + note.note_sn * matiere.coef_matiere) / (matiere.coef_matiere * 2) AS note_finale
    FROM 
        etudiant 
    INNER JOIN 
        note ON etudiant.id_etudiant = note.id_etudiant 
    INNER JOIN 
        matiere ON note.id_matiere = matiere.id_matiere 
    WHERE 
        etudiant.mat_etudiant = %s
    '''

    # Exécution de la requête pour récupérer les données de l'étudiant
    cursor.execute(etudiant_query, (mat_etudiant,))
    etudiant_data = cursor.fetchall()

    # Création du tableau du bulletin
    bulletin_table_data = [['Matière', 'Note CC', 'Note SN', 'Coef Matière', 'Note finale']]

    # Ajout des données de l'étudiant dans le tableau du bulletin
    for row in etudiant_data:
        bulletin_table_data.append(list(row[1:]))

    # Récupération de la note finale de l'étudiant
    note_finale = etudiant_data[0][5]

    # Requête SQL pour calculer la moyenne des camarades de classe de l'étudiant
    moyenne_camarades_query = '''
    SELECT 
        (SUM(note.note_cc * matiere.coef_matiere) + SUM(note.note_sn * matiere.coef_matiere)) / (SUM(matiere.coef_matiere)*2) AS moyenne
    FROM 
        etudiant 
    INNER JOIN 
        note ON etudiant.id_etudiant = note.id_etudiant 
    INNER JOIN 
        matiere ON note.id_matiere = matiere.id_matiere 
    WHERE 
        etudiant.id_classe = %s
        AND etudiant.mat_etudiant != %s
    GROUP BY 
        etudiant.mat_etudiant
    '''

    # Exécution de la requête pour calculer la moyenne des camarades de classe
    cursor.execute(moyenne_camarades_query, (classe, mat_etudiant))
    camarades_data = cursor.fetchall()

    # Calcul du rang de l'étudiant parmi ses camarades de classe
    rang_etudiant = 1
    for row in camarades_data:
        moyenne_camarade = row[0]
        if moyenne_camarade > note_finale:
            rang_etudiant += 1

    # Création du document PDF
    doc = SimpleDocTemplate("bulletin.pdf", pagesize=letter)

    # Création du tableau du bulletin avec le style
    bulletin_table = Table(bulletin_table_data)
    bulletin_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0,0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Création du paragraphe contenant la moyenne de l'étudiant
    moyenne_etudiant_paragraph = f"Moyenne : {note_finale}"

    # Création du paragraphe contenant le rang de l'étudiant
    rang_etudiant_paragraph = f"Rang : {rang_etudiant}"

    # Création du paragraphe contenant la moyenne des camarades de classe
    moyenne_camarades_paragraph = "Moyenne des camarades de classe : "

    for i, row in enumerate(camarades_data):
        moyenne_camarades_paragraph += f"{row[0]}"

        if i != len(camarades_data) - 1:
            moyenne_camarades_paragraph += ", "

    # Création du paragraphe contenant le nom et la matricule de l'étudiant
    nom_et_mat_paragraph = f"Nom : {nom_etudiant}\nMatricule : {mat_etudiant}"

    # Création de la liste des éléments à inclure dans le document PDF
    elements = [
        bulletin_table,
        moyenne_etudiant_paragraph,
        rang_etudiant_paragraph,
        moyenne_camarades_paragraph,
        nom_et_mat_paragraph
    ]

    # Ajout des éléments au document PDF
    doc.build(elements)

    # Fermeture de la connexion à la base de données
    db.close()

    # Affichage d'un message de confirmation
    tk.messagebox.showinfo("Bulletin généré", "Le bulletin a été généré avec succès.")

# Création de la fenêtre Tkinter
window = tk.Tk()

# Création des labels et des entry pour les informations de l'étudiant
mat_etudiant_label = tk.Label(window, text="Matricule de l'étudiant :")
mat_etudiant_label.pack()
mat_etudiant_entry = tk.Entry(window)
mat_etudiant_entry.pack()

nom_etudiant_label = tk.Label(window, text="Nom de l'étudiant :")
nom_etudiant_label.pack()
nom_etudiant_entry = tk.Entry(window)
nom_etudiant_entry.pack()

classe_etudiant_label = tk.Label(window, text="Classe de l'étudiant :")
classe_etudiant_label.pack()
classe_etudiant_entry = tk.Entry(window)
classe_etudiant_entry.pack()

# Création du bouton pour générer le bulletin
generer_bulletin_button = tk.Button(window, text="Générer le bulletin", command=generer_bulletin)
generer_bulletin_button.pack()

# Exécution de la boucle principale de la fenêtre Tkinter
window.mainloop()