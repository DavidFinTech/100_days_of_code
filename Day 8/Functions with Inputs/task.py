#def greet():
    #print("Hello World")
    #print("Hello World")
   #print("Hello World")
from pickle import EMPTY_LIST


#greet()

def greet_with_input(name):
    print("Hello " + name)
    print("How are you? " + name)
    print(f"I love you {name}")

greet_with_input("David")
#name = parameter

#def life_in_weeks(user_age):

    #x = str((90 - int(user_age)) * 52)
    #print("You have " + x + " weeks left")
#life_in_weeks("22")

#def greet_with(name1, location):
   # print(f"Hello {name1}")
   # print(f"What is it like in this {location}")

#greet_with(location="David", name1="NewYork")
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_in_numbers = 0
    true = ["t","r","u","e"]
    for letter in name1:
        if letter in true:
            true_in_numbers += 1
    for letter in name2:
        if letter in true:
            true_in_numbers += 1

    love_in_numbers = 0
    love = ["l", "o", "v", "e"]
    for letter in name1:
        if letter in love:
            love_in_numbers += 1
    for letter in name2:
        if letter in love:
            love_in_numbers += 1

    truelove = str(true_in_numbers) + str(love_in_numbers)
    print(truelove)


calculate_love_score("Lola", "David")