from tkinter import *

root=Tk()
root.geometry("300x450")
root.title("new window")


def open():
    global my_img
    top=Toplevel()
    top.title('check new window')
    my_img = PhotoImage(file="../flower.png")
    my_label = Label(top, image=my_img).pack()

    #closing the window using button.destroy
    button_2 = Button(top, text="Close window", command=top.destroy).pack()  # use destroy or quit
button = Button(root, text="Open", command=open).pack()



root.mainloop()