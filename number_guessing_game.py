from random import randint




def check_answer(guess, answer):
    if guess > answer:
        print(f'Your guessed number {guess} is too high')
    elif guess < answer:
        print(f'Your guessed number {guess} is too low')
    else:
        print(f"You got it! The answer was {answer}")
print('Welcome to the Guessing Game')

print("I am thinking of a number between 1 and 100.")


answer = randint(1, 100)

guess = int(input('Make a guess:\n'))
