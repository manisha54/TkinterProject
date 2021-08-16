from tkinter import *

root = Tk()
root.title("Radio button")


MODES = [
    ("Peperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Oninon", "Onion")
]

pizza = StringVar()
pizza.set("Peppperoni")
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Click", command=lambda : clicked(pizza.get())).pack()
root.mainloop()