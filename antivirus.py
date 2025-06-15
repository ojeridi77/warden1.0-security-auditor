import os 
import hashlib
import csv
import pandas as pd
import tkinter as tk
from tkinter import messagebox,simpledialog,ttk
from PIL import Image, ImageTk

def hash_calculator(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()
            


def downloads_hash():
    try:
        fpath = simpledialog.askstring("Demande du chemin", "Entrez le chemin à analyser :")
        if not fpath or not os.path.exists(fpath):
            raise ValueError("Chemin invalide ou inexistant.")

        for dirpath, _, filenames in os.walk(fpath):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                with open("file_hashes.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow([full_path, hash_calculator(full_path)])

        messagebox.showinfo("Scan terminé", "Analyse terminée avec succès.")

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")


def detector():
    try:
        f1 = pd.read_csv('Flagged_Hash_List.csv', header=None)
        f2 = pd.read_csv('file_hashes.csv', header=None)

        flagged_hashes = f1[0]
        infected = f2[f2[1].isin(flagged_hashes)]

        return infected
    except Exception as e:
        print(f"Erreur dans detector : {str(e)}")
        return pd.DataFrame()

def message(data):
    try:
        with open("logs.txt", "w") as f:
            if data.empty:
                messagebox.showwarning("Alerte", "Aucun virus n'a été détecté")
                f.write("Aucun virus détecté.\n")
            else:
                messagebox.showwarning("Alerte", "Un virus a été détecté !")
                f.write("Virus détecté :\n")
                for _, row in data.iterrows():
                    f.write(f"- {row[0]} (hash : {row[1]})\n")
    except Exception as e:
        with open("logs.txt", "a") as f:
            f.write(f"Erreur : {str(e)}\n")

def delete(data_frame):
    for i in range(data_frame.shape[0]):
        os.remove(data_frame.iloc[i, 0])

    messagebox.showwarning("Alerte", "Fichiers infectés supprimés")




window = tk.Tk()
window.title("Warden 1.0")
window.geometry("800x450")
window.resizable(False, False)

img = Image.open("warden 1.0 (1).png")
bg_img = ImageTk.PhotoImage(img)

icon = tk.PhotoImage(file="warden_logo-removebg-preview.png")
window.iconphoto(True, icon)

canvas = tk.Canvas(window, width=800, height=450, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_img, anchor="nw")

# Style moderne
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Segoe UI", 11),
                padding=10,
                relief="flat",
                background="#a70052",
                foreground="white")
style.map("TButton",
          background=[("active", "#cd3680")])

style.configure("TLabel",
                background="#a70052",
                foreground="white",
                font=("Segoe UI", 14))

frame = tk.Frame(window, bg="#01003B", highlightthickness=0)
frame.place(relx=0.5, rely=0.6, anchor="w")

titre = ttk.Label(window, text="Audit de fichiers - Analyse de sécurité", font=("Segoe UI", 22, "bold"))
titre.place(relx=0.42, rely=0.2, anchor="w")

btn_diag = ttk.Button(frame, text="Effectuer un diagnostic", command=lambda: message(detector()))
btn_diag.grid(row=1, column=2, padx=20, pady=10)

btn_delete = ttk.Button(frame, text="Supprimer les fichiers infectés", command=lambda: delete(detector()))
btn_delete.grid(row=2, column=2, padx=20, pady=10)

btn_dl = ttk.Button(frame, text="Télécharger les hash MD5 des fichiers", command=downloads_hash)
btn_dl.grid(row=0, column=2, padx=20, pady=10)

window.mainloop()