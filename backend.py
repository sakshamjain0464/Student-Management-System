import mysql.connector as db
def authenticate(user,pwd):
    if(user == 'saksham' and pwd == 'pwd'):
        return True
    else:
        return False