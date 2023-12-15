import mysql.connector
from tabulate import tabulate

# Fonction de connexion à la base de données
def connect_db():

  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="myscolar"
  )

  return db

# Fonction de calcul de moyenne trimestrielle  
def calcul_moyenne_trimestre(cursor, id_eleve, id_trimestre):

  # Récupérer les notes de l'élève
  notes = cursor.execute("""
    SELECT * FROM Note
    WHERE Id_eleve = %s AND Id_trimestre = %s
  """, (Id_eleve, id_trimestre))

  # Calcul de la moyenne
  #...

  return moyenne

# Fonction de génération du bulletin
def generer_bulletin(cursor, Id_eleve):

  bulletin = []

  # Récupérer l'élève
  cursor.execute("SELECT * FROM Eleve WHERE id=%s", (Id_eleve,))
  eleve = cursor.fetchone()

  # Remplir les infos élèves
  bulletin.append(eleve["nom"])

  # Parcourir les trimestres  
  for trimestre in TRIMESTRES:

    # Calcul de la moyenne trimestrielle
    moyenne = calcul_moyenne_trimestre(cursor, Id_eleve, trimestre)

    # Ajouter à la bulletin
    bulletin.append(moyenne)

  return bulletin

if __name__ == '__main__':

  # Connexion à la base
  db = connect_db()
  cursor = db.cursor()

  # Parcourir les élèves
  for eleve in cursor.execute("SELECT * FROM Eleve"): 

    # Générer le bulletin
    print(tabulate(generer_bulletin(cursor, eleve["Id_eleve"])))

  # Fermeture de la connexion
  cursor.close()
  db.close()
def calcul_moyenne_annuelle():
    pass