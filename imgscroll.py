from tkinter import *
import os
from PIL import ImageTk, Image

def nex_img(i):   # takes the current scale position as an argument
    # delete previous image
    canvas.delete('image')
    # create next image
    canvas.create_image(20, 20, anchor=NW, image=listing[int(i)-1], tags='image')

root = Tk()
image1 = ImageTk.PhotoImage(Image.open('C:/Users/gurun/Desktop/PNG_transparency_demonstration_1.png'))
image2 = ImageTk.PhotoImage(Image.open('C:/Users/gurun/Desktop/tnt hospital.png'))

listing = [image1, image2]

scale = Scale(master=root, orient=VERTICAL, from_=1, to=len(listing), resolution=1,
              showvalue=False, command=nex_img)
scale.pack(side=TOP, fill=X)
canvas = Canvas(root, width=800, height=600)
canvas.pack()

# show first image
nex_img(1)

root.mainloop()