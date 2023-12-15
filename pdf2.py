from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, LongTable, TableStyle
from reportlab.platypus.tables import Table
#from reportlab.platypus.paragraph import paragraph
from tkinter import Tk
from tkinter import messagebox
import pymysql

con76 = pymysql.connect(user='root', password='', database='g_note')
cursor = con76.cursor()

query = 'SELECT note.semestre, matiere.nom_matiere, note.note_cc, note.note_sn, matiere.coef_matiere ,(note.note_cc*cote.cote_cc) + (note.note_sn* cote.cote_sn), etudiant.mat_etudiant, etudiant.nom_etu, note.type_note from cote INNER JOIN note on cote.id_cote = note.id_cote INNER JOIN matiere on note.id_matiere = matiere.id_matiere INNER JOIN etudiant on etudiant.id_etudiant = note.id_etudiant order by ((note.note_cc*cote.cote_cc) + (note.note_sn* cote.cote_sn)) desc;'
r = cursor.execute(query)
data = cursor.fetchall()

con76.close()
def imprimer_rs ():
# Créez un document PDF
    pdf_filename = 'tableresultat1.pdf'
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Créez un tableau avec les données
    table_data = [["semestre", "matière", "note du cc", "note de la sn", "coef", "sn + cc", "matricule", "nom etudiant", "type de note"]] # En-têtes de colonnes
    table_data += data
   ## salut = paragraph()

    table = LongTable(table_data)

    # Appliquez un style au tableau
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)

    # Ajoutez le tableau au document PDF
    elements = [table]
    document.build(elements)

    # Affichez un message de confirmation
    Tk().withdraw()  # masquer la fenêtre racine Tkinter
    messagebox.showinfo("PDF créé", "Le PDF du tableau a été créé avec succès.")


imprimer_rs()