from tkinter import *
import sqlite3
def registrationform():
    root = Toplevel()
    root.title('Registration')
    root.geometry('1450x800+0+0')
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
        # Create a databases or connect to one
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
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


    def delete():
        # Create a databases or connect to one
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        # delete a record
        c.execute("DELETE from addressb WHERE oid = " + delete_box_entry.get())
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
        query_label.place(x=0, y=0 )

        conn.commit()

        conn.close()

    def edit():
        global editor

        editor = Tk()
        editor.title('Update Data')
        editor.geometry('1350x750')

        # Create a databases or connect to one
        conn = sqlite3.connect('Hospitalmanagement.db')

        # Create cursor
        c = conn.cursor()

        record_id = delete_box_entry.get()

        # query of the database
        c.execute("SELECT * FROM addressb WHERE oid=" + record_id)

        records = c.fetchall()
        # print(records)
        # Creating global variable for all text boxes
        global first_name_editor
        global last_name_editor
        global age_editor
        global address_editor
        global date_of_birth_editor
        global gender_editor
        global father_name_editor
        global mother_name_editor
        global Blood_group_editor
        global Contact_number_editor
        global marital_status_editor
        global Email_status_editor

        # Create text boxes
        first_name_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        first_name_editor.place(x=-220, y=40)
        last_name_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        last_name_editor.place(x=250, y=40)
        age_editor = Entry(editor, font=('calibri', 14,), width=5, borderwidth=5)
        age_editor.place(x=-220, y=100)
        address_editor = Entry(editor, font=('calibri', 14,), width=63, borderwidth=5)
        address_editor.place(x=190, y=100)
        date_of_birth_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        date_of_birth_editor.place(x=-220, y=220)
        gender_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        gender_editor.place(x=-220, y=160)
        father_name_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        father_name_editor.place(x=250, y=160)
        mother_name_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        marital_status_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        marital_status_editor.place(x=250, y=220)
        Blood_group_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        Blood_group_editor.place(x=650, y=40)
        Contact_number_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        Contact_number_editor.place(x=-220, y=280)
        marital_status_editor = Entry(editor, font=('calibri', 14,), width=20, borderwidth=5)
        marital_status_editor.place(x=190, y=280)
        Email_status_editor = Entry(editor, font=('calibri', 14,), width = 20, borderwidth=5)
        Email_status_editor.place(x=500, y=280)

        # Create textbox labels

        first_name_label = Label(editor, text="First Name", font=('calibri', 14, 'bold'))
        first_name_label.place(x=-220, y=40)
        last_name_label = Label(editor, text="Last Name ", font=('calibri', 14, 'bold'))
        last_name_label.place(x=250, y=40)
        age_label = Label(editor, text="Age", font=('calibri', 14, 'bold'))
        age_label.place(x=-220, y=100)
        address_label = Label(editor, text="Address", font=('calibri', 14, 'bold'))
        address_label.place(x=190, y=100)
        date_of_birth_label = Label(editor, text="Date Of Birth", font=('calibri', 14, 'bold'))
        date_of_birth_label.place(x=-220, y=220)
        gender_label = Label(editor, text="Gender", font=('calibri', 14, 'bold'))
        gender_label.place(x=-220, y=160)
        father_name_label = Label(editor, text="Father's name", font=('calibri', 14, 'bold'))
        father_name_label.place(x=250, y=160)
        mother_name_label = Label(editor, text="Mother's name", font=('calibri', 14, 'bold'))
        mother_name_label.place(x=250, y=220)
        Blood_group_label = Label(editor, text="Blood Group", font=('calibri', 14, 'bold'))
        Blood_group_label.place(x=650, y=40)
        Contact_number_label = Label(editor, text="Contact number", font=('calibri', 14, 'bold'))
        Contact_number_label.place(x=-220, y=280)
        marital_status_label = Label(editor, text="Marital status", font=('calibri', 14, 'bold'))
        marital_status_label.place(x=190, y=280)
        Email_label = Label(editor, text="Email address", font=('calibri', 14, 'bold'))
        Email_label.place(x=500, y=280)

        # loop through the results
        for record in records:
            first_name_editor.insert(0, record[0])
            last_name_editor.insert(0, record[1])
            age_editor.insert(0, record[2])
            address_editor.insert(0, record[3])
            date_of_birth_editor.insert(0, record[4])
            gender_editor.insert(0, record[5])
            father_name_editor.insert(0, record[6])
            mother_name_editor.insert(0, record[7])
            Blood_group_editor.insert(0, record[8])
            Contact_number_editor.insert(0, record[9])
            marital_status_editor.insert(0, record[10])
            Email_status_editor.insert(0, record[11])
        # Create a update button
        edit_btn = Button(editor, text=" SAVE ", command=update, font=('calibri', 16, 'bold'), bg='green', fg='white')

        edit_btn.place(x=220, y=430)

        # title
        # Title_frame = Frame(root,bd = 10 , width =1500 , padx= 20 , relief = RIDGE)
        # Title_frame.pack(side = TOP, fill=X)

    Title_frame_label = Label(root, font=('calibri', 30, 'bold'), fg='green', bg='#C4FFB5',
                              text='HOSPITAL MANAGEMENT SYSTEM', bd=10, relief=RIDGE, padx=2, pady=6)
    Title_frame_label.pack(side=TOP, fill=X)

    frame = Frame(root, bd=12, relief=RIDGE, padx=20, bg='#C4FFB5')
    frame.place(x=0, y=100, width=1450, height=490)

    Entry_frame_details = LabelFrame(frame, bd=10, bg='#B3E5FF', padx=250, relief=RIDGE)
    Entry_frame_details.place(x=0, y=5, width=1150, height=450)

    Button_frame_rights = LabelFrame(frame, bd=10, bg='#78CFF6', padx=250, relief=RIDGE)
    Button_frame_rights.place(x=1180, y=5, width=200, height=450)

    Bottom_frame_details = Frame(root, bd=10, bg='#C4FFB5', padx=25, relief=RIDGE)
    Bottom_frame_details.place(x=0, y=600, width=1450, height=200)

    Recordframedetails = LabelFrame(Bottom_frame_details, text='Records', bd=7, bg='#78CFF6',
                                    font=("times new roman", 12, "bold"), relief=RIDGE)
    Recordframedetails.place(x=0, y=5, width=1375, height=175)

    first_name_label = Label(Entry_frame_details, text='First Name', bg='#B3E5FF', font=('calibri', 16, 'bold'))
    first_name_label.place(x=-220, y=40)
    last_name_label = Label(Entry_frame_details, bg='#B3E5FF', font=('calibri', 16, 'bold'), text='Last Name',
                            anchor='e')
    last_name_label.place(x=250, y=40)
    age_label = Label(Entry_frame_details, bg='#B3E5FF', font=('calibri', 16, 'bold'), text='Age')
    age_label.place(x=-220, y=100)
    address_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Address')
    address_label.place(x=250, y=100)
    date_of_birth_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Date Of Birth ')
    date_of_birth_label.place(x=-220, y=220)
    gender_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Gender')
    gender_label.place(x=-220, y=160)
    father_name_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text="Father's name ")
    father_name_label.place(x=250, y=160)
    mother_name_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text="Mother's name ")
    mother_name_label.place(x=250, y=220)
    Blood_group_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Blood Group')
    Blood_group_label.place(x=250, y=340)
    Contact_number_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Contact Number')
    Contact_number_label.place(x=-220, y=280)
    marital_status_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Marital status')
    marital_status_label.place(x=-220, y=340)
    Email_label = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Email address')
    Email_label.place(x=250, y=280)
    delete_box = Label(Entry_frame_details, font=('calibri', 14, 'bold'), text='Delete ID')
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

    submit_btn = Button(Button_frame_rights, font=('calibri', 16, 'bold'), text="Save", bg='green', fg='white',
                        command=submit)
    submit_btn.grid(row=1, column=1)
    query_btn = Button(Button_frame_rights, font=('calibri', 16, 'bold',), text="Display", bg='green', fg='white',
                       command=query)
    query_btn.grid(row=2, column=1)
    delete_box = Button(Button_frame_rights, font=('calibri', 16, 'bold'), text="Delete", bg='red', fg='white',
                        command=delete)
    delete_box.grid(row=3, column=1)
    edit_btn = Button(Button_frame_rights, font=('calibri', 16, 'bold'), text="Update", bg='green', fg='white',
                      command=edit)
    edit_btn.grid(row=4, column=1)
    conn.commit()
    conn.close()
    mainloop()