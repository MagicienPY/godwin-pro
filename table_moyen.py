import tkinter as tk
from tkinter import ttk
import pymysql
from fpdf import FPDF
from tkinter import messagebox

class StatistiquesClasse:
    def __init__(self):
        # Création de la fenêtre Tkinter
        self.window = tk.Tk()
        self.window.title("Statistiques")
        self.window.geometry("600x300")

        # Création du champ d'entrée de texte pour la recherche
        self.search_entry = tk.Entry(self.window)
        self.search_entry.pack()

        # Création du bouton de recherche
        self.search_button = tk.Button(self.window, text="Rechercher", command=self.rechercher_etudiant)
        self.search_button.pack()

        # Création du tableau
        self.table = ttk.Treeview(self.window, columns=('Nom', 'Matricule', 'Classe', 'Moyenne'))
        self.table.heading('Nom', text='Nom')
        self.table.heading('Matricule', text='Matricule')
        self.table.heading('Classe', text='Classe')
        self.table.heading('Moyenne', text='Moyenne')
        self.table.pack()

        # Création du bouton d'impression du bulletin
        self.print_button = tk.Button(self.window, text="Imprimer bulletin", command=self.imprimer_bulletin)
        self.print_button.pack()

        # Lancement de la boucle principale Tkinter
        tk.mainloop()

    def afficher_table(self):
        # Connexion à la base de données
        connexion = pymysql.connect(host='localhost', user='root', password='', db='g_note')
        cursor = connexion.cursor()

        # Exécution de la requête SQL
        bulletin_query = '''
            SELECT 
                etudiant.nom_etu,
                etudiant.mat_etudiant, 
                classe.nom_classe,
                SUM((note.note_cc * cote.cote_cc + note.note_sn * cote.cote_sn) * matiere.coef_matiere) / SUM(matiere.coef_matiere) AS moyenne
            FROM 
                cote 
            INNER JOIN 
                note ON cote.id_cote = note.id_cote 
            INNER JOIN 
                matiere ON note.id_matiere = matiere.id_matiere 
            INNER JOIN 
                etudiant ON etudiant.id_etudiant = note.id_etudiant
            INNER JOIN
                classe ON etudiant.id_classe = classe.id_classe 
            WHERE 
                note.type_note IN ("cc", "sn", "examen") 
            GROUP BY 
                etudiant.nom_etu, etudiant.mat_etudiant, classe.nom_classe
            ORDER BY 
                etudiant.nom_etu
            '''

        # Récupération des données
        cursor.execute(bulletin_query)
        results = cursor.fetchall()

        # Effacer les données précédentes dans le tableau
        self.table.delete(*self.table.get_children())

        for row in results:
            nom = row[0]
            matricule = row[1]
            classe = row[2]
            moyenne = row[3]
            self.table.insert('', 'end', values=(nom, matricule, classe, moyenne))

        # Fermeture de la connexion à la base de données
        cursor.close()
        connexion.close()

    def rechercher_etudiant(self):
        # Récupérer le matricule de l'étudiant à rechercher
        matricule = self.search_entry.get()

        # Connexion à la base de données
        connexion = pymysql.connect(host='localhost', user='root', password='', db='g_note')
        cursor = connexion.cursor()

        # Exécution de la requête SQL de recherche
        recherche_query = f'''
            SELECT 
                etudiant.nom_etu,
                etudiant.mat_etudiant, 
                classe.nom_classe,
                SUM((note.note_cc * cote.cote_cc + note.note_sn * cote.cote_sn) * matiere.coef_matiere) / SUM(matiere.coef_matiere) AS moyenne
            FROM 
                cote 
            INNER JOIN 
                note ON cote.id_cote = note.id_cote 
            INNER JOIN 
                matiere ON note.id_matiere = matiere.id_matiere 
            INNER JOIN 
                etudiant ON etudiant.id_etudiant = note.id_etudiant
            INNER JOIN
                classe ON etudiant.id_classe = classe.id_classe 
            WHERE 
                note.type_note IN ("cc", "sn", "examen") 
                AND etudiant.mat_etudiant = '{matricule}'
            GROUP BY 
                etudiant.nom_etu, etudiant.mat_etudiant, classe.nom_classe
            '''

        # Récupération des données de recherche
        cursor.execute(recherche_query)
        results = cursor.fetchall()

        # Effacer les données précédentes dans le tableau
        self.table.delete(*self.table.get_children())

        for row in results:
            nom = row[0]
            matricule = row[1]
            classe = row[2]
            moyenne = row[3]
            self.table.insert('', 'end', values=(nom, matricule, classe, moyenne))

        # Fermeture de la connexion à la base de données
        cursor.close()
        connexion.close()

    def imprimer_bulletin(self):
        # Récupérer les informations de l'étudiant sélectionné dans le tableau
        selected_item = self.table.selection()
        if selected_item:
            values = self.table.item(selected_item)['values']
            nom = values[0]
            matricule = values[1]
            classe = values[2]
            moyenne = values[3]

            # Générer le fichier PDF du bulletin
            pdf = FPDF()
            pdf.add_page()

            # Ajouter les informations du bulletin
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Bulletin de notes", ln=True, align='C')
            pdf.cell(200, 10, txt=f"Nom: {nom}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Matricule: {matricule}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Classe: {classe}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Moyenne: {moyenne}", ln=True, align='L')

            # Enregistrer le fichier PDF
            pdf.output("bulletin.pdf")
            messagebox.showinfo("cool ","Bulletin généré avec succès! vous pouvez le retrouver dans les fichers sous le nom de bulletins.pdf  !!!")
            print("Bulletin généré avec succès!")
            self.window.destroy()
        else:
            messagebox.showinfo("Attention","Veuillez sélectionner un étudiant dans le tableau.")
            print("Veuillez sélectionner un étudiant dans le tableau.")

# Création de l'instance de la classe
#statistiques_classe = StatistiquesClasse()