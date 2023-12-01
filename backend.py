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
    

