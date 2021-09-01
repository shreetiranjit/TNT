from tkinter import *
from tkinter import messagebox
import os
from registration import registrationform
def login_success():

    messagebox.showinfo(screen, "Login Successful")
    screen2.destroy()
    registrationform()
def password_not_recognised():
    messagebox.showwarning('ALERT', 'INCORRECT PASSWORD.')
def user_not_found():
    messagebox.showwarning('ALERT','USER NOT FOUND!!!')


def register_user():
    a = ''
    if username_entry.get() == a and password_entry.get() == a and password_entry2.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE FILL ALL THE BOXES.')
    elif username_entry.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE FILL THE BOX.')
    elif password_entry.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE WRITE THE PASSWORD.')
    elif password_entry2.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE CONFIRM YOUR PASSWORD TO CONTINUE.')
    elif password_entry.get()  != password_entry2.get() :
        messagebox.showwarning('ALERT', "SORRY !!! PASSWORD DONOT MATCH.")

    else :
        username_info = username.get()
        password_info = password.get()
        file = open(username_info, "a+")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        screen1.destroy()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    # os returns the list containing name of entries in the directory in the path
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global  password
    global username_entry
    global  password_entry
    global  password_entry2
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()
    Label(screen1, text="Please enter detail below", fg="blue",font=("calbria", 13)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username  ", fg="blue",font=("calbria", 13)).pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password  ", fg="blue",font=("calbria", 13)).pack()
    password_entry = Entry(screen1, textvariable= password)
    password_entry.pack()
    Label(screen1, text="Confirm Password  ", fg="blue", font=("calbria", 13)).pack()
    password_entry2 = Entry(screen1,textvariable = confirmpassword)
    password_entry2.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1,fg="blue",font=("calbria", 13), command=register_user).pack()
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    #image
    #bg = PhotoImage(file="tnt hospital .png")
    #label1 = Label(screen2, image=bg)
    #label1.place(x=0, y=0)
    Label(screen2, text="Please enter details below to login", fg="blue",font=("calbria", 13)).pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username  ", fg="blue",font=("calbria", 13)).pack()
    username_entry1 = Entry(screen2, textvariable= username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password  ", fg="blue",font=("calbria", 13)).pack()
    password_entry1 = Entry(screen2,show = "*", textvariable=password_verify)
    password_entry1.pack()

    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, fg="blue",font=("calbria", 13),command=login_verify).pack()
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('1000x560')
    screen.title('Login | Hospital Management System')
    #image
    global bg
    bg = PhotoImage(file="tnt.png")
    label1 = Label(screen, image=bg)
    label1.place(x=0, y=0)
    #textboxes
    Label(text=" ",bg ='white').pack()
    Label(text="",bg ='white').pack()
    Label(text="", bg='white').pack()
    Label(text="", bg='white').pack()
    Button(text="Login", height="3", width="30", font=("CALBRIA", 14, "bold"),fg="black", command=login).pack()
    Label(text="",bg='white').pack()
    Button(text="Register", height="3", width="30", font=("CALBRIA", 14, "bold"), fg="black",  command=register).pack()

    screen.mainloop()

main_screen()
def login_success():

    messagebox.showinfo(screen, "Login Successful")
    screen2.destroy()
    registrationform()
def password_not_recognised():
    messagebox.showwarning('ALERT', 'INCORRECT PASSWORD.')
def user_not_found():
    messagebox.showwarning('ALERT','USER NOT FOUND!!!')


def register_user():
    a = ''
    if username_entry.get() == a and password_entry.get() == a and password_entry2.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE FILL ALL THE BOXES.')
    elif username_entry.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE FILL THE BOX.')
    elif password_entry.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE WRITE THE PASSWORD.')
    elif password_entry2.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE CONFIRM YOUR PASSWORD TO CONTINUE.')
    elif password_entry.get()  != password_entry2.get() :
        messagebox.showwarning('ALERT', "SORRY !!! PASSWORD DONOT MATCH.")

    else :
        username_info = username.get()
        password_info = password.get()
        file = open(username_info, "a+")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        screen1.destroy()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    # os returns the list containing name of entries in the directory in the path
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global  password
    global username_entry
    global  password_entry
    global  password_entry2
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()
    Label(screen1, text="Please enter detail below", fg="blue",font=("calbria", 13)).pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username  ", fg="blue",font=("calbria", 13)).pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password  ", fg="blue",font=("calbria", 13)).pack()
    password_entry = Entry(screen1, textvariable= password)
    password_entry.pack()
    Label(screen1, text="Confirm Password  ", fg="blue", font=("calbria", 13)).pack()
    password_entry2 = Entry(screen1,textvariable = confirmpassword)
    password_entry2.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1,fg="blue",font=("calbria", 13), command=register_user).pack()
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    #image
    bg = PhotoImage(file="tnt hospital .png")
    label1 = Label(screen2, image=bg)
    label1.place(x=0, y=0)
    Label(screen2, text="Please enter details below to login", fg="blue",font=("calbria", 13)).pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username  ", fg="blue",font=("calbria", 13)).pack()
    username_entry1 = Entry(screen2, textvariable= username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password  ", fg="blue",font=("calbria", 13)).pack()
    password_entry1 = Entry(screen2,show = "*", textvariable=password_verify)
    password_entry1.pack()

    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, fg="blue",font=("calbria", 13),command=login_verify).pack()
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('1000x560')
    screen.title('Login | Hospital Management System')
    #image
    global bg
    bg = PhotoImage(file="tnt hospital .png")
    label1 = Label(screen, image=bg)
    label1.place(x=0, y=0)
    #textboxes
    Label(text=" ",bg ='white').pack()
    Label(text="",bg ='white').pack()
    Label(text="", bg='white').pack()
    Label(text="", bg='white').pack()
    Button(text="Login", height="3", width="30", font=("CALBRIA", 14, "bold"),fg="black", command=login).pack()
    Label(text="",bg='white').pack()
    Button(text="Register", height="3", width="30", font=("CALBRIA", 14, "bold"), fg="black",  command=register).pack()

    screen.mainloop()

main_screen()