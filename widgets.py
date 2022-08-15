from cProfile import label
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Les widgets de Tkinter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# cadre principal
cadrePrincipal = ttk.Frame(root, padding=10, width=400,
                           height=400, borderwidth=2, relief='sunken')
cadrePrincipal.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(cadrePrincipal, text="Revue des widgets",
          width=20).grid()

# 2 frames à mettre côte à côte
#   frame a
cadre2 = ttk.Frame(cadrePrincipal, padding=5, width=100,
                   height=150, borderwidth=2, relief='sunken')
cadre2.grid()
img_fox = PhotoImage(file='fox.gif')
lbl_cadre2 = ttk.Label(cadre2, image=img_fox).grid()
#   frame b
cadre3 = ttk.Frame(cadrePrincipal, padding=5, width=150,
                   height=100, borderwidth=2, relief='sunken')
cadre3.grid()
lbl_cadre3 = ttk.Label(cadre3, text='Cadre 3').grid()


root.mainloop()
