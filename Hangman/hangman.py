import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
lives = 6

chosen_word = random.choice(word_list)
placeholder = ""

#Generate as many blanks as letters in the word
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)


game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess the letter: ").lower()

    display = ""

    if guess in correct_letters:
        print("You've already entered this letter!")


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(stages[lives])

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            print(stages[lives])

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

