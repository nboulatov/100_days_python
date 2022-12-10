import random

number_card_pool = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
face_card_pool = {"Jack":10,"Queen":10,"King":10, "Ace":11}
print(number_card_pool)
card1 = random.choice(number_card_pool)
del number_card_pool[number_card_pool.index(card1)]
print(number_card_pool)
card2 = random.choice(number_card_pool)
del number_card_pool[number_card_pool.index(card2)]
print(number_card_pool)
comp_card1 = random.choice(number_card_pool)
del number_card_pool[number_card_pool.index(comp_card1)]
print(number_card_pool)
comp_card2 = random.choice(number_card_pool)
del number_card_pool[number_card_pool.index(comp_card2)]
print(number_card_pool)
print(f"Your cards: [{card1}, {card2}]")

def identify_card1(card):
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
print(f"Comp total is {comp_total}")

you_again = True
while you_again:
    if input("Type 'y' to get another card, type 'n' to pass: ")=='y':
        new_card = random.choice(number_card_pool)
        new_card_identified = identify_card1(new_card)
        print(f"Your new card is {new_card_identified}")
        print(number_card_pool)
        total+=new_card_identified
        if new_card_identified == 11 and total>21:
            total-=10
        print(f"Your new total is {total}")
        you_again = True
    else:
        you_again = False

comp_again = True
while comp_again:
    if comp_total<17 and comp_total<21:
        new_card = random.choice(number_card_pool)
        new_card_identified = identify_card1(new_card)
        print(f"Comp new card is {new_card_identified}")
        comp_total+=new_card_identified
        if new_card_identified == 11 and total > 21:
            comp_total -= 10
        print(f"Comp total is {comp_total}")
        comp_again = True
    else:
        comp_again = False

print(f"Your total is {total}")
print(f"Comp total is {comp_total}")
if total>21:
    print("You Lose")
elif total==comp_total:
    print("Tie")
elif total>comp_total:
    print("You Win")
else:
    print("You lose")

#print(f"Computer's final hand [{comp_card1},{comp_card2}]")