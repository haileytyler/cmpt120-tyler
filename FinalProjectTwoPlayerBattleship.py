# This program will allow two players to play a local game of Battleship
# Hailey Tyler
# Final Project
# Intro to Programming
# 5-9-19

import time

# Global Variables:
player1_placement = [[None for y in range(10)] for x in range(10)]
player2_placement = [[None for y in range(10)] for x in range(10)]
player1_bombs = [[None for y in range(10)] for x in range(10)]
player2_bombs = [[None for y in range(10)] for x in range(10)]

#          0    1    2    3    4    5    6    7
symbol = [" ", "✖", "☮", "☐", "●", "▲", "❤", "◆"]


def reset_board(board):
    # Fill the board with 0's
    for x in range(10):
        for y in range(10):
            board[x][y] = 0


def print_board(board):
    # Add the column headings
    print("    A   B   C   D   E   F   G   H   I   J")
    for x in range(10):
        print("  +---------------------------------------+")
        # Add the row headings by printing the index number of the iteration
        print(x, "|", end="")
        for y in range(10):
            # "symbol[board[x][y]]" will put the correct symbol corresponding to the index number (Each ship has a
            # different symbol)(Hits are an ✖ and misses are a peace symbol).
            print(" " + symbol[board[x][y]] + " " + "|", end="")
        print(end='\n')
    print("  +---------------------------------------+")


def in_battleship_placement(length):
    start = input("What is the starting coordinate for your battleship of length " + str(length) + "? ").upper()
    end = input("What is the ending coordinate for your battleship of length " + str(length) + "? ").upper()
    return [start, end]


def coordinate_check(coord):
    # This will make sure that the user inputs a two character string and that the first character is a letter and
    # that the second character is a number.
    if len(coord) != 2 or coord[0].isnumeric() or coord[1].isalpha():
        print("Invalid coordinate. Try again. (ex. A0)")
        return False
    # Change the first character to a number. Subtract 65 to get the correct index number (ie. A = 65).
    x = ord(coord[0]) - 65
    y = int(coord[1])
    # Make sure that the rows are indexed from 0-9 and the columns are indexed from A-J.
    if x < 0 or x > 9 or y < 0 or y > 9:
        print("Invalid coordinate. Try again.")
        return False
    return True


def battleship_placement(board, coords, length, ship):
    # Validate that there are two good coordinates.
    if not coordinate_check(coords[0]):
        return False
    if not coordinate_check(coords[1]):
        return False
    # Horizontal ship:
    if coords[0][0] == coords[1][0]:
        # Calculate the length of the ship. Take absolute value in case the user inputs a ship backwards.
        if length != abs(int(coords[0][1]) - int(coords[1][1])) + 1:
            print("Invalid length. Must be", str(length), "units long.")
            return False
        y = ord(coords[0][0]) - 65
        # Find the minimum coordinate
        x1 = min(int(coords[0][1]), int(coords[1][1]))
        # Find the maximum coordinate
        x2 = max(int(coords[1][1]), int(coords[0][1]))
        for x in range(x1, x2 + 1):
            # Make sure that the ships do not overlap. If there is a ship there, there will be a number > 0 there.
            if board[x][y] != 0:
                print("Ships cannot overlap. Try Again.")
                return False
        for x in range(x1, x2 + 1):
            # Plot the ship
            board[x][y] = ship
    # Vertical Ship:
    elif coords[0][1] == coords[1][1]:
        # Calculate the length of the ship. Take absolute value in case the user inputs a ship backwards.
        if length != abs(ord(coords[0][0]) - ord(coords[1][0])) + 1:
            print("Invalid length. Must be", str(length), "units long.")
            return False
        x = int(coords[0][1])
        # Find the minimum coordinate
        y1 = min(ord(coords[0][0]), ord(coords[1][0])) - 65
        # Find the maximum coordinate
        y2 = max(ord(coords[1][0]), ord(coords[0][0])) - 65
        for y in range(y1, y2 + 1):
            # Make sure that the ships do not overlap. If there is a ship there, there will be a number > 0 there.
            if board[x][y] != 0:
                print("Ships cannot overlap. Try Again.")
                return False
        for y in range(y1, y2 + 1):
            # Plot the ship
            board[x][y] = ship
    else:
        # Print an error if the ship is not horizontal or vertical
        print("Coordinates must create a ship that is vertical or horizontal")
        return False
    return True


def place_ships(other_player, board):
    # Define the lengths of the ships (battleship = 4 units, cruiser = 3 units, submarine = 3 units,
    # destroyer = 2 units).
    lengths = [5, 4, 3, 3, 2]
    reset_board(board)
    # Start the loop at 3 because the first three elements in symbol are not for the ships.
    for ship in range(3, 8):
        length = lengths[ship - 3]
        print_board(board)
        # Loop will run the battleship_placement function until it returns a True.
        while not battleship_placement(board, in_battleship_placement(length), length, ship):
            print("")
    print_board(board)
    # The next three lines will make sure that the next player does not see the previous one's board.
    input("All ships have been placed. Press <Enter> when ready to pass to player " + str(other_player) +
          " (A 3 second delay will begin).")
    print(75 * "\n")
    # This will delay the next line from executing.
    time.sleep(3)


def battleship_bomb(bomb_board, placement_board):
    while True:
        bomb = input("Where do you want to drop your bomb?").upper()
        if coordinate_check(bomb):
            # Check to see if a bomb was already dropped in that location.
            x = int(bomb[1])
            y = ord(bomb[0]) - 65
            if bomb_board[x][y] != 0:
                print("You already dropped a bomb there. Try Again")
            # Check to see if there is a ship there.
            elif placement_board[x][y] == 0:
                bomb_board[x][y] = 2
                placement_board[x][y] = 2
                print("Miss.")
                return False
            else:
                bomb_board[x][y] = 1
                placement_board[x][y] = 1
                print("Hit!")
                return True


def turn_over_to(player):
    # This function is for the end of a player's turn.
    input("Turn over. Press <Enter> when ready to pass to player " + str(player) + " (A 3 second delay will begin).")
    print(50 * "\n")
    time.sleep(3)
    return player


def main():

    reset_board(player1_bombs)
    reset_board(player2_bombs)

    print("This program is a local game of battleship. \n Players: \n   -2 \n Goal: \n   -Sink all of the other"
          "player's ships! \n Setup: \n   -Input coordinates to place your ships on your board. \n Rules: \n"
          "   -Take turns dropping bombs onto the other player's board. \n   -If you hit a ship, drop another bomb! \n"
          "   -Game ends when all of one player's ships sink.")
    input("Press <Enter> for player 1 to place their ships!")

    place_ships(2, player1_placement)
    place_ships(1, player2_placement)

    game_over = 0
    player = 1
    # Initialize each player's hit count at 0.
    player1_hits = 0
    player2_hits = 0

    while game_over == 0:
        if player == 1:
            print_board(player1_placement)
            print_board(player1_bombs)
            # If player 1 hits, add 1 to the hit counter.
            if battleship_bomb(player1_bombs, player2_placement):
                player1_hits = player1_hits + 1
                # If a player makes 17 hits, then the game ends (17 is the sum of lengths of the ships).
                if player1_hits == 17:
                    game_over = 1
                else:
                    # Player will get to drop another bomb if they get a hit
                    print("Drop another bomb!")
            else:
                # If no hit or the game ends -> end turn
                player = turn_over_to(2)
        else:
            print_board(player2_placement)
            print_board(player2_bombs)
            # If player 2 hits, add 1 to the hit counter
            if battleship_bomb(player2_bombs, player1_placement):
                player2_hits = player2_hits + 1
                if player2_hits == 17:
                    game_over = 2
                else:
                    print("Drop another bomb!")
            else:
                player = turn_over_to(1)

    print("Game over! Player", game_over, "wins!")
    # Print the players boards to see how close the game was!
    print_board(player1_placement)
    print_board(player2_placement)


main()
