import random
from guess_art import logo


def check_answer(guess, answer, turns):
    """check answer against guess. Return the number of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")



EASY_LEVEL = 10
HARD_LEVEL = 5

# create a level difficulty function
def difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    turns = difficulty()

    guess = 0

    # allow the user to repeat playing till they run out of turns
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Play again.")

    
play_game()

