import mysql.connector as db

try:
    connection = db.connect(
        host="localhost",
        user="root",
        password="root123",
        database="Student_Management_System",
        port=3309
    )
    connected = True
except:
    connected = False
    print("Db connection error")

cursor = connection.cursor()
    
# Login authentication from database
def authenticate(username,pwd):
    '''Function for login authentication from database'''
    try:
        cursor.execute("select * from users")
        users_data = cursor.fetchall()
        for user in users_daa:
            if(user[0] == username and user[1] == pwd):
                print(user[0], user[1])
                return True
            else:
                return False
    except:
        return "Error"

authenticate("jkhfk","kjdhfk")