from tkinter import *

from tkinter import messagebox

root = Tk()

def hello():
    messagebox.showinfo("New MessageBox", "Hello World")

button = Button(root, text="New MessageBox", command=hello)
button.pack()

root.mainloop()