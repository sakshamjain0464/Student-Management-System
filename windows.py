from tkinter import *
import CTkMessagebox as message
import customtkinter as c
from PIL import Image
from PIL import ImageTk
import utilities
import backend


# Create User Dashboard
def createUser(login_window):
    create_window = c.CTkToplevel(login_window)
    create_window.geometry('500x280')
    create_window.title("Create User")

    # Headings
    heading_label = c.CTkLabel(create_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=1, pady=(10,5))

    sub_heading_label = c.CTkLabel(create_window, text="Create User", font=("Helvetica", 18,"bold"))
    sub_heading_label.grid(row=1, column=1, padx=(0,10), pady=(0, 10))

     #entries
    user_label = c.CTkLabel(create_window, text="Username:")
    user_label.grid(row=2, column=0, padx=(30,10), pady=3, sticky=W)

    user_entry = c.CTkEntry(create_window)
    user_entry.grid(row=2, column=1, padx=(3,10), pady=3, sticky=W)

    pwd_label = c.CTkLabel(create_window, text="Password:")
    pwd_label.grid(row=3, column=0, padx=(30,10), pady=3, sticky=W)

    pwd_entry = c.CTkEntry(create_window, show='*')
    pwd_entry.grid(row=3, column=1, padx=(3,10), pady=3, sticky=W)

    conf_pwd_label = c.CTkLabel(create_window, text="Confirm Password:")
    conf_pwd_label.grid(row=4, column=0, padx=(30,10), pady=3, sticky=W)

    conf_pwd_entry = c.CTkEntry(create_window)
    conf_pwd_entry.grid(row=4, column=1, padx=(3,10), pady=3, sticky=W)

    create_button = c.CTkButton(create_window, text="Create User", command= lambda : utilities.createUser(create_window, user_entry, pwd_entry, conf_pwd_entry))
    create_button.grid(row=5, column=1, pady=(10,5))

    login_button = c.CTkButton(create_window, text="Login", command=lambda : create_window.destroy())
    login_button.grid(row=6, column=1)

# Main Dashboard Window
def mainWindow():
# Window Creation
    window =c.CTk()
    window.title("Welcome to Student Management Portal")
    window.geometry("600x500")

    # logo = PhotoImage(file=logo_path)
    try:
        logo_img = Image.open("logo.png")
        resize_img = logo_img.resize((100,100))
        logo = ImageTk.PhotoImage(resize_img)
        #Image for logo
        logo_label = c.CTkLabel(window, text='', image=logo).pack(pady=(50,0))
    except:
        print("Logo loading error")

    # Heading c.CTkLabel
    heading_label = c.CTkLabel(window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.pack(pady=10)

    # Buttons
    addBtn = c.CTkButton(window, text="Add Student Details", command= lambda : addWindow(window), font=("Ariel",16 , "bold"), border_spacing=4)
    addBtn.pack(pady=10)

    updateBtn = c.CTkButton(window, text="Update Student Details", command= lambda : updateWindow(window), font=("Ariel",16 , "bold"), border_spacing=4)
    updateBtn.pack(pady=10)

    viewBtn = c.CTkButton(window, text="View Student Details", font=("Ariel",16 , "bold"), border_spacing=4)
    viewBtn.pack(pady=10)

    deleteBtn = c.CTkButton(window, text="Delete Student Details", font=("Ariel",16 , "bold"), border_spacing=4)
    deleteBtn.pack(pady=10)

    footer_label = c.CTkLabel(window, text="Created By - Saksham Jain and Ritika Nainani", font=("Helvetica", 12))
    footer_label.pack(pady=10, side='bottom')
    window.mainloop()
    backend.connection.close()


def addWindow(window):
    add_window = c.CTkToplevel(window)
    add_window.geometry('600x400')
    add_window.title("Add Student")

    # Headings
    heading_label = c.CTkLabel(add_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=1, pady=10)

    sub_heading_label = c.CTkLabel(add_window, text="Add Student", font=("Helvetica", 16))
    sub_heading_label.grid(row=1, column=1, pady=(0,10))

    #entries

    first_name_label = c.CTkLabel(add_window, text="First Name:", font=("Helvetica", 16))
    first_name_label.grid(row=3, column=0, padx=(30,10), pady=10, sticky=W)

    first_name_entry = c.CTkEntry(add_window)
    first_name_entry.grid(row=3, column=1, padx=(30,10), pady=10, sticky=W)

    last_name_label = c.CTkLabel(add_window, text="Last Name:", font=("Helvetica", 16))
    last_name_label.grid(row=4, column=0, padx=(30,10), pady=10, sticky=W)

    last_name_entry = c.CTkEntry(add_window)
    last_name_entry.grid(row=4, column=1, padx=(30,10), pady=10, sticky=W)

    course_label = c.CTkLabel(add_window, text="Course:", font=("Helvetica", 16))
    course_label.grid(row=5, column=0, padx=(30,10), pady=10, sticky=W)

    courses = backend.getCourses()

    course_entry = c.CTkOptionMenu(add_window, fg_color="gray13", button_color="gray10")
    course_entry.grid(row=5, column=1, padx=(30,10), pady=10, sticky=W)
    course_entry.configure(values=courses)
    course_entry.set("CSE")

    cgpa_label = c.CTkLabel(add_window, text="CGPA:", font=("Helvetica", 16))
    cgpa_label.grid(row=6, column=0, padx=(30,10), pady=10, sticky=W)

    cgpa_entry = c.CTkEntry(add_window)
    cgpa_entry.grid(row=6, column=1, padx=(30,10), pady=10, sticky=W)

    add_button = c.CTkButton(add_window, text="Add Student", font=("Helvetica", 16), command=lambda : utilities.addStudent(first_name_entry, last_name_entry, course_entry, cgpa_entry))
    add_button.grid(row=7, column=1, pady=10)

# Update function
def updateWindow(window):
    update_window = Toplevel(window)
    update_window.geometry('600x400')
    update_window.title("Update Student")

    # Headings
    heading_label = c.CTkLabel(update_window, text="Student Management System", font=("Helvetica", 16, "bold"))
    heading_label.grid(row=0, column=2, padx=(0,10), pady=10)

    sub_heading_label = c.CTkLabel(update_window, text="Update Student Details", font=("Helvetica", 12))
    sub_heading_label.grid(row=1, column=2, padx=(0,10), pady=10)

    #entries
    roll_label = c.CTkLabel(update_window, text="Roll Number:")
    roll_label.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    roll_entry = c.CTkEntry(update_window)
    roll_entry.grid(row=2, column=2, padx=10, pady=10, sticky=W)
