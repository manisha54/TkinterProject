

from tkinter import *

font = ('Arial', 20)
root = Tk()
root.title('Image Viewer')
root.configure(bg='black')

# images
img1 = PhotoImage(file='../insta.png')
img2 = PhotoImage(file='../fb.png')
img3 = PhotoImage(file='../flower.png')

# list of images
img_list = [img1, img2, img3]

# status
stat = Label(
    root,
    text=f'1 of {len(img_list)}',
    bg='black',
    fg='white',
    font=('Arial', 10),
    anchor=E,
)
stat.grid(row=2, column=1, columnspan=2, sticky=W + E)


# functions
def back(num):
    global lab, b_forward, b_back, stat

    lab.grid_forget()  # deletes the current image on the screen
    lab = Label(image=img_list[num - 1])
    lab.grid(row=0, column=0, columns=3)

    # forward button update
    b_forward = Button(
        root,
        text='>>',
        bd=0,
        activebackground='black',
        activeforeground='white',
        bg='black',
        fg='white',
        font=font,
        command=lambda: forward(num + 1)
    )
    b_forward.grid(row=1, column=2)

    # backward button update
    b_back = Button(
        root,
        text='<<',
        bd=0,
        activebackground='black',
        activeforeground='white',
        bg='black',
        fg='white',
        font=font,
        command=lambda: back(num - 1)
    )
    b_back.grid(row=1, column=0)

    # status update
    stat = Label(
        root,
        text=f'{num} of {len(img_list)}',
        bd=1,
        bg='black',
        fg='white',
        font=('Arial', 10),
        anchor=E,
    )
    stat.grid(row=2, column=1, columnspan=2, sticky=W + E)

    # disabled backward if reached at start of the list
    if num == 1:
        b_back = Button(
            root,
            text='<<',
            bd=0,
            activebackground='black',
            activeforeground='white',
            bg='black',
            fg='white',
            font=font,
            state=DISABLED
        )
        b_back.grid(row=1, column=0)


def forward(num):
    global lab, b_forward, b_back, stat

    lab.grid_forget()
    lab = Label(image=img_list[num - 1])
    lab.grid(row=0, column=0, columns=3)

    # forward button update
    b_forward = Button(
        root,
        text='>>',
        bd=0,
        activebackground='black',
        activeforeground='white',
        bg='black',
        fg='white',
        font=font,
        command=lambda: forward(num + 1)
    )
    b_forward.grid(row=1, column=2)

    # status update
    stat = Label(
        root,
        text=f'{num} of {len(img_list)}',
        anchor=E,
        bg='black',
        fg='white',
        font=('Arial', 10),

    )
    stat.grid(row=2, column=1, columnspan=2, sticky=W + E)

    # disabled forward if reached at end of the list
    if num == len(img_list):
        b_forward = Button(
            root,
            text='>>',
            bd=0,
            activebackground='black',
            activeforeground='white',
            bg='black',
            fg='white',
            font=font,
            state=DISABLED
        )
        b_forward.grid(row=1, column=2)

    # backward button update
    b_back = Button(
        root,
        text='⇚',
        bd=0,
        activebackground='black',
        activeforeground='white',
        bg='black',
        fg='white',
        font=font,
        command=lambda: back(num - 1)
    )
    b_back.grid(row=1, column=0)


# buttons

# initial label showing first image
lab = Label(image=img1)
lab.grid(row=0, column=0, columns=3)

b_back = Button(
    root,
    text='<<',
    bd=0,
    activebackground='black',
    activeforeground='white',
    font=font,
    bg='black',
    fg='white',
    command=lambda: back,
    state=DISABLED  # disabled cuz at the starting of the list
)
b_back.grid(row=1, column=0)

b_exit = Button(
    root,
    text='Exit',
    bd=0,
    activebackground='black',
    activeforeground='red',
    font=font,
    bg='black',
    fg='red',
    command=root.quit
)
b_exit.grid(row=1, column=1)

b_forward = Button(
    root,
    text='>>',
    bd=0,
    font=font,
    activebackground='black',
    activeforeground='white',
    bg='black',
    fg='white',
    command=lambda: forward(2)  # starts at 2 cuz first image is already on display
)
b_forward.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
