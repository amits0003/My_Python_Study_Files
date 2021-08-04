from tkinter import *

panedWin1 = PanedWindow()
#, height=10, orient=HORIZONTAL, relief=FLAT)

panedWin1.pack(fill=BOTH, expand=1)

left = Label(panedWin1, text="Left Pane")
panedWin1.add(left)

right = Label(panedWin1, text="Right Pane")
panedWin1.add(right)

panedWin2 = PanedWindow(panedWin1, orient=VERTICAL)

top = Label(panedWin2, text="Top Pane")
panedWin2.add(top)

bottom = Label(panedWin2, text="Bottom Pane")
panedWin2.add(bottom)

panedWin2.pack(fill=BOTH, expand=1)
mainloop()