import os 

order = 0 # This variable is used to identify the PLayer 1 or 2. If order is even it's player 1(O), if it's odd it's player 2(X)
game_board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
def game_logic(order, game_board):
    if player > 9 or player < 1:
        print("\033[1;31mInvalid Input PLease Try Again!\033[0m")
    else:
        row = (player - 1) // 3
        col = (player - 1) % 3
        if game_board[row][col] == "":
            if order % 2 == 0:
                game_board[row][col] = "O"
                order += 1
            else:
                game_board[row][col] = "X"
                order += 1
        else:
            print("\033[1;31mThe box is already filled, Please Try Again!\033[0m")
    return order, game_board

def result_handler(game_board):
    for i in range(0, 3):
        if game_board[i][0] != "" and game_board[i][0] == game_board[i][1] == game_board[i][2]:
            return True
        elif game_board[0][i] != "" and game_board[0][i] == game_board[1][i] == game_board[2][i]:
            return True 
    if game_board[0][0] != "" and game_board[0][0] == game_board[1][1] == game_board[2][2]:
        return True
    elif game_board[0][2] != "" and game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return True
    else:
        if order >= 9:
            return False
def board_printer():
    print(f'\t | \t |')
    print(f'      {game_board[0][0]}\t |   {game_board[0][1]}\t |  {game_board[0][2]}')
    print(f'    -------------------')
    print(f'\t | \t |')
    print(f'      {game_board[1][0]}\t |   {game_board[1][1]}\t |  {game_board[1][2]}')
    print(f'    -------------------')
    print(f'\t | \t |')
    print(f'      {game_board[2][0]}\t |   {game_board[2][1]}\t |  {game_board[2][2]}')
    print('')
while True:
    board_printer()
    if order == 0:
        print("Player One is always O")
        print("Player Two is always X")
        print("The first to fill three horizontally, vertically or perpendicularly wins! Enjoy!")
    player = int(input("Enter ur desired position: "))
    os.system('clear')
    order, game_board = game_logic(order, game_board)
    result_handler(game_board)
    if result_handler(game_board) == True:
        board_printer()
        if order % 2 == 0:
            print(f"\033[1;32mX wins!\033[0m")
            break
        else:
            print(f"\033[1;32mO wins!\033[0m")
            break
    else:
        if result_handler(game_board) == False:
            board_printer()
            print('\033[1;32mTied!\033[0m')
            break
    
