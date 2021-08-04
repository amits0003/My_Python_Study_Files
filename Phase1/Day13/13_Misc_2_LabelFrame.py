from tkinter import *

root = Tk()

labelFrame = LabelFrame(root, text="Main Label Frame", width=500)

labelFrame.pack(fill=BOTH, expand="yes")

left = Label(labelFrame, text="Inside main label frame", width=50)
left.pack()

root.mainloop()
