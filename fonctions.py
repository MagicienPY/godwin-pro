#################################################################
from tkinter import *
import tkinter.messagebox as msgbox
import customtkinter as ctk
import tkinter.ttk as ttk
import aspose.pdf as pdf
import pymysql


class fonc:
    def __init__(self):
        pass
    def actualiser2 ():
        con = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con.cursor()
          # Supprimer tous les éléments existants dans la table
        table.delete(*table.get_children())
            # Récupérer les données depuis la base de données
        cursor = con.cursor()
        cursor.execute("SELECT * FROM matiere")
        data = cursor.fetchall()
        print("ok1")

            # Insérer les données dans le tableau
        for row in data:
            table.insert("", "end", values=row)
    def ajouterMatier (self,a,b,c,d):
        con = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con.cursor()
        f = fonc()
        f.actualiser2
     
     


        sql = "INSERT INTO matiere (id_matiere, nom_matiere, id_module, coef_matiere) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (a, b, c, d))
            
        con.commit()
        f.actualiser2()
        con.close()

    def modifierMatier (self,a,b,c,d):
        con = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con.cursor()
        f = fonc()
        f.actualiser2
        
        # 696354742 BA2B ############################################

        sql = "UPDATE matiere SET nom_matiere = %s, coef_matiere = %s, id_module = %s WHERE id_matiere = %s"
        cursor.execute(sql, (a, b, c,d ))
        con.commit()
        f.actualiser1()
        con.close()

    def supprimerMatier(self,a):
        con = pymysql.connect(user='root', password ='',database = 'g_note')
        cursor = con.cursor()
        f = fonc()
        f.actualiser2
        #actualiser1()
        iden = chama.get()
        nom = chama1.get()
        coef = chama2.get()

        sql = "DELETE FROM matiere WHERE id_matiere = %s"
        cursor.execute(sql, (a))
        con.commit()
        f.actualiser1()
        con.close()
###############################
        def ajouterclasse ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "INSERT INTO module (id_module,nom_module, coef_module) VALUES (%s, %s, %s)"
            cursor.execute(sql, (iden, nom, coef))
            
            con.commit()
            actualiser1()
            con.close()

        def modifierclasse ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "UPDATE module SET nom_module =%s, coef_module  = %s WHERE id_module = %s"
            cursor.execute(sql, (nom, coef, iden))
            con.commit()
            actualiser1()
            con.close()

        def supprimerClasse():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "DELETE FROM module WHERE id_module = %s"
            cursor.execute(sql, (iden))
            con.commit()
            actualiser1()
            con.close()
#################################
        def ajouterspecial ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "INSERT INTO module (id_module,nom_module, coef_module) VALUES (%s, %s, %s)"
            cursor.execute(sql, (iden, nom, coef))
            
            con.commit()
            actualiser1()
            con.close()

        def modifierspecial ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "UPDATE module SET nom_module =%s, coef_module  = %s WHERE id_module = %s"
            cursor.execute(sql, (nom, coef, iden))
            con.commit()
            actualiser1()
            con.close()

        def supprimerspecial():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "DELETE FROM module WHERE id_module = %s"
            cursor.execute(sql, (iden))
            con.commit()
            actualiser1()
            con.close()
#########################################
        def ajouteruser ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "INSERT INTO module (id_module,nom_module, coef_module) VALUES (%s, %s, %s)"
            cursor.execute(sql, (iden, nom, coef))
            
            con.commit()
            actualiser1()
            con.close()

        def modifieruser ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "UPDATE module SET nom_module =%s, coef_module  = %s WHERE id_module = %s"
            cursor.execute(sql, (nom, coef, iden))
            con.commit()
            actualiser1()
            con.close()

        def supprimeruser():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "DELETE FROM module WHERE id_module = %s"
            cursor.execute(sql, (iden))
            con.commit()
            actualiser1()
            con.close()
############################

        def ajouternote ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "INSERT INTO module (id_module,nom_module, coef_module) VALUES (%s, %s, %s)"
            cursor.execute(sql, (iden, nom, coef))
            
            con.commit()
            actualiser1()
            con.close()

        def modifiernote():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "UPDATE module SET nom_module =%s, coef_module  = %s WHERE id_module = %s"
            cursor.execute(sql, (nom, coef, iden))
            con.commit()
            actualiser1()
            con.close()

        def supprimernote():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "DELETE FROM module WHERE id_module = %s"
            cursor.execute(sql, (iden))
            con.commit()
            actualiser1()
            con.close()
#########################################
        def ajouteretudiant ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "INSERT INTO module (id_module,nom_module, coef_module) VALUES (%s, %s, %s)"
            cursor.execute(sql, (iden, nom, coef))
            
            con.commit()
            actualiser1()
            con.close()

        def modifieretudiant ():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "UPDATE module SET nom_module =%s, coef_module  = %s WHERE id_module = %s"
            cursor.execute(sql, (nom, coef, iden))
            con.commit()
            actualiser1()
            con.close()

        def supprimeretudiant():
            con = pymysql.connect(user='root', password ='',database = 'g_note')
            cursor = con.cursor()
            actualiser1()
            iden = chama.get()
            nom = chama1.get()
            coef = chama2.get()

            sql = "DELETE FROM module WHERE id_module = %s"
            cursor.execute(sql, (iden))
            con.commit()
            actualiser1()
            con.close()