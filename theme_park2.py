print("Welcome to the theme park rides!")
height = int(input("What is your height? "))
bill = 0
if height > 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif 45 >= age <= 55:
        bill = 0
    else:
        bill = 12
        print("Cost $12")
    photo = input("Do you want a photo Y or N ")
    if photo == "Y":
        bill +=3
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")
else:
    print("Get lost")