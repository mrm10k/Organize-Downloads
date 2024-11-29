import os
import shutil
from tkinter import Tk, filedialog

def org_downloads(download_dir):
    categories = {
        "Compressed": [".zip", ".7z", ".rar", ".tar", ".gz"],
        "PDFs": [".pdf"],
        "Code": [".py", ".sh", ".ps1"],
        "Text": [".txt", ".doc", ".docx", ".odt"],
        "Images": [".jpg", ".jpeg", ".png", ".svg", ".gif"],
        "Executables": [".exe", ".msi"],
        "Other": []
    }

    sub_categories = {
        "Compressed": {".zip": "ZIP", ".7z": "7Z", ".rar": "RAR", ".tar": "TAR", ".gz": "GZ"},
        "Code": {".py": "Python", ".sh": "Shell", ".ps1": "PowerShell"},
        "Text": {".txt": "TXT", ".doc": "DOC", ".docx": "DOCX", ".odt": "ODT"},
        "Images": {".jpg": "JPG", ".jpeg": "JPEG", ".png": "PNG", ".svg": "SVG", ".gif": "GIF"},
        "Executables": {".exe": "EXE", ".msi": "MSI"},
    }

    for categorie, extensions in categories.items():
        folder_categorie = os.path.join(download_dir, categorie)
        if not os.path.exists(folder_categorie):
            os.makedirs(folder_categorie)
        
        if categorie in sub_categories:
            for ext, subfolder in sub_categories[categorie].items():
                subfolder_path = os.path.join(folder_categorie, subfolder)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)

    for file in os.listdir(download_dir):
        file_dir = os.path.join(download_dir, file)
        
        if os.path.isdir(file_dir):
            continue

        _, extension = os.path.splitext(file)
        extension = extension.lower()
        
        moved = False
        for categorie, extensions in categories.items():
            if extension in extensions:

                if categorie in sub_categories and extension in sub_categories[categorie]:
                    subfolder_destination = os.path.join(
                        download_dir, 
                        categorie, 
                        sub_categories[categorie][extension], 
                        file
                    )
                    shutil.move(file_dir, subfolder_destination)
                else:
                    destination = os.path.join(download_dir, categorie, file)
                    shutil.move(file_dir, destination)
                moved = True
                break
        
        if not moved:
            destination = os.path.join(download_dir, "Other", file)
            shutil.move(file_dir, destination)

    print("Done!")

# Configuración de la interfaz gráfica para seleccionar la carpeta
def select_download_folder():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    folder_selected = filedialog.askdirectory(title="Select your Downloads folder")
    return folder_selected

download_folder = select_download_folder()

if download_folder and os.path.exists(download_folder) and os.path.isdir(download_folder):
    org_downloads(download_folder)
else:
    print("No valid folder selected or folder does not exist.")

#                O  o
#           _\_   o
# >('>   \\/  o\ .
#        //\___=
#           ''
#   made by mrm10k
