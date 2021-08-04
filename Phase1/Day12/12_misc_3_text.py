from tkinter import *

''' code for text '''
root = Tk()
'''def scroll():
    pass
    
text = Text(root)
text.insert(INSERT,"here\n")
text.insert(END, "start")
text.pack()'''

'''Toplevel Code'''
'''
top = Toplevel(class_="New window")
var = StringVar()
var.set("Hi New Message")
message = Message(top, textvariable=var)
message.pack()
'''
'''SpinBox'''

spin = Spinbox(root, from_=-5, to=5, width=100, bd = 50)

spin.pack()

root.mainloop()
