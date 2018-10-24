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


def define_ships(board):
    number, letter = check_input(board)
    ship_row = int(number)*2
    for key in coordinates:
        if letter == key:
            ship_col = coordinates[key]
    board[ship_row][ship_col] = ship_one
    return ship_row, ship_col


def check_input(board):
    print("Enter row number 1-10")
    number = (input("1-10: "))
    while number not in coordinates_numbers:
        print("enter valid number")
        number = (input("1-10: "))
    print('enter a letter A-J')
    letter = input("A-J: ")
    while letter not in coordinates_letters:
        print('enter valid letter A-J')
        letter = input("A-J: ")
    return number, letter


def define_doubleships(board):             # putting ships on a board
        ship_row, ship_col = define_ships(board)
        draw_board(board)
        orient = input("""Choose orientation of two-masted ship:
        (or it will be random)
        (V)ertically
        (H)orizontally: """).upper()
        if orient not in orientation:
                orient = random.choice(orientation)
        if orient == "V":
                if ship_row == 20:
                        board[ship_row-2][ship_col] = ship_one
                else:
                        board[ship_row+2][ship_col] = ship_one
        elif orient == "H":
                if ship_col == 20:
                        board[ship_row][ship_col-2] = ship_one
                else:
                        board[ship_row][ship_col+2] = ship_one
        

define_doubleships(board_four)
draw_board(board_four)