import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql

class Statistiques:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Statistiques")
        self.window.geometry("400x300")

        self.button = tk.Button(self.window, text="Afficher", command=self.afficher_diagramme)
        self.button.pack()

    def afficher_diagramme(self):
        # Connexion à la base de données
        connexion = pymysql.connect(host='localhost', user='root', password='', db='g_note')
        cursor = connexion.cursor()

        # Exécution de la requête SQL pour calculer le taux de réussite par classe
        taux_reussite_query = '''
            SELECT 
                classe.nom_classe, 
                AVG((note.note_cc * cote.cote_cc + note.note_sn * cote.cote_sn) / 2) AS taux_reussite
            FROM 
                note 
            INNER JOIN 
                cote ON note.id_cote = cote.id_cote
            INNER JOIN 
                etudiant ON etudiant.id_etudiant = note.id_etudiant
            INNER JOIN 
                classe ON classe.id_classe = etudiant.id_classe
            WHERE 
                note.type_note IN ("examen")
            GROUP BY 
                classe.nom_classe
            '''

        # Récupération des données
        cursor.execute(taux_reussite_query)
        results = cursor.fetchall()
        classes = []
        taux_reussite = []
        for row in results:
            classes.append(row[0])
            taux_reussite.append(row[1])

        # Création de la fenêtre Tkinter pour le diagramme en cercle
        window3 = tk.Toplevel(self.window)
        window3.title("Diagramme en cercle")
        window3.geometry("800x600")

        # Création du diagramme en cercle
        figure = Figure(figsize=(6, 4), dpi=100)
        subplot = figure.add_subplot(111)
        colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        subplot.pie(taux_reussite, labels=classes, autopct='%1.1f%%', colors=colors)
        subplot.set_title('Taux de réussite par classe')

        # Affichage du diagramme dans Tkinter
        canvas = FigureCanvasTkAgg(figure, master=window3)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Fermeture de la connexion à la base de données
        cursor.close()
        connexion.close()

    def run(self):
        self.window.mainloop()

# Création de l'instance de la classe Statistiques
#statistiques = Statistiques()
#statistiques.run()