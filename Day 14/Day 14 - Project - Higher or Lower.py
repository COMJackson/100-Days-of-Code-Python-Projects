# Import the data for the game in the form of a list of dicts and the art.
from higherlower_data import data
from higherlower_art import logo, vs


from time import sleep # User when making random choices to delay the system clock by a random float between 0 and 1.
from random import choice, uniform # Used to get a random choice from a list and to get a random float.
from copy import deepcopy # Used to create deep copies to not modify orignal of a iterable.
from os import system # Used to clear the terminal.

# Constants
CLEAR_TEMRINAL = True # True clears terminal.
SHOW_CHOICE_VALUES = False # True shows the choice followers.

# The dicts in data follow this format.
# key = str(name): value = str(name of the IG account)
# key = str(follower_count): value = int(number of followers of the IG account)
# key = str(description): value = str(description of the IG account)
# key = str(country): value = str(country of the IG account)

# Key constants.
N_KEY    = "name"
FC_KEY   = "follower_count"
D_KEY    = "description"
C_KEY    = "country"

def get_data(local_data, starter_choice_a=None):
    """
    Randomly gets data from the local_data list containing a dict with 
    a IG users name, followers, description of that user and the country 
    they are in.

    Returns a deepcopy of the selected data.
    """
    sleep(uniform(0, 1)) # This is here to help randomize the choice.
    
    # Checks to see if the starter_choice_a has been set, 
    # this is used to get the starting choices without a duplicate.
    if starter_choice_a != None:
        selected_data = deepcopy(choice(local_data))
        if selected_data == starter_choice_a: # If the selected_data is the starter_choice_a recall the function.
            return(get_data(local_data, starter_choice_a))
    
    # If the game has already started just get a choice
    # from the current local_data.
    else:
        selected_data = deepcopy(choice(local_data))
    
    # After the all statements are done return selected_data.
    return(selected_data)
    

def get_player_choices(local_data, current_correct_choice, current_choice_a, current_choice_b):
    """
    Takes the local_data and returns two choices (choice_a and choice_b).

    If the game just started then it will be get two non-duplicate 
    random choices and return them.
    
    Otherwise the correct choice from last round will be choice_a 
    and a random choice from the local_data list as choice_b.

    Returns two choices to be used as the vs. in the game.
    """
    
    # If the current correct choice has not yet been set get two non-duplicate choices.
    if current_correct_choice == None:
        choice_a = get_data(local_data)
        choice_b = get_data(local_data, choice_a)
    
    # If current correct choice has been set than set the current correct choice to
    # choice_a and a random non-duplicate choice to choice_b
    else:
        if current_correct_choice == "a":
            choice_a = current_choice_a
        else:
            choice_a = current_choice_b
        choice_b = get_data(local_data)
    
    # Return the choices
    return(choice_a, choice_b)
        
def get_player_input():
    """
    Get's the players input as either "a" or "b".

    Not case senstive.

    Will not allow the player to input an invalid input.
    """
    
    player_input = input("Type \'A\' or \'B\' to choose: ").casefold()
    if player_input not in ("a", "b"):
        print("Invalid input, please only input \'A\' or \'B\' (not case senstive).")
        return(get_player_input)
    else:
        return(player_input)

def did_player_win(passed_cho_a_followers, passed_cho_b_followers):
    """
    Compares the two choices follower count, then takes the players
    choice for who they think has a higher follower count and will
    return True if they are winning or False if they aren't

    Will also return the choice the player chose.

    Returns True/False, "a"/"b"
    """
    
    players_choice = get_player_input() # Gets the players choice and returns a str: "a" or "b".
    
    # If the players choice is "a" and they won returns True and "a", otherwise False and "b"
    if players_choice == "a":
        if passed_cho_a_followers >= passed_cho_b_followers:
            return(True, "a")
        else:
            return(False, "b")
    
    # If the players choice is "b" and they won returns True and "b", otherwise False and "a"
    else:
        if passed_cho_b_followers >= passed_cho_a_followers:
            return(True, "b")
        else:
            return(False, "a")

def hi_lo_game():
    """
    Main game function.
    """
    # Game data and while loop flag
    local_data = deepcopy(data)
    alive      = True
    
    # Player flab and score tracker.
    player_winning = True
    score          = 0
    
    # Init choices.
    correct_choice = None
    choice_a = None
    choice_b = None
    

    while alive:
        # Will clear terminal every time the loop runs.
        if CLEAR_TEMRINAL: 
            system("cls")

        print(logo) # Print the starting logo.
        
        # If the players is winning then the score will incerment here.
        if player_winning:
            if correct_choice != None:
                score += 1
                print(f"Your right! Current score: {score}\n")

            print("Who do you think has more followers on Instagram?\n")

            # Set the two choices and call the get_player_choices 
            # function decide what IG accounts they are choosing between.
            choice_a, choice_b = get_player_choices(local_data, correct_choice, choice_a, choice_b)

            # Get the relevant values from the choice_a dict.
            cho_a_name = choice_a[N_KEY]
            cho_a_followers = choice_a[FC_KEY]
            cho_a_desc = choice_a[D_KEY]
            cho_a_country = choice_a[C_KEY]
            cho_a_msg = (f"Choice \'A\': {cho_a_name}, a {cho_a_desc}, from {cho_a_country}.")

            # Get the relevant values from the choice_b dict.
            cho_b_name = choice_b[N_KEY]
            cho_b_followers = choice_b[FC_KEY]
            cho_b_desc = choice_b[D_KEY]
            cho_b_country = choice_b[C_KEY]
            cho_b_msg = (f"Choice \'B\': {cho_b_name}, a {cho_b_desc}, from {cho_b_country}.\n")


            # These two if statements will remove the current choices from the local_data list.
            #
            # This is to limit the new choices to ones not already displayed.
            if choice_a in local_data:
                local_data.remove(choice_a)
            if choice_b in local_data:
                local_data.remove(choice_b)

            # Prints the each choice as a msg and a big "VS" in ascii between them on the console.
            print(cho_a_msg)
            print(vs)
            print(cho_b_msg)

            # DEBUG: if the SHOW_CHOICE_VALUES is set to True then it will show the 
            # number of followers for both choices.
            if SHOW_CHOICE_VALUES:
                print(f"DEBUG: Number of A followers: {cho_a_followers}")
                print(f"DEBUG: Number of B followers: {cho_b_followers}")

            player_winning, correct_choice = did_player_win(cho_a_followers, cho_b_followers)


            # If somehow the player has guessed EVERY choice correctly, then the game will end here.
            if local_data == []:
                if CLEAR_TEMRINAL: 
                    system("cls")
                
                print(logo) # Print the starting logo.
                print(f"We've run out of choices for you! I guess that means you win :)")
                print(f"Final score: {score+1}")
                alive = False

        # If the player is no longer winning clears terminal, prints starting logo,
        # prints the final score and ends the while loop.
        if not player_winning:
            if CLEAR_TEMRINAL: 
                system("cls")

            print(logo) # Print the starting logo.
            print(f"Sorry, thats wrong. Final score: {score}")
            alive = False

# Call the hi_lo_game function.
hi_lo_game()