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
    sub_heading_label.grid(row=1, column=1, pady=10)

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

    def showDetails():
        frame =  c.CTkFrame(update_window)
        details = utilities.fetchDetails(roll_entry.get())
        if(details == False):
            pass
        else:
            update_window.geometry('600x700')
            frame.grid(row=5, column=0, columnspan = 3, sticky='nsew')
            frame.columnconfigure((0, 1), weight=1, uniform="equal")
            frame.columnconfigure(2, weight=2, uniform="equal")

            details_heading_label = c.CTkLabel(frame, text="Student Details:", font=("Ariel",16 , "bold"))
            details_heading_label.grid(row=4, column=1, pady=10)

            roll_no_label = c.CTkLabel(frame, text="Roll No: ", font=("Ariel",14))
            roll_no_label.grid(row=5, column=1, pady=10, sticky=W, padx=20)
            roll_no = c.CTkLabel(frame, text=details[0], font=("Ariel",14))
            roll_no.grid(row=5, column=2, pady=10,  sticky=W, padx=20)

            f_name_label = c.CTkLabel(frame, text="First Name: ", font=("Ariel",14))
            f_name_label.grid(row=6, column=1, pady=10, sticky=W, padx=20)
            f_name = c.CTkLabel(frame, text=details[1], font=("Ariel",14))
            f_name.grid(row=6, column=2, pady=10, sticky=W, padx=20)

            l_name_label = c.CTkLabel(frame, text="Last Name: ", font=("Ariel",14))
            l_name_label.grid(row=7, column=1, pady=10, sticky=W, padx=20)
            l_name = c.CTkLabel(frame, text=details[2], font=("Ariel",14))
            l_name.grid(row=7, column=2, pady=10, sticky=W, padx=20)

            course_label = c.CTkLabel(frame, text="Course: ", font=("Ariel",14))
            course_label.grid(row=8, column=1, pady=10, sticky=W, padx=20)
            course = c.CTkLabel(frame, text=details[3], font=("Ariel",14))
            course.grid(row=8, column=2, pady=10, sticky=W, padx=20)
            
            cgpa_label = c.CTkLabel(frame, text="CGPA: ", font=("Ariel",14))
            cgpa_label.grid(row=9, column=1, pady=10, sticky=W, padx=20)
            cgpa = c.CTkLabel(frame, text=details[4], font=("Ariel",14))
            cgpa.grid(row=9, column=2, pady=10, sticky=W, padx=20)

            innerframe = c.CTkFrame(frame)
            innerframe.grid(row=10, column=0, columnspan = 3, sticky='nsew')
            innerframe.columnconfigure((0, 1, 2), weight=1, uniform="equal")

            update_button1 = c.CTkButton(innerframe, text="Update Name", font=("Helvetica", 16), command=lambda : updateNameWindow(details))
            update_button1.grid(row=10, column=0, pady=10, padx=10, sticky='nsew')
            update_button2 = c.CTkButton(innerframe, text="Update Course", font=("Helvetica", 16), command=lambda : updateCourseWindow(details))
            update_button2.grid(row=10, column=1, pady=10, padx=10, sticky='nsew')
            update_button3 = c.CTkButton(innerframe, text="Update CGPA", font=("Helvetica", 16), command=lambda : updateCGPAWindow(details))
            update_button3.grid(row=10, column=2, pady=10, padx=10, sticky='nsew')

        def updateNameWindow(details):
            update_name_window = c.CTkToplevel(update_window)
            update_name_window.geometry('400x300')
            update_name_window.title("Update Name")

            heading_label = c.CTkLabel(update_name_window, text="Update Name", font=("Ariel",20 , "bold"))
            heading_label.grid(row=0, column=0,columnspan=2, pady=10)

            prev_name_label = c.CTkLabel(update_name_window, text=f"Current Name: {details[1]} {details[2]}", font=("Helvetica", 13), text_color='#ABB2B9')
            prev_name_label.grid(row=1, column=0, pady=3, padx=10)

            first_name_label = c.CTkLabel(update_name_window, text="First Name:", font=("Helvetica", 16))
            first_name_label.grid(row=2, column=0, padx=(30,10), pady=10, sticky=W)

            first_name_entry = c.CTkEntry(update_name_window)
            first_name_entry.grid(row=2, column=1, padx=(30,10), pady=10, sticky=W)

            last_name_label = c.CTkLabel(update_name_window, text="Last Name:", font=("Helvetica", 16))
            last_name_label.grid(row=3, column=0, padx=(30,10), pady=10, sticky=W)

            last_name_entry = c.CTkEntry(update_name_window)
            last_name_entry.grid(row=3, column=1, padx=(30,10), pady=10, sticky=W)

            update_button = c.CTkButton(update_name_window, text="Update Detalis", font=("Helvetica", 16), command= lambda: utilities.updateName(details, first_name_entry, last_name_entry))
            update_button.grid(row=4, column=0,columnspan=3, pady=10)

        def updateCourseWindow(details):
            update_course_window = c.CTkToplevel(update_window)
            update_course_window.geometry('300x200')
            update_course_window.title("Update Course")

            heading_label = c.CTkLabel(update_course_window, text="Update Course", font=("Ariel",20 , "bold"))
            heading_label.grid(row=0, column=0,columnspan=3, pady=10)

            prev_course_label = c.CTkLabel(update_course_window, text=f"Course: {details[3]}", font=("Helvetica", 13), text_color='#ABB2B9')
            prev_course_label.grid(row=1, column=0, pady=3, padx=10)

            course_label = c.CTkLabel(update_course_window, text="Course:", font=("Helvetica", 16))
            course_label.grid(row=2, column=0, padx=(30,10), pady=10, sticky=W)

            courses = backend.getCourses()

            course_entry = c.CTkOptionMenu(update_course_window, fg_color="gray13", button_color="gray10")
            course_entry.grid(row=2, column=1, padx=(30,10), pady=10, sticky=W)
            course_entry.configure(values=courses)
            course_entry.set(details[3])

            update_button = c.CTkButton(update_course_window, text="Update Detalis", font=("Helvetica", 16), command=lambda : utilities.updateCourse(details, course_entry))
            update_button.grid(row=3, column=0,columnspan=3, pady=10)

        def updateCGPAWindow(details):
            update_cgpa_window = c.CTkToplevel(update_window)
            update_cgpa_window.geometry('400x300')
            update_cgpa_window.title("Update Name")

            heading_label = c.CTkLabel(update_cgpa_window, text="Update CGPA", font=("Ariel",20 , "bold"))
            heading_label.grid(row=0, column=0, pady=10, columnspan=3)

            prev_cgpa_label = c.CTkLabel(update_cgpa_window, text=f"CGPA: {details[4]}", font=("Helvetica", 13), text_color='#ABB2B9')
            prev_cgpa_label.grid(row=1, column=0, pady=3, padx=10)

            cgpa_label = c.CTkLabel(update_cgpa_window, text="CGPA:", font=("Helvetica", 16))
            cgpa_label.grid(row=2, column=0, padx=(30,10), pady=10, sticky=W)

            cgpa_entry = c.CTkEntry(update_cgpa_window)
            cgpa_entry.grid(row=2, column=1, padx=(30,10), pady=10, sticky=W)

            update_button = c.CTkButton(update_cgpa_window, text="Update Detalis", font=("Helvetica", 16), command=lambda : utilities.updateCGPA(details, cgpa_entry))
            update_button.grid(row=3, column=0,pady=10, columnspan=3)


    update_window = c.CTkToplevel(window)
    update_window.geometry('600x400')
    update_window.title("Update Details")
    update_window.columnconfigure((0, 1, 2), weight=1, uniform="equal")
    frame =  c.CTkFrame(update_window)
    # Headings
    heading_label = c.CTkLabel(update_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=0,columnspan=3, pady=10) 

    sub_heading_label = c.CTkLabel(update_window, text="Update Student Details", font=("Helvetica", 16))
    sub_heading_label.grid(row=1, column=0, columnspan=3, pady=10)

    #entries

    roll_label = c.CTkLabel(update_window, text="Roll No:", font=("Helvetica", 16))
    roll_label.grid(row=2, column=0,  pady=10, padx=10,sticky=E)

    roll_entry = c.CTkEntry(update_window)
    roll_entry.grid(row=2, column=1,columnspan=3,  pady=10, sticky=W)

    check_button = c.CTkButton(update_window, text="Check Detalis", font=("Helvetica", 16), command=lambda : showDetails())
    check_button.grid(row=3, column=1, pady=10)
