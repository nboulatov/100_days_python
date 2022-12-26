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
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# for item in MENU['espresso']['ingredients']:
#     if MENU['espresso']['ingredients'][item]>resources[item]:
#         print(item)
#     else:
#         print(item)

for item in MENU['espresso']['ingredients']:
    resources[item] -= MENU['espresso']['ingredients'][item]
print(resources)
