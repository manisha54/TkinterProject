from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    messagebox.showwarning("this is my popup", "danger")

Button(root, text="popup", command=popup).pack()

root.mainloop()
