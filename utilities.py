from tkinter import *
from CTkMessagebox import CTkMessagebox as message
import backend
import re

# Function to create user
def createUser(create_window, user_entry, pwd_entry, conf_pwd_entry):
    if(user_entry.get() == "" or pwd_entry.get() == "" or conf_pwd_entry.get() == ""):
        message(title="WARNING", message="Kindly Fill all the fields!", icon='warning')
    elif(pwd_entry.get() != conf_pwd_entry.get()):
        message(title="WARNING", message="Password and Confirm Password Does not Match!", icon='warning')
    else:
        if(message(title="Confirm", message="Do you want to proceed!", option_2 = 'YES', option_1 = 'NO', icon='question').get() == 'YES'):
            created = backend.createUserToDb(user_entry.get(), pwd_entry.get())
            if(created == True):
                message(title="Created", message="User Created Successfully!", icon='check')
            elif(created == "exists"):
                message(title="Already Exists", message="User Already Exists!", icon='info')
            else:
                message(title="WARNING", message="Username or password must be unique!", icon='warning')
            user_entry.delete(0, END)
            pwd_entry.delete(0, END)
            conf_pwd_entry.delete(0, END)
        else:
            pass

# Function to add new student
def addStudent(first_name, last_name, course, cgpa):
    if(first_name.get() == "" or last_name.get() == "" or course.get() == "" or cgpa.get() == ''):
        message(title="WARNING", message="Kindly Fill all the fields!", icon='warning')
    elif(bool(re.search("\s", first_name.get())) or bool(re.search("\s", last_name.get())) or bool(re.search("\s", cgpa.get()))):
        message(title="WARNING", message="Any field cannot contain spaces", icon='warning')
    elif(any(not c.isalnum() for c in first_name.get()) or any(not c.isalnum() for c in last_name.get())):
        message(title="WARNING", message="Any field cannot special characters", icon='warning')
    elif(not cgpa.get().isnumeric()):
        message(title="WARNING", message="CGPA can only be a two digit integer ", icon='warning')
    elif(int(cgpa.get()) < 0 or int(cgpa.get()) > 100):
        message(title="WARNING", message="CGPA can not be less than 0 or greater than 10", icon='warning')
    else:
        print(int(cgpa.get()), course.get())
        if(message(title="Confirm", message="Do you want to proceed!", option_2 = 'YES', option_1 = 'NO', icon='question').get() == 'YES'):
            new_roll = f'S{backend.students+1}'
            added = backend.addStudentToDb(new_roll, first_name.get(), last_name.get(), course.get(), int(cgpa.get()))
            if(added == True):
                message(title="Created", message="Student Added Successfully!", icon='check')
                first_name.delete(0, END)
                last_name.delete(0, END)
                cgpa.delete(0, END)
            elif(added == 'Error'):
                message(title="Error", message="An Error Occurred", icon='cancel')
            else:
                message(title="Error", message="Cannot add Student, contact the administrator", icon='cancel')
        else:
            pass