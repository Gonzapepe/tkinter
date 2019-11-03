import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

win.resizable(0, 0)

oracion = ttk.Label(win, text='A Label.')
oracion.grid(column=0, row=0)

def clicker():
    action.configure(text='** fui clickeado.')
    oracion.configure(foreground='red')

action = ttk.Button(win, text='clickeame', command=clicker)
action.grid(column=1, row=0)

win.mainloop()
