""" Pack Example """

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)

redButton = Button(frame, text="Red", fg="red")
redButton.pack(side=LEFT)

blueButton = Button(frame, text="green", fg="green")
blueButton.pack(side=LEFT)

oceanButton = Button(frame, text="Blue", fg="blue")
redButton.pack(side=LEFT)

blackButton = Button(buttonFrame, text="Black", fg="black")
blackButton.pack(side=BOTTOM)

root.mainloop()
