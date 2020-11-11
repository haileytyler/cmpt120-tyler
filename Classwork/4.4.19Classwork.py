# CMPT 120 Intro to Programming
# Chapter 11 lab: Lists and Error Handling
# Author: Hailey Tyler
# Created: 2019-04-04

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
symbol = [" ", "x", "o"]


def printRow(row):

    print("|", end="")
    for j in range(3):
        print(" " + symbol[row[j]] + " " + "|", end="")
    print(end='\n')


def printBoard(board):

    for i in range(3):
        print("+-----------+")
        printRow(board[i])
    print("+-----------+")


def markBoard(board, row, col, player):

    if row > 3 or col > 3 or row <= 0 or col <= 0:
        print("Invalid row or column. Try again.")
        return False
    elif board[row - 1][col - 1] == 0:
        board[row - 1][col - 1] = player
        return True
    else:
        print("This space has already been taken. Try Again.")
        return False


def getPlayerMove():

    row = int(input("Pick a row: "))
    col = int(input("Pick a column: "))
    return row, col


def hasBlanks(board):

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                return True
    return False


def hasWinner(board):

    # Check the rows:
    if board[0][0] == board[0][1] == board[0][2] == 1:
        return 1
    if board[1][0] == board[1][1] == board[1][2] == 1:
        return 1
    if board[2][0] == board[2][1] == board[2][2] == 1:
        return 1
    if board[0][0] == board[0][1] == board[0][2] == 2:
        return 2
    if board[1][0] == board[1][1] == board[1][2] == 2:
        return 2
    if board[2][0] == board[2][1] == board[2][2] == 2:
        return 2
    # Check the columns:
    if board[0][0] == board[1][0] == board[2][0] == 1:
        return 1
    if board[0][1] == board[1][1] == board[2][1] == 1:
        return 1
    if board[0][2] == board[1][2] == board[2][2] == 1:
        return 1
    if board[0][0] == board[1][0] == board[2][0] == 2:
        return 2
    if board[0][1] == board[1][1] == board[2][1] == 2:
        return 2
    if board[0][2] == board[1][2] == board[2][2] == 2:
        return 2
    # Check the diagonals:
    if board[0][0] == board[1][1] == board[2][2] == 1:
        return 1
    if board[0][2] == board[1][1] == board[2][0] == 1:
        return 1
    if board[0][0] == board[1][1] == board[2][2] == 2:
        return 2
    if board[0][2] == board[1][1] == board[2][0] == 2:
        return 2
    return 0
    # This return statement is used for when there is no winner yet


def main():

    player = 1
    while hasBlanks(board):
        printBoard(board)
        print("It's Player " + str(player) + "'s turn!")
        row, col = getPlayerMove()
        if markBoard(board, row, col, player):
            player = player % 2 + 1
        winner = hasWinner(board)
        if winner > 0:
            print("Player", winner, "wins!")
            break
    printBoard(board)
    print("Game Over")


main()

