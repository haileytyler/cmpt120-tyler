# Hailey Tyler
# Chapter 7 Assignment: 5-Question Quiz
# 2/22/19

def quiz():
    print("This program is a 5-Question Quiz.")
    score = 0

    ques_1 = input("T/F: Mitochondria is the powerhouse of the cell.").upper()
    if ques_1 == "T":
        print("Correct!")
        score = 1
    else:
        print("Incorrect.")

    ques_2 = input("Which Marist freshmen dorm is the BEST? \n a) Leo \n b) Marian \n c) Sheahan \n d) Midrise").upper()
    if ques_2 == "C":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect.")

    ques_3 = input("Which shape's interior angles add up to 180°? \n a) Square \n b) Triangle "
                   "\n c) Hexagon \n d) Circle").upper()
    if ques_3 == "B":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect.")

    ques_4 = input("T/F: The sun makes up 99.8% of the mass of our solar system.").upper()
    if ques_4 == "T":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect.")

    ques_5 = input("Simplify the following expression: 4 - 9 / 3 + 5 * 2 \n a) 10 \n b) 12 \n c) 11 \n d) 13").upper()
    if ques_5 == "C":
        print("Correct!")
        score = score + 1
    else:
        print("Incorrect.")

    print("Your score is", score, "out of 5.")
    if score <= 2:
        print("Better luck next time.")
    elif score == 3 or score == 4:
        print("Not bad. Try again soon!")
    else:
        print("Awesome! You rock!")
    input("Press <Enter> to exit the program.")
quiz()
quiz()
quiz()
