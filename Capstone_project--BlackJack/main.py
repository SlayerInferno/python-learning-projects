import random
from art import logo

def deal_cards():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compute_score(cards):
    '''Takes a list of cards and returns the calculated score'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 🥂"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        #Hands 2 random cards to each player
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = compute_score(user_cards)
        computer_score = compute_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            print(compare_score(user_score, computer_score))
            print("\n")
            is_game_over = True
            return
        else:
            print(f"Your cards: {user_cards}, your score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if input("Do you want to draw another card? [y/n]: ") == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 18:
        computer_cards.append(deal_cards())
        computer_score = compute_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))
    print("\n")

while input("Do you want to play a game of BlackJack? [y/n]: ") == 'y':
    print("\n" * 20)
    play_game()