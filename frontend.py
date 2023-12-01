from tkinter import *
from tkinter import messagebox
from PIL import Image
import backend
from PIL import ImageTk
import windows

def authenticateUser():
        authenticated = backend.authenticate(user_entry.get(), pwd_entry.get())
        if(authenticated):
            print("Authenticated")
            login_window.destroy()
            windows.mainWindow()
        else:
            messagebox.showwarning(title="Login Failed!", message="Login Failed!")


login_window = Tk()
login_window.geometry('500x200')
login_window.title("Login")
# Headings
heading_label = Label(login_window, text="Student Management System", font=("Helvetica", 16, "bold"))
heading_label.grid(row=0, column=1, padx=(0,10), pady=10)

sub_heading_label = Label(login_window, text="Login", font=("Helvetica", 12))
sub_heading_label.grid(row=1, column=1, padx=(0,10), pady=10)

 #entries
user_label = Label(login_window, text="Username:")
user_label.grid(row=2, column=0, padx=(30,10), pady=3, sticky=W)

user_entry = Entry(login_window)
user_entry.grid(row=2, column=1, padx=(3,10), pady=3, sticky=W)

pwd_label = Label(login_window, text="Password:")
pwd_label.grid(row=3, column=0, padx=(30,10), pady=3, sticky=W)

pwd_entry = Entry(login_window)
pwd_entry.grid(row=3, column=1, padx=(3,10), pady=3, sticky=W)
login_button = Button(login_window, text="Login",  command=lambda : authenticateUser())
login_button.grid(row=4, column=1, pady=5)
signup_button = Button(login_window, text="Sign UP")
signup_button.grid(row=4, column=2, pady=5)
login_window.mainloop()