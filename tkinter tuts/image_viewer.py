from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

my_img1 = ImageTk.PhotoImage(Image.open('.Images/1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('.Images/2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('.Images/3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('.Images/4.jfif'))
my_img5 = ImageTk.PhotoImage(Image.open('.Images/5.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('.Images/6.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('.Images/7.jpg'))
my_img8 = ImageTk.PhotoImage(Image.open('.Images/8.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  # The 1st image will disappear
    my_label = Label(image=image_list[img_num - 1])


def back():
    global my_label
    global button_forward
    global button_back


button_back = Button(root, text='<<Back', command=back)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='Forward>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_exit.grid(row=1, column=2)


root.mainloop()
