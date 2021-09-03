from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Prescription')
root.geometry('580x750')
root.resizable(False, False)
label_title = Label(root, text='DOCTORS', font=('san fransisco', 22, 'bold'), bg='light grey', fg="red")
label_title.place(x=5, y=9)
label_title2 = Label(root, text='Medical Prescription', font=('san fransisco', 18, 'bold'),bg='light grey', fg='black')
label_title2.place(x=5, y=50)

frame1 = Frame(root, bg='#FFA07A')
frame1.place(x=0, y=100, width=580, height=30)
frame2 = Frame(root, bg='#FFDAB9')
frame2.place(x=0, y=130, width=580, height=30)
frame3 = Frame(root, bg="#FFA07A")
frame3.place(x=0, y=160, width=580, height=30)
frame4 = Frame(root, bg='#FFDAB9')
frame4.place(x=0, y=190, width=580, height=30)
frame5 = Frame(root, bg='#FFA07A')
frame5.place(x=0, y=220, width=580, height=30)
frame6 = Frame(root, bg='#FFDAB9')
frame6.place(x=0, y=250, width=580, height=30)
frame7 = Frame(root, bg='#FFA07A')
frame7.place(x=0, y=280, width=580, height=90)

frame8 = Frame(root, bg='#FFDAB9')
frame8.place(x=0, y=370, width=580, height=30)

frame9 = Frame(root, bg='#FFA07A')
frame9.place(x=0, y=400, width=580, height=30)

frame10 = Frame(root, bg='#FFDAB9')
frame10.place(x=0, y=430, width=580, height=30)
frame11 = Frame(root, bg='#FFA07A')
frame11.place(x=0, y=460, width=580, height=30)
frame12 = Frame(root, bg='#FFDAB9')
frame12.place(x=0, y=490, width=580, height=30)
frame13 = Frame(root, bg='#FFA07A')
frame13.place(x=0, y=520, width=580, height=30)
frame14 = Frame(root, bg='#FFDAB9')
frame14.place(x=0, y=550, width=580, height=30)
frame15 = Frame(root, bg='#FFA07A')
frame15.place(x=0, y=580, width=580, height=70)
frame16 = Frame(root, bg='#FFDAB9')
frame16.place(x=0, y=650, width=580, height=70)
frame17 = Frame(root, bg='#FFA07A')
frame17.place(x=0, y=720, width=580, height=30)

label1 = Label(root, text='Patients name:', font=('georgia', 11, 'bold'))
label1.place(x=0, y=102)
label2 = Label(root, text='Date:', font=('georgia', 11, 'bold'))
label2.place(x=350, y=102)
label3 = Label(root, text='Date Of Birth:',font=('georgia', 11, 'bold'))
label3.place(x=0, y=132)
label4 = Label(root, text='Age:', font=('georgia', 11, 'bold'))
label4.place(x=340, y=132)

label6 = Label(root, text='Patients ID:', font=('georgia', 11, 'bold'))
label6.place(x=0, y=162)
label7 = Label(root, text='Gender:', font=('georgia', 11, 'bold'))
label7.place(x=270, y=162)
label8 = Label(root, text='Patients Address:', font=('georgia', 11, 'bold'))
label8.place(x=0, y=192)

label10 = Label(root, text='Contact No:', font=('georgia', 11, 'bold'))
label10.place(x=0, y=222)
label11 = Label(root, text='Diagnosed With:', font=('georgia', 11,  'bold'))
label11.place(x=0, y=282)

label14 = Label(root, text='Allergies:', font=('georgia', 11, 'bold'))
label14.place(x=0, y=372)

label16 = Label(root, text='Drugs:', font=('georgia', 11, 'bold'))
label16.place(x=80, y=402)
label17 = Label(root, text='Unit(Tablet/Syrup):', font=('georgia', 11, 'bold'))
label17.place(x=227, y=402)
label18 = Label(root, text='Dosage(Per Day):', font=('georgia', 11, 'bold'))
label18.place(x=420, y=402)
label19 = Label(root, text='Diet To Follow:', font=('georgia', 11, 'bold'))
label19.place(x=0, y=580)
label20 = Label(root, text='Brief History Of Patient:', font=('georgia', 11, 'bold'))
label20.place(x=0, y=650)
label21 = Label(root, text='Signature Of Physician', font=('georgia', 11,  'bold'))
label21.place(x=0, y=720)
label22 = Label(root, text='1.', font=('georgia', 11,  'bold'))
label22.place(x=0, y=432)
label23 = Label(root, text='2.', font=('georgia', 11,  'bold'))
label23.place(x=0, y=462)
label24 = Label(root, text='3.', font=('georgia', 11,  'bold'))
label24.place(x=0, y=492)
label25 = Label(root, text='4.', font=('georgia', 11,  'bold'))
label25.place(x=0, y=522)
label26 = Label(root, text='5.', font=('georgia', 11,  'bold'))
label26.place(x=0, y=552)
label27 = Label(root, text="", font=('georgia',115))
label27.place(x=210, y=400)
label28 = Label(root, text="", font=('georgia',115))
label28.place(x=400, y=400)


name_entry = Entry(root, font=('georgia', 11,))
name_entry.place(x=130, y=103)
date_entry = Entry(root, font=('georgia', 11), width=18)
date_entry.place(x=400, y=103)
dob_entry = Entry(root, font=('georgia', 11), width=18)
dob_entry.place(x=123, y=133)
age_entry = Entry(root, font=('georgia', 11), width=10)
age_entry.place(x=390, y=133)
id_entry = Entry(root, font=('georgia', 11), width=10)
id_entry.place(x=110, y=163)
gender_entry = Entry(root, font=('georgia', 11), width=15)
gender_entry.place(x=350, y=163)
address_entry = Entry(root, font=('georgia', 11), width=35)
address_entry.place(x=150, y=193)
contact_entry = Entry(root, font=('georgia', 11), width=25)
contact_entry.place(x=102, y=223)
diagnosed_entry1 = Entry(root, font=('georgia',11),width=47)
diagnosed_entry1.place(x=140, y=285)
diagnosed_entry2 = Entry(root, font=('georgia',11),width=47)
diagnosed_entry2.place(x=140, y=305)
diagnosed_entry3 = Entry(root, font=('georgia',11),width=47)
diagnosed_entry3.place(x=140, y=325)
diagnosed_entry4 = Entry(root, font=('georgia',11),width=47)
diagnosed_entry4.place(x=140, y=345)

allergies_entry = Entry(root, font=('georgia',11), width=50)
allergies_entry.place(x=80, y=373)
d1_entry = Entry(root, font=('georgia', 11), width=19)
d1_entry.place(x=29, y=434)
d2_entry = Entry(root, font=('georgia', 11), width=19)
d2_entry.place(x=29, y=464)
d3_entry = Entry(root, font=('georgia', 11), width=19)
d3_entry.place(x=29, y=494)
d4_entry = Entry(root, font=('georgia', 11), width=19)
d4_entry.place(x=29, y=524)
d5_entry = Entry(root, font=('georgia', 11), width=19)
d5_entry.place(x=29, y=554)
unit1_entry = Entry(root, font=('georgia',11),width=19)
unit1_entry.place(x=221, y=434)
unit2_entry = Entry(root, font=('georgia',11),width=19)
unit2_entry.place(x=221, y=464)
unit3_entry = Entry(root, font=('georgia',11),width=19)
unit3_entry.place(x=221, y=494)
unit4_entry = Entry(root, font=('georgia',11), width=19)
unit4_entry.place(x=221, y=524)
unit5_entry = Entry(root, font=('georgia',11), width=19)
unit5_entry.place(x=221, y=554)
dose1_entry = Entry(root, font=('georgia',11), width=18)
dose1_entry.place(x=411, y=434)
dose2_entry = Entry(root, font=('georgia',11), width=18)
dose2_entry.place(x=411, y=464)
dose3_entry = Entry(root, font=('georgia',11), width=18)
dose3_entry.place(x=411, y=494)
dose4_entry = Entry(root, font=('georgia',11), width=18)
dose4_entry.place(x=411, y=524)
dose5_entry = Entry(root, font=('georgia',11), width=18)
dose5_entry.place(x=411, y=554)

diet_entry1 = Entry(root, font=('georgia',11), width=47)
diet_entry1.place(x=129, y=584)
diet_entry2 = Entry(root, font=('georgia',11), width=47)
diet_entry2.place(x=129, y=604)
diet_entry3 = Entry(root, font=('georgia',11), width=47)
diet_entry3.place(x=129, y=624)

history_entry1 = Entry(root, font=('georgia',11), width=40)
history_entry1.place(x=200, y=654)
history_entry2 = Entry(root, font=('georgia',11), width=40)
history_entry2.place(x=200, y=674)
history_entry3 = Entry(root, font=('georgia',11), width=40)
history_entry3.place(x=200, y=694)
mainloop()
