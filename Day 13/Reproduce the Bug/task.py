from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #taking from 0 to 5 in positions so it never goes out of range
print(dice_images[dice_num])
