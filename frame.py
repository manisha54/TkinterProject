#adding frame in the program
from tkinter import *
root=Tk()
frame = LabelFrame(root, text="My Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)
Button = Button(frame, text="manisha")
Button.grid(row=0,column=0)

root.mainloop()


