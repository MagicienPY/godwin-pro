import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql

def stat():
    # Connexion à la base de données
    connexion = pymysql.connect(host='localhost', user='root', password='', db='g_note')
    cursor = connexion.cursor()

    # Exécution de la requête SQL
    bulletin_query = '''
        SELECT 
            note.semestre, 
            matiere.nom_matiere, 
            matiere.coef_matiere,
            etudiant.mat_etudiant, 
            etudiant.nom_etu, 
            note.type_note, 
            (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) AS moyenne, 
            RANK() OVER (PARTITION BY etudiant.mat_etudiant, note.semestre ORDER BY (SUM(note.note_cc * cote.cote_cc * matiere.coef_matiere) + SUM(note.note_sn * cote.cote_sn * matiere.coef_matiere)) / SUM(matiere.coef_matiere) DESC) AS ordre_merite
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
            etudiant.mat_etudiant, note.semestre, matiere.nom_matiere, matiere.coef_matiere
        ORDER BY 
            note.semestre, moyenne DESC
        '''

    # Calcul de la moyenne de passage
    moyenne_passage_query = '''
        SELECT 
            AVG((note.note_cc * cote.cote_cc + note.note_sn * cote.cote_sn) / 2) 
        FROM 
            note 
        INNER JOIN 
            cote ON note.id_cote = cote.id_cote
        WHERE 
            note.type_note IN ("cc", "sn")
        '''

    # Récupération des données
    cursor.execute(bulletin_query)
    results = cursor.fetchall()
    semestres = []
    matieres = []
    moyennes = []
    for row in results:
        semestres.append(row[0])
        matieres.append(row[1])
        moyennes.append(row[6])
    
    # Récupération de la moyenne de passage
    cursor.execute(moyenne_passage_query)
    moyenne_passage = cursor.fetchone()[0]

    # Vérification si la moyenne de passage est None
    if moyenne_passage is None:
        moyenne_passage = 0.0

    # Calcul du taux de réussite
    nb_reussite = sum(moyenne >= moyenne_passage for moyenne in moyennes)
    taux_reussite = (nb_reussite / len(moyennes)) * 100

    # Création de la fenêtre Tkinter
    window3 = tk.Tk()
    window3.title("Diagramme à barres")
    window3.geometry("800x600")
    
    # Création du diagramme à barres
    figure = Figure(figsize=(10, 6), dpi=100)
    subplot = figure.add_subplot(111)
    x = range(len(semestres))
    subplot.bar(x, moyennes)
    subplot.set_xticks(x)
    subplot.set_xticklabels(matieres, rotation=45)
    subplot.set_xlabel('Matière')
    subplot.set_ylabel('Moyenne')
    subplot.set_title('Moyenne par matière')

    # Affichage du diagramme dans Tkinter
    canvas = FigureCanvasTkAgg(figure, master=window3)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Affichage du taux de réussite
    label = tk.Label(window3, text=f"Taux de réussite : {taux_reussite:.2f}%")
    label.pack()

    # Fermeture de la connexion à la base de données
    cursor.close()
    connexion.close()

    # Lancement de la boucle principale Tkinter
    tk.mainloop()

# Création de la fenêtre Tkinter
window = tk.Tk()
window.title("Statistiques")
window.geometry("800x600")

# Création d'un boutonbutton = tk.Button(window, text="Afficher les statistiques", command=stat)
button.pack()

# Lancement de la boucle principale Tkinter
tk.mainloop()