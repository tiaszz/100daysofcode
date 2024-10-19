import random

from hangman_art import *
from hangman_words import word_list


lives = 6

print(logo)

word = random.choice(word_list)

placeholder = ""

for position in range(len(word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letter = []
guessed_letter = []

while not game_over:
    print(f"**********************{lives} lives left**********************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letter:
        print(f"You've already guessed {guess}")
        continue

    if guess not in guessed_letter:
        guessed_letter.append(guess)

    display = ""
    for letter in word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in word:
        print(f"The letter {guess} is not in the word")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"****************IT WAS {word}! YOU LOSE****************")

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("****************YOU WIN****************")
