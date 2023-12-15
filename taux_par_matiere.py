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
            matiere.nom_matiere, 
            COUNT(*) AS count
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
            matiere.nom_matiere
        '''

    # Récupération des données
    cursor.execute(bulletin_query)
    results = cursor.fetchall()
    matieres = []
    counts = []
    for row in results:
        matieres.append(row[0])
        counts.append(row[1])

    # Création de la fenêtre Tkinter
    window3 = tk.Tk()
    window3.title("Diagramme en cercle")
    window3.geometry("800x600")

    # Création du diagramme en cercle
    figure = Figure(figsize=(6, 4), dpi=100)
    subplot = figure.add_subplot(111)
    subplot.pie(counts, labels=matieres, autopct='%1.1f%%')
    subplot.set_title('Répartition par matière')

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

# Création du bouton pour afficher le diagramme
button = tk.Button(window, text="Afficher", command=stat)
button.pack()

# Lancement de la boucle principale Tkinter
tk.mainloop()