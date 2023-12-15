#from importation import *
#from tkinter import *
#import tkinter.messagebox as msgbox
import customtkinter as ctk
class Vueri:
    

    def __init__(self):
        pass
    def acceuil(self):
        def mode ():
            if (ctk.get_appearance_mode() == "Light"):
                ctk.set_appearance_mode("Dark")
            else:
                ctk.set_appearance_mode("Light")
            
        #ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("Light")
        #customtkinter.set_appearance_mode("Dark")
        #ctk.set_appearance_mode("System")  # macOS only

        print(ctk.get_appearance_mode())

        root = ctk.CTk()
        root.title("Gestage")
        root.geometry("1000x500")
#frame pricipale
        haut_frame = ctk.CTkFrame(master=root,fg_color="light gray",border_width=10,border_color="dark blue")
        haut_frame.pack(padx=1,pady=2,fill="both",expand=False)

        droit_frame = ctk.CTkFrame(master=root,fg_color="dark gray")
        droit_frame.pack(padx=20,pady=50,side="right",fill="both",expand=True)

        gauche_frame = ctk.CTkFrame(master=root,fg_color="dark gray",width=270)
        gauche_frame.pack(padx=20,side="left",fill="both",expand=False)
#fin frame pricipale
#frame interne
        frame = ctk.CTkFrame(master=haut_frame,fg_color="orange")
        frame.pack(side="top", fill= "both", expand = True) 
        button = ctk.CTkButton(master=frame, text="light/black",command=mode)
        button.pack(side="right")
        letitre = ctk.CTkLabel(master=frame,text = "SUIVI DE STAGIAIRE DU CJARC (RI)",font=("arial",40) )
        letitre.pack(side="top",fill="x",expand=False)
#fin frame interne

 #       root.mainloop()

#ri = Vueri()

#ri.acceuil()

        


   