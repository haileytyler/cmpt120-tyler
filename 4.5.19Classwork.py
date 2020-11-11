# Hailey Tyler
# Chapter 6 Assignment: Functions
# 4-5-19

password = ""
def createUserName():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    userid = first[0] + last
    return userid


def createPassword():
    password = input("Create a new password: ")
    return password


def checkFirstCharacter(pw):
    if pw[0].isalpha():
        return True
    else:
        return False


def checkRemainingChars(pw):
    for i in range((len(pw))-1):
        if not pw.isalnum():
            return False
    return True


def main():
    print("This program creates a userid based on your first and last name and allows you to input a password.")
    print("Your userid is: " + createUserName())
    # This will prompt the user to input their first and last name and then will create a userid and print it out.
    while True:
        # We will stay in the loop while checkFirstCharacter() and checkRemainingChars() are false (and therefore they
        # have a not in front of them).
        password = createPassword()
        # This will prompt the user to input a new password and will ask for another password each time
        # checkFirstCharacter() and/or checkRemainingChars() are false.
        if not checkFirstCharacter(password[0]):
            # checkFirstCharacter() receives the first character of the password and checks it to make sure it is
            # alphabetic.
            print("The first character must be alphabetic.")
        elif not checkRemainingChars(password[1:]):
            # checkRemainingChars() receives the second character up to the last character and checks that they are
            # alphanumeric.
            print("Your password must be alphabetic or numeric.")
        else:
            break
            # The loop will break when there is a good password.
    print("Password accepted.")
    input("Press <Enter> to exit the program.")


main()

