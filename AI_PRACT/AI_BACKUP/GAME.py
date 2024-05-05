# -*- coding: utf-8 -*-
"""game_backup.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I3nVgKP7WE48gFslOqGWo1X3Tz24pRZQ
"""

import random

def computer_move(board):
    while True:
        row= random.randint(0,2)
        col=random.randint(0,2)
        if(board[row][col]==' '):
            return row,col



def display(board):
    print("__________________")
    print(f"|  {board[0][0]}  |  {board[0][1]}  |{board[0][2]}   |")
    print("__________________")
    print(f"|  {board[1][0]}  |  {board[1][1]}  |{board[1][2]}   |")
    print("__________________")
    print(f"|  {board[2][0]}  |  {board[2][1]}  |{board[2][2]}   |")
    print("__________________")

def check_win(board,player):
    for i in range(3):
        if(board[i][0]==player and board[i][1]==player and board[i][2]==player):
            return True
        if(board[0][i]==player and board[1][i]==player and board[2][i]==player):
            return True

    if(board[0][0]==player and board[1][1]==player and board[2][2]==player):
        return True

    if(board[0][2]==player and board[1][1]==player and board[2][0]==player):
        return True

    return False

def main():
    board= [[' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    ]

    player ='X'
    #display(board)

    for turn in range(9):
        display(board)
        while True:
            if(player=='X'):
                print(f"player : {player}")
                row = int(input("Enter row:"))
                col = int(input("Enter col:"))
            else:
                print("computers move:")
                row,col=computer_move(board)

            if(row<0 or row>2 or col<0 or col>2):
                print("invalid input, try again..")
            elif(board[row][col]!=' '):
                print("occupied")
            else:
                break

        board[row][col]=player

        if(check_win(board, player)):
            display(board)
            print(f"{player} wins!!")
            break

        if(player=='X'):
            player='O'
        else:
            player='X'

        if(turn==8 and not check_win(board,'X') and not check_win(board,'Y')):
            print("its a draw!!!!!")




main()

