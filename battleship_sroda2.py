import colorama
from colorama import init
from colorama import Fore, Back, Style
import os
import time
import random

board_one = [['  ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' ', 'F', ' ', 'G', ' ', 'H', ' ', 'I', ' ', 'J', ' '],  # player1 ships
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
board_two = [['  ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' ', 'F', ' ', 'G', ' ', 'H', ' ', 'I', ' ', 'J', ' '],  # player2 ships/computer
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
board_three = [['  ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' ', 'F', ' ', 'G', ' ', 'H', ' ', 'I', ' ', 'J', ' '],  # player1 ships
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


# - - - - - - - - - - - - - - - - - - - - - def functions
# drawing board
def draw_board(board):
    print(Style.BRIGHT)  # showing board in 5 lines
    print(Back.CYAN)
    for s in board:
        print(*s)
    print(Style.RESET_ALL)

# instructions


def instructions():
    with open("instructions.txt", "r") as file:
        reader = file.read()
        print(reader)

# choosing type of enemy (another player or computer)


def choice_of_enemy():
    print("""You can play with computer or second player. 
    Press C to play with computer
    Press P to play with second player""")
    game_mode = input()
    game_mode = game_mode.upper()
    if game_mode == "C":
        comp_game_mode()
    elif game_mode == "P":
        human_game_mode()
    else:
        print("Choose better next time")
        exit()

# checking the correctness of inputs (player)


def check_input(board):
    print("Enter row number 1-10")
    number = (input("1-10: "))
    while number not in coordinates_numbers:
        print("enter valid number")
        number = (input("1-10: "))
    print('enter a letter A-J')
    letter = input("A-J: ").upper()
    while letter not in coordinates_letters:
        print('enter valid letter A-J')
        letter = input("A-J: ").upper()
    return number, letter

# define the one-masted ship (player)


def define_ships(board):
    number, letter = check_input(board)
    ship_row = int(number)*2
    for key in coordinates:
        if letter == key:
            ship_col = coordinates[key]
    board[ship_row][ship_col] = ship_one
    return ship_row, ship_col

# define the two-masted ship (player)


def define_doubleships(board):
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

# define the three-masted ship (player)


def define_tripleships(board):
    ship_row, ship_col = define_ships(board)
    draw_board(board)
    orient = input("""Choose orientation of three-masted ship:
        (or it will be random)
        (V)ertically
        (H)orizontally: """).upper()
    if orient not in orientation:
        orient = random.choice(orientation)
    if orient == 'V':
        if ship_row == 20:
            board[ship_row-2][ship_col] = ship_one
            board[ship_row-4][ship_col] = ship_one
        elif ship_row == 18:
            board[ship_row-2][ship_col] = ship_one
            board[ship_row+2][ship_col] = ship_one
        else:
            board[ship_row][ship_col+2] = ship_one
            board[ship_row][ship_col+4] = ship_one
    elif orient == "H":
        if ship_col == 20:
            board[ship_row][ship_col-2] = ship_one
            board[ship_row][ship_col-4] = ship_one
        elif ship_col == 18:
            board[ship_row][ship_col-2] = ship_one
            board[ship_row][ship_col+2] = ship_one
        else:
            board[ship_row][ship_col+2] = ship_one
            board[ship_row][ship_col+4] = ship_one

# player puts one-masted ships on the board and gets them printed -> the output is board 1 or board 2


def phase_one(board):
    define_ships(board)  # player puts ships on the board and gets them printed -> the output is board 1 or board 2
    os.system("clear")
    draw_board(board)

# player puts two-masted ships on the board and gets them printed -> the output is board 1 or board 2


def phase_double(board):
    define_doubleships(board)
    os.system("clear")
    draw_board(board)

# player puts three-masted ships on the board and gets them printed -> the output is board 1 or board 2


def phase_triple(board):
    define_tripleships(board)
    os.system("clear")
    draw_board(board)


def shoot_ships(enemy_board, board):
    draw_board(board)        # player shoots ships of the enemy -> output is board 3/ board 4
    guess_ship_row_raw = (input("Guess row 1-5: "))
    while guess_ship_row_raw not in coordinates_numbers:
        print("enter valid number")
        guess_ship_row_raw = (input("1-5: "))
    guess_ship_row = int(guess_ship_row_raw)*2

    guess_ship_col_raw = (input("Guess column A-E: "))
    while guess_ship_col_raw not in coordinates_letters:
        print('enter valid letter A-E')
        guess_ship_col_raw = (input("A-E: "))
    if guess_ship_col_raw == "A":
        guess_ship_col_raw = 2
    elif guess_ship_col_raw == "B":
        guess_ship_col_raw = 4
    elif guess_ship_col_raw == "C":
        guess_ship_col_raw = 6
    elif guess_ship_col_raw == "D":
        guess_ship_col_raw = 8
    elif guess_ship_col_raw == "E":
        guess_ship_col_raw = 10
    guess_ship_col = int(guess_ship_col_raw)
    board[guess_ship_row][guess_ship_col] = ship_one
    os.system("clear")

    if (enemy_board[guess_ship_row][guess_ship_col]) == ship_one:      # marking  good shots
        print("You sank you enemy's ship!")
        board[guess_ship_row][guess_ship_col] = u"\u2620"
        enemy_board[guess_ship_row][guess_ship_col] = u"\u2620"
    elif (enemy_board[guess_ship_row][guess_ship_col]) == u"\U0001F6E5":      # marking  good shots
        print("You sank you enemy's ship!")
        board[guess_ship_row][guess_ship_col] = u"\u2620"
        enemy_board[guess_ship_row][guess_ship_col] = u"\u2620"
    elif (enemy_board[guess_ship_row][guess_ship_col]) == u"\U0001F6F3":      # marking  good shots
        print("You sank you enemy's ship!")
        board[guess_ship_row][guess_ship_col] = u"\u2620"
        enemy_board[guess_ship_row][guess_ship_col] = u"\u2620"

    else:
        print("You missed!")                                 # marking missed shots
        board[guess_ship_row][guess_ship_col] = u"\u2717"
        enemy_board[guess_ship_row][guess_ship_col] = u"\u2717"


def phase_two_player_one(enemy_board, board):  # shooting - player's one turn + output
    print(player_one, ", your turn!")
    shoot_ships(board_two, board_three)
    draw_board(board)
    time.sleep(3)
    os.system('clear')


def phase_two_player_two(enemy_board, board):  # shooting - player's two turn + output
    print(player_two, ", your turn!")
    shoot_ships(board_one, board_four)
    draw_board(board)
    time.sleep(3)
    os.system('clear')


def welcome(board):
    draw_board(board)
    print("Put your 3 single ships on the board")
    i = 1
    while i in range(0, 4):
        phase_one(board)
        i = i+1
    print("Put 2 double ships on the board")
    k = 1
    while k in range(0, 3):
        phase_double(board)
        k = k+1
    print("Put 1 triple ship on the board")
    l = 1
    while l in range(0, 2):
        phase_triple(board)
        l = l+1
    os.system('clear')
    print("\033[8;15HThose are your ships:")
    draw_board(board)


def ending():
    print("\033[8;15H")
    print("Battle finished!")
    if all(elems in board_four for elems in board_one) and all(elems in board_three for elems in board_two):
        print(player_one, player_two, "it's a draw!")
    elif all(elems in board_four for elems in board_one):   # defining the winner
        print(player_two, ", you won!")
    elif all(elems in board_three for elems in board_two):
        print(player_one, ", you won!")


def gameplay():
    j = 1
    while j in range(0, 26):     # comparing boards - condition to end the battle
        if all(elems in board_four for elems in board_one) or all(elems in board_three for elems in board_two):
            break
        else:
            phase_two_player_one(board_two, board_three)
            phase_two_player_two(board_one, board_four)
        j = j+1
    os.system('clear')
    ending()

# game mode with second player


def human_game_mode():
    print(Fore.RESET)
    os.system('clear')
    print("First player turn\n ")
    player_one = input("What is your name?: ")
    welcome(board_one)
    input(Fore.BLUE + "Press enter to continue and invite second player: ")
    print(Fore.RESET)
    os.system('clear')
    print("Second player turn\n")
    player_two = input("What is your name?: ")
    welcome(board_two)
    input(Fore.RED + "Press enter to start the battle: ")
    print(Fore.RESET)
    os.system('clear')
    gameplay()
    escape = input(Fore.RED + "Do you want to play again?\n Press 1 for YES or press n to exit".center(80))
    print(Style.RESET_ALL)
    while escape in escape_game:
        battleship_main()
    else:
        exit()

# - - - - - - - - - - - - - - - - - - gameplay


print(" ")
print(Fore.RED + "Welcome to BattleShip Game!\n".center(80))
print(Fore.RESET)
instructions()
input(Fore.BLUE + "Press enter to start game".center(80))
choice_of_enemy()


print(Fore.RESET)
os.system('clear')
print("\033[3;15HFirst player turn\n")
player_one = input("What is your name?: ")
welcome(board_one)
input(Fore.BLUE + "\033[3;15HPress enter to continue and invite second player: ")
print(Fore.RESET)
os.system('clear')
print("\033[3;15HSecond player turn\n ")
player_two = input("What is your name?: ")
welcome(board_two)
input(Fore.RED + "\033[3;15HPress enter to start the battle: ")
print(Fore.RESET)
os.system('clear')
gameplay()
escape = input(Fore.RED + "Do you want to play again?\n Press 1 for YES or press n to exit".center(80))
print(Style.RESET_ALL)
while escape in escape_game:
    battleship_main()
else:
    exit()
