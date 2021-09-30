import time
import random
from utilities import clear, loading, welcome
from password_manager import add_service, get_service, del_service, edit_service, getall_service
from database_manager import create_account, login, database_init
from pwd_generator import get_hashed_password, check_password

def main():
    database_init() 
    while True:
        clear()
        welcome()
        ask_user = input(
            "\n// login(L) or create account(C): ").upper()

        if ask_user == 'C':
            time.sleep(0.2)
            create_account()
            clear()
            welcome()
            print("\n// creating new account")
            loading()
            print("\n // new account created")
            time.sleep(1)

        elif ask_user == 'L':
            time.sleep(0.1)
            
            # tries to login and assigns a login_status respectively
            login_attempt = login()
            try:
                login_status = login_attempt[0]
            except:
                login_status = False

            # starts a loging session if login succesful
            if login_status:
                clear()
                welcome()
                login_username = login_attempt[1] 
                print("\n// logging in")
                loading()
                print("\n// logged in")
                time.sleep(1)
                login_session(login_username)

            else:
                print("// login unsuccesful")
                time.sleep(1)
                main()

        elif ask_user == 'Q':
            print("\n// exiting...")
            loading()
            clear()
            time.sleep(0.2)
            exit()

        else:
            print('\n// enter a valid input')
            time.sleep(0.5)


def login_session(user):
    # runs infinitely until user logs out

    while True:
        clear()
        welcome()
        print("\n// choose one of the following: ")
        print("(1) add a new password\n(2) see a saved password\n(3) edit an existing password\n(4) delete an existing password\n(5) see all saved passwords\n(Q) log out and go back to main menu")
        ask_user = input("// enter: ")

        if ask_user=="1":
            add_service(user)

        elif ask_user=="2":
            get_service(user)

        elif ask_user=="3":
            edit_service(user)

        elif ask_user=="4":
            del_service(user)

        elif ask_user=="5":
            getall_service(user)

        elif ask_user in ["Q", 'q', 'quit', 'exit']:
            print("// logging out")
            loading()
            time.sleep(1)
            main()

        else:
            print("// please supply a valid input")

main()