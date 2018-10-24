import random
import colorama
from colorama import init
from colorama import Fore, Back, Style

board_one = [[' ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' '],  # player1 ships
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['1', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['2', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['3', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['4', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['5', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
board_two = [[' ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' '],  # comp2 ships
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['1', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['2', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['3', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['4', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['5', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
             [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
board_three = [[' ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' '],  # player1 shots
               [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['1', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
               [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['2', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
               [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['3', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
               [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['4', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
               [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
               ['5', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
               [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
board_four = [[' ', ' ', 'A', ' ', 'B', ' ', 'C', ' ', 'D', ' ', 'E', ' '],  # comp2 shots
              [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['1', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['2', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['3', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['4', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['5', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|', ' ', '|'],
              [' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

coordinates_numbers = ['1', '2', '3', '4', '5']
coordinates_letters = ['A', 'B', 'C', 'D', 'E']


def draw_board(board):
    print(Style.BRIGHT)  # showing board in 5 lines
    print(Back.CYAN)
    for s in board:
        print(*s)
    print(Style.RESET_ALL)


def choice_of_enemy():
    print("""You can play with computer or second player. 
    Press C to play with computer
    Press P to play with second player""")
    game_mode = input()
    if game_mode == "C":
        comp_game_mode()
    elif game_mode == "P":
        human_game_mode()
    else:
        print("Choose better next time")
        exit()


def human_game_mode():
    print(chr(27) + "[2J")
    print("\033[3;15HFirst player turn\n")
    player_one = input("What is your name?: ")
    welcome(board_one)
    input(Fore.BLUE + "\033[3;15HPress enter to continue and invite second player: ")
    print(Fore.RESET)
    print(chr(27) + "[2J")
    print("\033[3;15HSecond player turn\n ")
    player_two = input("What is your name?: ")
    welcome(board_two)
    input(Fore.RED + "\033[3;15HPress enter to start the battle: ")
    print(Fore.RESET)
    print(chr(27) + "[2J")
    gameplay()
    escape = input(Fore.RED + "Do you want to play again?\n Press 1 for YES or press n to exit".center(80))
    print(Style.RESET_ALL)
    while escape in escape_game:
        battleship_main()
    else:
        exit()


def define_comp_ships(board):
    i = 0
    while i < 3:
        ship_row = random.randrange(2, 11, 2)
        ship_col = random.randrange(2, 11, 2)
        if board[ship_row][ship_col] == u"\u26F5":
            ship_row = random.randrange(2, 11, 2)
            ship_col = random.randrange(2, 11, 2)
        else:
            board[ship_row][ship_col] = u"\u26F5"
            i += 1

def define_ships(board):             # putting ships on a board
    print('Enter row number 1-5')
    ship_row_raw = (input("1-5: "))
    while ship_row_raw not in coordinates_numbers:
        print("enter valid number")
        ship_row_raw = (input("1-5: "))
    ship_row = int(ship_row_raw)*2
    print('enter a letter A-E')
    ship_col_raw = input("A-E: ")
    while ship_col_raw not in coordinates_letters:
        print('enter valid letter A-E')
        ship_col_raw = input("A-E: ")
    if ship_col_raw == "A":
        ship_col_raw = 2
    elif ship_col_raw == "B":
        ship_col_raw = 4
    elif ship_col_raw == "C":
        ship_col_raw = 6
    elif ship_col_raw == "D":
        ship_col_raw = 8
    elif ship_col_raw == "E":
        ship_col_raw = 10
    ship_col = int(ship_col_raw)
    board[ship_row][ship_col] = u"\u26F5"
    draw_board(board_two)


def welcome(board):
    draw_board(board)
    print("Put your ships on the board")
    i = 1
    while i in range(0, 3):
        define_ships(board)
        i = i+1
    print(chr(27) + "[2J")
    print("\033[8;15HThose are your ships:")
    draw_board(board)

def shoot_ships(enemy_board, board):         # player shoots ships of the enemy -> output is board 3/ board 4
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
    board[guess_ship_row][guess_ship_col] = u"\u26F5"
    if (enemy_board[guess_ship_row][guess_ship_col]) == u"\u26F5":      # marking  good shots
        print("You sank you enemy's ship!")
        board[guess_ship_row][guess_ship_col] = u"\u2620"
        enemy_board[guess_ship_row][guess_ship_col] = u"\u2620"
    else:
        print("You missed!")                                 # marking missed shots
        board[guess_ship_row][guess_ship_col] = u"\u2717"
        enemy_board[guess_ship_row][guess_ship_col] = u"\u2717"

def shoot_ships_comp(enemy_board, board):         # comp shoots ships of the enemy -> output is board 3/ board 4
    i = 0
    while i < 1:
        guess_ship_row = random.randrange(2, 11, 2)
        guess_ship_col = random.randrange(2, 11, 2)
        if enemy_board[guess_ship_row][guess_ship_col] == u"\u2717" or enemy_board[guess_ship_row][guess_ship_col] == u"\u2620":
            guess_ship_row = random.randrange(2, 11, 2)
            guess_ship_col = random.randrange(2, 11, 2)
        else:
            if (enemy_board[guess_ship_row][guess_ship_col]) == u"\u26F5":      # marking  good shots
                print("I sank your ship!")
                board[guess_ship_row][guess_ship_col] = u"\u2620"
                enemy_board[guess_ship_row][guess_ship_col] = u"\u2620"
                i += 1
            else:
                print("I missed!")                                 # marking missed shots
                board[guess_ship_row][guess_ship_col] = u"\u2717"
                enemy_board[guess_ship_row][guess_ship_col] = u"\u2717"
                i += 1



def phase_two_player_one(enemy_board, board):  # shooting - player's one turn + output
    print(player_one, ", your turn!")
    shoot_ships(board_two, board_three)
    draw_board(board)

def phase_two_comp(enemy_board, board):  # shooting - comp turn + output
    print("It's my turn!")
    shoot_ships_comp(board_one, board_four)
    draw_board(board)


def gameplay_comp():
    j = 1
    while j in range(0, 26):     # comparing boards - condition to end the battle
        if all(elems in board_four for elems in board_one) or all(elems in board_three for elems in board_two):
            break
        else:
            phase_two_player_one(board_two, board_three)
            phase_two_comp(board_one, board_four)
        j = j+1
    print(chr(27) + "[2J")
    ending()

def ending():
    print("\033[8;15H")
    print("Battle finished!")
    if all(elems in board_four for elems in board_one) and all(elems in board_three for elems in board_two):
        print(player_one, player_two, "it's a draw!")
    elif all(elems in board_four for elems in board_one):   # defining the winner
        print(player_two, ", you won!")
    elif all(elems in board_three for elems in board_two):
        print(player_one, ", you won!")

def instructions():
    with open("instructions.txt", "r") as file:
        reader = file.read()
        print(reader)






print(" ")
print(Fore.RED + "Welcome to BattleShip Game!\n".center(80))
print(Fore.RESET)
instructions()
input(Fore.BLUE + "Press enter to start game".center(80))
print(Fore.RESET)
choice_of_enemy()

# tu będzie computer game mode

print(chr(27) + "[2J")
print("\033[3;15HFirst player turn\n")
player_one = input("What is your name?: ")
player_two = ("")
welcome(board_one)
define_comp_ships(board_two)
input(Fore.RED + "\033[3;15HPress enter to start the battle: ")
print(Fore.RESET)
print(chr(27) + "[2J")
gameplay_comp()














