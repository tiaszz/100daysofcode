from art import logo
import random


def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, comp_score):
    if u_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, opponent has blackjack"
    elif u_score == 0:
        return "Win with a blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif u_score > comp_score:
        return "You win"
    else:
        return "You lose"


def game_loop():

    print(logo)

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if (
            user_score == 0
            or computer_score == 0
            or user_score > 21
            or computer_score > 21
        ):
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, time 'n' to pass: ")
            if another_card == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final socre: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want play a game of blackjack? type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game_loop()
