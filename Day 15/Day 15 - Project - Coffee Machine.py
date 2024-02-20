MENU = {
    "espresso": {
        "ingredients": {
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

def yn_input(msg: str):
    uinput = input(msg).casefold()
    if uinput in ("y", "yes", "n", "no"):
        if uinput in ("y", "yes"):
            return True
        else:
            return False
    else:
        return yn_input("The input you enter was invalid.\n" + msg)

def validate_int_input(msg, custom_error_msg=None):
    """
    Validates that a users input is a decimal number and
    turns the input string into an integer if it is.

    Return (int)
    """
    uinput = input(msg)
    
    if custom_error_msg != None:
        error_msg = custom_error_msg
    else:
        error_msg = "Invalid input. Only accepts numbers 0-9."
    
    if not uinput.isdecimal():
        validate_int_input(error_msg, error_msg)
    else:
        return int(uinput)

def coffee_machine():
    """
    Main function that contains local sub-functions.

    Will take a users input and give the user a "coffee".

    If the resources run out will stop the code.
    """

    def get_resources():
        """
        Returns a tuple of the current coffee machine's
        resources.

        Return (tuple)
        """
        
        c_water = resources["water"]
        c_milk = resources["milk"]
        c_coffee = resources["coffee"]
        return (c_water, c_milk, c_coffee)

    def report_resources():
        """
        Prints a report of the current resources and money
        inside the coffee machine.

        Return (None)
        """
        
        w, m, c = get_resources()
        print(f"Water: {w}ml")
        print(f"Milk: {m}ml")
        print(f"Coffee: {c}g")
        print(f"Money: ${machine_money:.2f}")
    
    def get_user_choice():
        """
        Gets the users choice and returns the drink
        cost, resource cost and the choice the user made.

        If the user runs a 'report' will print machines
        current resources.

        If the user doesn't input a valid input will
        call itself.

        Return (tuple)/iteself
        """
        # Get the users choice.
        choice = input("What would you like? (Espresso/Latte/Cappuccino): ").casefold()
        
        # If the user's choice is in the MENU
        if choice in MENU:
            
            # Select proper dictonary and dictionary items in MENU
            selected_drink    = MENU[choice]
            drink_ingredients = selected_drink["ingredients"]
           
            # Get the cost and resource cost of the drink.
            d_cost   = selected_drink["cost"]
            w_needed = drink_ingredients["water"]
            c_needed = drink_ingredients["coffee"]
            
            if "milk" in drink_ingredients: 
                m_needed = drink_ingredients["milk"]
            else:
                m_needed = 0

            return d_cost, w_needed, c_needed, m_needed, choice
        
        # If the user wants a report on the machinces resources.
        elif choice == "report":
            report_resources()
            return get_user_choice()
        
        elif choice == "off":
            return None, None, None, None, "off"
        
        # If the user doesn't input a valid input.
        else:
            print("Invalid choice. Please select a valid choice (not case sensitive).")
            return get_user_choice()

    def request_money(cost_of_drink: int):
        """
        Takes the selected drinks cost and ask the user
        to input the proper amount of coins into the machine.

        If the user does it will return none.

        If the user doesn't will ask the user to add more coins.

        Return (cost_of_drink)
        """

        money = 0
        diff = cost_of_drink

        while True:
            print(f"Please insert ${diff:.2f} in coins.")
            num_quarters = validate_int_input("How many quarters?: ")
            num_dimes    = validate_int_input("How many dimes?: ")
            num_nickles  = validate_int_input("How many nickles?: ")
            num_pennies  = validate_int_input("How many pennies?: ")

            money += ((num_quarters * 0.25)
                    + (num_dimes * 0.10)
                    + (num_nickles * 0.05)
                    + (num_pennies * 0.01))
            
            if money >= cost_of_drink:
                change = money - cost_of_drink
                print(f"Here is ${change:.2f} in change.")
                return cost_of_drink
            else:
                diff = cost_of_drink - money
                print(f"You inserted ${money:.2f}. You need ${diff:.2f} more to buy this drink.")
                num_quarters, num_dimes, num_nickles, num_pennies = 0, 0, 0, 0        # Reset num of each coin.

    def has_res_for_drink(watr_need, coff_need, milk_need, no_msg=False):
        """
        Checks to see if the machine has enough
        resources for the selected drink.

        Will return True if it does and False
        if it doesn't.

        Return (bool)
        """
        
        c_watr, c_milk, c_coff = get_resources()
        not_enough_resources = False

        if c_watr < watr_need:
            if not no_msg: print("Sorry machine doesn't have enough water for that drink.")
            not_enough_resources = True
        if c_coff < coff_need:
            if not no_msg: print("Sorry machine doesn't have enough coffee for that drink.")
            not_enough_resources = True
        if c_milk < milk_need:
            if not no_msg: print("Sorry machine doesn't have enough milk for that drink.")
            not_enough_resources = True

        return(not not_enough_resources)

     # Starting counter vars.
    
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        }
    machine_money = 0
    running = True

    while running:
        
        # Set current drinks cost and resource cost.
        drink_cost, water_needed, coffee_needed, milk_needed, user_choice = get_user_choice()

        # Checks to make sure the user choice is in the MENU
        if user_choice in MENU:
            print(f"You selected {user_choice.capitalize()}, this drink cost: ${drink_cost:.2f}")

            # If the machine has enough resources.
            if has_res_for_drink(water_needed, coffee_needed, milk_needed):
                machine_money += request_money(drink_cost)
                print(f"Here is your {user_choice.capitalize()} ☕. Enjoy!")
                # Removes the water, milk and coffee used from the resources in the resoruces dict
                resources["water"] -= water_needed
                resources["milk"] -= milk_needed
                resources["coffee"] -= coffee_needed

            # If drink user chose requires more resources than the machine has.
            else:
                running = yn_input("Would you like to get a different drink? (y/n): ")

        # If user inputs the secret word "off", stops the loop.
        elif user_choice == "off":
            running = False

        else:
            running = False
            print("ERROR user_choice wasn't set to a valid option.")

        # If machine doesn't have enough resources for the drink with 
        # least resource requirement stop the while loop.
        if has_res_for_drink(watr_need=50, coff_need=18, milk_need=0, no_msg=True) != True:
            print("Machine doesn't have enough resources for any drink.")
            running = False

coffee_machine()