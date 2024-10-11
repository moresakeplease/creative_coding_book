import random
import time

user_wins = 0
computer_wins = 0
rounds = 3

#Fuction to roll dice
def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

#Function to Reroll
def re_roll(choices, dice_list):
    print('Rolling again...')
    for i in range(len(choices)):
        if choices[i] == 'r':
            dice_list[i] = random.randint(1,6)
    time.sleep(3)

#Function to deciding winner:
def find_winner(computer_list, user_list):
    computer_total = sum(computer_list)
    user_total = sum(user_list)
    print('Computer Total: ', computer_total)
    print('User Total: ', user_total)
    if user_total > computer_total:
        print('User Wins!')
        return 'user'
    elif user_total < computer_total:
        print('Computer Wins!')
        return 'computer'
    else:
        print('Tie Game!')
        return 'tie'

#commputer strategies
def computer_strategy1(n):
    print('Computer thinking...')
    time.sleep(3)
    choices = ''
    for i in range(n):
        if sum(computer_rolls) <= sum(user_rolls):
            choices = choices + 'r'
    return choices

def computer_strategy2(n):
    print('Computer thinking...')
    time.sleep(3)
    choices = ''
    for i in range(n):
        if computer_rolls[i] < 3:
            choices = choices + 'r'
        else:
            choices = choices + '-'
    return choices
    
def computer_strategy3(n):
    print('Computer thinking...')
    time.sleep(3)
    choices = ''
    for i in range(n):
        if computer_rolls[i] < 2:
            choices = choices + 'r'
        else:
            choices = choices + '-'
    return choices   

#Fuction choose difficulty:
def difficulty(level):
    if level == 'e':
        return computer_strategy1(number_dice)
    elif level == 'm':
        return computer_strategy2(number_dice)
    elif level == 'h':
        return computer_strategy3(number_dice)

#Start Dice Game

print("      _______                       ")
print("    / \\ °    \\        ________      ")
print("   / ° \\ ___°_\\      /° . ° / \\     ")
print("   \\ ° /      /     /°___° / ° \\    ")
print("    \\°/___°_ /      \\ °  ° \\ ° /    ")
print("                     \\ _°__°\\ /     ")
print()
print("========================================")
print()
print("      Welcome to the Dice Game!         ")
print("Where the higher number wins the round  ")
print("     Best out of 3 wins the game!       ")
print()
time.sleep(2)
print('Lets get started!')
time.sleep(2)
number_dice = input('Enter number of dice: ')
number_dice = int(number_dice)
select_level = input('Choose difficulty: Easy(e), Medium(m), Hard(h): ')
while not(select_level == 'e' or select_level == 'm' or select_level == 'h'):
    select_level = input('Input Error, Choose difficulty: Easy(e), Medium(m), Hard(h): ')
ready = input('Ready to start? Hit any key to continue')


#Initiate game
for round_num in range(1, rounds + 1):
    print('Round', round_num,)
    time.sleep(2)
    user_rolls = roll_dice(number_dice)
    print('User rolls: ', user_rolls)
    time.sleep(2)
    user_choices = input("Enter (-) to hold or (r) to roll again:")
    while len(user_choices) != number_dice:
        print('You must enter', number_dice, 'choices')
        user_choices = input("Enter - to hold or (r) to roll again:")
    re_roll(user_choices, user_rolls)
    print('Player new roll: ', user_rolls)  

    computer_rolls = roll_dice(number_dice)
    print('Computer rolls: ', computer_rolls)

    computer_choices = difficulty(select_level)
    print('Computer Choice: ', computer_choices)

    re_roll(computer_choices, computer_rolls)
    print('Computer new roll: ', computer_rolls)

    #Calling Winner
    winner = find_winner(computer_rolls, user_rolls)

    if winner == 'user':
        user_wins += 1
    elif winner == 'computer':
        computer_wins += 1

    

#Declare Winner
print("\n--- Game Over ---")
print(f"User Wins: {user_wins}, Computer Wins: {computer_wins}")
if user_wins > computer_wins:
    print("Overall Winner: User!")
elif user_wins < computer_wins:
    print("Overall Winner: Computer!")
else:
    print("Overall Result: Tie Game!")

print()



