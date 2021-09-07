from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Logout Application")
root.geometry('400x150')
def logout():
    response = messagebox.askyesno("Logout Application","Are you sure want to close this application")
    if response > 0:
        root.destroy()
        return

mybutton = Button(text="Logout", height="3", width="30", font=("gudy old style", 12, "bold"), fg="#6162FF", bg="#99c2ff",  command=logout)
mybutton.place(x=20, y=10)

root.mainloop()



