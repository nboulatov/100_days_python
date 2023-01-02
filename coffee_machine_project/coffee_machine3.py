from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

restaurant_money_machine = MoneyMachine()
restaurant_coffee_maker = CoffeeMaker()
restaurant_menu = Menu()

is_on = True

while is_on:
    options = restaurant_menu.get_items()
    choice = input(f"What would you like {options}")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        restaurant_coffee_maker.report()
        restaurant_money_machine.report()
    else:
        drink = restaurant_menu.find_drink(choice)
        if restaurant_coffee_maker.is_resource_sufficient(drink):
            if restaurant_money_machine.make_payment(drink.cost):
                restaurant_coffee_maker.make_coffee(drink)
