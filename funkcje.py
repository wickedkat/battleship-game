coordinates = {"A": 2, "B": 4, "C": 6, "D" : 8, "E": 10, "F": 12, "G": 14, "H": 16, "I": 18, "J": 20}


a = input("A-J: ")
for k in slow:
    if a == k:
        b = slow[k]
print(b)
    

def define_ships(board):             # putting ships on a board
    print("Enter row number 1-10")
    ship_row_raw = (input("1-10: "))
    while ship_row_raw not in coordinates_numbers:
        print("enter valid number")
        ship_row_raw = (input("1-10: "))
    ship_row = int(ship_row_raw)*2
    print('enter a letter A-J')
    ship_col_raw = input("A-J: ")
    while ship_col_raw not in coordinates_letters:
        print('enter valid letter A-J')
        ship_col_raw = input("A-J: ")
        for key in slow:
            if ship_col_raw == key
            ship_col = slow[key]
    
    board[ship_row][ship_col] = u"\u26F5"