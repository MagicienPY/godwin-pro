import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql

def stat():
    mat_etudiant = chama.get()  # Récupération du matricule saisi
    
    # Connexion à la base de données
    connexion = pymysql.connect(host='localhost', user='root', password='', db='g_note')
    cursor = connexion.cursor()

    # Exécution de la requête SQL
    bulletin_query = f'''
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
            AND etudiant.mat_etudiant = "{mat_etudiant}"
        GROUP BY 
            etudiant.mat_etudiant, note.semestre, matiere.nom_matiere, matiere.coef_matiere
        ORDER BY 
            note.semestre, moyenne DESC
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

    # Création de la fenêtre Tkinter
    window3 = tk.Tk()
    window3.title("Diagramme à barres")
    window3.geometry("800x600")
    
    # Création du widget de saisie du matricule
    chama_label = tk.Label(window3, text="Matricule")
    chama_label.pack()
    chama_entry = tk.Entry(window3)
    chama_entry.pack()
    
    # Création du bouton pour afficher le diagramme
    button = tk.Button(window3, text="Afficher", command=stat)
    button.pack()

    # Création du diagramme à barres
    figure = Figure(figsize=(6, 4), dpi=100)
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

    # Fermeture de la connexion à la base de données
    cursor.close()
    connexion.close()

    # Lancement de la boucle principale Tkinter
    tk.mainloop()
    
# Création de la fenêtre Tkinter
window = tk.Tk()
window.title("Statistiques")
window.geometry("400x300")

# Création du widget de saisie du matricule
chama_label = tk.Label(window, text="Matricule")
chama_label.pack()
chama = tk.Entry(window)
chama.pack()

# Création du bouton pour afficher le diagramme
button = tk.Button(window, text="Afficher", command=stat)
button.pack()

# Lancement de la boucle principale Tkinter
window.mainloop()