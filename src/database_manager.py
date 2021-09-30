import mysql.connector as mysqlcon 
from pwd_generator import get_hashed_password, check_password
from utilities import welcome, clear
import time

# replace user and password with your MySQL credentials
mycon = mysqlcon.connect(
    host="localhost",
    user="root",
    password="notarealpassword",
    autocommit=True)
mycur = mycon.cursor()

def database_init():
    # manages database creation and maintainence

    dbCreateQuery = "CREATE DATABASE IF NOT EXISTS PWDmanager;"
    mycur.execute(dbCreateQuery)
    mycur.execute("USE PWDmanager;")

    userTableCreateQuery = "CREATE TABLE IF NOT EXISTS Users (userID int NOT NULL AUTO_INCREMENT, username varchar(255), emailID varchar(255),password varchar(255), PRIMARY KEY (userID))"
    mycur.execute(userTableCreateQuery)

def create_account(numOfTries=0):
    # creates a new account

    clear()
    welcome()
    if numOfTries>2:
        return False

    usernameInput = input("\n// choose a username: ")

    checkUsernameQuery = f"SELECT EXISTS(SELECT * from users where username='{usernameInput}')"
    mycur.execute(checkUsernameQuery)
    checkUserName = mycur.fetchall()[0][0]

    if checkUserName == 1:
        numOfTries += 1
        print("// username already exists")
        time.sleep(1)
        create_account(numOfTries)
    
    else:
        passwordInput = input("// choose a master password: ")
        passwordInput = get_hashed_password(passwordInput)
        emailInput = input("// enter a backup email: ")

        newUserTableCreateQuery = f"CREATE TABLE IF NOT EXISTS {usernameInput+'_data'} (service varchar(255), username varchar(255), email varchar(255), password varchar(255))"
        mycur.execute(newUserTableCreateQuery)

        usersTableUpdateQuery = f"INSERT INTO users (username, emailID, password) VALUES('{usernameInput}', '{emailInput}', '{passwordInput}');"
        mycur.execute(usersTableUpdateQuery)


def login(numOfTries=0):
    # logins an existing user and starts a login session

    clear()
    welcome()
    if numOfTries>2:
        return False

    username = input("\n// username: ")
    
    checkUsernameQuery = f"SELECT EXISTS(SELECT * from users where username='{username}')"
    mycur.execute(checkUsernameQuery)
    checkUserName = mycur.fetchall()[0][0]

    if checkUserName != 1:
        numOfTries += 1
        print("// incorrect username")
        time.sleep(1)
        login(numOfTries)

    else:

        password = input("// password: ")

        checkPasswordQuery = f"SELECT password from users where username='{username}'"
        mycur.execute(checkPasswordQuery)
        checkPassword = mycur.fetchall()[0][0]

        if not check_password(password, checkPassword):
            numOfTries += 1
            print("// incorrect password")
            time.sleep(1)
            login(numOfTries)
            
        else:
            return [True, username]
