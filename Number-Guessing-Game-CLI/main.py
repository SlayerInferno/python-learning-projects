import random
from art import logo
TURNS_HARD_DIFFICULTY = 5
TURNS_EASY_DIFFICULTY = 10

def numbergen():
    '''Returns a random number between 1 and 100'''
    return random.randint(1,100)
def set_difficulty():
    '''Function to return attempts for 'hard' and 'easy' difficulty respectively.'''
    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return TURNS_EASY_DIFFICULTY
    elif difficulty == 'hard':
        return TURNS_HARD_DIFFICULTY
    else:
        print("Invalid input detected, please try again.")
        return -1
def check_answer(user_guess, answer, attempts):
    '''Checks the answer against user's guess, returns the number of turns remaining'''
    if user_guess > answer:
        print("Too high.")
        return attempts - 1
    elif user_guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}")
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    answer = numbergen()
    attempts = set_difficulty()
    guess = 0

    while guess != answer:
        if attempts == -1:
            #Exits the game upon an invalid input during set_difficulty()
            return
        print(f"You have {attempts} attempts remaining to guess the number")
        #Let user guess a number
        guess = int(input("Make a guess: "))
        #Track the number of turns remaining, reduce by 1 if guess is wrong
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()