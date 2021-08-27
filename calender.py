from tkinter import *
from tkcalendar import*

cal= Tk()
cal.geometry("600x400")

cale= Calendar(cal, selectmode="day", year=2021, month=8, day=19)
cale.pack(pady=20)

def grab_date():
    my_label.config(text="today's date is " + cale.get_date())


my_button= Button(cal, text= "Get Date", command= grab_date)
my_button.pack(pady=20)

my_label= Label(cal,text= "")
my_label.pack(pady=20)

cal.mainloop()