from cx_Freeze import setup, Executable

# Chemin d'accès à votre script Python principal
script = "main.py"

# Liste des bibliothèques à inclure
includes = [
    "customtkinter",
    "tkinter.messagebox",
    "tkinter.ttk",
    "aspose.pdf",
    "pymysql",
    "reportlab.lib.pagesizes",
    "reportlab.lib",
    "reportlab.platypus",
    "reportlab.lib.styles",
    "PIL",
    "tkinter",
    "matplotlib.figure",
    "matplotlib.backends.backend_tkagg",
    "sqlite3",
    "mysql.connector",
    "subprocess"
    # Ajoutez ici les autres bibliothèques que vous utilisez
]

# Liste des modules à exclure
excludes = ["main.py"]

# Chemin d'accès aux fichiers supplémentaires (images, bases de données, etc.)
include_files = ["logo/godwin.jpg", "godwin.jpg","photo_user/","logo/","ib/","iab/","i/","photo_etu/","individuel/","impression_enseignant/","bul_generale"]

options = {
    "build_exe": {
        "includes": includes,
        "excludes": excludes,
        "include_files": include_files,
    }
}

executables = [
    Executable(script)
]

setup(
    name="GODWIN",
    version="1.0",
    description="Cette application est une application de gestion de projet permettant de simplifier la vie de l'administration",
    options=options,
    executables=executables
)