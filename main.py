from answer import Answer


class GameplayController:

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.player_valid = False

    def verify_player(self, player_ans):
        if player_ans.valid:
            self.player_valid = True
        else:
            self.player_valid = False

    def determine_winner(self, player, program):
        if player.number == program.number:
            self.draws += 1
            return 'Draw'
        elif player.number == 1 and program.number == 2:
            self.losses += 1
            return 'Program'
        elif player.number == 1 and program.number == 3:
            self.wins += 1
            return 'Player'
        elif player.number == 2 and program.number == 1:
            self.wins += 1
            return 'Player'
        elif player.number == 2 and program.number == 3:
            self.losses += 1
            return 'Program'
        elif player.number == 3 and program.number == 1:
            self.losses += 1
            return 'Program'
        elif player.number == 3 and program.number == 2:
            self.wins += 1
            return 'Player'


# Initial Display
print('''-----------------------------------------------------------------------------------------------------------------------
Rock Paper Scissors
Enter in 1 - Rock, 2 Paper, or 3 Scissors. The program will then choose its answer randomly and determine a winner
-----------------------------------------------------------------------------------------------------------------------''')

game_handler = GameplayController()

# Main  Gameplay Loop
while True:
    print('''
    Enter any Option:
        1 - Rock
        2 - Paper
        3 - Scissors\n''')

    # Player picks until a valid answer is given
    user_input = Answer(input('Choose an Option: '))
    game_handler.verify_player(user_input)
    while not game_handler.player_valid:
        user_input = Answer(input('Choose a valid Option: '))
        game_handler.verify_player(user_input)

    # Program Chooses Now
    program_selection = Answer('1')
    program_selection.generate_answer()

    # Determine winner and show results
    results = game_handler.determine_winner(user_input, program_selection)

    print('========================= Player Choice ============================')
    print(user_input.number, ' - ', user_input.name)
    print('====================================================================\n')
    print('========================= Program Choice ===========================')
    print(program_selection.number, ' - ', program_selection.name)
    print('====================================================================')

    match results:
        case 'Draw':
            print('\nThe match is a Draw')
        case 'Player':
            print('\nYou have won')
        case 'Program':
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

    Wins: {game_handler.wins}
    Losses: {game_handler.losses}
    Draws {game_handler.draws}

    Win Percentage: {round(game_handler.wins / (game_handler.wins + game_handler.losses + game_handler.draws), 2)}%''')
