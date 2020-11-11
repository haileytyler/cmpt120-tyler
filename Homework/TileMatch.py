board=[["fruit", "fruit", "fruit", "fruit"],["fruit", "fruit", "fruit", "fruit"],["fruit", "fruit", "fruit", "fruit"]]
hidden_board=[["cherry", "banana", "grape", "apple"],["pear","grape", "banana", "lemon"],["cherry", "lemon", "apple", "pear"]]
def printRow(row):
# initialize output to the left border
 print("|", end="")
# for each square in the row...
 for j in range(4):
    # add to output the symbol for this square followed by a border
    print(" " + row[j]+" |", end="")
 print(end='\n')

def printBoard(board):
# print the top border
 print("+-----------+")
# for each row in the board...
 for i in range(3):
               printRow((board[i]))  # print the row
               print("+-----------+")# print the next border

def checkTiles(board, tile1row, tile1col, tile2row, tile2col):
    if tile1row < 3 and tile2row < 3 and tile1col < 4 and tile2col < 4:
        if tile1row == tile2row and tile1col == tile2col:
            print("Choose unique tiles. Pick again.")
            return False
        if (tile1row and tile1col) == board[tile1row][tile1col] or (tile2row and tile2col) == board[tile2row][tile2col]:
            print("Tile already chosen. Pick again.")
            return False
        else:
            return True
    else:
        print("Row must be less than 4. Column must be less than 6. Try Again.")
        return False
            
        
def checkForMatchingTiles(board, tile1row, tile1col,tile2row,tile2col):
        
        temp_board=board
        temp_board[tile1row][tile1col],board[tile2row][tile2col]=hidden_board[tile1row][tile1col],hidden_board[tile2row][tile2col]
    
        printBoard(temp_board)
        if hidden_board[tile1row][tile1col]==hidden_board[tile2row][tile2col]:
            print(" You found a match!")
            board[tile1row][tile1col],board[tile2row][tile2col]=hidden_board[tile1row][tile1col],hidden_board[tile2row][tile2col]
        
        else:
            print("Sorry, try again")
            board[tile1row][tile1col],board[tile2row][tile2col]="fruit", "fruit"
    
    

    
def unMatchedTilesRemaining(board):
               # for each row in the board...
               for i in range(3):
                  # for each square in the row...
                  for j in range(4):
                      if board[i][j]=="fruit":
                          print("tiles remaining")
                          return True
               print("All tiles are turned over")
               return False # if no square is blank, return False

# --------------------End of functions-----------------------------------

# main function

def main():
 printBoard(board)
 while unMatchedTilesRemaining(board):   
   choice1row=int(input("Pick the row for the first tile: "))
   choice1col=int(input("Pick the col for the first tile: "))
   choice2row=int(input("Pick the row for the second tile: "))
   choice2col=int(input("Pick the col for the second tile: "))
   tile1, tile2 = [choice1row, choice1col], [choice2row, choice2col]
   print(tile1[1])
   print("The first tile is:", hidden_board[choice1row][choice1col])
   print("The second tile is:", hidden_board[choice2row][choice2col])
   if checkTiles(board,choice1row,choice1col,choice2row,choice2col):
       checkForMatchingTiles(board, choice1row, choice1col, choice2row, choice2col)
   else:
       continue
       
   printBoard(board)  # Print board at the end to show the last move
 print("Game Over")
main()

tile_check(board, choice1[0], choice1[1], choice2[0], choice2[1])
