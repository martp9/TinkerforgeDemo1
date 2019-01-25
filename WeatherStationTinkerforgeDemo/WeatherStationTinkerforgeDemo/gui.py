from tkinter import *
from time import sleep

class Gui():

    def __init__(self):
        self.ImaCounter = 0
        super().__init__()
        self.initMe()

    def initMe(self):
        MainWindow = Tk()
        self.ImaLabel = Label(MainWindow, text="zero")
        self.ImaButton_add = Button(MainWindow, text="+", command= self.ImaAdd)
        self.ImaButton_sub = Button(MainWindow, text="-", command= self.ImaSub)

        self.ImaLabel.pack()
        self.ImaButton_add.pack(side=LEFT)
        self.ImaButton_sub.pack(side=RIGHT)
        MainWindow.geometry("300x200+250+250")
        MainWindow.mainloop()

    def ImaAdd(self):
        self.ImaCounter += 1
        self.ImaLabel.config(text=self.ImaCounter)
        print("add")

    def ImaSub(self):
        self.ImaCounter -= 1
        self.ImaLabel.config(text=self.ImaCounter)
        print("sub")


G = Gui()
G()