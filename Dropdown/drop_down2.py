from tkinter import *

root = Tk()
root.title("Dropdown Menu")


def show():
    myLabel =Label(root, text=clicked.get()).pack()

#making options in to list
options = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday"
]

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()