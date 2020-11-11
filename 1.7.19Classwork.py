#Hailey Tyler
#Lab 3
from math import *
#4
#a
for i in range(1, 11):
    print(i*i)
#b
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i**3)
print(i)
#c
x = 2
y = 10
for j in range(0, y, x):
    print(j, end="")
    print(x + y)
print("done")
#d
ans = 0
for i in range(1, 11):
    ans = ans + i*i
    print(i)
print(ans)

#2
def pizza():
    print("This program calculates the cost per square inch of a circular pizza")
    diameter = int(input("What is the diameter of the pizza? (inches)"))
    price = round(float(input("What is the price of the pizza?")), 2)
    radius = diameter/2
    area = pi*((radius) ** 2)
    cost = round(price/area, 2)
    print("The cost per square inch of the pizza is", cost, "dollars.")
    print("Press <Enter> to end the program.")
pizza()

#10
def ladder():
    print("This program calculates the length of a ladder required to reach a given height when leaned against a house.")
    height = float(input("What is the height of the house? (feet)"))
    angle_degrees = float(input("What is the angle of the ladder against the house? (degrees)"))
    angle_radians = (pi/180)*angle_degrees
    length = round((height/sin(angle_radians)), 2)
    print("The length of the ladder is", length, "feet.")
    print("Press <Enter> to end the program.")
ladder()
