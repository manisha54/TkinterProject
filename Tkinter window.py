from tkinter import*

root=Tk()

#creating a button widget
redbutton=Button(root,text = "LEFT",fg="green")
redbutton.pack( side=LEFT )

#shoving it on to the screen
greenbutton=Button(root,text = "RIGHT", fg= "black")
greenbutton.pack(side = RIGHT)
bluebutton=Button(root,text = "TOP" , fg = "blue")
bluebutton.pack(side = TOP)
blackbutton=Button(root,text = "BUTTOM" ,fg = "red")
blackbutton.pack(side = BOTTOM)
root.mainloop()