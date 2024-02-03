
def new_game():
    A = 0
    player_choices = []
    Correct_choices = 0

    for question in questions:
        print(question)

        for option in options[A]:
            print(option)
        A += 1
        player_choice = input('chose A,B,C,D:  ').upper()
        player_choices.append(player_choice)
        Correct_choices += check(questions.get(question),player_choice)

    score_display(Correct_choices,player_choices)
def check(right_answer,player_choice):

    if right_answer == player_choice:
        print('Correct')
        return 1

    else:
        print('Not Correct')
        return 0
def score_display(Correct_choices, player_choices):
    print('<--------------->')
    print('Result')
    print('<--------------->')

    print('Answer:', end='')
    for i in questions:
        print(questions.get(i), end='')
    print()
    print('player_choices:', ' '.join(player_choices), end='')
    print()
    score = int((Correct_choices/len(questions))*100)
    print('player score: ' f'{score} %')
def playagain():
    player = input('Do you wnat to play again ( Yes or No)').upper()
    if player == 'Yes':
        return True
    else:
        return False

#dictionary
questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}
#list
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
new_game()
while playagain():
    new_game()
print('Byeeee')
