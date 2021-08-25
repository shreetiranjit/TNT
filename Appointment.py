from tkinter import *
import sqlite3
from tkinter import  messagebox
root = Tk()
root.title('Appointment' )
root.geometry('1100x800')

title = Label(root, text='PATIENTS DETAILS', bg='powder blue', fg='green',bd=10,relief=RIDGE, font=("times new roman", 25,"bold"),padx=2, pady=6)
title.pack(side=TOP, fill=X)
frame=Frame(root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
frame.place(x=0 , y=90, width=1100, height=430)
Dataframeleft =LabelFrame(frame,text='Patient Information', bg='powder blue', fg='green',bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
Dataframeleft.place(x=0,y=5, width=280,height=380)
Dataframeright1 = LabelFrame(frame, bg='powder blue',bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
Dataframeright1.place(x=300,y=5, width=600,height=380)
Dataframeright2 = LabelFrame(frame, text="Calendar",fg='green', bg='powder blue', bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
Dataframeright2.place(x=750,y=5, width=300,height=380)


from tkcalendar import*
cale= Calendar(Dataframeright2, selectmode="day", year=2021, month=8, day=19)
cale.pack(pady=20)
def grab_date():
    my_label.config(text="today's date is " + cale.get_date())

my_button= Button(Dataframeright2, text= "Get Date", command= grab_date)
my_button.pack(pady=20)
my_label= Label(Dataframeright2,text= "")
my_label.pack(pady=20)




framedetails= Frame(root,bd=12, relief=RIDGE, padx=20, bg='powder blue')
framedetails.place(x=0, y=580, width=1300, height=210)
framedetails1 = LabelFrame(framedetails, text="Records",  bg='powder blue', fg='green',bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
framedetails1.place(x=0,y=5, width=500,height=170)

framedetails2_label = LabelFrame(framedetails, text="Prescription",  bg='powder blue', fg='green',bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
framedetails2_label.place(x=550,y=5, width=500,height=170)
framedetails2 = Entry(framedetails2_label, font=('calibri', 14,),width=50, relief=SUNKEN)
framedetails2.place(x=3,y=5, width=450,height=130)


FrameButton =Frame(root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
FrameButton.place(x=0 , y=525, width=1100, height=60)
myButton_label = Button(FrameButton, text="Only Use For Doctors",bg='grey', font=('calibri', 10, 'bold'),width=20, relief=SUNKEN)
myButton_label.grid(row=0, column=1)
#myButton = Entry(FrameButton, font=('calibri', 14,),width=40, relief=SUNKEN)
#myButton.grid(row=0, column=2, padx=15, pady=10)

# dropdown
# drop down menu for doctors
myButton = ["Shreeti", "Rupica", "Manisha", "Shrijan","others doctor"]
myButton_dropdown = StringVar()
myButton_dropdown.set("Doctor Name")
drop1 = OptionMenu(FrameButton,myButton_dropdown, *myButton)
drop1.grid(row=0, column=2, padx=780)


name_label = Label(Dataframeright1, text='Name', font=('calibri', 14,),width=10, relief=SUNKEN)
name_label.grid(row=0, column=0,columnspan=2)
age_label = Label(Dataframeright1, text='Age', font=('calibri', 14,),width=10, relief=SUNKEN)
age_label.grid(row=2, column=0)
gender_label = Label(Dataframeright1, text='Gender', font=('calibri', 14,),width=10, relief=SUNKEN)
gender_label.grid(row=4, column=0)
condition_label = Label(Dataframeright1, text='Previous Condition', font=('calibri', 14,),width=15, relief=SUNKEN)
condition_label.grid(row=6, column=0, )
mediation_label = Label(Dataframeright1, text='Mediation you are on', font=('calibri', 14,),width=18, relief=SUNKEN)
mediation_label.grid(row=8, column=0, columnspan=2)
symptom1_label = Label(Dataframeright1, text='Symptom of what', font=('calibri', 14,),width=15, relief=SUNKEN)
symptom1_label.grid(row=10, column=0, columnspan=2)

name = Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
name.grid(row=0, column=2, padx=15, pady=10)
age = Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
age.grid(row=2, column=2, padx=15, pady=10)
gender = Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
gender.grid(row=4, column=2, padx=15, pady=10)
condition = Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
condition.grid(row=6, column=2, padx=15, pady=10)
mediation = Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
mediation.grid(row=8, column=2, padx=15, pady=10)
symptom1= Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
symptom1.grid(row=10, column=2, padx=15, pady=10)




ID_label = Label(Dataframeleft,text = 'ENTER PATIENT ID' , font = ('calibri', 14 , ) , width = 22, bg = 'green' , fg = "WHITE" )
ID_label.grid(row = 0 , columnspan = 2)
ID_e =Entry(Dataframeleft, font = ('calibri', 14 , ) ,width = 10   )
ID_e.grid(row = 1 ,column = 0)
enter_button =Button(Dataframeleft,text = "ENTER" ,  font = ('calibri', 14 , ) ,width = 10  , bg = 'GREY' )
enter_button.grid(row = 1,column = 1)
exit_button =Button(Dataframeleft,text = "EXIT" ,  font = ('calibri', 14 , ) ,width = 22  , bg = 'grey', relief = SUNKEN,borderwidth = 5)
exit_button.grid(row = 2,columnspan = 2)
update_button =Button(Dataframeleft,text = "UPDATE" ,  font = ('calibri', 14 , ) ,width = 22 , bg = 'grey' , relief = SUNKEN ,borderwidth = 5)
update_button.grid(row = 3 ,columnspan = 2)
save_button =Button(Dataframeleft,text = "SAVE " ,  font = ('calibri', 14 , ) ,width = 22 , bg = 'grey', relief = SUNKEN ,borderwidth = 5 )
save_button.grid(row = 4,columnspan = 2)
doctors_button =Button(Dataframeleft,text = "OUR DOCTORS" ,  font = ('calibri', 14 , ) ,width = 22 , bg = 'grey', relief =SUNKEN  ,borderwidth = 5 )
doctors_button.grid(row = 5,columnspan = 2)
logout_button =Button(Dataframeleft,text = "LOG OUT" ,  font = ('calibri', 14 , ) ,width = 22 , bg = 'grey', relief =SUNKEN  ,borderwidth = 5 )
logout_button.grid(row = 6,columnspan = 2)






root.mainloop()