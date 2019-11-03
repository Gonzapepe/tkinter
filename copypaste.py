import tkinter as tk
from tkinter import ttk
from sys import argv, exit

if argv[1:]:
    file_name = argv[1]
    file_name2 = argv[2]
    with open(file_name) as file:
        f = file.read()

else:
    print('por favor ingrese el nombre del archivo al iniciar el programa.')
    exit(0)

win = tk.Tk()
win.title('copiando.......')

label = ttk.Label(win, text='copiar {} a {}'.format(file_name, file_name2))
label.grid(column = 0, row = 0)


def Copy():
    f2 = open(file_name2, 'w')
    action.configure(f2.write(f))
    label.configure(foreground = 'red')
    f2.close()


action = ttk.Button(win, text='click para copiar', command = Copy)
action.grid(column = 1, row = 0)











win.mainloop()
