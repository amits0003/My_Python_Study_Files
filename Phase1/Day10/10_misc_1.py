from tkinter import *

root = Tk(screenName="My Python Application", baseName='New Py Application', className="New Application")


def default_command():
    file_view = Toplevel(root)
    button = Button(file_view, text="Default Command")
    button.pack()


def new_project():
    file_view = Toplevel(root)
    button = Button(file_view, text="New Project")
    button.pack()


def new_file():
    file_view = Toplevel(root)
    button = Button(file_view, text="New file")
    button.pack()


def new_scratch_file():
    file_view = Toplevel(root)
    button = Button(file_view, text="New scratch file")
    button.pack()


def open_file():
    file_view = Toplevel(root)
    button = Button(file_view, text="open File")
    button.pack()


menu_bar = Menu(root)

fileMenu = Menu(menu_bar, tearoff=0)  # closing the tear-off : (detachment from main window)
fileMenu.add_command(label="New Project", command=new_project)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="New Scratch File", command=new_scratch_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=default_command)
fileMenu.add_command(label="Save As", command=default_command)
fileMenu.add_command(label="Open Recent", command=default_command)
fileMenu.add_command(label="Save Project", command=default_command)
fileMenu.add_command(label="Close Project", command=default_command)

fileMenu.add_separator()

fileMenu.add_command(label="Settings", command=default_command)
fileMenu.add_command(label="File Properties", command=default_command)

fileMenu.add_separator()

fileMenu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=fileMenu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Edit File", command=default_command)

edit_menu.add_separator()

edit_menu.add_command(label="Undo Action", command=default_command)
edit_menu.add_command(label="Redo Action", command=default_command)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Get Info", command = default_command)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()
