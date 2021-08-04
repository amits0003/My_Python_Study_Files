from tkinter import *

tk = Tk(className='MessageBox')

var = StringVar()
var.set('Hello, This is a new Message example')
messageLabel = Message(tk, textvariable=var, relief=RAISED)

messageLabel.pack()
tk.mainloop()
