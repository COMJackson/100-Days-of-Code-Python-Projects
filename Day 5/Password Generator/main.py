# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# I chose to only do the HARD level #

# --BEGIN CODE-- #

# Create a int out of the combined total of letters, numbers and symbols requested by the user for the password.
password_length = nr_letters + nr_numbers + nr_numbers

# Get the length of each list to use in the random number generator.
letters_len = len(letters)
symbols_len = len(symbols)
numbers_len = len(numbers)

# Create blank list to store the letter, symbols and numbers selected by for loops.
letters_list = []
symbols_list = []
numbers_list = []

# Create a list with references to the letters, numbers and symbols list connect to and integer ranging from 0-2
list_pool = [letters_list, symbols_list, numbers_list]

# -BEGIN-# For loops to create list of selected letters, numbers and symbols.
for num in range(1, (nr_letters + 1)):
    index = random.randint(0, (letters_len - 1))
    letters_list.append(letters[index])

for num in range(1, (nr_symbols + 1)):
    index = random.randint(0, (symbols_len - 1))
    symbols_list.append(symbols[index])

for num in range(1, (nr_numbers + 1)):
    index = random.randint(0, (numbers_len - 1))
    numbers_list.append(numbers[index])

# -END-# For loops to create list of selected letters, numbers and symbols.

# Create a blank string to store the password generated.
password = ""

# Create a bool to initialize the generator.
generator_init = False

# Create a nil var for the currently selected list.
selected_list = None

for num in range(1, (password_length + 1)):

    # Ensures that if the selected list is blank it gets removed from the list_pool list.
    if selected_list == []:
        list_pool.remove(selected_list)

    # Randomly selects a list from the current list pool to draw the char currently being written to the password.
    selected_list = list_pool[random.randint(0, (len(list_pool) - 1))]

    # It is important to store the selected char's index for future use in deleting it from the selected list in addition to selecting the char itself.
    selected_char_index = random.randint(0, (len(selected_list) - 1))

    # Randomly selects a char from the currently selected list to write to the password.
    selected_char = selected_list[selected_char_index]

    # If the generator has been initialized, then the binary indexer will choose if the selected char will be placed on the rightmost or leftmost position of the password.
    if generator_init:
        binary_indexer = random.randint(0, 1)

        if binary_indexer == 0:
            password = selected_char + password
        else:
            password = password + selected_char

    # If the generator has not been initialized, begins the password by writing the selected char to the blank password.
    else:
        password += selected_char

    # At the end, remove the selected char from the selected list.
    selected_list.pop(selected_char_index)

print(f"Here is your password: {password}")

# --END CODE-- #

"""
Ending notes:

I learned about the random modules choice and shuffle function which I didn't know about after watching the instructors video on their solution.

"""
