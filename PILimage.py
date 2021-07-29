from tkinter import *
from PIL import ImageTK, Image

root=Tk()
root.title('Image Insertion')
root.iconbitmap('insta.ico')

my_image = ImageTk.PhotoImage(Image.open('insta1.png'))
my_label = Label(image= my_image)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit,width=20)
button_quit.pack()


root.mainloop()
