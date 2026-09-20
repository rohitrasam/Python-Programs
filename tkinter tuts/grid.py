from tkinter import *

# Everything is a widget

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My name is Rohit Rasam')
myLabel3 = Label(root, text='     Blank          ')


# Shoving it onto the screen lol!!
# It's all relative
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=1, column=3)

root.mainloop()
