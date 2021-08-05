

from tkinter import *


root = Tk()
root.title('Image Insertion')
root.iconbitmap('medicine.ico')

my_image1 = PhotoImage(file='../insta.png')
my_image2 = PhotoImage(file='../fb.png')
my_image3 = PhotoImage(file='../flower.png')

image_list = [my_image1, my_image2, my_image3]
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()  # delete the current image on the screen
    my_label = Label(image=image_list[image_number-1])
    button_forward= Button(root, text=">>", command=lambda:forward(image_number+1))
    button_backward= Button(root, text="<<", command=lambda:backward(image_number-1))

    if image_number == 3:
        button_forward= Button(root, text=">>", state=DISABLED)
        button_forward.grid(row=1, column=2)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=3)
    button_backward.grid(row=1, column=0)

    status = Label(root, text="image" + str(image_number) + str(len(image_list)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def backward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3)

    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_backward = Button(root, text="<<", command=lambda:backward(image_number-1))

    if image_number==1:
        button_backward= Button(root, text="<<", state=DISABLED)
        button_backward.grid(row=1, column=0)

    button_forward.grid(row=1,column=2)
    button_backward.grid(row=1,column=0)

    #update status bar
    status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

button_backward = Button(root, text="<<",command=lambda: backward, state=DISABLED)
button_exit = Button(root, text="exit program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_forward.grid(row=1, column=2, pady=10)
button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)


root.mainloop()
