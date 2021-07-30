from tkinter import *


root = Tk()
root.title('Image Insertion')
root.iconbitmap('medicine.ico')

my_image = PhotoImage(file='insta.png')
my_label = Label(image=my_image)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit, width=20)
button_quit.pack()


root.mainloop()
