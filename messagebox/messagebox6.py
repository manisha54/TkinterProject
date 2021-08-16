from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("messagebox")

def popup():
    response = messagebox.askquestion("What is your name", "manisha")
    Label(root, text=response).pack()





Button(root,text="Popup", command=popup).pack()


root.mainloop()