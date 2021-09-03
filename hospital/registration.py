from tkinter import *
import sqlite3



def registrationform():
    root = Toplevel()
    root.title('Registration')
    root.geometry('1350x750')
    #connect to database
    conn = sqlite3.connect('Hospitalmanagement.db')
    #create a cursor
    c = conn.cursor()

    #c.execute(('''CREATE TABLE addressb(
    #        first_name  text ,
     #         last_name text ,
     #      age integer ,
     #        address text ,
      #       date_of_birth integer ,
      #      gender text ,
      #      father_name text ,
      #       mother_name text ,
      #     blood_group text ,
      #      contact_number integer ,
      #      email_address text,
      #     marital_status text
       #   )'''))

    def submit():
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO addressb VALUES (:first_name, :last_name, :age, :address, :date_of_birth, :gender, :father_name, :mother_name, :blood_group, :contact_number, :email_address, :marital_status)",
            {
                'first_name': first_name.get(),
                'last_name': last_name.get(),
                'age': age.get(),
                'address': address.get(),
                'date_of_birth': date_of_birth.get(),
                'gender': gender_dropdown.get(),
                'father_name': father_name.get(),
                'mother_name': mother_name.get(),
                'blood_group': btype_dropdown.get(),
                'contact_number': Contact_number.get(),
                'email_address': Email_address.get(),
                'marital_status': marital_dropdown.get()
            })
        print("saved")
        conn.commit()
        conn.close()
        first_name.delete(0, END)
        last_name.delete(0, END)
        age.delete(0, END)
        address.delete(0, END)
        date_of_birth.delete(0, END)
        father_name.delete(0, END)
        mother_name.delete(0, END)
        Contact_number.delete(0, END)
        Email_address.delete(0, END)

    def query():
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM addressb")
        records = c.fetchall()
        print(records)

        print_records = ''
        for record in records[0]:
            print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + "\n"
        query_label = Label(Bottom_frame_details, text=print_records)
        query_label.pack(side=BOTTOM)

        conn.commit()
        conn.close()

    def delete():
        # Create a databases or connect to one
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        # delete a record
        c.execute("DELETE from addressb WHERE oid = " + delete_box.get())
        print('Deleted Successfully')
        # query of the database
        c.execute("SELECT *, oid FROM addressb")
        records = c.fetchall()
        # print(records)
        # Loop through the results
        print_record = ''
        for record in records:
            # str(record[12]) added for displaying the id
            print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[12]) + "\n"
        query_label = Label(Bottom_frame_details, text=print_record)
        query_label.place(x=0, y=0)
        conn.commit()
        conn.close()

    # title
    Title_frame = Frame(root, bd=10,bg='red', width=1500, padx=20, relief=RIDGE)
    Title_frame.pack(side=TOP)
    Title_frame_label = Label(Title_frame, font=('calibri', 20, 'bold'), bg='red',fg='white',
                              text='HOSPITAL MANAGEMENT SYSTEM', padx=20)
    Title_frame_label.grid()
    Bottom_frame_details = Frame(root, bd=10,width=1350,bg='white', height=200, padx=25, relief=RIDGE)
    Bottom_frame_details.pack(side=BOTTOM)
    Entry_frame_details =Frame(root, bd=10,bg='light blue', width=1250, height=450, padx=250, relief=RIDGE)
    Entry_frame_details.pack(side=BOTTOM)

    # create textLabels
    first_name_label = Label(Entry_frame_details, text='First Name',bg='light blue', font=('calibri', 14, 'bold'))
    first_name_label.place(x=-220, y=40)
    last_name_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue', text='Last Name', anchor='e')
    last_name_label.place(x=250, y=40)
    age_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), bg='light blue', text='Age')
    age_label.place(x=-220, y=100)
    address_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue',  text='Address')
    address_label.place(x=190, y=100)
    date_of_birth_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), bg='light blue', text='Date Of Birth ')
    date_of_birth_label.place(x=-220, y=220)
    gender_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue',  text='Gender')
    gender_label.place(x=-220, y=160)
    father_name_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue',  text="Father's name ")
    father_name_label.place(x=250, y=160)
    mother_name_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), bg='light blue', text="Mother's name ")
    mother_name_label.place(x=250, y=220)
    Blood_group_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), bg='light blue', text='Blood Group')
    Blood_group_label.place(x=650, y=40)
    Contact_number_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue',  text='Contact Number')
    Contact_number_label.place(x=-220, y=280)
    marital_status_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue',  text='Marital status')
    marital_status_label.place(x=190, y=280)
    Email_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), bg='light blue', text='Email address')
    Email_label.place(x=500, y=280)

    delete_box = Label(Entry_frame_details, font=('calibri', 14, 'bold'),bg='light blue',  text='ID')
    delete_box.place(x=600, y=350)

    # create textboxes
    first_name = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    first_name.place(x=-80, y=40)
    last_name = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    last_name.place(x=380, y=40)
    age = Entry(Entry_frame_details, font=('calibri', 14,), width=5, borderwidth=5)
    age.place(x=-80, y=100)
    address = Entry(Entry_frame_details, font=('calibri', 14,), width=63, borderwidth=5)
    address.place(x=290, y=100)
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
    Email_address.place(x=630, y=280)
    delete_box = Entry(Entry_frame_details, font=('calibri', 14,), width=13, borderwidth=5)
    delete_box.place(x=630, y=350)
    # dropdown
    # drop down menu for gender
    gender = ["Male", "Female", "Other", "Prefer not to say",]
    gender_dropdown = StringVar()
    gender_dropdown.set("Prefer not to say")
    drop1 = OptionMenu(Entry_frame_details, gender_dropdown, *gender)
    drop1.place(x=-80, y=160)

    # drop down menu for marital status
    marital = ["Married", "Unmarried"]
    marital_dropdown = StringVar()
    marital_dropdown.set("Unmarried")
    drop2 = OptionMenu(Entry_frame_details, marital_dropdown, *marital)
    drop2.place(x=310, y=280)

    # drop down menu for blood group
    blood_type = ["O+", "O-", "A+", "A-", "AB+", "AB-", "B+", "B-"]
    btype_dropdown = StringVar()
    btype_dropdown.set("0+")
    drop3 = OptionMenu(Entry_frame_details, btype_dropdown, *blood_type)
    drop3.place(x=780, y=40)

    submit_btn = Button(root, font=('calibri', 16, 'bold'), text="Save", bg='green', fg='white', command=submit)
    submit_btn.place(x=320, y=440)
    query_btn = Button(root, font=('calibri', 16, 'bold',), text="Display", bg='green', fg='white')
    query_btn.place(x=400, y=440)
    delete_box = Button(root, font=('calibri', 16, 'bold'), text="Delete", bg='red', fg='white', command=submit)
    delete_box.place(x=600, y=440)
    edit_btn = Button(root, font=('calibri', 16, 'bold'), text="Update", bg='green', fg='white')
    edit_btn.place(x=500, y=440)

    conn.commit()
    conn.close()

    mainloop()