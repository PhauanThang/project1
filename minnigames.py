import random
while True:
    player_choices = None
    choices = {'rock', 'paper', 'scissor'}

    while player_choices not in list(choices):
        player_choices = input(f' select {choices} :').lower()
    computer_choices = random.choice(list(choices))
    print(f'computer plays {computer_choices}')
    print('you play {}'.format(player_choices))
    if player_choices == computer_choices:
        print('Tie!')
    elif player_choices == 'rock':
        if computer_choices == 'paper':
                print('you lose')
        if computer_choices == 'scissor':
                print('you win')
    elif player_choices == 'paper':
        if computer_choices == 'scissor':
                print('you lose')
        if computer_choices == 'rock':
                print('you win')
    elif player_choices == 'scissor':
        if computer_choices == 'rock':
                print('you lose')
        if computer_choices == 'paper':
                print('you win')
    player_choices = input('do you want to play again(y/n)').lower()
    if player_choices != 'yes':
            break
print('bye')
