import random

options = ['rock', 'paper', 'scissors']
timer = 0
computer_score = 0
user_score = 0

def game_logic(timer, computer_score, user_score):
    if user == 'rock' and computer == 'scissors':
        user_score += 1
        print(f"User wins! Rock always beats Scissors! {user_score} - {computer_score}")
        timer += 1
    elif user == 'scissors' and computer == 'paper':
        user_score += 1
        print(f"User wins! Scissors always beats Paper! {user_score} - {computer_score}")
        timer += 1  
    elif user == 'paper' and computer == 'rock':
        user_score += 1
        print(f"User wins! Paper always beats Rock! {user_score} - {computer_score}")
        timer += 1
    elif computer == 'rock' and user == 'scissors':
        computer_score += 1
        print(f"Computer wins! Rock always beats Scissors! {user_score} - {computer_score}")
        timer += 1
    elif computer == 'scissors' and user == 'paper':
        computer_score += 1
        print(f"Computer wins! Scissors always beats Paper! {user_score} - {computer_score}")
        timer += 1
    elif computer == 'paper' and user == 'rock':
        computer_score += 1
        print(f"Computer wins! Paper always beats Rock! {user_score} - {computer_score}")
        timer += 1
    else:
        if computer == user:
            user_score += 1
            computer_score += 1
            print(f'Tie! {user_score} - {computer_score}')
            timer += 1
    return timer, computer_score, user_score 

def final_game_logic(user_score, computer_score):
    if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        user_score += 1
        if user_score > computer_score:
            print(f"Victory for the User! {user_score} - {computer_score}")
        elif user_score < computer_score:
            print(f"User wins this round but lost overall! {user_score} - {computer_score}")
        else:
            print(f'Tie! {user_score} - {computer_score}')
    elif (computer == 'rock' and user == 'scissors') or (computer == 'scissors' and user == 'paper') or (computer == 'paper' and user == 'rock'):
        computer_score += 1
        if computer_score > user_score:
            print(f"Victory for Computer! {user_score} - {computer_score}")
        elif computer_score < user_score:
            print(f'Computer wins this round but lost overall! {user_score} - {computer_score}')
        else:
            print(f'Tie! {user_score} - {computer_score}')
    else:
        if computer == user:
            computer_score += 1
            user_score += 1
            if computer_score > user_score:
                print(f'Tied this round but Computer wins overall! {user_score} - {computer_score}')
            elif computer_score < user_score:
                print(f'Tied this round but User wins overall! {user_score} - {computer_score}')
            else:
                print(f'Tie! {user_score} - {computer_score}')
while timer < 3:
    random_int = random.randint(0,2)
    computer = options[random_int]
    user = input("Rock, Paper, Scissors: ").lower()
    if timer < 2:
        timer, computer_score, user_score = game_logic(timer, computer_score, user_score)
    else:
        final_game_logic(user_score, computer_score)
        break