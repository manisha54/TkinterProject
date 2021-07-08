from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Button ic clicked!!")
    myLabel.pack()

myButton = Button(root, text='CLICK', command=myClick, fg="black", bg="grey")
myButton.pack()

root.mainloop()