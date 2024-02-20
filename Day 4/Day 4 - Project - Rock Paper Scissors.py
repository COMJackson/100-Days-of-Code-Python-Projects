rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random as rand

user_input_invalid = True

# Create a dictionary to use to convert a number into the proper string representation of rock, paper or scissors.
valid_answers = {0: rock, 1: paper, 2: scissors}

# User Input
user_input = input("Rock, Paper, Scissors! Which do you choose? - 0 = Rock, 1 = Paper, 2 = Scissors.\n")

# Check to make sure the user choice is valid, and if not ask again until the choice is valid.
while user_input_invalid:
    if user_input in ("0", "1", "2"):
        user_choice = valid_answers[int(user_input)]
        user_input_invalid = False
    
    else:
        user_input = input("Invalid input! - 0 = Rock, 1 = Paper, 2 = Scissors.\n")

# Randomaly generate the computers answer using the random module. The answer will always be between 0 and 2.
computer_choice      = valid_answers[rand.randint(0, 2)]

print(user_choice)
print("Computer chose:"
      + "\n"
      + computer_choice)

# Check for tie.
if user_choice == computer_choice:
    print("It's a tie!")

# Print the proper statement for if the user chooses rock as their choice.
elif user_choice == rock:
    if computer_choice == paper:
        print("You lost.")
    elif computer_choice == scissors:
        print("You win!")

# Print the proper statement for if the user chooses paper as their choice.
elif user_choice == paper:
    if computer_choice == rock:
        print("You win!")
    elif computer_choice == scissors:
        print("You lose.")

# Print the proper statement for if the user chooses scissors as their choice.
elif user_choice == scissors:
    if computer_choice == rock:
        print("You lose.")
    elif computer_choice == paper:
        print("You win!")

else:
    print("An error occured with the input checker, please fix it :(")