#!/usr/bin/python
from random import randint
import os
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
turns_x=9
for turn in range(turns_x):
    os.system('clear')
    print "Turn", turn+1, " from ", turns_x

    print_board(board)

    guess_row = int(raw_input("Guess Row(1-5):"))-1
    guess_col = int(raw_input("Guess Col(1-5):"))-1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col] = "S"
        print_board(board)
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)
    if turn==turns_x-1:
         os.system('clear')
         board[ship_row][ship_col] = "S"
         print_board(board)
        print "Game Over"
