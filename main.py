import random

# Initial Display
print('''Rock Paper Scissors
Enter in 1 - Rock, 2 Paper, or 3 Scissors. The program will then choose its answer randomly and determine a winner''')

# Vars
wins = 0
losses = 0
draws = 0

# Functions
def convertToWord(number):
    match number:
        case 1:
            return 'Rock'
        case 2:
            return 'Paper'
        case 3:
            return 'Scissors'


def convertToInt(word):
    match word:
        case 'Rock':
            return 1
        case 'Paper':
            return 2
        case 'Scissors':
            return 3


def validateInput(player_input):
    if player_input in range(1,4):
        return True
    else:
        return False


def checkResults(user, program):
    if user == program:
        return 'Draw'
    elif user == 1 and program == 2:
        return 'Program'
    elif user == 1 and program == 3:
        return 'Player'
    elif user == 2 and program == 1:
        return 'Player'
    elif user == 2 and program == 3:
        return 'Program'
    elif user == 3 and program == 1:
        return 'Program'
    elif user == 3 and program == 2:
        return 'Player'


# Main  Gameplay Loop
while True:
    print('''
    Enter any one  of the shown numbers:
        1 - Rock
        2 - Paper
        3 - Scissors\n''')

    # Player picks number until a valid answer is given
    user_input = input('Choose an Option: ')
    valid_choice = validateInput(int(user_input))
    while not valid_choice:
        user_input = input('Enter a valid option: ')
        valid_choice = validateInput(int(user_input))

    # Program Chooses Now
    program_selection = random.randint(1, 3)

    # Determine winner and show results
    results = checkResults(int(user_input), program_selection)
    print(f'''
        Your Choice: {convertToWord(int(user_input))}
        Program\'s Choice: {convertToWord(program_selection)}''')

    if results == 'Draw':
        draws += 1
        print('\nThe match is a Draw')
    elif results == 'Player':
        wins += 1
        print('\nYou have won')
    elif results == 'Program':
        losses += 1
        print('\nYou have lost')

    # Again?
    replay = input('Play Again? (y/n)')
    if replay.lower() == 'n' or replay.lower() == 'no':
        break
    else:
        continue

# Print Player Results
print(f'''
    Your Stats:

    Wins: {wins}
    Losses: {losses}
    Draws {draws}

    Win Percentage: {round(wins / (wins + losses + draws),2)}%''')
