from tkinter import *

root = Tk()
count = 0

def myClick():

    global count
    
    count += 1
    myLabel = Label(root, text=f'{count} Look! I clicked a Button!')
    myLabel.pack()


myButton = Button(root, text='Click me', command=myClick, fg='blue', bg='red')
myButton.pack()

root.mainloop()
