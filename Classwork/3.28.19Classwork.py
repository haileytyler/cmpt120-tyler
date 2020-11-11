# Lab on Functions
# Author: Hailey Tyler
# Created: 3-28-19

# a)
def main():
    # Get the user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # Create a username using the first and last name
    uname = first + "." + last

    # ask the user to create a new password
    passwd = input("Create a new password: ")

    # make sure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Account configured.  Your new email address is: ", uname + "@marist.edu")

main()

# b)
def get_first_and_last_names():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first, last

def create_username(name_list):
    uname = name_list[0] + "." + name_list[1]
    return uname

def create_password():
    passwd = input("Create a new password: ")

    # make sure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    print("The force is strong in this one...")
    print("Your password has been accepted.")
    return passwd

def main():
    # Get user's first and last names
    first_last_name_list = get_first_and_last_names()

    # Create a username using the first and last names
    username = create_username(first_last_name_list)

    # ask the user to create a new password
    password = create_password()

    print("Account configured.  Your new email address is: ", username + "@marist.edu")

main()

# c)
def get_first_and_last_names():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first.lower(), last.lower()


def create_username(name_list):
    uname = name_list[0] + "." + name_list[1]
    return uname


def create_password():
    passwd = input("Create a new password: ")

    # make sure the password has at least 8 characters
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    # make sure the password has at least 1 uppercase character
    while passwd.lower() == passwd:
        print("The password must contain at least one upper-case character")
        passwd = input("Create a new password: ")

    print("The force is strong in this one...")
    print("Your password has been accepted.")
    return passwd


def main():
    # Get user's first and last names
    first_last_name_list = get_first_and_last_names()

    # Create a username using the first and last names
    username = create_username(first_last_name_list)

    # ask the user to create a new password
    password = create_password()

    print("Account configured.  Your new email address is: ", username + "@marist.edu")

main()

# d)
def get_first_and_last_names():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return first.lower(), last.lower()


def create_username(name_list):
    uname = name_list[0] + "." + name_list[1]
    return uname

def hasUpper(pw):
    for i in range(len(pw)):
        if pw[i].isupper():
            return True
    return False

def hasNum(pw):
    for i in range(len(pw)):
        if pw[i].isnumeric():
            return True
    return False

def create_password():
    # make sure the password satisfies the conditions
    while True:
        passwd = input("Create a new password: ")
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
        elif not hasUpper(passwd):
            print("Password must contain at least one capital letter.")
        elif not hasNum(passwd):
            print("The password must contain at least one number.")
        else:
            break
    print("The force is strong in this one...")
    print("Your password has been accepted.")
    return passwd


def main():
    # Get user's first and last names
    first_last_name_list = get_first_and_last_names()

    # Create a username using the first and last names
    username = create_username(first_last_name_list)

    # ask the user to create a new password
    password = create_password()

    print("Account configured.  Your new email address is: ", username + "@marist.edu")


main()
