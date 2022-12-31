from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

restaurant_money_machine = MoneyMachine()
restaurant_coffee_maker = CoffeeMaker()
restaurant_menu = Menu()



restaurant_coffee_maker.report()
restaurant_money_machine.report()


espresso = restaurant_menu.find_drink("espresso")

is_on = True

while is_on:
    options = restaurant_menu.get_items()
    choice = input(f"What would you like {options}")
    print(restaurant_coffee_maker.is_resource_sufficient(espresso))
