from cx_Freeze import setup, Executable

setup(
    name="MyScolar",
    version="1.0",
    description="Mon programme Python de gestion de note d'un etablissement",
    executables=[Executable("/home/magicien/Documents/mbam/gestion_note/main.py")]
)