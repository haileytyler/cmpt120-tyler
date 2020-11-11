# This program will allow two players to play a local game of Battleship
# Hailey Tyler
# Final Project Pseudo Code
# Intro to Programming
# 4-11-19

# Set up four instances of two dimensional arrays sized 10 by 10
# the column headings will be letters from A to J and the rows will be 0 to 9.
# This will index the board and give the players a way to call the space they want to bomb.

# show an empty board with column and row headings
# prompt the user to choose where they want to place their ships by asking for sets of coordinates
# For each ship, ask for the starting and ending coordinates
# Calculate the length of the ship and if input is greater or less than X print "Invalid length. Try again"
# if input is not in the same row or in the same column print "Coordinates must create a ship that is vertical or
# horizontal"
# The first ship that they must pick is the carrier which is 5 units long
# The next one is the battleship which is four units long and follows a similar structure
# Then the cruiser (three units long)
# The submarine (three units long)
# the destroyer (two units long)
# if input is repeated (ie. two ships on top of each other) print "Ship locations must not overlap"
# save the array with the new ship locations for that player

# After the player has placed all of their ships- the next player will place all of theirs the same way in a different
# array

# show an empty board with column and row headings
# prompt the user to choose a coordinate to drop a bomb on
# that coordinate will be used to check the other player's array of ship location
# if coordinate has a battleship print "Hit! Drop another bomb!"
# if coordinate does not have a battleship print "Miss."

# repeat for player 2

# Before each turn:
# Have an input statement that requires the player to press enter to make sure that the opposing player's board is not
# exposed.
# Print the player's board whose turn it is to see how their ships are doing (ships will be green squares)

# during the turns:
# if coordinate is invalid print "Invalid coordinate. Rows must be indexed from 0-9 and columns must be indexed
# from A-J.
# if coordinate is repeated print "Coordinate already chosen. Try again."
# Mark the coordinates with hits with red X's and the coordinates with misses with blue O's

# if a player sinks all the opposing player's ships print game over, which player won, and the players' boards

player1_placement = [[None for y in range(10)] for x in range(10)]
print(player1_placement)
