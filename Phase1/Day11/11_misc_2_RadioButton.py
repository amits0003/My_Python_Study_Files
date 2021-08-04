from tkinter import *

root = Tk(className="RadioButton")
var = IntVar()
label = Label(root, width=40)

def selection():
    selectvar = "You have selected the option " + str(var.get())
    label.config(text=selectvar)

R1 = Radiobutton(root, text = "Option 1", variable=var, value=1, command=selection)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=selection)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command= selection)
R3.pack(anchor=W)

label.pack()
root.mainloop()
