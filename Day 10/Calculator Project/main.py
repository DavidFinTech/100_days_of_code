from art import logo
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
my_operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
    }

def calculator():
    print(logo)
    active_calculator = True
    number1 = float(input("What's the first number?: "))
    while active_calculator:
        operation_chosen = input("'+',\n'-'\n'*'\nor\n'/'\nChoose an operation: ")
        number2 = float(input("What's the next number?: "))
        for operation in my_operations:
            if operation == operation_chosen:
                result = my_operations[operation](number1, number2)
                print(f"{number1} {operation_chosen} {number2} = {result}")
                continue_or_no = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation\n")
                if continue_or_no == 'y':
                    number1 = result
                else:
                    active_calculator = False
                    print("\n" *20)
                    calculator()

calculator()








