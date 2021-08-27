from tkinter import *

btn= Tk()
btn.title(' img Button')
btn.geometry("400x400")

def thing():
    my_label.config(text= " U Just clicked the button....")

login_btn= PhotoImage(file='C:/Users/gurun/Desktop/login (2).png')

img_label=Label(image=login_btn)
#img_label.pack(pady=20)

my_button= Button(btn, image=login_btn, command= thing, borderwidth=5)
my_button.pack(pady=20)

my_label= Label(btn,text='')
my_label.pack(pady=20)


mainloop()