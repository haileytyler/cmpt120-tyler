# Hailey Tyler
# Lab 4
# 2/21/19

def main():
    n = int(input("Number? "))
    if n < 0:
        print("The absolute value of", n, "is", -n)
    else:
        print("The absolute value of", n, "is", n)
main()
main()

def main():
    a = 0
    while a < 10:
        a = a + 1
        if a > 5:
            print(a, ">", 5)
        elif a <= 3:
            print(a, "<=", 3)
        else:
            print("Neither test was true")
main()

# This Program Demonstrates the use of the == operator
# using numbers
print(5 == 6)
# Using variables
x = 5
y = 8
print(x == y)

# Plays the guessing game higher or lower

# This should actually be something that is semi random like the
# last digits of the time or something else, but that will have to
# wait till a later lab.

number = 7
guess = -1

print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))

    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")

# Asks for a number.
# Prints if it is even or odd

def number():
    number = float(input("Tell me a number: "))
    if number % 2 == 0:
        print(int(number), "is even.")
    elif number % 2 == 1:
        print(int(number), "is odd.")
    else:
        print(number, "is very strange.")
number()
number()
number()

# keeps asking for numbers until 0 is entered.
# Prints the average value.

count = 0
sum = 0.0
number = 1  # set to something that will not exit the while loop immediately.

print("Enter 0 to exit the loop")

while number != 0:
    number = float(input("Enter a number: "))
    if number != 0:
        count = count + 1
        sum = sum + number
    if number == 0:
        print("The average was:", sum / count)


# Programming Exercise #1 pg. 238

def hours():
    print("This program calculates the total wages for the week given the number of hours worked and the hourly rate.")
    hours = float(input("What is the total number of hours worked?"))
    rate = round(float(input("What is the hourly rate?")), 2)
    if hours <= 40:
        print("The total wages for the week is: $", (rate * hours))
    else:
        OT = hours - 40
        print("The total wages for the week is: $", (40 * rate) + (OT * rate))
    print("Press <Enter> to exit the program.")
hours()
hours()
hours()