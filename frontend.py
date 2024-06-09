from tkinter import *
import customtkinter as c
from CTkMessagebox import CTkMessagebox as message
from PIL import Image
import backend
import windows

def authenticateUser():
        '''Fuction For Login User Authentication of User'''
        global attempts
        if(user_entry.get() == "" or pwd_entry.get() == ""):
            message(title="Login Failed!", message="No fields can be left Empty!", icon='warning')
        else:
            authenticated = backend.authenticate(user_entry.get(), pwd_entry.get())
            if(authenticated == True):
                print("Authenticated")
                login_window.destroy()
                windows.studentDashboard()
            elif(authenticated == "Error"):
                  message(title="Login Failed!", message="Database Error!", icon='cancel')
            else:
                message(title="Login Failed!", message="Login Failed! Please Try again", icon='cancel')
                attempts -=1;
                attempt_label = c.CTkLabel(login_window, text=f"Attempts Left {attempts}")
                attempt_label.grid(row=6, column=1, pady=5)
                if(attempts <= 0):
                    if(message(title="Login Failed!", message="No of attempts exceeded", icon='cancel', option_1='OK').get() == 'OK'):
                        backend.connection.close()
                        login_window.destroy()



'''Window for Login'''
# Login window initialization
login_window = c.CTk()
login_window.geometry('500x300')
login_window.title("Login")

# No of attempts
attempts = 3

# Headings
heading_label = c.CTkLabel(login_window, text="Student Management System", font=("Ariel",20 , "bold"))
heading_label.grid(row=0, column=1, padx=10, pady=(20,10))

sub_heading_label = c.CTkLabel(login_window, text="Login", font=("Helvetica", 18, "bold"))
sub_heading_label.grid(row=1, column=1, padx=10, pady=(0,10))

 #entries
user_label = c.CTkLabel(login_window, text="Username:", font=("Helvetica", 16, "bold"))
user_label.grid(row=2, column=0, padx=(30,10), pady=3, sticky=W)

user_entry = c.CTkEntry(login_window, placeholder_text="username", font=("Helvetica", 14))
user_entry.grid(row=2, column=1, padx=(3,10), pady=3, sticky=W)

pwd_label = c.CTkLabel(login_window, text="Password:", font=("Helvetica", 16, "bold"))
pwd_label.grid(row=3, column=0, padx=(30,10), pady=3, sticky=W)

pwd_entry = c.CTkEntry(login_window, placeholder_text="password",show='*', font=("Helvetica", 14))
pwd_entry.grid(row=3, column=1, padx=(3,10), pady=3, sticky=W)


# Buttons
login_button = c.CTkButton(login_window, text="Login",  command=lambda :  authenticateUser())
login_button.grid(row=4, column=1, pady=(20,0))

create_button = c.CTkButton(login_window, text="Create User", command=lambda : windows.createUser(login_window))
create_button.grid(row=5, column=1, pady=5)

if(backend.connected == False):
    '''If databse connection has any problem!, the application will automatically exit'''
    if(message(title="Login Failed!", message="Database Error, Quitting App", icon='cancel', option_1='OK').get() == 'OK'):
        backend.connection.close()
        login_window.destroy()

    
login_window.mainloop()