from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("600x600")
root.title("lotto")
root.config(bg="yellow")

class Lotto_machine():
        def __init__(self,slave):
            self.heading_label = Label(slave, text = "Pick 6 numbers", font="Consolas", bg="white")
            self.heading_label.place(x=150,y=10)






y=Lotto_machine(root)
root.mainloop()
