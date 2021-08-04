from tkinter import *

root = Tk(className="ScrollBar")

scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)

for index in range(0, 100, 1):
    mylist.insert(index+1, f'''You have inserted {index+1}''')

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command = mylist.yview)
root.mainloop()