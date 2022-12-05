import random

number_card_pool = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
face_card_pool = {"Jack":10,"Queen":10,"King":10, "Ace":11}
card1 = random.choice(number_card_pool)
card2 = random.choice(number_card_pool)
comp_card1 = random.choice(number_card_pool)
comp_card2 = random.choice(number_card_pool)
print(f"Your cards: [{card1}, {card2}]")

def identify_card1(card):
    if type(card) == int:
        return card
    elif type(card) == str and card == "Ace":
        return 11
    else:
        return 10
def identify_card2(card):
    if type(card) == int:
        return card
    elif type(card) == str and card == "Ace":
        return 11
    else:
        return 10

card1 = identify_card1(card1)
card2 = identify_card1(card2)
comp_card1 = identify_card1(comp_card1)
comp_card2 = identify_card1(comp_card2)
total = card1 + card2

comp_total = comp_card1+comp_card2

print(f"Your cards: [{card1}, {card2}]")
print(f"Comp cards: [{comp_card1}, {comp_card2}]")

print(f"Your total is {total}")
again = True
while again:
    your_total = 0
    if input("Type 'y' to get another card, type 'n' to pass: ")=='y':
        new_card = random.choice(number_card_pool)
        new_card_identified = identify_card2(new_card)
        print(new_card_identified)
        your_total = total+new_card_identified
        print(f"Your new total is {your_total}")
        again = True
    else:
        again = False
print(your_total)
if your_total>21:
    print("You Lose")
elif your_total==comp_total:
    print("Tie")
elif your_total>comp_total:
    print("You Win")

print(f"Computer's final hand [{comp_card1},{comp_card2}]")