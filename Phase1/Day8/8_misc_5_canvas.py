""" Canvas Example """
from tkinter import *

top = Tk()

canvas_1 = Canvas(top, bg='blue', height=300, width=500)
coord = 10, 50, 300, 400
arc = canvas_1.create_arc(coord, start=0, extent=400, fill='red')

canvas_1.pack()
top.mainloop()

exit()
