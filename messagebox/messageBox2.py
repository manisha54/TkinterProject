from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("messagebox")

def popup():
    response = messagebox.askyesno("This is my Popup", "Female")
    Label(root, text=response).pack()

    if response == 1:
        Label(root, text="Clicked Yes").pack()
    else:
        Label(root, text="Clicked No").pack()

Button(root,text="Popup", command=popup).pack()


root.mainloop()