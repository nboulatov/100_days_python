MENU = {
    "espresso":
    {
        "ingredients":
        {
            "water": 50,
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

# Coin operated: penny: 1c, nickel: 5c, dime: 10c, quarter: 25c
# must output an error if there isn't enough resources and ask again
# 2 when ordering ask the user for how many quarters, dimes, nickels, pennies to be inserted
# resources are reduced after each successful purchase
# Feedback on successful purchase: here's your coffee, count all the coins up, subract the cost and output change
# Feedback on insufficient funds: Not enough. Money refunded

# using report keyword, output its resources: water, milk, coffee
def report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return f"Water remaining {water}\nMilk remaining {milk}\nCoffee remaining {coffee}"


#check resources
def check_resources_for(choice,MENU,resources):
    if choice == 'espresso':
        water = MENU['espresso']['ingredients']['water']
        coffee = MENU['espresso']['ingredients']['coffee']
        water_left = resources['water']
        coffee_left = resources['coffee']
        if water_left-water < 0 or coffee_left-coffee < 0:
            return



# 1 asks what the user would like (espresso, latte, cappuccino)
choice = input("What would you like to have? 'Espresso', 'Latte', or 'Cappuccino'? Type 'Report' to see resources \n").lower()
if choice == 'report':
    print(report(resources))
elif choice == 'espresso':
    check_resources_for(choice,MENU,resources)