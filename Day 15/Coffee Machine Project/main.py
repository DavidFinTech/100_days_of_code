MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def money_insert():
    quarters = int(input('How many quarters: ')) * 0.25
    dimes = int(input('How many dimes: ')) * 0.10
    nickels = int(input('How many nickels: ')) * 0.05
    pennies = int(input('How many pennies: ')) * 0.01
    return quarters + dimes + nickels + pennies

def check_transaction(money_insertedd, coffee_cost, drink_ingredients, coffee):
    if money_insertedd < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
    elif money_insertedd >= coffee_cost:
        resources["Money"] += coffee_cost
        for item in drink_ingredients:
            resources[item] -= drink_ingredients[item]
        print(f'Here is your {coffee}, enjoy!')
    if money_insertedd > coffee_cost:
        print(f'here is your change: {round(money_insertedd - coffee_cost, 2)}')

while True:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    if ask == 'off':
        break
    elif ask == "report":
        print(resources)
    elif ask in MENU:
        drink_data = MENU[ask]
        can_make = True

        for item in drink_data["ingredients"]:
            if drink_data["ingredients"][item] > resources[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False

        if can_make:
            money_inserted = money_insert()
            print('you inserted $', money_inserted)
            check_transaction(money_inserted, drink_data["cost"], drink_data['ingredients'], ask)


