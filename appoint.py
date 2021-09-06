from tkinter import *
from prescriptionB import *
from list_of_doctors import *
import sqlite3
from tkinter import messagebox

def appoint2():
    root = Toplevel()
    root.title('Appointment')
    root.geometry('1100x800')
    title = Label(root, text='PATIENTS DETAILS', bg='powder blue', fg='green', bd=10, relief=RIDGE,
                  font=("times new roman", 25, "bold"), padx=2, pady=6)
    title.pack(side=TOP, fill=X)

    # creating to database
    conn = sqlite3.connect('check.db')
    # Creating the cursor
    c = conn.cursor()
    # creating tables
    """
    c.execute(('''CREATE TABLE appointment_test3 (
             p_conditions text , 
             medication text , 
           symptoms text , 
           cal_check text , 
           allergy text , 
           doctors text 
         )'''))
    print('TABLE CREATED SUCCESSFULLY ')
    """


    def submit():
        conn = sqlite3.connect('check.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO appointment_test3 VALUES (:p_conditions, :medication, :symptom, :cal_check , :allergy , :doctors )",
            {
                'p_conditions': condition.get(),
                'medication': medications.get(),
                'symptom': symptoms.get(),
                'cal_check': cale_entry.get(),
                'allergy': symptom2.get(),
                'doctors': doc_entry.get()

            })
        print('INSERTED')
        conn.commit()
        conn.close()


    def query():
        conn = sqlite3.connect("Hospitalmanagement.db")
        c = conn.cursor()
        c.execute(
             "SELECT * FROM addressb  WHERE oid=" + ID_e.get())
        record1 = c.fetchall()
        print(record1)

        for records in record1:
            name.insert(0, records[1])
            name.insert(0, records[0])
            age.insert(0, records[2])
            gender.insert(0, records[5])


        conn1  = sqlite3.connect('check.db')
        c1 = conn1.cursor()
        c1.execute("SELECT * FROM appointment_test3 where oid=" + ID_e.get())
        record2 = c1.fetchall()
        print(record2)

        for recordss in record2 :
            condition.insert(0 , recordss[0])
            medications.insert(0, recordss[1])
            symptoms.insert(0 , recordss[2])
            cale_entry.insert(0 , recordss[3])
            symptom2.insert(0 , recordss[4])
            doc_entry.insert(0 , recordss[5])

        global print_record
        global print_record1
        print_record = ''
        print_record1 = ''
        for records in record1 :
            print_record += str(records[0]) + "\t" + str(records[1]) + str(records[2]) + str(records[3])  + " " + "\n"
        query_label = Label(framedetails, text=print_record , bg = "powder blue")
        query_label.place(x=50, y=20)
        for records1 in record2 :
            print_record1 += str(records1[0]) + "\t" + str(records1[1]) + str(records1[2]) + str(records1[3])+ str(records1[4])+ str(records1[5])

        query_label1 = Label(framedetails, text=print_record1 , bg = "powder blue")
        query_label1.place(x =100  , y  = 20 )


    def update():
        conn = sqlite3.connect("Hospitalmanagement.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM addressb  WHERE oid=" + ID_e.get())
        record1 = c.fetchall()

        print(record1)

        for records in record1:
            name.insert(0, records[0])
            age.insert(0, records[2])
            gender.insert(0, records[5])


        conn1 = sqlite3.connect('check.db')
        c1 = conn1.cursor()
        c1.execute("SELECT  * FROM appointment_test3 WHERE oid=" + ID_e.get())
        record2 = c1.fetchall()

        for records in record2:
            condition.insert(0, records[0])
            medications.insert(0, records[1])
            symptoms.insert(0, records[2])
            cale_entry.insert(0, records[3])
            symptom2.insert(0, records[4])
            doc_entry.insert(0, records[5])

    def editor():
        conn = sqlite3.connect('check.db')
        c = conn.cursor()
        record_id1 = ID_e.get()
        c.execute("""UPDATE appointment_test3 SET 
                  p_conditions = :condition , 
             medication = :medicine , 
           symptoms = :symptom , 
           cal_check = :date, 
           allergy = :allergies , 
           doctors = :doc
           
           WHERE oid = :oid""",
                  {'condition': condition.get(),
                   'medicine': medications.get(),
                   'symptom': symptoms.get(),
                   'date': cale_entry.get(),
                   'allergies': symptom2.get(),
                   'doc': doc_entry.get(),
                   'oid': record_id1

                  })
        conn.commit()
        conn.close()
        messagebox.showinfo('SUCCESS ', 'DATA HAS BEEN UPDATED SUCCESFULLY!!!')

    def clear():
        name.delete(0, END)
        age.delete(0, END)
        gender.delete(0, END)
        condition.delete(0, END)
        symptoms.delete(0, END)
        symptom2.delete(0, END)
        doc_entry.delete(0, END)
        cale_entry.delete(0, END)
        medications.delete(0, END)

    # ourdoctors
    def doctors():
        lod()



    def prescription_for_patient():
        prescribe2()

    #frames
    frame=Frame(root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
    frame.place(x=0 , y=90, width=1100, height=430)
    Dataframeleft =LabelFrame(frame,text='Patient Information', bg='powder blue', fg='green',bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
    Dataframeleft.place(x=0,y=5, width=280,height=380)
    Dataframeright1 = LabelFrame(frame, bg='powder blue',bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
    Dataframeright1.place(x=300,y=5, width=600,height=380)
    Dataframeright2 = LabelFrame(frame, text="Calendar",fg='green', bg='powder blue', bd=12,relief=RIDGE, font=("times new roman", 12,"bold"))
    Dataframeright2.place(x=750,y=5, width=300,height=380)
    #calendar
    cale = Label(Dataframeright2 , text = 'Enter the date for your appointment : ' , font=("times new roman", 12,"bold") )
    cale.place(x = 10 ,  y = 1)
    cale_entry = Entry(Dataframeright2 ,font=("times new roman", 12,"bold")   )
    cale_entry.place (x = 20 , y = 30)


    global framedetails
    global framedetails1
    framedetails = Frame(root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
    framedetails.place(x=0, y=580, width=1300, height=210)
    framedetails1 = LabelFrame(framedetails, text="Records", bg='powder blue', fg='green', bd=12, relief=RIDGE,
                               font=("times new roman", 12, "bold"))
    framedetails1.place(x=0, y=5, width=500, height=170)
    framedetails2_label = LabelFrame(framedetails, text="Prescription", bg='powder blue', fg='green', bd=12, relief=RIDGE,
                                     font=("times new roman", 12, "bold"))
    framedetails2_label.place(x=550, y=5, width=500, height=170)
    framedetails2 = Text(framedetails2_label, font=('calibri', 14,), width=50, relief=SUNKEN)
    framedetails2.place(x=3, y=5, width=450, height=130)

    FrameButton = Frame(root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
    FrameButton.place(x=0, y=525, width=1100, height=60)
    myButton_label = Button(FrameButton, text="Only For Doctors use*", bg='red', font=('calibri', 10, 'bold'), width=20,
                            relief=SUNKEN)
    myButton_label.grid(row=0, column=1)

    #doctors
    doc_label = Label(FrameButton , text = "Please enter the doctor's name")
    doc_label.place(x = 600 , y = -2)
    doc_entry = Entry(FrameButton , font=('calibri', 14,),width=15, relief=SUNKEN)
    doc_entry.place(x = 800 , y = -2 )

    name_label = Label(Dataframeright1, text='Name', font=('calibri', 14,), width=10, relief=SUNKEN)
    name_label.grid(row=0, column=0, columnspan=2)
    age_label = Label(Dataframeright1, text='Age', font=('calibri', 14,), width=10, relief=SUNKEN)
    age_label.grid(row=2, column=0)
    gender_label = Label(Dataframeright1, text='Gender', font=('calibri', 14,), width=10, relief=SUNKEN)
    gender_label.grid(row=4, column=0)
    condition_label = Label(Dataframeright1, text='Previous Conditions ', font=('calibri', 14,), width=15, relief=SUNKEN)
    condition_label.grid(row=6, column=0, )
    mediation_label = Label(Dataframeright1, text='Medication you are on', font=('calibri', 14,), width=18, relief=SUNKEN)
    mediation_label.grid(row=8, column=0, columnspan=2)
    symptom1_label = Label(Dataframeright1, text='Symptoms you are having ', font=('calibri', 14,), width=15, relief=SUNKEN)
    symptom1_label.grid(row=10, column=0, columnspan=2)
    symptom2_label = Label(Dataframeright1, text='Any Allergies', font=('calibri', 14,),width=15, relief=SUNKEN)
    symptom2_label.grid(row=12, column=0, columnspan=2)

    global name
    global age
    global gender
    global condition
    global medications
    global symptoms
    global ID_e

    name = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    name.grid(row=0, column=2, padx=15, pady=10)
    age = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    age.grid(row=2, column=2, padx=15, pady=10)
    gender = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    gender.grid(row=4, column=2, padx=15, pady=10)
    condition = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    condition.grid(row=6, column=2, padx=15, pady=10)
    medications = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    medications.grid(row=8, column=2, padx=15, pady=10)
    symptoms = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    symptoms.grid(row=10, column=2, padx=15, pady=10)
    symptom2= Entry(Dataframeright1, font=('calibri', 14,),width=15, relief=SUNKEN)
    symptom2.grid(row=12, column=2, padx=15, pady=10)
    #forID
    ID_label = Label(Dataframeleft, text='ENTER PATIENT ID', font=('calibri', 14,), width=22, bg='green', fg="WHITE")
    ID_label.grid(row=0, columnspan=2)
    ID_e = Entry(Dataframeleft, font=('calibri', 14,), width=10)
    ID_e.grid(row=1, column=0)
    #buttons
    enter_button = Button(Dataframeleft, text="ENTER", font=('calibri', 14,), width=10, bg='GREY' ,command = query)
    enter_button.grid(row=1, column=1)
    submit_button = Button(Dataframeleft, text="SUBMIT", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
                           borderwidth=5  , command = submit)
    submit_button.grid(row=2, columnspan=2)
    update_button = Button(Dataframeleft, text="UPDATE", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
                           borderwidth=5 ,command = update)
    update_button.grid(row=3, columnspan=2)
    save_button = Button(Dataframeleft, text="SAVE ", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
                         borderwidth=5  , command = editor )
    save_button.grid(row=4, columnspan=2)
    doctors_button = Button(Dataframeleft, text="OUR DOCTORS", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
                            borderwidth=5 ,command = doctors)
    doctors_button.grid(row=5, columnspan=2)
    # logout_button = Button(Dataframeleft, text="LOG OUT", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
    #                        borderwidth=5 ,command = logout)
    # logout_button.grid(row=6, columnspan=2)
    clear_button = Button(Dataframeleft, text="CLEAR", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
                           borderwidth=5 , command = clear)
    clear_button.grid(row=7, columnspan=2)
    precription_button = Button(Dataframeright2, text="CLICK HERE FOR YOUR PRECRIPTION.", font=('calibri', 14,), width=22, bg='grey', relief=SUNKEN,
                          borderwidth=5, command=prescription_for_patient)
    precription_button.place(x = 20 , y = 50)


    mainloop()