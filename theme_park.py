print("Welcome to the theme park rides!")
height = int(input("What is your height? "))
if height > 100:
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5")
    elif 12 < age < 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12")
else:
    print("Get lost")