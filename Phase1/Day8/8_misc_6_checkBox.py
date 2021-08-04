
from tkinter import *
from tkinter import messagebox

top = Tk()

checkVar1 = IntVar()
checkVar2 = IntVar()

def onMarkCheckBox():
    messagebox.showinfo("Hi", 'New Box')

checkButton1 = Checkbutton(top, text="Video")
checkButton2 = Checkbutton(top, text="Video")

checkButton1.pack()
checkButton2.pack()

top.mainloop()
