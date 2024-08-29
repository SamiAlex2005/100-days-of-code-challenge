start = 0
order = 0 # This variable is used to identify the PLayer 1 or 2. If order is even it's player 1(O), if it's odd it's player 2(X)
game_board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
def game_logic(order, game_board, start):
    if start == 0:
        print("Player One is always O")
        print("Player Two is always X")
        print("The first to fill three horizontally, vertically or perpendicularly wins! Enjoy!")
        start += 1
    player = int(input("\033[1;32mEnter your desired position: \033[0m"))
    if player <= 3:
        if order % 2 == 0 and game_board[0][player - 1] == "":
            game_board[0][player - 1] = "O"
            order += 1
        elif order % 2 != 0 and game_board[0][player - 1] == "":
            game_board[0][player - 1] = "X"
            order += 1
        else:
            if game_board[0][player - 1] != "":
                print("\033[1;31mThe place is already taken please try again!\033[0m")
    elif player <= 6:
        if order % 2 == 0 and game_board[1][player - 4] == "":
            game_board[1][player - 4] = "O"
            order += 1
        elif order % 2 != 0 and game_board[1][player - 4] == "":
            game_board[1][player - 4] = "X"
            order += 1
        else:
            if game_board[1][player - 4] != "":
                print("\033[1;31mThe place is already taken please try again!\033[0m")
    elif player <= 9:
        if order % 2 == 0 and game_board[2][player - 7] == "":
            game_board[2][player - 7] = "O"
            order += 1
        elif order % 2 != 0 and game_board[2][player - 7] == "":
            game_board[2][player - 7] = "X"
            order += 1
        else:
            if game_board[2][player - 7] == "":
                print("\033[1;31mThe place is already taken please try again!\033[0m")
    else:
        if player > 9 or player < 1:
            print("\033[1;31mInvalid Input Please Try Again!\033[0m")
    return order, game_board, start
   
while True:
    print(f'\t | \t |')
    print(f'      {game_board[0][0]}\t |   {game_board[0][1]}\t |  {game_board[0][2]}')
    print(f'    -------------------')
    print(f'\t | \t |')
    print(f'      {game_board[1][0]}\t |   {game_board[1][1]}\t |  {game_board[1][2]}')
    print(f'    -------------------')
    print(f'\t | \t |')
    print(f'      {game_board[2][0]}\t |   {game_board[2][1]}\t |  {game_board[2][2]}')
    print('')
    if game_board[0][0] != "" and game_board[0][0] == game_board[0][1] and game_board[0][1] == game_board[0][2]:
        if game_board[0][0] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break
    elif game_board[1][0] != "" and game_board[1][0] == game_board[1][1] and game_board[1][1] == game_board[1][2]:
        if game_board[1][0] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break 
    elif game_board[2][0] != "" and game_board[2][0] == game_board[2][1] and game_board[2][1] == game_board[2][2]:
        if game_board[2][0] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break 
    elif game_board[0][0] != "" and game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]:
        if game_board[0][0] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break
    elif game_board[0][2] != "" and game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]:
        if game_board[0][2] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break  
    elif game_board[0][0] != "" and game_board[0][0] == game_board[1][0] and game_board[1][0] == game_board[2][0]:
        if game_board[0][0] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break 
    elif game_board[0][1] != "" and game_board[0][1] == game_board[1][1] and game_board[1][1] == game_board[2][1]:
        if game_board[0][1] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break 
    elif game_board[0][2] != "" and game_board[0][2] == game_board[1][2] and game_board[1][2] == game_board[2][2]:
        if game_board[0][2] == "O":
            print("\033[1;32mPlayer One Wins!\033[0m")
            break
        else:
            print("\033[1;32mPlayer Two Wins!\033[0m")
            break 
    else:
        if order >= 9 and game_board[1][1] != "":
            print("\033[1;32mTied!\033[0m")
            break

    order, game_board, start = game_logic(order, game_board, start)