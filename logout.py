from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Logout Application")
root.geometry('400x150')
#root.iconbitmap('medical.ico')
def logout():
    response = messagebox.askyesno("Logout Application","Are you sure want to close this application")
    if response > 0:
        root.destroy()
        return
mybutton = Button(text="Logout", height="3", width="30", font=("CALIBRI", 12, "bold"), fg="BLACK", bg="#BC85A3",  command=logout).pack()
root.mainloop()
