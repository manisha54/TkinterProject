from tkinter import *
root = Tk()

#Buttob without any function
myButton = Button(root, text="Click Me")
myButton.pack()

#state disabled button
myButton1= Button(root, text="Click, state=DISABLED")
myButton1.pack()

#button x and y padding

myButton2 = Button(root, text="Click", padx=50, pady=50)
myButton2.pack()
myButton3 = Button(root, text="Click", padx=50, pady=50)
myButton3.pack()

root.mainloop()