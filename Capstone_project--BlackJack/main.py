import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    '''Returns a random card from the deck'''
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Take list of cards and return the calculated score'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "You Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "You Win! A BlackJack 😎"
    elif u_score > 21:
        return "You Lose, you went over 😭"
    elif c_score > 21:
        return "You Win! Opponent went over 😁"
    elif u_score > c_score:
        return "You Win! 🙂"
    else:
        return "You Lose! 🙁"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        #Hands 2 random cards to each player
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: [{user_cards}], Your score: {user_score}")
        print(f"Computer first card: [{computer_cards[0]}]\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    if user_score == 0:
        print(f"Your final hand: {user_cards}, final score: BlackJack!!")
    else:
        print(f"Your final hand: {user_cards}, final score: {user_score}")

    if computer_score == 0:
        print(f"Computer's final hand: {computer_cards}, final score: BlackJack!!")
    else:
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack?[y/n]: ") == 'y':
    print("\n" * 20)
    play_game()