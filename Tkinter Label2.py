from tkinter import *
root=Tk()

#creating a label widget
myLabel1 = Label(root, text="Tkinter Program Beginning")
myLabel2 = Label(root, text="I am Manisha Kumari Tharu")
myLabel3 = Label(root, text="maksjdf")

#shoving it onto the screen based upon x-axis and y-axis
# that does not ,ove having a constant position
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=2, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()