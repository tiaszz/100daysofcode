import random

from hangman_art import *
from hangman_words import word_list


def get_word():
    word = random.choice(word_list)
    return word


def get_user_guess():
    guess = input("Guess a letter: ").lower()
    return guess


def check_guess(guess, word):
    for letter in word:
        if letter == guess:
            print("Right")
        else:
            print("Wrong")


word = get_word()
guess = get_user_guess()
check_guess(guess, word)
