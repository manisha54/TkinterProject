from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("messagebox")

def popup():
    response = messagebox.askokcancel("This is my Popup", "Are you want to exit")
    Label(root, text=response).pack()

    if response ==1:
        Label(root, text="Clicked ok").pack()

    else:
        Label(root, text="Clicked cancel").pack()



Button(root,text="Popup", command=popup).pack()


root.mainloop()