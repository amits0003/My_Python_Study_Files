""" Label _ Text in Tkinter """

from tkinter import *
from tkinter import messagebox

top = Tk()

label = Label(top, text="New Entry Label")

label.pack(side=LEFT)

entry_1 = Entry(top, bd=5)

entry_1.pack(side=RIGHT)

top.mainloop()