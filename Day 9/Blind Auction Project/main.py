from tarfile import AbsoluteLinkError

from art import logo
print(logo)
name = input("What is your name?\n")
bid = int(input("What is your bid?\n"))
Blind_Auction = {name: bid}
continue_biding = True
other_user = input("Is there another  user who wants to bid? ('Yes' or 'No')\n".lower())
while other_user == "no":
    print("\n" * 20)
    name = input("What is your name?\n")
    bid = input("What is your bid?\n")
    Blind_Auction[name] = int(bid)
    other_user = input("Is there another user who wants to bid? ('Yes' or 'No')\n".lower())
for winner, value in Blind_Auction.items():
    if value == max(Blind_Auction.values()):
        print("the winner is" + winner)
        break



