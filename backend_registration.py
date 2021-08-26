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

#query
def query():
    conn = sqlite3.connect('Hospitalmanagement.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addressb")
    records = c.fetchall()
    print(records)

    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[12]) + "\n"
    query_label = Label(Bottom_frame_details, text=print_record)
    query_label.place(x= 0, y = 0)
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
    query_label.place(x = 0 , y = 0 )
    conn.commit()
    conn.close()

def update():


    conn = sqlite3.connect('Hospitalmanagement.db')
    c = conn.cursor()
    record_id = delete_box_entry.get()

    c.execute("SELECT *FROM addressb WHERE oid=" + record_id)
    record = c.fetchall()


    for records in record:
        first_name.insert(0, records[0])
        last_name.insert(0, records[1])
        age.insert(0, records[2])
        address.insert(0, records[3])
        date_of_birth.insert(0, records[4])
        father_name.insert(0, records[5])
        mother_name.insert(0, records[7])
        Contact_number.insert(0, records[9])
        Email_address.insert(0, records[11])



def editor():
    conn = sqlite3.connect('Hospitalmanagement.db')
    c = conn.cursor()
    record_id = delete_box_entry.get()
    c.execute("""UPDATE addressb SET
         first_name = :first,
         last_name = :last,
         age= :age,
         address = :address,
         date_of_birth= :dob,
         father_name = :father,
         mother_name = :mother,
         Contact_number = :contact,
         Email_address = :email

         WHERE oid = :oid""",
              {'first': first_name.get(),
               'last': last_name.get(),
               'age' : age.get(),
               'address': address.get(),
               'dob': date_of_birth.get(),
               'father': father_name.get(),
               'mother': mother_name.get(),
               'contact': Contact_number.get(),
               'email': Email_address.get(),
               'oid': record_id
               })

    conn.commit()
    conn.close()
