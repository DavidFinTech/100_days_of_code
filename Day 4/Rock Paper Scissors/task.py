import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choose = int(input("Welcome to Rock Paper Scissors game  Type 0 for rock, 1 for paper, 2 for scissors\n"))
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)

computer_choice = random.randint(0,2)
print("Computer chose: " + str(computer_choice))

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)


if any([computer_choice == 0 and choose == 2, computer_choice == 2 and choose == 1, computer_choice == 1 and choose == 0]):
    result ="you lost"

elif computer_choice == choose:
    result = "its a draw"

else:
    result = "you won"

print(result)


fruits = ["apple", "orange", "banana", "strawberry"]
for fruit in fruits:
    print(fruit)
    print(fruit.title())
