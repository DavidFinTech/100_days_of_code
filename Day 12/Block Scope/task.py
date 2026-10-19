
import math

def is_prime(num):
    number_prime = True
    if num <= 1:
        number_prime = False
    elif num == 2:
        number_prime = True
    elif num > 2 and num % 2 == 0:
        number_prime = False
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            number_prime = False

    print(number_prime)


is_prime(73)