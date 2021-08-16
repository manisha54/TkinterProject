from tkinter import *

root = Tk()
root.title("Dropdown Menu")


def show():
    myLabel =Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Mondey")

drop = OptionMenu(root, clicked, "sunday", "Monday","Tuesday", "Wednesday")
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()



root.mainloop()