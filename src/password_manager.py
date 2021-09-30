import mysql.connector as mysqlcon
from pwd_generator import get_hashed_password, check_password
from utilities import clear, loading, welcome
import time
import prettytable

# replace user and password with your MySQL credentials
mycon = mysqlcon.connect(
    host="localhost",
    user="root",
    password="notarealpassword",
    database="pwdmanager",
    autocommit=True)
mycur = mycon.cursor()

def add_service(user):
    # adding a new service to a user's database

    try:
        clear() 
        welcome()
        print("// adding new password\n")
        service = input("// service name: ")
        username = input(f"// username registered in {service}: ")
        email = input(f"// email registered in {service}: ")
        password = input(f"// enter {service}'s password: ")

        userDataTableUpdateQuery = f"INSERT INTO {user+'_data'} VALUES ('{service}', '{username}', '{email}', '{password}')"
        mycur.execute(userDataTableUpdateQuery)

    except Exception as e:
        print(e)
        print("\n// some error occured")
        time.sleep(1)

    else:
        print(f"// adding {service} to database")
        loading()
        print(f"\n// added {service}")
        time.sleep(2)

def get_service(user):
    # gets the save password of a service from user's database
    
    try:
        clear()
        welcome()
        print("// fetching saved password\n")
        service = input("// service name: ")
        username = input(f"// username registered in {service}: ")
        userDataFetchQuery = f"SELECT password FROM {user+'_data'} WHERE username='{username}' AND service='{service}'"
        mycur.execute(userDataFetchQuery)
        returnData = mycur.fetchall()
        password = returnData[0][0]
        print(f"// {service}'s pass: {password}")
        input("\n// [enter] to go back ")


    except Exception:
        print("\n// some error occured")
        time.sleep(1)



def del_service(user):
    # deletes a service from the user's database

    try:
        clear()
        welcome()
        print("// deleting saved password\n")
        service = input("// service name: ")
        username = input(f"// username registered in {service}: ")
        userDataDelQuery = f"DELETE FROM {user+'_data'} WHERE username='{username}' AND service='{service}'"
        mycur.execute(userDataDelQuery)

    except Exception as e:
        print(e)
        print("\n// some error occured")
        time.sleep(1)
    
    else:
        print(f"// deleting {service}'s password")
        loading()
        print(f"\n// {service}'s password deleted")
        time.sleep(2)

def edit_service(user):
    # edit saved password of service in user's database

    try:
        clear()
        welcome()
        print("// editing saved password\n")
        service = input("// service name: ")
        username = input(f"// username registered in {service}: ")
        password = input(f"// new password: ")
        userDataDelQuery = f"UPDATE {user+'_data'} SET password='{password}' WHERE username='{username}' AND service='{service}'"
        mycur.execute(userDataDelQuery)

    except Exception as e:
        print(e)
        print("\n// some error occured")
    
    else:
        print(f"\n// {service}'s password edited")
        time.sleep(2)

def getall_service(user):
    # gets all saved passwords from user's database and prints it in a table

    try:
        clear()
        welcome()
        print("\n// saved passwords")
        userDataFetchAllQuery = f"SELECT * FROM {user+'_data'}"
        mycur.execute(userDataFetchAllQuery)
        data = mycur.fetchall()

        x = prettytable.PrettyTable(["Service", "Username", "Email", "Password"])
        for record in data:
            x.add_row(list(record))
        print(x)

        input("\n// [enter] to go back ")

    except Exception as e:
        print(e)
        print("\n // some error occured")
        input()
        time.sleep(1)