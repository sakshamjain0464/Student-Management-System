import mysql.connector as db        #for database connection

# Connecting database
try:
    connection = db.connect(
        host="localhost",
        user="root",
        password="root123",
        database="Student_Management_System",
        port=3309
    )
    cursor = connection.cursor()
    connected = True
except:
    connected = False


# Login authentication from database
def authenticate(username,pwd):
    '''Function for login authentication from database'''
    try:
        cursor.execute("select * from users")
        users_data = cursor.fetchall()
        print(cursor.rowcount)
        for user in users_data:
            if(user[0] == username and user[1] == pwd):
                print(user[0], user[1])
                return True
        return False
    except:
        return "Error"

def createUserToDb(username,pwd):
    '''Function to add user to database'''
    try:
        cursor.execute(f"insert into users values('{username}', '{pwd}')")
        connection.commit()
        return True
    except:
        if(authenticate(username, pwd) == True):
            return "exists"
        return False
    
def getCoursesFromDb():
    '''Function for getting course codes from database, returns a list of course codes'''
    try:
        cursor.execute("select course_id from courses")
        courses = cursor.fetchall()
        courses_list = []
        for course in courses:
            courses_list.append(course[0])
        return courses_list
    except:
        return "error"
    
    
def getLastRollNumber():
    '''Function to get roll number of last added student, return the numerical part of last roll number'''
    try:
        cursor.execute("select roll_no from student_details")
        global last_roll
        students = cursor.fetchall()
        roll = []
        for roll_no in students:
            roll.append(int(roll_no[0].replace("S",'')))
        return max(roll)
    except:
        return 0
    
getLastRollNumber()
    
def fetchStudentDetailsFromDb(roll):
    '''Function to fetch sudent details from database, returns a tuple of student details'''
    try:
        cursor.execute(f"select * from student_details where roll_no = '{roll}'")
        details = cursor.fetchall()
        if(details == []):
            return False
        else:
            return details[0]
    except:
        return "error"
    

def fetchCourseDetailsFromDb(courseid):
    '''Function to fetch course details from database, returns a tuple of course details'''
    try:
        cursor.execute(f"select * from courses where course_id = '{courseid}'")
        details = cursor.fetchall()
        if(details == []):
            return False
        else:
            return details[0]
    except:
        return "error"
    

def addStudentToDb(roll_no, f_name, l_name, course, cgpa):
    '''Function to add new student to database'''
    try:
        query = "INSERT INTO STUDENT_DETAILS VALUES(%s,%s,%s,%s, %s)"
        cursor.execute(query,(roll_no, f_name, l_name,course,cgpa))
        if(cursor.rowcount == 1):
            connection.commit()
            return True
        else:
            connection.rollback()
            return False
    except:
        return "Error"
    
    
def updateNameToDb(roll, f_name, l_name):
    '''Function to add update student name to database'''
    try:
        cursor.execute(f"UPDATE STUDENT_DETAILS SET FIRST_NAME = '{f_name}', LAST_NAME = '{l_name}' WHERE ROLL_NO = '{roll}'")
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
    

    
def updateCourseToDb(roll, course):
    '''Function to add update student course to database'''
    try:
        cursor.execute(f"UPDATE STUDENT_DETAILS SET COURSE_ID = '{course}' WHERE ROLL_NO = '{roll}'")
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
    
    
def updateCGPAToDb(roll, cgpa):
    '''Function to add update student CGPA to database'''
    try:
        cursor.execute(f"UPDATE STUDENT_DETAILS SET CGPA = {cgpa} WHERE ROLL_NO = '{roll}'")
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
    

def deleteFromDb(roll):
    '''Function to add delete student from database'''
    try:
        cursor.execute(f"DELETE FROM STUDENT_DETAILS WHERE ROLL_NO = '{roll}'")
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
    

  
def addCourseToDb(id, name):
    '''Function to add new course to database'''
    try:
        query = "INSERT INTO Courses VALUES(%s,%s)"
        cursor.execute(query,(id, name))
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
    
def updateCourseNameToDb(id, name):
    '''Function to add update course name to database'''
    try:
        cursor.execute(f"UPDATE Courses SET Course_Name = '{name}' WHERE course_id = '{id}'")
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
    

    
def getCourseReportFromDb():
    '''Function to get details of course to put on course report from database, returns a list of details'''
    try:
        cursor.execute("select c.course_id, course_name, count(roll_no) from Student_details S inner join Courses C where c.Course_id = s.course_id group by c.course_id;")
        return cursor.fetchall()
    except:
        return "error"
    
