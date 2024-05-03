# Step 5

import random

import hangman_words as h_words

word_list = h_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art as h_art

logo = h_art.logo
print(logo)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You already guessed the letter: "{guess}"')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'The letter "{guess}" is not in the word.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages = h_art.stages
    print(stages[lives])
