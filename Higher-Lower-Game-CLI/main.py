import random
from art import logo, vs
from game_data import data

#Function to take data from dictionary and return it in printable format
def format_data(account):
    '''Takes account data and returns the printable format'''
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description}, from {account_country}"

#Function to check the answer
def check_answer(user_guess, a_followers, b_followers):
    '''Take a user's guess and the follower count and returns if they got it right'''
    if a_followers > b_followers:
        return user_guess == 'A'
    else:
        return user_guess == 'B'



def game():
    print(logo)
    should_game_continue = True
    #Generates a random account from game_data.py
    account_b = random.choice(data)
    score = 0

    while should_game_continue:
        #Making account at B become the next account at position A
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        #Get follower count of each account
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        #Ask user for a guess
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        #Check if user is correct
        is_correct = check_answer(user_guess, a_followers, b_followers)

        #Clear the screen
        print("\n" * 20)
        print(logo)

        #Score keeping and user feedback
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, That's wrong. Final score: {score}")
            should_game_continue = False

game()
