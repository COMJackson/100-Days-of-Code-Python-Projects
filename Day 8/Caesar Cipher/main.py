# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,   #
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  #
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          #
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          #
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          #
#             88             88                                     #
#            ""             88                                      #
#                           88                                      #
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,       #
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8       #
# 8b         88 88       d8 88       88 8PP""""""" 88               #
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88               #
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88               #
#               88                                                  #
#               88                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import the art to print.
import cipher_art as art

alphabet = [
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
]
logo = art.logo
cipher_running = True

print(logo)


# Function for shifting letters given to it.
def letter_shifter(starting_char, shift_amount, operator):

    # Checking to make sure the starting char is in the alphabet, if it is return it.
    if not starting_char.isalpha():
        return starting_char

    # Set the old char's index to be used later on.
    old_char_index = alphabet.index(starting_char)

    # Checks the operator parameter to go back or forward in index to select the new shifted letter's index.
    if operator == "+":
        new_char_index = old_char_index + shift_amount
        # Corrects indexes out of range.
        if new_char_index >= 26:
            new_char_index = new_char_index - 26

    else:
        new_char_index = old_char_index - shift_amount
        # Corrects indexes negative indexes.
        if new_char_index < 0:
            new_char_index = 26 + new_char_index

    # After all if/else statements and the shift letter index is found set the shifted letter and return it.
    new_char = alphabet[new_char_index]
    return new_char


# Combined function for both encode (going forward in the alphabet)
# and decoding (going backward in the alphabet).
def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""

    # Checks to see if the shift amount is greater than the number of letters in the alphabet.
    # If it is then modulus divides the shift amount by 26 and sets the new shift amount to that.
    if shift_amount > 26:
        shift_amount %= 26

    # Loop through all letters in the plain text
    for char in plain_text:
        # Check which 'direction' the user wishes to go in the alphabet.
        if cipher_direction == "encode":
            cipher_text += letter_shifter(char, shift_amount, "+")
        else:
            cipher_text += letter_shifter(char, shift_amount, "-")

    # At the end print the finished cipher text with the direction included.
    print(f'The {cipher_direction}d text is "{cipher_text}"')


# While loop that will run until the user answers no to the keep_running input.
while cipher_running:
    # User input vars.
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the function that will encrypt or decrypt the user inputed text.
    caesar(text, shift, direction)

    # User input to check if the user would like to continue to use the app.
    keep_running = input(
        "Would you like to continue using the Caesar Cipher?\nType yes or no: "
    ).casefold()
    no_answer = True

    # While loop that will only stop if the user types yes or no, and checks for invalid answers.
    while no_answer:
        if keep_running in ("no", "n"):
            print("Goodbye")
            cipher_running = False
            no_answer = False

        elif keep_running in ("yes", "y"):
            no_answer = False

        else:
            keep_running = input(
                'Invalid answer, please only type in "yes" or "no".\nType yes or no: '
            )
