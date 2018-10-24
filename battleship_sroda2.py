import colorama
from colorama import init
from colorama import Fore, Back, Style
import os
import time
import random

board_primal = [['  ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' ',
                'F', ' ', 'G', ' ', 'H', ' ', 'I', ' ', 'J', ' '],  # player1 ships
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
                ['  ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
board_one = [x[:] for x in board_primal]
board_two = [x[:] for x in board_primal]
board_three = [x[:] for x in board_primal]
board_four = [x[:] for x in board_primal]

# variables

coordinates = {"A": 2, "B": 4, "C": 6, "D": 8, "E": 10, "F": 12, "G": 14, "H": 16, "I": 18, "J": 20}
coordinates_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
coordinates_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
orientation = ['V', 'H']
ship_one = u"\u26F5"
ship_two = u"\U0001F6E5"
ship_three = u"\U0001F6F3"
miss = u"\u2717"
sunk = u"\u2620"


# - - - - - - - - - - - - - - - - - - - - - def functions
# drawing board
def draw_board(board):
    print(Style.BRIGHT)
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

# define one-masted ships by computer


def define_comp_ships(board):
    i = 0
    while i < 4:
        ship_row = random.randrange(2, 21, 2)
        ship_col = random.randrange(2, 21, 2)
        if board[ship_row][ship_col] == ship_one:
            ship_row = random.randrange(2, 21, 2)
            ship_col = random.randrange(2, 21, 2)
        else:
            board[ship_row][ship_col] = ship_one
            i += 1

# define two-masted ships by computer


def define_comp_doubleships(board):
    i = 0
    while i < 3:
        ship_row = random.randrange(2, 19, 2)
        ship_col = random.randrange(2, 19, 2)
        ship_row1 = ship_row + 2
        ship_col1 = ship_col + 2
        if board[ship_row][ship_col] == ship_one or board[ship_row1][ship_col] == ship_one:
            ship_row = random.randrange(2, 19, 2)
            ship_col = random.randrange(2, 19, 2)
        elif board[ship_row][ship_col] == ship_one or board[ship_row][ship_col1] == ship_one:
            ship_row = random.randrange(2, 19, 2)
            ship_col = random.randrange(2, 19, 2)
        else:
            los = random.randint(1, 2)
            if los == 1:
                board[ship_row][ship_col] = ship_one
                board[ship_row][ship_col1] = ship_one
                i += 1
            else:
                board[ship_row][ship_col] = ship_one
                board[ship_row1][ship_col] = ship_one
                i += 1

# define three-masted ships by computer


def define_comp_tripleships(board):
    i = 0
    while i < 1:
        ship_row = random.randrange(2, 17, 2)
        ship_col = random.randrange(2, 17, 2)
        ship_row1 = ship_row + 2
        ship_col1 = ship_col + 2
        ship_row2 = ship_row + 4
        ship_col2 = ship_col + 4
        if board[ship_row][ship_col] == ship_one or board[ship_row1][ship_col] == ship_one or board[ship_row2][ship_col] == ship_one:
            ship_row = random.randrange(2, 17, 2)
            ship_col = random.randrange(2, 17, 2)
        elif board[ship_row][ship_col] == ship_one or board[ship_row][ship_col1] == ship_one or board[ship_row][ship_col2] == ship_one:
            ship_row = random.randrange(2, 17, 2)
            ship_col = random.randrange(2, 17, 2)
        else:
            los = random.randint(1, 2)
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

# shoot ship define - player


def shoot_ships(enemy_board, board):
    draw_board(board)        # player shoots ships of the enemy -> output is board 3/ board 4
    number, letter = check_input(board)
    guess_ship_row = int(number)*2
    for key in coordinates:
        if letter == key:
            guess_ship_col = coordinates[key]
    board[guess_ship_row][guess_ship_col] = ship_one
    os.system("clear")

    if (enemy_board[guess_ship_row][guess_ship_col]) == ship_one:      # marking  good shots
        print("You sank you enemy's ship!")
        board[guess_ship_row][guess_ship_col] = sunk
        enemy_board[guess_ship_row][guess_ship_col] = sunk
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
        board[guess_ship_row][guess_ship_col] = miss
        enemy_board[guess_ship_row][guess_ship_col] = miss

# shoot ship - define - comp


def shoot_ships_comp(enemy_board, board):
    i = 0
    while i < 1:
        guess_ship_row = random.randrange(2, 21, 2)
        guess_ship_col = random.randrange(2, 21, 2)
        if enemy_board[guess_ship_row][guess_ship_col] == miss or enemy_board[guess_ship_row][guess_ship_col] == sunk:
            guess_ship_row = random.randrange(2, 21, 2)
            guess_ship_col = random.randrange(2, 21, 2)
        else:
            if (enemy_board[guess_ship_row][guess_ship_col]) == ship_one:
                print("I sank your ship!")
                board[guess_ship_row][guess_ship_col] = sunk
                enemy_board[guess_ship_row][guess_ship_col] = sunk
                i += 1
            else:
                print("I missed!")                                 # marking missed shots
                board[guess_ship_row][guess_ship_col] = miss
                enemy_board[guess_ship_row][guess_ship_col] = miss
                i += 1


# shoot ships player one

def phase_two_player_one(enemy_board, board):  # shooting - player's one turn + output
    print(player_one, ", your turn!")
    shoot_ships(board_two, board_three)
    draw_board(board)
    time.sleep(3)
    os.system('clear')

# shoot ships player two


def phase_two_player_two(enemy_board, board):  # shooting - player's two turn + output
    print(player_two, ", your turn!")
    shoot_ships(board_one, board_four)
    draw_board(board)
    time.sleep(3)
    os.system('clear')

# shoot ships phase - computer


def phase_two_comp(enemy_board, board):
    print("My turn!")
    shoot_ships_comp(board_one, board_four)
    draw_board(board)
    time.sleep(3)
    os.system('clear')

# putting all ships by player(s)


def welcome(board):
    draw_board(board)
    print("Put your 4 single ships on the board")
    a = 0
    while i in range(0, 4):
        phase_one(board)
        a += 1
    print("Put 3 double ships on the board")
    b = 0
    while k in range(0, 3):
        phase_double(board)
        b += 1
    print("Put 1 triple ship on the board")
    c = 0
    while l in range(0, 1):
        phase_triple(board)
        c += 1
    os.system('clear')
    print("\033[8;15HThose are your ships:")
    draw_board(board)

# ending when two players play


def ending():
    print("\033[8;15H")
    print("Battle finished!")
    if all(elems in board_four for elems in board_one) and all(elems in board_three for elems in board_two):
        print(player_one, player_two, "it's a draw!")
    elif all(elems in board_four for elems in board_one):   # defining the winner
        print(player_two, ", you won!")
    elif all(elems in board_three for elems in board_two):
        print(player_one, ", you won!")

# ending for human and computer


def ending_comp():
    print("\033[8;15H")
    print("Battle finished!")
    if all(elems in board_four for elems in board_one) and all(elems in board_three for elems in board_two):
        print(player_one, "it's a draw!")
    elif all(elems in board_four for elems in board_one):
        print("I won!")
    elif all(elems in board_three for elems in board_two):
        print(player_one, ", you won!")

# gameplay for two players


def gameplay():
    j = 1
    while j in range(0, 100):     # comparing boards - condition to end the battle
        if all(elems in board_four for elems in board_one) or all(elems in board_three for elems in board_two):
            break
        else:
            phase_two_player_one(board_two, board_three)
            phase_two_player_two(board_one, board_four)
        j = j+1
    os.system('clear')
    ending()

# gameplay fo player and computer


def gameplay_comp():
    j = 1
    while j in range(0, 100):     # comparing boards - condition to end the battle
        if all(elems in board_four for elems in board_one) or all(elems in board_three for elems in board_two):
            break
        else:
            phase_two_player_one(board_two, board_three)
            phase_two_comp(board_one, board_four)
        j = j+1
    os.system('clear')
    ending_comp()

# game mode with second player


def human_game_mode():
    global player_one
    global player_two
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


# game mode with computer

def comp_game_mode():
    global player_one
    print(Fore.RESET)
    os.system('clear')
    print("Your turn\n ")
    player_one = input("What is your name?: ")
    welcome(board_one)
    define_comp_ships(board_two)
    define_comp_doubleships(board_two)
    define_comp_tripleships(board_two)
    input(Fore.RED + "Press enter to start the battle: ")
    print(Fore.RESET)
    os.system('clear')
    gameplay_comp()


# - - - - - - - - - - - - - - - - - - gameplay
print(" ")
print(Fore.RED + "Welcome to BattleShip Game!\n".center(80))
print(Fore.RESET)
instructions()
input(Fore.BLUE + "Press enter to start game".center(80))
choice_of_enemy()
print("Thank you for playing".center(80))
exit()
