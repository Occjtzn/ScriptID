
# Générateur d'identifiants uniques

Bienvenue dans **Générateur d'ID**, une application de bureau développée en **Python 3** avec **Tkinter** et **NanoID**, permettant de générer facilement des identifiants uniques, personnalisés, et de les copier ou sauvegarder.

---

## 📅 Description

Cette application propose une interface graphique simple et intuitive pour créer des identifiants alphanumériques personnalisables. Grâce à la bibliothèque `nanoid`, les IDs générés sont uniques et sûrs. L'utilisateur peut définir un **préfixe** et une **longueur** pour chaque ID.

Le projet inclut également un exécutable autonome (`generateur_id.exe`) pour les utilisateurs ne disposant pas de Python.

---

## 📚 Fonctionnalités

- Génération d’ID uniques avec personnalisation du préfixe et de la longueur
- Copie automatique dans le presse-papier
- Sauvegarde dans un fichier `.txt`
- Interface GUI via Tkinter
- Exécutable Windows disponible (`generateur_id.exe`)

---

## 🔧 Installation (mode développeur)

1. Clonez ce dépôt :

```bash
git clone <https://github.com/Occjtzn/ScriptID>
```

2. Installez les dépendances nécessaires :

```bash
pip install nanoid pyperclip
```

3. Lancez l’application :

```bash
python generateur_id.py
```

---

## 💡 Build d'un exécutable

Ce projet utilise **PyInstaller** pour générer un exécutable autonome.

```bash
pyinstaller --onefile --noconsole generateur_id.py
```

Le fichier `.spec` est fourni pour personnalisation avancée.

---

## 💚 Technologies utilisées

- **Python 3**
- **Tkinter** (interface graphique)
- **NanoID** (génération d’identifiants sécurisés)
- **Pyperclip** (copie dans le presse-papier)
- **PyInstaller** (création de l’exécutable)

---

## 🔖 Arborescence

```
generateur_id/
├── generateur_id.py         # Script principal
├── generateur_id.spec       # Config PyInstaller
├── ids_generes.txt          # Fichier de sauvegarde
├── generateur_id.exe        # Exécutable Windows
└── update.bat               # Script batch (optionnel)
```

---

## 📇 Auteur

Ce projet a été conçu pour faciliter la génération rapide d’identifiants uniques avec une interface conviviale et des options de sauvegarde et de déploiement.

---

