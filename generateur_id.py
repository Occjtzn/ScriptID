import tkinter as tk
import pyperclip
from nanoid import generate
from tkinter import messagebox, filedialog

def generer_id():
    """Génère un ID unique."""
    try:
        longueur = int(entry_longueur.get())
        prefixe = entry_prefixe.get()
        id_unique = prefixe + generate(size=longueur)
        label_result.config(text=id_unique)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")

def copier_id():
    """Copie l'ID généré dans le presse-papier."""
    id_unique = label_result.cget("text")
    if id_unique:
        pyperclip.copy(id_unique)
        messagebox.showinfo("Copié", "L'ID a été copié dans le presse-papier !")
    else:
        messagebox.showwarning("Erreur", "Aucun ID à copier.")

def sauvegarder_id():
    """Sauvegarde l'ID dans un fichier texte."""
    id_unique = label_result.cget("text")
    if not id_unique:
        messagebox.showwarning("Erreur", "Aucun ID généré à sauvegarder.")
        return
    
    fichier = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("Fichiers texte", "*.txt")])
    if fichier:
        with open(fichier, "a") as f:
            f.write(id_unique + "\n")
        messagebox.showinfo("Sauvegarde", "L'ID a été sauvegardé.")

# Création de l'interface
app = tk.Tk()
app.title("Générateur d'ID")
app.geometry("400x350")
app.config(bg="#2C2F33")

# Labels et champs de saisie
tk.Label(app, text="Générateur d'ID", font=("Arial", 14, "bold"), fg="white", bg="#2C2F33").pack(pady=10)

tk.Label(app, text="Nombre de caractères :", font=("Arial", 12), fg="white", bg="#2C2F33").pack()
entry_longueur = tk.Entry(app, font=("Arial", 12))
entry_longueur.pack(pady=5)

tk.Label(app, text="Préfixe (optionnel) :", font=("Arial", 12), fg="white", bg="#2C2F33").pack()
entry_prefixe = tk.Entry(app, font=("Arial", 12))
entry_prefixe.pack(pady=5)

label_result = tk.Label(app, text="", font=("Arial", 14, "bold"), fg="#FFDD57", bg="#2C2F33")
label_result.pack(pady=10)

# Boutons
tk.Button(app, text="Générer", font=("Arial", 12), bg="#7289DA", fg="white", command=generer_id).pack(pady=5)
tk.Button(app, text="Copier", font=("Arial", 12), bg="#7289DA", fg="white", command=copier_id).pack(pady=5)
tk.Button(app, text="Sauvegarder", font=("Arial", 12), bg="#7289DA", fg="white", command=sauvegarder_id).pack(pady=5)

app.mainloop()
