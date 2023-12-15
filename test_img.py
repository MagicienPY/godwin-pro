from PIL import Image, ImageTk
import tkinter as tk
import tkinter.ttk as ttk

# Créer une fenêtre principale Tkinter
root = tk.Tk()

# Ouvrir l'image avec PIL
image_pil = Image.open("logo/godwin.jpg")

# Définir la nouvelle taille souhaitée
nouvelle_taille = (50, 50)

# Redimensionner l'image
image_redimensionnee = image_pil.resize(nouvelle_taille)

# Convertir l'image PIL en un objet Tkinter
image_tk = ImageTk.PhotoImage(image_redimensionnee)

# Créer un widget Label pour afficher l'image redimensionnée
profile_photo_label = ttk.Label(root, image=image_tk)
profile_photo_label.image = image_tk
profile_photo_label.pack()

# Lancer la boucle principale Tkinter
root.mainloop()