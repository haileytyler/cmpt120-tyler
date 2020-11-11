# Daniel Rinaldi, Allie Texter, & Hailey Tyler
# Debugging Lab
# 4-18-19

# 1

greeting = input("Hello, possible pirate! What's the password?")
# Added a quotation mark
if greeting == "Arrr!":
    # Changed "in" to "==" and deleted the bracket and quotation
    print("Go away, pirate.")
else:
    # Changed "elif" to "else" and added a colon
    print("Greetings, hater of pirates!")
    # Indented the print statement

# 2

year = int(input("Greetings! What is your year of origin?"))
# Changed "==" to "=" and changed the period to a paren

if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")

# 3

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0

for grade in grades:

  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"


for i in grades:
    print("Exam: " + str(i))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade is "F":
    print("Student is failing.")
else:
    print("Student is passing.")
