from tkinter import *
# -> submodule de Tkinter permettant l'usage des 'themed widgets' de TK V8.5
from tkinter import ttk

# fonction(s), à déclarer au début


def calculate(*args):
    try:
        value = float(valeur_entree.get())
        affichage_resultat.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


# Fenêtre principale de l'application
root = Tk()
root.title("Convertisseur pieds en mètres")

# définition du cadre principal qui contiendra les objets de l'interface
cadre_principal = ttk.Frame(
    root, padding="3 3 140 10")  # nord, sud, est, ouest
cadre_principal.grid(column=0, row=0, sticky=(N, W, E, S))
#   les deux lignes suivantes permettent au cadre principal de s'adapter
#   quand la fenêtre change de taille.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

valeur_entree = StringVar()
# -> input box: 1) on le créé et 2) on le place sur l'interface
txt_valeurAConvertir = ttk.Entry(
    cadre_principal, width=10, textvariable=valeur_entree)
txt_valeurAConvertir.grid(column=2, row=1, sticky=(W, E))

# Les widgets suivants ne sont pas stockés dans des variables
# Comme celui au-dessus, on les créé et on les place

# -> label du résultat à afficher
affichage_resultat = StringVar()
ttk.Label(cadre_principal, textvariable=affichage_resultat,
          borderwidth=1, relief="solid").grid(column=2, row=2, sticky=(W, E))

# -> bouton "calculer"
ttk.Button(cadre_principal, text="Calculer", command=calculate).grid(
    column=3, row=3, sticky=W)

# -> labels
ttk.Label(cadre_principal, text="pied(s)").grid(column=3, row=1, sticky=W)
ttk.Label(cadre_principal, text="valent").grid(
    column=1, row=2, sticky=(E))
ttk.Label(cadre_principal, text="mètre(s)").grid(column=3, row=2, sticky=W)

# -> boucle qui cible les widgets et définit leur séparation Hor et Vert
for child in cadre_principal.winfo_children():
    child.grid_configure(padx=10, pady=3)

txt_valeurAConvertir.focus()
root.bind("<Return>", calculate)  # assigne la fonction à la touche "return"

root.mainloop()
