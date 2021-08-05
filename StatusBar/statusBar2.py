from tkinter import *

root = Tk()
# title
root.title('Images Insertion')
# icon images
# png icons does not support sometimes
root.iconbitmap('medicine.ico')

my_image1 = PhotoImage(file="../insta.png")
my_image2 = PhotoImage(file="../fb.png")

image_list = [my_image1, my_image2]
# adding a status bar at end
#1.
#status = Label(root, text="Image 1 of 5")

#2. image_list passed to get total number of list
#status = Label(root, text="1 of " + str(len(image_list)))
#3. status to be with border and shrinken with align on east
status = Label(root, text="1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image= my_image1)
my_label.grid(row=0, column=0, columnspan=3)
# function for forward image
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number== 2:
        button_forward=Button(root,text=">>", state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
# status change during image change
    status = Label(root, text= str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E)
# function for backward image
def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command= lambda : forward(image_number + 1))
    button_back = Button(root, text="<<", command= lambda : back(image_number -1))
    if image_number == 1:
        button_back=Button(root,text="<<", state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    # status change during image change -- update status bar
    status = Label(root, text=str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
# Button quit option
button_quit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
# adding pady =10 for gap within status and button
# 1. status.grid(row=2,column=0,columnspan=3)
# sticky --> direction or stretch
status.grid(row=2,column=0,columnspan=3, sticky=W+E)
root.mainloop()
