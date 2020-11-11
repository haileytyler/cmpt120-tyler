# Hailey Tyler
# Lab on Data Validation
# 3-7-19

# 1
def main():
    # Get user's first and last name
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # Create a username using the first and last name
    uname = first + "." + last

    # ask the user to create a new password
    passwd = input("Create a new password: ")

    # make sure the password has at least 8 characters
    while len(passwd)<8:
        print("Fool of a Took! That password is feeble!")
        passwd = (input("Create a new password: "))
    print("The force is strong in this one...")
    print("Account configured. Your new email address is: ", uname + "@marist.edu")
main()

# 2
# .isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company10"
x = txt.isalpha()
print(x, "\n")

# .isdigit()
txt = "50800"
x = txt.isdigit()
print(x)

a = "\u0030" # unicode for 0
b = "\u00B2" # unicode for ^2
print(a.isdigit())
print(b.isdigit(), "\n")

# .isalum()
txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x, "\n")

# .isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper(), "\n")

# .islower()
txt = "hello world!"
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

# 3
def hasUpper(pw):
    for i in range(len(pw)):
        if pw[i].isupper():
            return True
    return False

def hasNonAlphaNum(pw):
    for i in range(len(pw)):
        if not pw[i].isalnum():
            return True
    return False

def main():
    # Get user's first and last name
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # Create a username using the first and last name
    uname = first + "." + last

    # Testing the conditions
    while True:
        passwd = input("Create a new password: ")
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            print("Password must be at least 8 characters.")
        elif not passwd[0].isalpha():
            print("Your password must start with a letter.")
        elif not hasUpper(passwd):
            print("Password must contain at least one capital letter.")
        elif hasNonAlphaNum(passwd):
            print("Your password must only contain letters and numbers.")
        else:
            break

    print("The force is strong in this one...")
    print("Account configured. Your new email address is: ", uname + "@marist.edu")

main()
