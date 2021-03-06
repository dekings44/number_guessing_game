from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    '''Checks answer against guess. Returns the number of turns remaining'''
    if guess > answer:
        print(f'Your guessed number {guess} is too high\n\nGuess again')
        return turns - 1
    elif guess < answer:
        print(f'Your guessed number {guess} is too low\n\nGuess again')
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input('Choose a difficulty level. "easy" or "hard":\n')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return set_difficulty()
def game():
    print(f'WELCOME TO THE \n\n {logo}')

    print("I am thinking of a number between 1 and 100.")


    answer = randint(1, 100)

    turns = set_difficulty()
    

    guess = 0

    while guess != answer:
        print(f'You have {turns} attempts remaining to guess the correct number.')
        guess = int(input('Make a guess:\n'))

        turns = check_answer(guess, answer, turns)
        if turns == 1:
            print(f'Your have used up your lives. You have {turns} life. \n You lose')
            return

game()