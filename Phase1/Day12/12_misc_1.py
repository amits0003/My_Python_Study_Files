from tkinter import *

root = Tk(className="Scale Calculator")
var = DoubleVar()

def selection():
    selctedComand = "Value " + str(var.get())
    label.config(text=selctedComand)

scale = Scale(root, variable=var, from_=-50, to=50, orient=HORIZONTAL, length=500)
scale.pack(anchor=CENTER)

label = Label(root, width=50)
label.pack()

button = Button(root, text= "Get Scale Value", command=selection)
button.pack(anchor=CENTER)

root.mainloop()