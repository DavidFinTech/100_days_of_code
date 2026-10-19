import random
from builtins import input

import art
from game_data import data
score = 0
first_option = random.choice(data)#setting up the variables
second_option = random.choice(data)
#setting up the variables
print(art.logo)
#Logo display
print(f"Compare A: {first_option['name']}, a {first_option['description']}, from {first_option['country']}")
print(art.vs)
print(f"Against B: {second_option['name']}, a {second_option['description']}, from {second_option['country']}")
#displaying the variables
while True:
    question = input("Who has more followers? Type 'A' or 'B': ").upper()
    if (question == 'A' and first_option['follower_count'] > second_option['follower_count']) or (question == 'B' and second_option['follower_count'] > first_option['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}")
        first_option = second_option
        print(f"Compare A: {first_option['name']}, a {first_option['description']}, from {first_option['country']}")
        print(art.vs)
        second_option = random.choice(data)
        print(f"Against B: {second_option['name']}, a {second_option['description']}, from {second_option['country']}")
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break


