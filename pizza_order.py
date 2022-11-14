Spizza = 15
Mpizza = 20
Lpizza = 25
pepperoni_for_Spizza = 2
pepperoni_for_MLpizza = 3
cheese = 1
print("Welcome to pizza")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want cheese? Y or N ")
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            final_bill = Spizza+pepperoni_for_Spizza+cheese
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = Spizza + pepperoni_for_Spizza
            print(f"Your final bill is: ${final_bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            final_bill = Spizza + cheese
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = Spizza
            print(f"Your final bill is: ${final_bill}")
if size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            final_bill = Mpizza+pepperoni_for_MLpizza+cheese
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = Mpizza + pepperoni_for_MLpizza
            print(f"Your final bill is: ${final_bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            final_bill = Mpizza + cheese
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = Mpizza
            print(f"Your final bill is: ${final_bill}")
if size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            final_bill = Lpizza+pepperoni_for_MLpizza+cheese
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = Lpizza + pepperoni_for_MLpizza
            print(f"Your final bill is: ${final_bill}")
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            final_bill = Lpizza + cheese
            print(f"Your final bill is: ${final_bill}")
        else:
            final_bill = Lpizza
            print(f"Your final bill is: ${final_bill}")