from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tkinter Tutorials')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    messagebox.showinfo("This is my Pop-up!", "Hello People of Earth")


Button(root, text='Pop-up', command=popup).pack()

root.mainloop()
