from tkinter import *
import sqlite3
def registrationform():
    root = Toplevel()
    root.title('Registration')
    root.geometry('1490x800+0+0')
    root.resizable(0, 0)

    #connect to database
    conn = sqlite3.connect('Hospitalmanagement.db')
    #create a cursor
    c = conn.cursor()
    #c.execute(('''CREATE TABLE addressb(
    #        first_name  text ,
    #         last_name text ,
    #       age integer ,
    #         address text ,
    #         date_of_birth integer ,
    #        gender text ,
    #         father_name text ,
    #         mother_name text ,
    #         blood_group text ,
    #         contact_number integer ,
    #        email_address text,
    #       marital_status text
    #      )'''))


        # title
        # Title_frame = Frame(root,bd = 10 , width =1500 , padx= 20 , relief = RIDGE)
        # Title_frame.pack(side = TOP, fill=X)

    Title_frame_label = Label(root, font=('calibri', 30, 'bold'), fg='green', bg='#C4FFB5',
                              text='HOSPITAL MANAGEMENT SYSTEM', bd=10, relief=RIDGE, padx=2, pady=6)
    Title_frame_label.pack(side=TOP, fill=X)

    frame = Frame(root, bd=12, relief=RIDGE, padx=20, bg='#C4FFB5')
    frame.place(x=0, y=100, width=1490, height=490)

    Entry_frame_details = LabelFrame(frame, bd=10, bg='#B3E5FF', padx=250, relief=RIDGE)
    Entry_frame_details.place(x=0, y=5, width=1150, height=450)

    Button_frame_rights = LabelFrame(frame, bd=10, bg='#B3E5FF', padx=250, relief=RIDGE)
    Button_frame_rights.place(x=1150, y=5, width=290, height=450)

    Bottom_frame_details = Frame(root, bd=10, bg='#C4FFB5', padx=25, relief=RIDGE)
    Bottom_frame_details.place(x=0, y=600, width=1490, height=200)

    Recordframedetails = LabelFrame(Bottom_frame_details, text='Records', bd=7, bg='#B3E5FF',
                                    font=("times new roman", 12, "bold"), relief=RIDGE)
    Recordframedetails.place(x=0, y=5, width=1440, height=175)

    first_name_label = Label(Entry_frame_details, text='First Name', bg='#B3E5FF', font=('calibri', 16, 'bold'))
    first_name_label.place(x=-220, y=40)
    last_name_label = Label(Entry_frame_details, bg='#B3E5FF', font=('calibri', 16, 'bold'), text='Last Name',
                            anchor='e')
    last_name_label.place(x=250, y=40)
    age_label = Label(Entry_frame_details, bg='#B3E5FF', font=('calibri', 16, 'bold'), text='Age')
    age_label.place(x=-220, y=100)
    address_label = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text='Address')
    address_label.place(x=250, y=100)
    date_of_birth_label = Label(Entry_frame_details, bg='#B3E5FF',font=('calibri', 14, 'bold'), text='Date Of Birth ')
    date_of_birth_label.place(x=-220, y=220)
    gender_label = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text='Gender')
    gender_label.place(x=-220, y=160)
    father_name_label = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text="Father's name ")
    father_name_label.place(x=250, y=160)
    mother_name_label = Label(Entry_frame_details, bg='#B3E5FF',font=('calibri', 14, 'bold'), text="Mother's name ")
    mother_name_label.place(x=250, y=220)
    Blood_group_label = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text='Blood Group')
    Blood_group_label.place(x=250, y=340)
    Contact_number_label = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text='Contact Number')
    Contact_number_label.place(x=-220, y=280)
    marital_status_label = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text='Marital status')
    marital_status_label.place(x=-220, y=340)
    Email_label = Label(Entry_frame_details, bg='#B3E5FF',font=('calibri', 14, 'bold'), text='Email address')
    Email_label.place(x=250, y=280)
    delete_box = Label(Entry_frame_details,bg='#B3E5FF', font=('calibri', 14, 'bold'), text='Delete ID')
    delete_box.place(x=-220, y=400)

    # create textboxes
    first_name = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    first_name.place(x=-80, y=40)
    last_name = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    last_name.place(x=380, y=40)
    age = Entry(Entry_frame_details, font=('calibri', 14,), width=5, borderwidth=5)
    age.place(x=-80, y=100)
    address = Entry(Entry_frame_details, font=('calibri', 14,), width=40, borderwidth=5)
    address.place(x=380, y=100)
    date_of_birth = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    date_of_birth.place(x=-80, y=220)
    # gender = Entry(Entry_frame_details, font = ('calibri', 14 , ), width = 15, borderwidth = 5)
    # gender.place(x =-80 , y = 160)
    father_name = Entry(Entry_frame_details, font=('calibri', 14,), width=40, borderwidth=5)
    father_name.place(x=380, y=160)
    mother_name = Entry(Entry_frame_details, font=('calibri', 14,), width=40, borderwidth=5)
    mother_name.place(x=380, y=220)
    Contact_number = Entry(Entry_frame_details, font=('calibri', 14,), width=17, borderwidth=5)
    Contact_number.place(x=-80, y=280)
    Email_address = Entry(Entry_frame_details, font=('calibri', 14,), width=30, borderwidth=5)
    Email_address.place(x=380, y=280)
    delete_box_entry = Entry(Entry_frame_details, text="Delete ID", font=('calibri', 14,), width=5, borderwidth=5)
    delete_box_entry.place(x=-80, y=400)

    # dropdown
    # drop down menu for gender
    gender = ["Male", "Female", "Other", "Prefer not to say"]
    gender_dropdown = StringVar()
    gender_dropdown.set("Prefer not to say")
    drop1 = OptionMenu(Entry_frame_details, gender_dropdown, *gender)
    drop1.place(x=-80, y=160)
    # drop down menu for marital status
    marital = ["Married", "Unmarried"]
    marital_dropdown = StringVar()
    marital_dropdown.set("Unmarried")
    drop2 = OptionMenu(Entry_frame_details, marital_dropdown, *marital)
    drop2.place(x=-80, y=340)
    # drop down menu for blood group
    blood_type = ["O+", "O-", "A+", "A-", "AB+", "AB-", "B+", "B-"]
    btype_dropdown = StringVar()
    btype_dropdown.set("0+")
    drop3 = OptionMenu(Entry_frame_details, btype_dropdown, *blood_type)
    drop3.place(x=380, y=340)


    global bg1
    bg1 = PhotoImage(file="save.png")


    global bg2
    bg2 = PhotoImage(file="record.png")


    global bg3
    bg3 = PhotoImage(file="update .png")


    global bg4
    bg4 = PhotoImage(file="Delete.png")

    global bg5
    bg5 = PhotoImage(file="Appointment.png")

    submit_btn = Button(Button_frame_rights, image=bg1, borderwidth=0, height=40, width=150)
    submit_btn.place(x=-210, y=20)
    query_btn = Button(Button_frame_rights, image=bg2, borderwidth=0, height=40, width=150)
    query_btn.place(x=-210, y=100)
    edit_btn = Button(Button_frame_rights, image=bg3, borderwidth=0, height=55, width=150)
    edit_btn.place(x=-210, y=180)
    delete_box = Button(Button_frame_rights, image=bg4, borderwidth=0, height=40, width=150)
    delete_box.place(x=-210, y=260)
    appointment_btn = Button(Button_frame_rights, image=bg5, borderwidth=0, height=30, width=250)
    appointment_btn.place(x=-240, y=340)


    conn.commit()
    conn.close()
    mainloop()