# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk()
root.geometry('200x100')


# function to be called when mouse enters in a frame
def enter(event):
    print('Entered frame at x = % d, y = % d' % (event.x, event.y))

# function to be called when mouse double click inside frame.
def double_click(event):
    print("double click at x = %d, y = %d " % (event.x, event.y))

# function to be called when when mouse exits the frame
def exit_(event):
    print('Exited Frame at x = % d, y = % d' % (event.x, event.y))


# frame with fixed geometry
frame1 = Frame(root, height=100, width=200)

# these lines are showing the
# working of bind function
# it is universal widget method
frame1.bind('<Enter>', enter)
frame1.bind('<Double 1>', double_click)
frame1.bind('<Leave>', exit_)


frame1.pack()

mainloop()
