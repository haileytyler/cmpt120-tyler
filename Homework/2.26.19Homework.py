# Hailey Tyler
# Chapter 8 Assignment: Test with looping
# 2/26/19

def quiz():
    print("This program is a 5-Question Quiz.")

    ques_1 = input("T/F: Mitochondria is the powerhouse of the cell.").upper()
    while ques_1 != "T" and ques_1 != "SKIP":
        print("Sorry, try again!")
        ques_1 = input("T/F: Mitochondria is the powerhouse of the cell.").upper()

    if ques_1 == "T":
        print("Correct!")

    ques_2 = input("Which Marist freshmen dorm is the BEST? \n a) Leo \n b) Marian \n c) Sheahan \n d) Midrise").upper()
    while ques_2 != "C" and ques_2 != "SKIP":
        print("Sorry, try again!")
        ques_2 = input(
            "Which Marist freshmen dorm is the BEST? \n a) Leo \n b) Marian \n c) Sheahan \n d) Midrise").upper()

    if ques_2 == "C":
        print("Correct!")

    ques_3 = input("Which shape's interior angles add up to 180°? \n a) Square \n b) Triangle "
                   "\n c) Hexagon \n d) Circle").upper()
    while ques_3 != "B" and ques_3 != "SKIP":
        print("Sorry, try again!")
        ques_3 = input("Which shape's interior angles add up to 180°? \n a) Square \n b) Triangle "
                       "\n c) Hexagon \n d) Circle").upper()

    if ques_3 == "B":
        print("Correct!")

    ques_4 = input("T/F: The sun makes up 99.8% of the mass of our solar system.").upper()
    while ques_4 != "T" and ques_4 != "SKIP":
        print("Sorry, try again!")
        ques_4 = input("T/F: The sun makes up 99.8% of the mass of our solar system.").upper()

    if ques_4 == "T":
        print("Correct!")

    ques_5 = input("Simplify the following expression: 4 - 9 / 3 + 5 * 2 \n a) 10 \n b) 12 \n c) 11 \n d) 13").upper()
    while ques_5 != "C" and ques_5 != "SKIP":
        print("Sorry, try again!")
        ques_5 = input(
            "Simplify the following expression: 4 - 9 / 3 + 5 * 2 \n a) 10 \n b) 12 \n c) 11 \n d) 13").upper()

    if ques_5 == "C":
        print("Correct!")

    play_again = input("Would you like to play again? (yes/no)").lower()
    while play_again != "no":
        quiz()
        break
    if play_again == "no":
        print("Thank you for playing!")
quiz()