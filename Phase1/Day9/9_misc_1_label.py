
from tkinter import *


root = Tk()

var = StringVar()

label = Label(root, textvariable=var, relief=RAISED, fg="Red")

var.set("Hi This is a new Line")

label.pack()

root.mainloop()
