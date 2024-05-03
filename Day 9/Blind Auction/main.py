# NOTE: I made this project harder on myself by adding input error checking and additional formating,
# this project is beyond the scope of the orignal projects parameters.

import os
import random as rand
from auction_art import logo

# This allows you to toggle clearing of the console after each step in the code.
clear_console = False

# Start by clearing the terminal.
if clear_console:
    os.system("cls")

# Print art and introduction to the program.
print(logo)
print("Welcome to the secret action")

# - Setup vars - #
# Empty dict to record bidder name and bid.
bidder_dict = {}
# Boolen var to use in the auction while loop.
auction_open = True


# - FUNCTIONS - #


# Checks if the name is invalid, if it is ask the user to correct the name.
def valid_name_checker(name):
    invalid_name = False

    # Checks for names that contain non-alphabetical chars, prints an error message.
    if not name.isalpha():
        invalid_name = True
        invalid_name_msg = (
            "The name you entered contained a symbol not in the English alphabet."
            + "\n"
            + "Please only enter letters in the English alphabet."
        )
        print(invalid_name_msg)

    # Only active if the user entered an invalid char in the name. Ask the user for a valid input.
    while invalid_name:
        name = input("What is your name?: ")
        if name.isalpha():
            invalid_name = False
        else:
            print(invalid_name_msg)

    if name in bidder_dict:
        name = duplicate_name_fixer(name)

    return name


# If the above function found the name was already in the bidder dict, will add a number to the end of the name.
def duplicate_name_fixer(name):
    current_iter = 1
    name_not_fixed = True

    # While loop that will take a iterating number and add it to the name.
    #
    # If the name still exist in the bidder dict, it will strip the current
    # number from the name and replace it with the current iterator number.
    while name_not_fixed:
        if current_iter != 1:
            name = name.rstrip(str(current_iter - 1))

        name += str(current_iter)

        if name not in bidder_dict:
            name_not_fixed = False
        else:
            current_iter += 1

    return name


# Checks to see if the bid is a valid bid.
#
# A bid is valid if it contains only intergers and a single decimal point.
#
# If the bid is invalid it will ask the user to correct the bid.
def valid_bid_checker(bid):
    invalid_bid = False

    if not bid.isnumeric():

        if "." in bid:
            bid_split = bid.split()

            if len(bid_split) > 2:
                invalid_bid = True
            else:
                whole_num_bid = bid_split[0]
                fraction_of_bid = bid_split[1]

                if not whole_num_bid.isnumeric() or not fraction_of_bid.isnumeric():
                    invalid_bid = True
                else:
                    return bid

        else:
            invalid_bid = True

    if invalid_bid:
        print(
            "The bid you entered was invalid."
            + "\n"
            + "A bid can only contain numeric characters and a single decimal point with no spaces."
        )
        return invalid_bid_correcter()
    else:
        return bid


# Helper function that ask user to input a new bid and recalls the valid_bid_checker function.
def invalid_bid_correcter():
    new_bid = input("What's your bid?: $")
    valid_bid_checker(new_bid)


# Main function for recording the bidders to the bidder_dict.
#
# Calls the bid and name checker function and will record the
# entry to the bidder dict after it is valid.
def record_bidder():
    name = input("What is your name?: ")
    valid_name = valid_name_checker(name)
    bid = input("What's your bid?: $")
    valid_bid = float(valid_bid_checker(bid))

    bidder_dict[valid_name] = valid_bid


# ^ FUNCTIONS ^ #

# - Program While Loop - #

# While auction_open is True will call the record_bidder function and record the
# bidders inputed until the user answers "no" to the continue statement
while auction_open:
    record_bidder()

    # Checks to see if there is more then one bidder,
    # if there is ask if the user would like to add bidders
    if not len(bidder_dict) == 1:
        keep_bidding = input(
            "Are there any other bidders? Type 'yes' or 'no'.\n"
        ).casefold()
        keep_bidding_ans = False
    # If there is only one bidder the program will not ask
    # the user the user if they want to add more bidders
    else:
        keep_bidding_ans = True
        if clear_console:
            os.system("cls")

    # While loop made to validate the answer from the user on if they want to continue.
    while keep_bidding_ans == False:
        if keep_bidding in ("no", "n"):
            auction_open = False
            keep_bidding_ans = True
        elif keep_bidding in ("yes", "y"):
            keep_bidding_ans = True
            if clear_console:
                os.system("cls")
        else:
            keep_bidding = input(
                "Invalid answer. Only valid answer are 'yes' or 'no'."
                + "\n"
                + "Are there any other bidders? Type 'yes' or 'no'.\n"
            ).casefold()


# Clear the terminal.
if clear_console:
    os.system("cls")

# Creates a list of bidder tuples from the bidder dictonary.
bidder_tuples = bidder_dict.items()
# Reverse sorts the bidder tuple list by the bids of the bidder into a new list.
sorted_bidder_tuples = sorted(
    bidder_tuples, reverse=True, key=lambda bidder_tuples: bidder_tuples[1]
)

# If the first and second bid entry of the sorted bidder list are not equal
# the the winner is set to the first in the sorted bidder list.
if not sorted_bidder_tuples[0][1] == sorted_bidder_tuples[1][1]:
    winner = sorted_bidder_tuples[0]
# If the above is not the case, then the winning bidder are put into a new list
# and a winner of the tie is chosen randomly.
else:
    winner_list = []
    for b in sorted_bidder_tuples:
        print(b)
        if b[1] == sorted_bidder_tuples[0][1]:
            winner_list.append(b)

    print(
        "There was a tie for highest bid! Randomly choosing a winner among the highest bidders."
    )
    winner = winner_list[rand.randint(0, len(winner_list) - 1)]

# Seperate the winner tuple into the winners bid and winner name.
winner_bid = winner[1]
winner_name = winner[0]

# Print the winner's name and formated winning bid to two decimals.
print(f"The winner is {winner_name} with a bid of ${winner_bid:.2f}!")
