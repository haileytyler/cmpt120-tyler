# Solution to number 2 on the Python Final Exam Version B Fall 2018

"""Create the following dice game. There are two players. Each one takes a turn rolling two dice (think random number
generator from 1 - 6). If the sum of the two dice equals 6, the player gets the sum of the two dice added to their
score. If a player rolls two 6's, they get double the sum of the two dice (24 instead of 12). If a player rolls a double
(except for double 6's), the sum of the two dice get subtracted from their score. No other combination of dice results
in additional points being added or subtracted from the player's score. The first player to reach a score of 50 or
higher wins the game."""

from random import *


def rolling_dice():
    roll_1 = randint(1,6)
    roll_2 = randint(1,6)
    return roll_1, roll_2


def score(roll_1, roll_2, score):
    dice_sum = roll_1 + roll_2
    if dice_sum == 6:
        score = score + dice_sum
    elif roll_1 == 6 and roll_2 == 6:
        score = score + 2 * dice_sum
    elif roll_1 == roll_2 and dice_sum < 12:
        score = score - dice_sum
    else:
        print("No additional points added.")
    return score


def winner(p1_score, p2_score):
    if p1_score >= 50:
        return 1
    elif p2_score >= 50:
        return 2
    else:
        return 3


def main():
    p1_score = 0
    p2_score = 0
    print("This is a two player dice rolling game. First to 50 wins!")
    while winner(p1_score, p2_score) == 3:
        input("Player 1: Press <Enter> to roll the dice!")
        p1_roll1, p1_roll2 = rolling_dice()
        p1_score = score(p1_roll1, p1_roll2, p1_score)
        print("Your first roll is a", p1_roll1)
        print("Your second roll is a", p1_roll2)
        print("Your score is", p1_score)
        print("")

        winner(p1_score, p2_score)

        input("Player 2: Press <Enter> to roll the dice!")
        p2_roll1, p2_roll2 = rolling_dice()
        p2_score = score(p2_roll1, p2_roll2, p2_score)
        print("Your first roll is a", p2_roll1)
        print("Your second roll is a", p2_roll2)
        print("Your score is", p2_score)
        print("")

        winner(p1_score, p2_score)
    print("Game over. Player", winner(p1_score, p2_score), "wins!")


main()

