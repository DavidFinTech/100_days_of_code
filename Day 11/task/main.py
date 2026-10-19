import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # 0 represents Blackjack

    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a tie!"
    elif computer_score == 0:
        return "Computer hit Blackjack, you lose!"
    elif user_score == 0:
        return "Blackjack, you win!"
    elif user_score > 21:
        return "You went over! You lose!"
    elif computer_score > 21:
        return "Computer went over, you win!"
    elif user_score > computer_score:
        return "Your hand is higher than computer's, you win!"
    else:
        return "Computer's hand is higher than yours, you lose!"

def clear_screen():
    print("\n" * 100)

def play_game():
    print(logo)
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# 1. Ask the initial question once at the start
first_time = True

while True:
    if first_time:
        user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        first_time = False
    else:
        user_choice = input("Do you want to restart the game? Type 'y' or 'n': ").lower()

    if user_choice == "y":
        clear_screen()  # Clears previous output
        play_game()     # Calls game function (which prints the logo)
    else:
        print("Thanks for playing! Goodbye.")
        break