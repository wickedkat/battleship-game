import colorama
from colorama import init
from colorama import Fore, Back, Style
import os
import time
import random


board_four = [['  ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' ', 'F', ' ', 'G', ' ', 'H', ' ', 'I', ' ', 'J', ' '],  # player1 ships/computer
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 1', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 2', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 3', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 4', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 5', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 6', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 7', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 8', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              [' 9', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['10', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ',
                  '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
# variables

coordinates = {"A": 2, "B": 4, "C": 6, "D": 8, "E": 10, "F": 12, "G": 14, "H": 16, "I": 18, "J": 20}
coordinates_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
coordinates_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
orientation = ['V', 'H']
escape_game = ["1"]
ship_one = u"\u26F5"
ship_two = u"\U0001F6E5"
ship_three = u"\U0001F6F3"
miss = u"\u2717"
sunk = u"\u2620"


def draw_board(board):
    print(Style.BRIGHT)  # showing board in 5 lines
    print(Back.CYAN)
    for s in board:
        print(*s)
    print(Style.RESET_ALL)


def define_comp_tripleships(board):
    i = 0
    while i < 4:
        ship_row = random.randrange(2, 17, 2)
        ship_col = random.randrange(2, 17, 2)
        ship_row1 = ship_row + 2
        ship_col1 = ship_col + 2
        ship_row2 = ship_row + 4
        ship_col2 = ship_col + 4
        if board[ship_row][ship_col] == ship_one or board[ship_row1][ship_col] == ship_one or board[ship_row2][ship_col] == ship_one:
            ship_row = random.randrange(2, 19, 2)
            ship_col = random.randrange(2, 19, 2)
        elif board[ship_row][ship_col] == ship_one or board[ship_row][ship_col1] == ship_one or board[ship_row][ship_col2] == ship_one:
            ship_row = random.randrange(2, 19, 2)
            ship_col = random.randrange(2, 19, 2)
        else:
            los = random.randint(1,2)
            if los == 1:
                    board[ship_row][ship_col] = ship_one
                    board[ship_row1][ship_col] = ship_one
                    board[ship_row2][ship_col] = ship_one
                    i += 1
            else:
                    board[ship_row][ship_col] = ship_one
                    board[ship_row][ship_col1] = ship_one
                    board[ship_row][ship_col2] = ship_one
                    i += 1


define_comp_tripleships(board_four)
draw_board(board_four)