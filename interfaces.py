from tkinter import *
from tkinter import ttk


def afficher(*args):
    try:
        texte_a_afficher.set("Salut")
    except ValueError:
        pass


root = Tk()
ttk.Button(root, text="Hello World").grid()
ttk.Checkbutton(root, text="cocher").grid()
ttk.Button(root, text='Affichage', command=afficher).grid()
texte_a_afficher = StringVar()
ttk.Label(root, textvariable=texte_a_afficher, width=12,
          borderwidth=2, relief='solid').grid()

for child in root.winfo_children():
    child.grid_configure(padx=10, pady=3)
root.mainloop()
