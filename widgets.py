from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Les widgets de Tkinter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

cadrePrincipal = ttk.Frame(root, padding=10, width=400, height=400, borderwidth=2, relief='sunken')
cadrePrincipal.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(cadrePrincipal, text="Revue des widgets", width=20).grid(column=1, row=1)

root.mainloop()
