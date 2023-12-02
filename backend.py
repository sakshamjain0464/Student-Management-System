import mysql.connector as db

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
    print("Db connection error")

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
    
def getCourses():
    cursor.execute("select course_id from courses")
    courses = cursor.fetchall()
    courses_list = []
    for course in courses:
        courses_list.append(course[0])
    return courses_list
    
    
def getStudents():
    cursor.execute("select count(*) from student_details")
    global students
    students = cursor.fetchall()[0][0]
    print(students)

getStudents()

def addStudentToDb(roll_no, f_name, l_name, course, cgpa):
    try:
        query = "INSERT INTO STUDENT_DETAILS VALUES(%s,%s,%s,%s, %s)"
        cursor.execute(query,(roll_no, f_name, l_name,course,cgpa))
        if(cursor.rowcount == 1):
            connection.commit()
            getStudents()
            return True
        else:
            connection.rollback()
            return False
    except:
        return "Error"
    
def fetchDetailsFromDb(roll):
    try:
        cursor.execute(f"select * from student_details where roll_no = '{roll}'")
        details = cursor.fetchall()
        if(details == []):
            return False
        else:
            return details[0]
    except:
        return "error"
    
def updateNameToDb(roll, f_name, l_name):
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
    try:
        cursor.execute(f"DELETE FROM STUDENT_DETAILS WHERE ROLL_NO = '{roll}'")
        if(cursor.rowcount ==1):
            connection.commit()
            return True
        else:
            return False
    except:
        return 'error'
  