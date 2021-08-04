from tkinter import *
from tkinter import messagebox
root = Tk(className='Pack Example')

def sel():
    label = messagebox.showinfo('Message', 'Button')

frame = Frame(root)
frame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
bottomFrame.place(height=100,width=100)

redButton = Button(frame, text='Red', fg='Red', command=sel)
redButton.pack(side=TOP)

blueButton = Button(frame, text='Blue', fg='blue', command=sel)
blueButton.pack(side=LEFT)

blackButton = Button(frame, text="Black", fg='black', command=sel)
blackButton.pack(side=RIGHT)

root.mainloop()