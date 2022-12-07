import random

number_card_pool = [2,3,4,11,11,11,11,11,11,"Jack","Queen","King","Ace"]
face_card_pool = {"Jack":10,"Queen":10,"King":10, "Ace":11}
card1 = random.choice(number_card_pool)
card2 = random.choice(number_card_pool)
comp_card1 = random.choice(number_card_pool)
comp_card2 = random.choice(number_card_pool)
print(f"Your cards: [{card1}, {card2}]")

have_ace=False
def identify_card1(card):
    if type(card) == int:
        return card
    elif type(card) == str and card == "Ace":
        have_ace = True
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
    if input("Type 'y' to get another card, type 'n' to pass: ")=='y':
        new_card = random.choice(number_card_pool)
        new_card_identified = identify_card1(new_card)
        print(new_card_identified)
        total+=new_card_identified
        if new_card_identified == 11 and total>21:
            total-=10
        print(f"Your new total is {total}")
        again = True
    else:
        again = False

print(total)
if total>21:
    print("You Lose")
elif total==comp_total:
    print("Tie")
elif total>comp_total:
    print("You Win")
else:
    print("you lose")

print(f"Computer's final hand [{comp_card1},{comp_card2}]")