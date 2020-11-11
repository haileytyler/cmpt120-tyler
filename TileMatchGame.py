# Solution to number 3 on the Python Final Exam Version B Fall 2018
1
11
"""A match game (sometimes called "concentration") is a game where objects are hidden behind tiles. The player turns two
tiles over at a time. If the objects behind the two tiles match, then the tiles are kept open, leaving the matched
objects revealed. Play continues until all the tiles are turned over. Given the following board made up of 3 rows and 4
columns: board=[["cherry", "banana", "grape", "apple"],["pear","grape", "banana", "lemon"],["cherry", "lemon", "apple",
"pear"]] NOTE: You do not need to display the board to the user. Assume that code has already been written. Allow the
user to input a row and a column, plus another row and column (you can do two input statements for first and second
choice). If the items match, then return a message stating the users found a match, and change the name in each square
from the fruit name to "open". If the two squares do not match, print out a message stating a match was not found.
If a player chooses a spot already "open", tell them to try again. Continue playing until all matches are made
(suggestions: keep score for each match found--there should be 6 in total; OR, you can search through the board at the
beginning of each play and when all spaces equal "open", end the game, etc.)
Print out introductory and closing messages along with the messages mentioned above.
"""
# Global Variables:

board = [["fruit", "fruit", "fruit", "fruit"], ["fruit", "fruit", "fruit", "fruit"],
         ["fruit", "fruit", "fruit", "fruit"]]
hidden_board = [["cherry", "banana", "grape", "apple"], ["pear", "grape", "banana", "lemon"],
                ["cherry", "lemon", "apple", "pear"]]


def print_board(board):
    # Print 1-4 to index the columns
    print("      1       2       3       4")
    for x in range(3):
        print("  +-------------------------------+")
        # Print the row headings by printing the index number of the iteration plus 1
        print(x + 1, "|", end="")
        for y in range(4):
            # "board[x][y]" is used to input the name of the tile
            print(" " + str(board[x][y]) + " " + "|", end="")
        print(end='\n')
    print("  +-------------------------------+")


def get_tile(instruction, max):
    # While the tile spot is invalid
    while True:
        # Try will convert to number
        try:
            choice = int(input(instruction))
            if choice < 1 or choice > max:
                print("Rows must be from 1-3. Columns must be from 1-4. Try Again.")
            else:
                return choice - 1
        except ValueError:
            print("Type in a number.")


def input_tiles():
    # Call the get_tile() function and pass it the maximum value of the row/column
    choice1row = get_tile("Pick the row for the first tile: ", 3)
    choice1col = get_tile("Pick the column for the first tile: ", 4)
    choice2row = get_tile("Pick the row for the second tile: ", 3)
    choice2col = get_tile("Pick the column for the second tile: ", 4)

    return [choice1row, choice1col], [choice2row, choice2col]


def tile_check(board, hidden_board, tile1, tile2):
    # Make sure that the rows are indexed with numbers 1-3 and the rows are indexed with numbers 1-4
    if tile1[0] < 3 and tile2[0] < 3 and tile1[1] < 4 and tile2[1] < 4:
        # Make sure that the user doesn't input the same tile spot in one turn
        if tile1[0] == tile2[0] and tile1[1] == tile2[1]:
            print("Choose unique tiles. Pick again.")
            return False
        # Make sure that the user doesn't input a tile spot that has an uncovered tile already in it
        if board[tile1[0]][tile1[1]] == hidden_board[tile1[0]][tile1[1]] or board[tile2[0]][tile2[1]] == \
                hidden_board[tile2[0]][tile2[1]]:
            print("Tile match already found. Pick again.")
            return False
        else:
            return True
    else:
        print("Rows must be from 1-3. Columns must be from 1-4. Try Again.")
        return False


def reset_board(board):
    # Fill the board with "fruit"
    for x in range(3):
        for y in range(4):
            board[x][y] = "fruit"


def matching_tiles_check(board, hidden_board, tile1, tile2):
    # Make sure that the user input a valid tile spot
    while not tile_check(board, hidden_board, tile1, tile2):
        print("")
        return False

    # Show the user what is under each tile
    print("The first tile is:", hidden_board[tile1[0]][tile1[1]])
    print("The second tile is:", hidden_board[tile2[0]][tile2[1]])

    # Create a temporary board to show the user what is under the tile spots they just entered (and any previous
    # matches).
    temp_board = board
    temp_board[tile1[0]][tile1[1]], board[tile2[0]][tile2[1]] = hidden_board[tile1[0]][tile1[1]],\
                                                                    hidden_board[tile2[0]][tile2[1]]
    print_board(temp_board)

    # If the tiles match, print a positive message to the user and update the user's board with the match
    if hidden_board[tile1[0]][tile1[1]] == hidden_board[tile2[0]][tile2[1]]:
        print(" You found a match!")
        board[tile1[0]][tile1[1]], board[tile2[0]][tile2[1]] = hidden_board[tile1[0]][tile1[1]], \
                                                                   hidden_board[tile2[0]][tile2[1]]
    else:
        # If the tiles do not match, print a negatuve message to the user and reset the board
        print("Sorry, no match, try again.")
        reset_board(temp_board)


def game_over(board):
    # Check each row and column for "fruit" and end the game when the user finds all the matches
    for x in range(3):
        for y in range(4):
            if board[x][y] == "fruit":
                return False
    print("All tiles have been matched. Game over!")
    return True


def main():
    print("This program is a match game called 'concentration'. \n Goal: \n   -Match all of the tiles. \n How to Play:"
          "  \n   -Input two sets of rows and columns. \n   -The tiles underneath will be revealed and, if you have a "
          "match, they will be added to your board. \n   -Keep trying to match the tiles until the whole board is "
          "uncovered!")
    input("Press <Enter> to begin!")
    # Show the empty board (of just fruit)
    print_board(board)
    # Keep playing while there are "fruit" tiles on the board
    while not game_over(board):
        choice1, choice2 = input_tiles()
        # Check to see if there are any matches and check user input
        matching_tiles_check(board, hidden_board, choice1, choice2)
        # Print the updated board
        print_board(board)
    input("Press <Enter> to quit.")


main()
