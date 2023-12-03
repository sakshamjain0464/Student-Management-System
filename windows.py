'''Module for creating all the windows'''

from tkinter import *                     #for GUI
import CTkMessagebox as message           #for displaying prompt messages
import customtkinter as c                 #for modern GUI
from PIL import Image                     #for image opening
from PIL import ImageTk                   #for logo
import utilities                          #for proocessing utlities 'Self Created'



# Create User Dashboard
def createUser(login_window):
    '''For user creation window'''
    # user widnow initialization
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

    #Buttons 
    create_button = c.CTkButton(create_window, text="Create User", command= lambda : utilities.createUser(create_window, user_entry, pwd_entry, conf_pwd_entry))
    create_button.grid(row=5, column=1, pady=(10,5))

    login_button = c.CTkButton(create_window, text="Login", command=lambda : create_window.destroy())
    login_button.grid(row=6, column=1)

# Main Dashboard student_dashboard
def studentDashboard():
    '''For Student Dashboard Creation'''
    # student_dashboard Creation
    student_dashboard =c.CTk()
    student_dashboard.title("Welcome to Student Management Portal")
    student_dashboard.geometry("600x530")

    #For Logo
    try:
        logo_img = Image.open("logo.png")
        resize_img = logo_img.resize((100,100))
        logo = ImageTk.PhotoImage(resize_img)
        #Image for logo
        logo_label = c.CTkLabel(student_dashboard, text='', image=logo).pack(pady=(50,0))
    except:
        print("Logo loading error")

    # Heading c.CTkLabel
    heading_label = c.CTkLabel(student_dashboard, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.pack(pady=10)

    sub_heading_label = c.CTkLabel(student_dashboard, text="Student Dahboard", font=("Helvetica", 16))
    sub_heading_label.pack(pady=10)

    # Buttons
    addBtn = c.CTkButton(student_dashboard, text="Add Student Details", command= lambda : addWindow(student_dashboard), font=("Ariel",16 , "bold"), border_spacing=4)
    addBtn.pack(pady=10)

    updateBtn = c.CTkButton(student_dashboard, text="Update Student Details", command= lambda : updateWindow(student_dashboard), font=("Ariel",16 , "bold"), border_spacing=4)
    updateBtn.pack(pady=10)

    viewBtn = c.CTkButton(student_dashboard, text="View Student Details", font=("Ariel",16 , "bold"), border_spacing=4, command= lambda : viewWindow(student_dashboard))
    viewBtn.pack(pady=10)

    deleteBtn = c.CTkButton(student_dashboard, text="Delete Student Details", font=("Ariel",16 , "bold"), border_spacing=4, command= lambda : deleteWindow(student_dashboard))
    deleteBtn.pack(pady=10)

    courseBtn = c.CTkButton(student_dashboard, text="Open Course Dashboard", font=("Ariel",16 , "bold"), border_spacing=4, command= lambda : courseDashboard(student_dashboard))
    courseBtn.pack(pady=10)

    #footer
    footer_label = c.CTkLabel(student_dashboard, text="Created By - Saksham Jain and Ritika Nainani", font=("Helvetica", 12))
    footer_label.pack(pady=10, side='bottom')

    student_dashboard.mainloop()
    utilities.close()



def addWindow(student_dashboard):
    '''For add student window'''
    add_window = c.CTkToplevel(student_dashboard)
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

    courses = utilities.getCourses()       #to get list of all courses

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
def updateWindow(student_dashboard):
    '''For update details window'''
    def showDetails():
        '''Function to show details of student'''
        #frame to contain student details
        frame =  c.CTkFrame(update_window)
        details = utilities.fetchStudentDetails(roll_entry.get())
        if(details == False):
            '''If no details are found'''
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
            
            # Update Buttons
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
            '''To update name of student'''
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
            '''to update course of student'''
            update_course_window = c.CTkToplevel(update_window)
            update_course_window.geometry('300x200')
            update_course_window.title("Update Course")

            heading_label = c.CTkLabel(update_course_window, text="Update Course", font=("Ariel",20 , "bold"))
            heading_label.grid(row=0, column=0,columnspan=3, pady=10)

            prev_course_label = c.CTkLabel(update_course_window, text=f"Course: {details[3]}", font=("Helvetica", 13), text_color='#ABB2B9')
            prev_course_label.grid(row=1, column=0, pady=3, padx=10)

            course_label = c.CTkLabel(update_course_window, text="Course:", font=("Helvetica", 16))
            course_label.grid(row=2, column=0, padx=(30,10), pady=10, sticky=W)

            courses = utilities.getCourses()

            course_entry = c.CTkOptionMenu(update_course_window, fg_color="gray13", button_color="gray10")
            course_entry.grid(row=2, column=1, padx=(30,10), pady=10, sticky=W)
            course_entry.configure(values=courses)
            course_entry.set(details[3])

            update_button = c.CTkButton(update_course_window, text="Update Detalis", font=("Helvetica", 16), command=lambda : utilities.updateCourse(details, course_entry))
            update_button.grid(row=3, column=0,columnspan=3, pady=10)

        def updateCGPAWindow(details):
            '''To update CGPA of student'''
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


    # Update window initialization
    update_window = c.CTkToplevel(student_dashboard)
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

def viewWindow(student_dashboard):
    '''Function to view details of student'''
    def showDetails():
        frame =  c.CTkFrame(view_window)
        details = utilities.fetchStudentDetails(roll_entry.get())
        if(details == False):
            pass
        else:
            view_window.geometry('600x700')
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

    
    #view window initialization
    view_window = c.CTkToplevel(student_dashboard)
    view_window.geometry('600x400')
    view_window.title("View Details")
    view_window.columnconfigure((0, 1, 2), weight=1, uniform="equal")

    frame =  c.CTkFrame(view_window)
    # Headings
    heading_label = c.CTkLabel(view_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=0,columnspan=3, pady=10) 

    sub_heading_label = c.CTkLabel(view_window, text="View Student Details", font=("Helvetica", 16))
    sub_heading_label.grid(row=1, column=0, columnspan=3, pady=10)

    #entries
    roll_label = c.CTkLabel(view_window, text="Roll No:", font=("Helvetica", 16))
    roll_label.grid(row=2, column=0,  pady=10, padx=10,sticky=E)

    roll_entry = c.CTkEntry(view_window)
    roll_entry.grid(row=2, column=1,columnspan=3,  pady=10, sticky=W)

    check_button = c.CTkButton(view_window, text="Check Detalis", font=("Helvetica", 16), command=lambda : showDetails())
    check_button.grid(row=3, column=1, pady=10)

def deleteWindow(student_dashboard):
    '''Function to delete details of student'''
    def showDetails():
        frame =  c.CTkFrame(delete_window)
        details = utilities.fetchStudentDetails(roll_entry.get())
        if(details == False):
            pass
        else:
            delete_window.geometry('600x700')
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

            delete_button = c.CTkButton(innerframe, text="Delete", font=("Helvetica", 16), command = lambda : utilities.deleteStudent(details))
            delete_button.grid(row=10, column=0, pady=10,columnspan=3, padx=10, sticky='nsew')

    # delete window initialization
    delete_window = c.CTkToplevel(student_dashboard)
    delete_window.geometry('600x400')
    delete_window.title("Delete Student Details")
    delete_window.columnconfigure((0, 1, 2), weight=1, uniform="equal")
    frame =  c.CTkFrame(delete_window)

    # Headings
    heading_label = c.CTkLabel(delete_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=0,columnspan=3, pady=10) 

    sub_heading_label = c.CTkLabel(delete_window, text="Update Student Details", font=("Helvetica", 16))
    sub_heading_label.grid(row=1, column=0, columnspan=3, pady=10)

    #entries
    roll_label = c.CTkLabel(delete_window, text="Roll No:", font=("Helvetica", 16))
    roll_label.grid(row=2, column=0,  pady=10, padx=10,sticky=E)

    roll_entry = c.CTkEntry(delete_window)
    roll_entry.grid(row=2, column=1,columnspan=3,  pady=10, sticky=W)

    check_button = c.CTkButton(delete_window, text="Check Detalis", font=("Helvetica", 16), command=lambda : showDetails())
    check_button.grid(row=3, column=1, pady=10)

def courseDashboard(existing_window):
    '''Function to create course dashboard'''
    course_dashboard = c.CTkToplevel(existing_window)
    course_dashboard.title("Welcome to Student Management Portal")
    course_dashboard.geometry("600x330")

    # Heading
    heading_label = c.CTkLabel(course_dashboard, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.pack(pady=10)

    sub_heading_label = c.CTkLabel(course_dashboard, text="Course Dahboard", font=("Helvetica", 16))
    sub_heading_label.pack(pady=10)

    # Buttons
    addBtn = c.CTkButton(course_dashboard, text="Add Course", command= lambda : addCourseWindow(course_dashboard), font=("Ariel",16 , "bold"), border_spacing=4)
    addBtn.pack(pady=10)

    updateBtn = c.CTkButton(course_dashboard, text="Update Course", command= lambda : updateCourseWindow(course_dashboard), font=("Ariel",16 , "bold"), border_spacing=4)
    updateBtn.pack(pady=10)

    reportBtn = c.CTkButton(course_dashboard, text="Get Course Report", font=("Ariel",16 , "bold"), border_spacing=4, command= lambda : utilities.getCourseReport())
    reportBtn.pack(pady=10)

    studentBtn = c.CTkButton(course_dashboard, text="Go To Student Dashboard", command= lambda : course_dashboard.destroy(), font=("Ariel",16 , "bold"), border_spacing=4)
    studentBtn.pack(pady=10)

    # Footer
    footer_label = c.CTkLabel(course_dashboard, text="Created By - Saksham Jain and Ritika Nainani", font=("Helvetica", 12))
    footer_label.pack(pady=10, side='bottom')
    
    
def addCourseWindow(course_dashboard):
    '''Function to add course'''
    add_course_window = c.CTkToplevel(course_dashboard)
    add_course_window.geometry('600x250')
    add_course_window.title("Add Course")

    # Headings
    heading_label = c.CTkLabel(add_course_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=1, pady=10)

    sub_heading_label = c.CTkLabel(add_course_window, text="Add Course", font=("Helvetica", 16))
    sub_heading_label.grid(row=1, column=1, pady=10)

    #entries
    courseid_label = c.CTkLabel(add_course_window, text="Course ID:", font=("Helvetica", 16))
    courseid_label.grid(row=3, column=0, padx=(30,10), pady=10, sticky=W)

    courseid_entry = c.CTkEntry(add_course_window)
    courseid_entry.grid(row=3, column=1, padx=(30,10), pady=10, sticky=W)

    course_name_label = c.CTkLabel(add_course_window, text="Course Name:", font=("Helvetica", 16))
    course_name_label.grid(row=4, column=0, padx=(30,10), pady=10, sticky=W)

    course_name_entry = c.CTkEntry(add_course_window)
    course_name_entry.grid(row=4, column=1, padx=(30,10), pady=10, sticky=W)

    add_button = c.CTkButton(add_course_window, text="Add Course", font=("Helvetica", 16), command=lambda : utilities.addCourse(courseid_entry, course_name_entry))
    add_button.grid(row=5, column=1, pady=10)

def updateCourseWindow(course_dashboard):
    '''Function to update course'''
    def showDetails():
        '''function to show course details'''
        frame =  c.CTkFrame(update_window)
        details = utilities.fetchCourseDetails(courseid_entry.get())
        if(details == False):
            pass
        else:
            update_window.geometry('600x500')
            frame.grid(row=5, column=0, columnspan = 3, sticky='nsew')
            frame.columnconfigure((0, 1), weight=1, uniform="equal")
            frame.columnconfigure(2, weight=2, uniform="equal")

            details_heading_label = c.CTkLabel(frame, text="Course Details:", font=("Ariel",16 , "bold"))
            details_heading_label.grid(row=4, column=1, pady=10)

            id_label = c.CTkLabel(frame, text="Course ID: ", font=("Ariel",14))
            id_label.grid(row=5, column=1, pady=10, sticky=W, padx=20)
            id = c.CTkLabel(frame, text=details[0], font=("Ariel",14))
            id.grid(row=5, column=2, pady=10,  sticky=W, padx=20)

            name_label = c.CTkLabel(frame, text="Course Name: ", font=("Ariel",14))
            name_label.grid(row=6, column=1, pady=10, sticky=W, padx=20)
            name = c.CTkLabel(frame, text=details[1], font=("Ariel",14))
            name.grid(row=6, column=2, pady=10, sticky=W, padx=20)

            innerframe = c.CTkFrame(frame)
            innerframe.grid(row=10, column=0, columnspan = 3, sticky='nsew')
            innerframe.columnconfigure((0, 1, 2), weight=1, uniform="equal")

            update_button = c.CTkButton(innerframe, text="Update", font=("Helvetica", 16), command=lambda : updateWindow(details))
            update_button.grid(row=10, column=0, columnspan=3, pady=10, padx=10, sticky='nsew')

        def updateWindow(details):
            '''To update course name window'''
            update_name_window = c.CTkToplevel(update_window)
            update_name_window.geometry('400x300')
            update_name_window.title("Update Course Name")

            heading_label = c.CTkLabel(update_name_window, text="Update Course Name", font=("Ariel",20 , "bold"))
            heading_label.grid(row=0, column=0,columnspan=2, pady=10)

            prev_name_label = c.CTkLabel(update_name_window, text=f"Current Name: {details[1]}", font=("Helvetica", 13), text_color='#ABB2B9')
            prev_name_label.grid(row=1, column=0, pady=3, padx=10)

            name_label = c.CTkLabel(update_name_window, text="Course Name:", font=("Helvetica", 16))
            name_label.grid(row=2, column=0, padx=(30,10), pady=10, sticky=W)

            name_entry = c.CTkEntry(update_name_window)
            name_entry.grid(row=2, column=1, pady=10, sticky=W)

            update_button = c.CTkButton(update_name_window, text="Update Detalis", font=("Helvetica", 16), command= lambda: utilities.updateCourseName(details, name_entry))
            update_button.grid(row=4, column=0,columnspan=3, pady=10)


    # Update window initialization
    update_window = c.CTkToplevel(course_dashboard)
    update_window.geometry('600x400')
    update_window.title("Update Details")
    update_window.columnconfigure((0, 1, 2), weight=1, uniform="equal")
    frame =  c.CTkFrame(update_window)

    # Headings
    heading_label = c.CTkLabel(update_window, text="Student Management System", font=("Ariel",20 , "bold"))
    heading_label.grid(row=0, column=0,columnspan=3, pady=10) 

    sub_heading_label = c.CTkLabel(update_window, text="Update Course Name", font=("Helvetica", 16))
    sub_heading_label.grid(row=1, column=0, columnspan=3, pady=10)

    #entries
    courseid_label = c.CTkLabel(update_window, text="Course ID:", font=("Helvetica", 16))
    courseid_label.grid(row=2, column=0,  pady=10, padx=10,sticky=E)

    courseid_entry = c.CTkEntry(update_window)
    courseid_entry.grid(row=2, column=1,columnspan=3,  pady=10, sticky=W)

    check_button = c.CTkButton(update_window, text="Check Detalis", font=("Helvetica", 16), command=lambda : showDetails())
    check_button.grid(row=3, column=1, pady=10)

'''All windows created, windows module ends here'''