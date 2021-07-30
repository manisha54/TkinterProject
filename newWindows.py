from tkinter import *

win1= Tk()

def new_window():

    win2 = Tk()
    my_label = Label(win2, text="This is a new window").pack()
    button2 = Button(win2, text="Close Window", command=win2.destroy).pack()


button = Button(win1, text="Open", command=new_window).pack()


win1.mainloop()