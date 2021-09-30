# Passkeep - Password Manager
--- 

## Summary
A Command Line Interface (CLI) based password manager to store all your passwords, built using python-3 and mysql. Access all your passwords just by remembering one master password. The Passwords are encrypted using the SHA1 encryption scheme.

![img.1: welcome screen](https://raw.githubusercontent.com/siphyshu/passkeep-password-manager/master/imgs/passkeep_welcome.png)

<br>

## Setup and Installation
###### 1. Making sure MySQL is running
Install MySQL in your system from [here](https://dev.mysql.com/downloads/) if it's not already installed.
Open MySQL Command Line Client and verify the user credentials by logging in.
###### 2. Changing MySQL Login Credentials
Open database_manager.py and password_manager.py in any code editor,  
then change login credentials for MySQL in the code present in the first few lines.

![img.2: sql login credentials](https://raw.githubusercontent.com/siphyshu/passkeep-password-manager/master/imgs/passkeep_sql_login_code.png)

###### 3. Installing Python Libraries
Open cmd or terminal and run the following commands:

`python -m pip install prettytable` to install prettytable library. 
Used to output the database query results in a nicely formatted table.

`python -m pip install mysql-connector-python` install MySQL-Python connector.

<br>

## Running the Program
Start main.py in python shell mode or run it directly from the command line.<br>
Create an account by entering "C" then follow the instructions afterwards.

![img.3: user menu](https://raw.githubusercontent.com/siphyshu/passkeep-password-manager/master/imgs/passkeep_menu.png)

<br>

## Side Quest
The program is vulnerable to SQLi, see if you can manage to do the following tasks:
- [ ]  Drop your own user_data table
- [ ]  Access the "users" table
- [ ]  See passwords of any user
- [ ]  Edit or Delete any user's table
- [ ]  Drop the "pwdmanager" database

> It's not a bug, It's a feature! 🐛
