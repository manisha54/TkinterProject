from tkinter import *

top = Tk()
top.geometry("400x250")

name = Label(top, text = "Name").place(x = 30,y = 50)
adress = Label(top, text = "Address").place(x = 30, y= 90)
contact = Label(top, text = "Contact").place(x = 30, y= 130)
e1 = Entry(top).place(x = 80, y = 50)
e2 = Entry(top).place(x = 80, y = 90)
e3 = Entry(top).place(x = 95, y = 130)

top.mainloop()