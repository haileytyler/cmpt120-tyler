# Hailey Tyler
# Chapter 8 Lab: Conditions and Loops
# 2/28/19

# Take user input
number = 2

# Condition of the while loop

while number < 5:
    print("Thank you")
    # Increment the value of the variable "number by 1"
    number = number + 1

# Take user input
number = 2

# Condition of the while loop
while number <5:
    # Find the mod of 2
    if number%2 == 0:
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")

    # Increment'number' by 1
    number = number + 1

def collatz(number):
    # Is the mod of 2 equal to 0?
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    # If the mod of 2 isn't equal to 0, print '3 * number +1'
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

# Ask input from the user
n = input("Give me a number: ")

# As long as 'n' is not equal to '1', run 'collatz()'
while n != 1:
    n = collatz(int(n))

#Print "Thank you" 5 times

for number in range(5):
    print("Thank you")

languages = ['R', 'Python', 'Scala', 'Java', 'Julia']

for index in range(len(languages)):
    print('Current language: ', languages[index])

for index in range(5):
    print('Current language: ', languages[index])

# Print "Thank you" 3 times

for number in range(3):
    print("Thank you")

# Set `fib_no` to 55, the number until where you want to print
fib_no = 55

# Set `first_no` to 0
first_no = 0

# Set `second_no` to 1
second_no = 1

# Set the counter `count` to 0
count = 0

# while loop to print the fibonacci series until the `fib_no`
while first_no <= fib_no:
    # Print `first_no`
    print(first_no)

    # Fibonnacci number
    nth = first_no + second_no

    # update values of `first_no` and `second_no`
    first_no = second_no
    second_no = nth

    # Set counter `count` +1
    count += 1

# Initialize `first_no` to `0`
first_no = 0

# Initialize `second_no` to `1`
second_no = 1

# Initialize `numbers`
numbers = range(0, 11)

# Find and display Fibonacci series
for num in numbers:
    if (num <= 1):
        # Update only `nth`
        nth = num
    else:
        # Update the values `nth`, `first_no` and `second_no`
        nth = first_no + second_no
        first_no = second_no
        second_no = nth

    # Print `nth`
    print(nth)

# Take user input
number = 2

""" #condition of the while loop
while number < 5:
    # condition of the nested while loop
    while number % 2 == 0:
        print("The number "+str(number)+" is even")"""
# Keeps printing "The number 2 is even" forever

# Print the below statement 3 times
for number in range(3):
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    # Inner loop
    for another_number in range(5):
        print("****************************")
        print("I am an inner loop iteration"+str(another_number))

# Initialize the first five rows
n = 5

# Start the loop to print the first five rows
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

# Start the loop to print the remaining rows in decreasing order of stars
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# Take user input
number = 2

# Condition of the while loop
while number < 5 :
    # condition of the nested while loop
    while number % 2 == 0:
        print("The number "+str(number)+" is even")
        break

    number+=1

""""# Take user input
number = 2

while number < 5 :
    while number % 2 == 0:
        print("The number "+str(number)+" is even")
        break

    continue

    number+=1"""
# The code prints "The number 2 is even" forever


# Print the below statement 3 times
for number in range(3) :
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    for another_number in range(3):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))
        break

# Print the below statement 3 times
for number in range(3) :
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    continue
    for another_number in range(3):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))
        break

# Print the below statement 3 times
for number in range(5,10,2) :
    print("I am number : "+str(number))

