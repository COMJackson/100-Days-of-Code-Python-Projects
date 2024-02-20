from random import randrange as r_range
from guessthenumber_art import art

# Print the starting art and text.
print(art)
print("Welcome to the Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")

# Used to set difficulty.
DIFFICULTY = {
    "easy": 10,
    "hard": 5
}

# Gets a random number between 1 and 100.
random_number = r_range(1, 101)

# Use this var to enable or disable a print 
# statement hinting at the correct answer.
show_answer = False

def validate_difficulty():
    """
    Gets a valid difficulty choice from the user and returns it.
    """
    
    p_diff_c = input("Choose a difficulty. Type \'easy\' or \'hard\': ").casefold()

    if p_diff_c not in DIFFICULTY:
        print(f"\'{p_diff_c}\' is not a valid difficulty.")
        return validate_difficulty()
    else:
        return p_diff_c

# If the player enters easy the player gets 10 guesses.
# If the player enter hard the player gets 5 guesses.
num_guesses_global = DIFFICULTY[validate_difficulty()]

def guess_number():
    """
    Gets the user guess.

    If the user doesn't input a number will tell them
    it's an invalid guess and ask again.

    Returns True if the user correctly guessed.

    Returns False if the user incorrectly guess.
    """
    
    user_guess = input("Make a guess: ")
    
    if user_guess.isnumeric():
        
        if int(user_guess) == random_number:
            return(True)
        elif int(user_guess) > random_number:
            print("Too high.")
            return(False)
        else:
            print("Too low.")
            return(False)
    
    else:
        print(f"\'{user_guess}\' is not a valid number.")
        return guess_number()

def guessing_game(num_guesses):
    """
    Main function of the game.
    
    When called it will starting the game with 
    the random number that was stored in the 
    random_number var as the number to guess.

    After the player has selected to player on
    hard or easy the player will be told how many
    guesses they have left and be told if their
    current guess is higher or lower than the number.
    """
    
    if show_answer:
        print(f"HINT: the correct answer is {random_number}.")

    if num_guesses > 0:
        print(f"You have {num_guesses} attempts remaining to guess the number.")
        guess_correct = guess_number()
        if guess_correct:
            print(f"You guessed the number! (Number was {random_number}) - Game over")
        else:
            print("Guess again")
            num_guesses -= 1
            guessing_game(num_guesses)

    else:
        print("Ran out of guesses. - Game over")

guessing_game(num_guesses_global)