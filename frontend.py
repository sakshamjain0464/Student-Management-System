from tkinter import *
from tkinter import messagebox
from PIL import Image
import backend
from PIL import ImageTk
import windows

def authenticateUser():
        '''Fuction For Login User Authentication'''
        global attempts
        if(user_entry.get() == "" or pwd_entry.get() == ""):
            messagebox.showwarning(title="Login Failed!", message="No fields can be left Empty!")
        else:
            authenticated = backend.authenticate(user_entry.get(), pwd_entry.get())
            if(authenticated == True):
                print("Authenticated")
                login_window.destroy()
                windows.mainWindow()
            
            elif(authenticated == "Error"):
                  messagebox.showerror(title="Login Failed!", message="Database Error!")
            else:
                messagebox.showwarning(title="Login Failed!", message="Login Failed! Please Try again")
                attempts -=1;
                attempt_label = Label(login_window, text=f"Attempts Left {attempts}")
                attempt_label.grid(row=5, column=1, pady=5)
                if(attempts == 0):
                    messagebox.showwarning(title="Login Failed!", message="No of attempts exceeded")
                    quit()
                return attempts




# Login window
login_window = Tk()
login_window.geometry('500x300')
login_window.title("Login")

# Database error Handling
if(backend.connected == False):
    messagebox.showerror(title="Error", message="Database Connection Error!")
    login_window.destroy()
    quit()

# No of attempts
attempts = 3

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
login_button = Button(login_window, text="Login",  command=lambda :  authenticateUser())
login_button.grid(row=4, column=1, pady=5)
signup_button = Button(login_window, text="Create User")
signup_button.grid(row=4, column=2, pady=5)
login_window.mainloop()