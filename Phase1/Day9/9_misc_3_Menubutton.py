from tkinter import *
from tkinter import messagebox
import tkinter

root = Tk()

menuButton = Menubutton(root, fg='Green', text='Groceries', relief=RAISED)

menuButton.grid()

menuButton.menu = Menu (menuButton, tearoff = 0)

menuButton["menu"] = menuButton.menu

riceVar = IntVar()
wheatVar = IntVar()

menuButton.menu.add_checkbutton(label = 'Rice', variable = riceVar)
menuButton.menu.add_checkbutton(label='Wheat', variable=wheatVar)

menuButton.pack()
root.mainloop()


