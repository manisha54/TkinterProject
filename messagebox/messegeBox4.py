from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    messagebox.showerror("this is my popup", "Error")

Button(root, text="popup", command=popup).pack()

root.mainloop()
