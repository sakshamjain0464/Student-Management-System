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
    elif(any(not c.isalpha() for c in first_name.get()) or any(not c.isalpha() for c in last_name.get())):
        message(title="WARNING", message="First Name or Last Name cannot contain numbers and special characters", icon='warning')
    elif(not cgpa.get().isnumeric()):
        message(title="WARNING", message="CGPA can only be a two digit integer ", icon='warning')
    elif(int(cgpa.get()) < 0 or int(cgpa.get()) > 100):
        message(title="WARNING", message="CGPA can not be less than 0 or greater than 10", icon='warning')
    else:
        if(message(title="Confirm", message="Do you want to proceed!", option_2 = 'YES', option_1 = 'NO', icon='question').get() == 'YES'):
            new_roll = f'S{backend.students+1}'
            added = backend.addStudentToDb(new_roll, first_name.get(), last_name.get(), course.get(), int(cgpa.get()))
            if(added == True):
                message(title="Created", message=f"Student Added Successfully! for Roll No {new_roll}", icon='check')
                first_name.delete(0, END)
                last_name.delete(0, END)
                cgpa.delete(0, END)
            elif(added == 'Error'):
                message(title="Error", message="An Error Occurred", icon='cancel')
            else:
                message(title="Error", message="Cannot add Student, contact the administrator", icon='cancel')
        else:
            pass


def fetchDetails(roll):
    if(roll == ""):
        message(title="WARNING", message="Kindly Enter Roll Number!", icon='warning')
        return False
    elif(roll[0] != 'S' or any(not c.isalnum() for c in roll)):
        message(title="WARNING", message="Kindly Enter a valid Roll Number!", icon='warning')
        return False
    else:
        details = backend.fetchDetailsFromDb(roll)
        print(details)
        if(details == False):
             message(title="WARNING", message="Student details not found!", icon='cancel')
             return False
        elif(details == "error"):
            message(title="Error", message="An Error Occurred", icon='cancel')
            return False
        else:
            return details
        

def updateName(details, first_name, last_name):
    if(first_name.get() == "" or last_name.get() == ""):
        message(title="WARNING", message="Kindly Fill all the fields!", icon='warning')
    elif(bool(re.search("\s", first_name.get())) or bool(re.search("\s", last_name.get()))):
        message(title="WARNING", message="Any field cannot contain spaces", icon='warning')
    elif(any(not c.isalpha() for c in first_name.get()) or any(not c.isalpha() for c in last_name.get())):
        message(title="WARNING", message="Any field cannot special characters or numbers", icon='warning')
    else:
        if(message(title="Confirm", message="Do you want to proceed!", option_2 = 'YES', option_1 = 'NO', icon='question').get() == 'YES'):
            updated = backend.updateNameToDb(details[0], first_name.get(), last_name.get())
            if(updated == True):
                message(title="Updated", message=f"Student Name Successfully Updated!", icon='check')
                first_name.delete(0, END)
                last_name.delete(0, END)
            elif(updated == 'Error'):
                message(title="Error", message="An Error Occurred", icon='cancel')
            else:
                message(title="Error", message="Cannot update Student, contact the administrator", icon='cancel')
        else:
            pass
        

def updateCourse(details, course):
    if(message(title="Confirm", message="Do you want to proceed!", option_2 = 'YES', option_1 = 'NO', icon='question').get() == 'YES'):
        updated = backend.updateCourseToDb(details[0], course.get())
        if(updated == True):
            message(title="Updated", message=f"Course Successfully Updated!", icon='check')
        elif(updated == 'Error'):
             message(title="Error", message="An Error Occurred", icon='cancel')
        else:
            message(title="Error", message="Cannot update Student, contact the administrator", icon='cancel')
    else:
        pass

def updateCGPA(details, cgpa):
    if(cgpa.get() == ''):
        message(title="WARNING", message="Kindly Fill all the fields!", icon='warning')
    elif(not cgpa.get().isnumeric()):
        message(title="WARNING", message="CGPA can only be a two digit integer ", icon='warning')
    elif(int(cgpa.get()) < 0 or int(cgpa.get()) > 100):
        message(title="WARNING", message="CGPA can not be less than 0 or greater than 10", icon='warning')
    if(message(title="Confirm", message="Do you want to proceed!", option_2 = 'YES', option_1 = 'NO', icon='question').get() == 'YES'):
        updated = backend.updateCGPAToDb(details[0], int(cgpa.get()))
        if(updated == True):
            message(title="Updated", message=f"Course Successfully Updated!", icon='check')
        elif(updated == 'Error'):
             message(title="Error", message="An Error Occurred", icon='cancel')
        else:
            message(title="Error", message="Cannot update Student, contact the administrator", icon='cancel')
    else:
        pass