def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_in_numbers = 0
    true = ["t", "r", "u", "e"]
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
