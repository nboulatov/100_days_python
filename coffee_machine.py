MENU = {
    "espresso":
        {
            "ingredients":
                {
                    "water": 50,
                    "milk": 0,
                    "coffee": 18,
                },
            "cost": 1.5,
        },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    """Show current resources"""
    for item in resources:
        if item in resources:
            print(f"{item}: {resources[item]}")


def check_resources_for(choice):
    """Check if there is enough resources. If yes, subtract cost from resource pool and continue, if no, stop"""
    drink = MENU[choice]
    for item in resources:
        if drink['ingredients'][item] > resources[item]:
            return False
    else:
        for item in drink['ingredients']:
            resources[item] -= drink['ingredients'][item]
        return True


def pay(choice):
    """Input money, return change. If not enough, ask again to input more"""
    cost = MENU[choice]['cost']
    input_more_money = True
    while input_more_money:
        quarters = int(input("Please input quarters: ")) * 0.25
        dimes = int(input("Please input quarters: ")) * 0.10
        nickles = int(input("Please input quarters: ")) * 0.05
        pennies = int(input("Please input quarters: ")) * 0.01
        sum = quarters+dimes+nickles+pennies
        if sum < cost:
            print("Not enough coin. Please input at least $%.2f" % (cost))
            input_more_money = True
        else:
            change = sum - cost
            print("Your change $%.2f" % (change))
            input_more_money = False


# 1 asks what the user would like (espresso, latte, cappuccino)
continue_process = True
while continue_process:
    choice = input(
        "What would you like to have? 'Espresso', 'Latte', or 'Cappuccino'? Type 'Report' to see resources \n").lower()
    if choice == 'report':
        report()
        continue_process = True
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        continue_process = check_resources_for(choice)
        if continue_process == True:
            pay(choice)
            print(f"Enjoy your {choice} for $%.2f" %(MENU[choice]['cost']))
            print("Resources left over")
            print(resources)
            continue_process = True
        else:
            print("Not enough resources")
            print(resources)
            continue_process = False