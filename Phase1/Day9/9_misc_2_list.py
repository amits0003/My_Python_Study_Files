
from tkinter import *
from tkinter import messagebox
import tkinter

root = Tk()

listBox = Listbox(root, fg="Red", selectmode=MULTIPLE,selectbackground='Green')
listBox.insert(1, 'Amit')
listBox.insert(2, "Sumit")
listBox.insert(3, 'new')

listBox.pack()
root.mainloop()