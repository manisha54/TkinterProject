from tkinter import *

root = Tk()

e1 = Entry(root,width=50, fg="blue", bg="white", borderwidth=5)
e1.pack()

def myClick():
    textoutput = "Hello" + e1.get()

    myButton= Button(root, text=textoutput)
    myButton.pack()

myButton = Button(root, text="Click Me!" , command=myClick)
myButton.pack()

root.mainloop()