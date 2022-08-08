from tkinter import *
from tkinter import ttk

# commit wwwwwwwwwwwww


def calculate(*args):
    try:
        value = float(valeur_entree.get())
        resultat.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Convertisseur pieds en mètres")
# définition du cadre principal
cadre_principal = ttk.Frame(
    root, padding="3 3 140 10")  # nord, sud, est, ouest
cadre_principal.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

valeur_entree = StringVar()
# -> input box
feet_entry = ttk.Entry(cadre_principal, width=10,
                       textvariable=valeur_entree)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# -> label du résultat à afficher
resultat = StringVar()
ttk.Label(cadre_principal, textvariable=resultat, borderwidth=1, relief="solid").grid(
    column=2, row=2, sticky=(W, E))

# -> bouton "calculer"
ttk.Button(cadre_principal, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

# -> labels
ttk.Label(cadre_principal, text="pied(s)").grid(column=3, row=1, sticky=W)
ttk.Label(cadre_principal, text="valent").grid(
    column=1, row=2, sticky=(E))
ttk.Label(cadre_principal, text="mètre(s)").grid(column=3, row=2, sticky=W)

# -> boucle qui cible les widgets et définit leur séparation Hor et Vert
for child in cadre_principal.winfo_children():
    child.grid_configure(padx=10, pady=3)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
