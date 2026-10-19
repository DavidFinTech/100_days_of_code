import random
from art import logo


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    chosen_number = random.randint(1, 100)
    difficulty_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    while difficulty_chosen not in ["easy", "hard"]:
        difficulty_chosen = input("Invalid! Pick 'easy' or 'hard': ").lower()

    easy_difficulty = 10
    hard_difficulty = 5

    def make_a_guess(difficulty):
        print(f'You have {difficulty} attempts remaining to guess the number.')
        not_the_number = True
        play_again = "no"  # Store the choice here

        while not_the_number:
            guess = int(input('Make a guess: '))

            if guess != chosen_number:
                difficulty -= 1
                if chosen_number > guess:
                    print('Too low\nGuess Again')
                elif chosen_number < guess:
                    print('Too high\nGuess Again')

                print(f'You have {difficulty} attempts remaining to guess the number.')

                if difficulty == 0:
                    play_again = input("You've run out of guesses! Would you like to play again? ").lower()
                    not_the_number = False

            else:
                print('You guessed the correct number! You win!')
                play_again = input("Would you like to play again? ").lower()
                not_the_number = False

        # ONLY restart if they chose 'yes'
        if play_again == "yes":
            play_game()
        else:
            print("Goodbye!")

    if difficulty_chosen == "easy":
        make_a_guess(easy_difficulty)
    elif difficulty_chosen == "hard":
        make_a_guess(hard_difficulty)


play_game()




