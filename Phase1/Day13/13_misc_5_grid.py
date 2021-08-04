from tkinter import *

root = Tk(className='Grid')

for c in range(4):
    for d in range(3):
        Label(root, text='[R%s C%s]' % (c+1, d+1), borderwidth=1, width=15).grid(row=c, column=d)

root.mainloop()
