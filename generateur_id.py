import os
import sys
import tkinter as tk
import pyperclip
from nanoid import generate
from tkinter import messagebox, filedialog

BG_COLOR = "#2C2F33"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#7289DA"
BUTTON_HOVER = "#5B6EAE"
FONT_MAIN = ("Arial", 12)
FONT_TITLE = ("Arial", 14, "bold")

def generer_id():
    longueur = int(entry_longueur.get())
    prefixe = entry_prefixe.get()
    id_unique = f"{prefixe}{generate(size=longueur)}"
    label_result.config(text=id_unique)

def copier_id():
    pyperclip.copy(label_result.cget("text"))
    messagebox.showinfo("Copié", "L'ID a été copié dans le presse-papier !")

def sauvegarder_id():
    id_unique = label_result.cget("text")
    if not id_unique:
        messagebox.showwarning("Erreur", "Aucun ID généré à sauvegarder.")
        return
    
    fichier = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
    )

    if fichier:
        with open(fichier, "a") as f:
            f.write(id_unique + "\n")
        messagebox.showinfo("Sauvegarde", f"L'ID a été sauvegardé dans :\n{fichier}")

def create_button(text, command, bg=BUTTON_COLOR, fg=TEXT_COLOR):
    btn = tk.Button(app, text=text, font=FONT_MAIN, bg=bg, fg=fg, command=command)
    btn.pack(pady=5)
    btn.bind("<Enter>", lambda e: e.widget.config(bg=BUTTON_HOVER))
    btn.bind("<Leave>", lambda e: e.widget.config(bg=bg))
    return btn

app = tk.Tk()
app.title("Générateur d'ID")
app.geometry("400x350")
app.config(bg=BG_COLOR)

tk.Label(app, text="🔹 Générateur d'ID 🔹", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

tk.Label(app, text="Nombre de caractères :", font=FONT_MAIN, fg=TEXT_COLOR, bg=BG_COLOR).pack()
entry_longueur = tk.Entry(app, font=FONT_MAIN)
entry_longueur.pack(pady=5)

tk.Label(app, text="Préfixe (optionnel) :", font=FONT_MAIN, fg=TEXT_COLOR, bg=BG_COLOR).pack()
entry_prefixe = tk.Entry(app, font=FONT_MAIN)
entry_prefixe.pack(pady=5)

label_result = tk.Label(app, text="", font=("Arial", 14, "bold"), fg="#FFDD57", bg=BG_COLOR)
label_result.pack(pady=10)

create_button("Générer", generer_id)
create_button("Copier", copier_id)
create_button("Sauvegarder", sauvegarder_id)

app.mainloop()
