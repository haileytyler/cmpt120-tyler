# Hailey Tyler
# Intro to Programming Final Exam- Question 1
# Professor Cathy Martensen
# 5-17-19

"""Write a program that plays the following game: 2 players begin counting up to a finite number, such as 50.
The players take turns back and forth, ie, player1 says "1", then player 2 says "2", then player 1 says "3", and so on.
A number between 3 and 9 is chosen at random and becomes the "special" number. If a player gets to a number that is a
multiple of this special number, then instead of saying the actual number, he/she will say "buzz". So if the number
chosen is 3, then the player would say "buzz" for 3, 6, 9, 12, etc. If they say the actual number by accident, then
they get a "strike". Once they get three strikes they are out of the game. If there are only two players, then the
other player is declared the winner. """

# Pseudo Code:

# Print out the directions to the game
# Players will input numbers up to 50.
# A "buzz" number will be picked (numbers 3-9) and will be printed at the beginning
# If the buzz number or a multiple of the buzz number is supposed to be counted, the player will have to input "buzz"
# instead of the number.
# A player will get a strike if they input the wrong number for their turn, do not input "buzz" or a number, or if
# they fail to input buzz.
# If a player gets 3 strikes, they lose.

# Source Code:

# import random in order to choose the buzz word
from random import *


def check_input(number, random_number, i):
    # will return true if the player inputs buzz when appropriate
    if number == "buzz" and (i == random_number or i % random_number == 0):
        return True
    # will return false if the player doesn't input a number if they aren't supposed to input buzz
    if not number == "buzz" and not number.isdigit():
        return False
    # will return false if the player doesn't count correctly
    if int(number) != i:
        return False
    # will return false if the player doesn't input 'buzz' when it equals the random number
    if int(number) == random_number:
        return False
    # will return false if the player doesn't input 'buzz' when it equals a multiple of the random number
    if int(number) % random_number == 0:
        return False
    # will return true if the player counts correctly
    if int(number) == i and not int(number) == random_number and not int(number) % random_number == 0:
        return True


def number_input():
    # function for the player to input their number
    number = input("Type in your number: ")
    return number


def main():
    print("This program is a counting game. \n Players: \n   -2 \n Goal: \n   -Count to 50 \n Rules: \n"
          "   -A random number will be picked at the beginning as the 'buzz' number. \n   -If it is your turn to input "
          "the 'buzz' number or a multiple of the 'buzz' number, simply input 'buzz'.\n   "
          "-If you fail to input 'buzz' or input the wrong number, you get a strike! \n "
          "  -Game ends when a player gets 3 strikes.")
    input("Press <Enter> for player 1 to start the game!")
    # chooses the random number
    random_number = randint(3, 9)
    print("The buzz number is:", random_number)

    # initialize game_over to 0 as well as the strike counters for each player
    game_over = 0
    player1_strikes = 0
    player2_strikes = 0

    while game_over == 0:
        # will count up to 50
        for i in range(50):
            number = number_input()
            # save i to use in check_input()
            i = i+1
            if not check_input(number, random_number, i):
                print("Strike!")
                # will add a strike to the appropriate player's counter
                if i % 2 == 0:
                    player2_strikes = player2_strikes + 1
                    if player2_strikes == 3:
                        game_over = 1
                        # break the counting loop when a player's strike count equals 3
                        break
                else:
                    player1_strikes = player1_strikes + 1
                    if player1_strikes == 3:
                        game_over = 2
                        break
    print("Game over! Player", game_over, "wins!")


main()
