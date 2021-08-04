""" GUI Programming using Tkinter """
import tkinter as pygui
from tkinter import messagebox

top = pygui.Tk()
def call_b_info():
    pygui.messagebox.showinfo("New Message Box", "Hello, This is a new  info message")
def call_b_warning():
    pygui.messagebox.showwarning("New Message Box", "Hello, This is a new Warning Message")
def call_b_error():
    pygui.messagebox.showerror("New Message Box", "Hello, This is a new Error Message")

b_info = pygui.Button(top, text="info", command=call_b_info)
b_warning = pygui.Button(top, text="warning", command=call_b_warning)
b_error = pygui.Button(top, text="Error", command=call_b_error)

b_info.pack()
b_warning.pack()
b_error.pack()
top.mainloop()
