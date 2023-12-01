from tkinter import *
import CTkMessagebox as message
from PIL import Image
from PIL import ImageTk
import backend

def createUser(create_window, user_entry, pwd_entry, conf_pwd_entry):
    if(user_entry.get() == "" and pwd_entry.get() == "" and conf_pwd_entry.get()):
        message.showwarning(title="WARNING", message="Kindly Fill all the fields!")
    elif(pwd_entry.get() != conf_pwd_entry.get()):
        message.showwarning(title="WARNING", message="Password and Confirm Password Does not Match!")
    else:
        if(message.askokcancel(title="Confirm", message="Do you want to proceed!")):
            created = backend.createUserToDb(user_entry.get(), pwd_entry.get())
            if(created == True):
                message.showinfo(title="Created", message="User Created Successfully!")

            elif(created == "exists"):
                message.showinfo(title="Already Exists", message="User Already Exists!")
            else:
                message.showwarning(title="WARNING", message="Username or password must be unique!")
            user_entry.delete(0, END)
            pwd_entry.delete(0, END)
            conf_pwd_entry.delete(0, END)
        else:
            pass