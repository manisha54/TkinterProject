from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("messagebox")
def popup():
    messagebox.showinfo("This is my Popup", "Manisha")

Button(root, text="Popup",command=popup).pack()
root.mainloop()