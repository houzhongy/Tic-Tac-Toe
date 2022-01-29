#Tic-Tac-Toe Game

"""
tic tac toe board 
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]

user_input -> 1-9
exception: prompt for user input again
check if user_input is already taken
add it to the board

check if user won: checking rows, columns and diagonals
toggle between users upon successful moves
"""

def print_board(board):
    for row in board:
        for slot in row:
            print(slot, end = " ")
        print()

def quit(user_input):
    if user_input == "q": 
        print("Thanks for playing!!!")
        return True
    else: return False

def check_input(user_input):
    #check if it is a number and within 1-9
    if not user_input.isnumeric() or int(user_input) > 9 or int(user_input) < 1:
        print("This is not a valid number")
        return False
    else:
        return True

def is_taken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":   
        return True
    return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = int(user_input % 3)
    return (row, col)

def add_to_board(coords, active_user, board):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(active_user):
    if active_user: return "X"
    else: return "O"

def is_win(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diagonals(user, board):return True
    
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False

def check_diagonals(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    return False
    
board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

user = True #player 1 if True, player 2 if False

turns = 0 #to track for draw

while(True):
    if turns >= 9:
        print_board(board)
        print("Its a draw!!!")
        break
    active_user = current_user(user)
    print_board(board)
    user_input = input("Please enter a position 1 - 9: ").lower()
    if quit(user_input): break
    if not check_input(user_input):
        continue
    user_input = int(user_input) - 1
    if is_taken(coordinates(user_input), board):
        print("The position is already taken, please choose another position!")
        continue
    else:
        add_to_board(coordinates(user_input), active_user, board)
        if is_win(active_user, board):
            print_board(board)
            print("Player " + active_user + " has won!")
            break

    user = not user #Change to player2's turn
    turns += 1
