from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import utilities
import backend


# Create User Dashboard
def createUser(login_window):
    create_window = Toplevel(login_window)
    create_window.geometry('500x250')
    create_window.title("Create User")

    # Headings
    heading_label = Label(create_window, text="Student Management System", font=("Helvetica", 16, "bold"))
    heading_label.grid(row=0, column=1, padx=(0,10), pady=10)

    sub_heading_label = Label(create_window, text="Create User", font=("Helvetica", 12))
    sub_heading_label.grid(row=1, column=1, padx=(0,10), pady=10)

     #entries
    user_label = Label(create_window, text="Username:")
    user_label.grid(row=2, column=0, padx=(30,10), pady=3, sticky=W)

    user_entry = Entry(create_window)
    user_entry.grid(row=2, column=1, padx=(3,10), pady=3, sticky=W)

    pwd_label = Label(create_window, text="Password:")
    pwd_label.grid(row=3, column=0, padx=(30,10), pady=3, sticky=W)

    pwd_entry = Entry(create_window, show='*')
    pwd_entry.grid(row=3, column=1, padx=(3,10), pady=3, sticky=W)

    conf_pwd_label = Label(create_window, text="Confirm Password:")
    conf_pwd_label.grid(row=4, column=0, padx=(30,10), pady=3, sticky=W)

    conf_pwd_entry = Entry(create_window)
    conf_pwd_entry.grid(row=4, column=1, padx=(3,10), pady=3, sticky=W)

    create_button = Button(create_window, text="Create User", command= lambda : utilities.createUser(create_window, user_entry, pwd_entry, conf_pwd_entry))
    create_button.grid(row=5, column=1, pady=5)

    login_button = Button(create_window, text="Login", command=lambda : create_window.destroy())
    login_button.grid(row=5, column=2, padx=(0,10))

# Main Dashboard Window
def mainWindow():
# Window Creation
    window =Tk()
    window.title("Welcome to Student Management Portal")
    window.geometry("600x500")

    # logo = PhotoImage(file=logo_path)
    try:
        logo_img = Image.open("logo.png")
        resize_img = logo_img.resize((100,100))
        logo = ImageTk.PhotoImage(resize_img)
        #Image for logo
        logo_label = Label(window, image=logo).pack(pady=(50,0))
    except:
        print("Logo loading error")

    # Heading Label
    heading_label = Label(window, text="Student Management System", font=("Helvetica", 16, "bold"))
    heading_label.pack(pady=10)

    # Buttons
    addBtn = Button(window, text="Add Student Details", command= lambda : addWindow(window))
    addBtn.pack(pady=10)

    updateBtn = Button(window, text="Update Student Details", command= lambda : updateWindow(window))
    updateBtn.pack(pady=10)

    viewBtn = Button(window, text="View Student Details")
    viewBtn.pack(pady=10)

    deleteBtn = Button(window, text="Delete Student Details")
    deleteBtn.pack(pady=10)

    footer_label = Label(window, text="Created By - Saksham Jain and Ritika Nainani", font=("Helvetica", 8))
    footer_label.pack(pady=10, side='bottom')
    window.mainloop()
    backend.connection.close()


def addWindow(window):
    add_window = Toplevel(window)
    add_window.geometry('600x400')
    add_window.title("Add Student")

    # Headings
    heading_label = Label(add_window, text="Student Management System", font=("Helvetica", 16, "bold"))
    heading_label.grid(row=0, column=1, padx=(0,10), pady=10)

    sub_heading_label = Label(add_window, text="Add Student", font=("Helvetica", 12))
    sub_heading_label.grid(row=1, column=1, padx=(0,10), pady=10)

    #entries

    first_name_label = Label(add_window, text="First Name:")
    first_name_label.grid(row=3, column=0, padx=(30,10), pady=10, sticky=W)

    first_name_entry = Entry(add_window)
    first_name_entry.grid(row=3, column=1, padx=(30,10), pady=10, sticky=W)

    last_name_label = Label(add_window, text="Last Name:")
    last_name_label.grid(row=4, column=0, padx=(30,10), pady=10, sticky=W)

    last_name_entry = Entry(add_window)
    last_name_entry.grid(row=4, column=1, padx=(30,10), pady=10, sticky=W)

    department_label = Label(add_window, text="Department:")
    department_label.grid(row=5, column=0, padx=(30,10), pady=10, sticky=W)

    department_entry = Entry(add_window)
    department_entry.grid(row=5, column=1, padx=(30,10), pady=10, sticky=W)

    marks_label = Label(add_window, text="Marks:")
    marks_label.grid(row=6, column=0, padx=(30,10), pady=10, sticky=W)

    marks_entry = Entry(add_window)
    marks_entry.grid(row=6, column=1, padx=(30,10), pady=10, sticky=W)

    add_button = Button(add_window, text="Add Student")
    add_button.grid(row=7, column=0, columnspan=2, pady=10)

# Update function
def updateWindow(window):
    update_window = Toplevel(window)
    update_window.geometry('600x400')
    update_window.title("Update Student")

    # Headings
    heading_label = Label(update_window, text="Student Management System", font=("Helvetica", 16, "bold"))
    heading_label.grid(row=0, column=2, padx=(0,10), pady=10)

    sub_heading_label = Label(update_window, text="Update Student Details", font=("Helvetica", 12))
    sub_heading_label.grid(row=1, column=2, padx=(0,10), pady=10)

    #entries
    roll_label = Label(update_window, text="Roll Number:")
    roll_label.grid(row=2, column=1, padx=10, pady=10, sticky=W)

    roll_entry = Entry(update_window)
    roll_entry.grid(row=2, column=2, padx=10, pady=10, sticky=W)
