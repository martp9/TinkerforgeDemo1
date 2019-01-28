
from tkinter import *

root = Tk()
photo = PhotoImage(file="png\_rain.png" )
label = Label(root, image=photo)
label.grid(row=0,column=0)
root.mainloop()