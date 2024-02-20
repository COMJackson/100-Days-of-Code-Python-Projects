from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").casefold()
    if user_choice != "":
        if user_choice == "off":
            on = False

        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        
        else:
            selected_drink = menu.find_drink(user_choice)
            sufficient_resources = coffee_maker.is_resource_sufficient(selected_drink)
            if sufficient_resources:
                enough_money = money_machine.make_payment(selected_drink.cost)
                if enough_money:
                    coffee_maker.make_coffee(selected_drink)
