# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Hailey Tyler
"""The program converts degrees celsius to degrees fahrenheit.  The user will input the temperature in celsius and recieve the temperature in fahrenheit."""
def main():
    for i in range(5):
        print("This program converts degrees celsius to degrees fahrenheit.")
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")

main()

# avg2.py
#   A simple program to average two exam scores
#   Illustrates use of multiple input
"""The program computes the average of three exams scores that the user inputs."""
def main():
    print("This program computes the average of three exam scores.")

    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 +score3) / 3

    print("The average of the scores is:", average)

main()
