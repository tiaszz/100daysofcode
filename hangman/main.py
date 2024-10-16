import random

from hangman_art import *
from hangman_words import word_list


lives = 6

word = random.choice(word_list)
print(word)

placeholder = ""

for position in range(len(word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()

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
        lives -= 1

    print(stages[lives])

    if "_" not in display:
        print("You win")
        game_over = True

    if lives == 0:
        print("You lose")
        game_over = True
