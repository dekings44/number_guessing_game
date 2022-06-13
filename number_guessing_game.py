from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer):
    if guess > answer:
        print(f'Your guessed number {guess} is too high')
    elif guess < answer:
        print(f'Your guessed number {guess} is too low')
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input('Choose a difficulty level. "easy" or "hard":')
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

print('Welcome to the Guessing Game')

print("I am thinking of a number between 1 and 100.")


answer = randint(1, 100)

guess = int(input('Make a guess:\n'))
turns = set_difficulty()
print(f'You have {turns} attempts remaining to guess the correct number.')
