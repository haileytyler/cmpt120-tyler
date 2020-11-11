# Hailey Tyler
# Homework due: 2-14-19
from math import *
def distance():
    print("This program will evaluate the distance between two points.")

    print()
    x1, y1 = input("What is the first ordered pair? (x1 , y1)").split(',')
    x2, y2 = input("What is the second ordered pair? (x2, y2)").split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = int(x2), int(y2)
    length_leg1 = (x2 - x1)
    length_leg2 = (y2 - y1)
    distance1 = round(sqrt(length_leg1 ** 2 + length_leg2 ** 2))
    distance2 = round(sqrt(length_leg1 ** 2 + length_leg2 ** 2), 1)
    distance3 = ceil(sqrt(length_leg1 ** 2 + length_leg2 ** 2))

    print()
    print("The distance between the two points rounded to the nearest whole number is", distance1)
    print("The distance between the two points rounded to the nearest tenth is", distance2)
    print("The distance between the two points rounded up to the next whole number is", distance3)

    print("Press <Enter> to end the program.")
distance()
# New Quadratic Formula
# quadratic.py
#    A program that computes the roots of a quadratic equation.
#    Illustrates use of the math library.

import math  # Makes the math library available.

def main():
    print("This program finds the solutions to a quadratic")
    print()

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    disc = (b * b - 4 * a * c)
    if disc < 0:
        imaginary = sqrt(abs(disc)) / (2 * a)
        real = -b/(2*a)
        iroot1 = complex(real, imaginary)
        iroot2 = complex(real, (-imaginary))

        print()
        print("There are no real roots.")
        print("The solutions are:", iroot1, iroot2)
    if disc == 0:
        discRoot = math.sqrt(disc)
        root = (-b + discRoot) / (2 * a)

        print()
        print("The solution is:", root)
    if disc > 0:
        discRoot = math.sqrt(disc)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        print()
        print("The solutions are:", root1, root2)
    print("Press <Enter> to end the program.")
main()