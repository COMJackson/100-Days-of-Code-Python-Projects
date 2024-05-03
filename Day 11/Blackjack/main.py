import os
import time
import copy
import random as rand
import blackjack_art as art

# Flag for allowing the clearing of terminal, if True whenever the os.system("cls") function is called the terminal will go blank.
clear_terminal = True


def starting_print(
    show_stages,
    show_card_values,
    p_hand=None,
    d_hand=None,
    show_dealers_second_card=None,
):
    """
    Starts by clearing terminal (if clear_terminal flag is True)

    Then prints the starting art, then the rules of the game.

    If the show_stages param is True then it will also show the explanation of each stage in the game.

    Finally if the p_hand, d_hand and show_dealers_second_card param are ALL NOT set to None
    then prints a formatted hand for the player and dealers hand and below that the values
    of the hands.
    """

    # If this is true clears the terminal
    if clear_terminal:
        os.system("cls")
    print(art.logo)

    rules = (
        "Rules:\n"
        + "1. Your objective is to have a higher valued hand then the dealer.\n"
        + '2. A perfect hand is 21 points, also known as a "Blackjack".\n'
        + "3. Any hand above 21 is a bust hand, meaning whoever has that hand has lost the game by default. (It is possible for both the player and dealer to have a bust hand).\n"
        + '4. If both the player and dealer have equal hands or bust hands the game ends in a "push" which means funds are returned to the player.\n'
        + "5. If a hand has gone over 21 but there is an Ace card in it, that ace's value can be set to 1 to continue play."
    )
    stages = (
        "\n--- Stages ---\n"
        + "\nBidding Stage:\n"
        + '1. The player will bet "x" number of dollars. This is subtracted from the players bank.\n'
        + "\nDeal Stage:\n"
        + "1. The dealer deals the player two cards faceup, then deals themself two cards, one being faceup, the other card face down.\n"
        + '2. If the players gets a blackjack then the player will skip their "Hit Stage", as they already have a perfect hand.\n'
        + "3. If the dealer has an Ace or Face card showing, the dealer will check the face down card to see if they have a blackjack.\n"
        + "3a. If the dealer has a blackjack they will flip their face down card up. If the player doesn't also have a blackjack the game is over and the player has lost.\n"
        + '3b. If the dealer doesn\'t have a blackjack the "Hit Stage".\n'
        + "Hit Stage - Player: (Skipped if player already has a Blackjack)\n"
        + '1. The player can choose to "hit" (draw a card) or "stand" (leave the hand as it is).\n'
        + "2. If the player didn't choose to stand, then Step 1 repeats until the player stands or bust out.\n"
        + '3. Once the player stands or bust. The dealers "Hit Stage" begins.\n'
        + "\nHit Stage - Dealer: (Skipped if the dealer already has a Blackjack)\n"
        + "1. Dealer will flip over their face down card.\n"
        + "2. The dealer will either hit until they bust out or stand if the total value of their hand is greater then or equal to 17.\n"
        + "\nSettlement Stage:\n"
        + "1. One of the following will happen.\n"
        + "1a. If the players hand is the winning hand their bet multiplied by 2 and returned to them.\n"
        + "2a. If the dealers hand is the winning hand the players bet is given to the dealer.\n"
        + '3a. If a "push" occurs the bet is returned to the player.\n'
        + "4a. If the player hand is bust, then the dealer takes the players bet.\n"
        + "5a. If the dealers hand is bust, then the players gets their bet multiplied by 2 returned to them."
    )

    print(rules)
    if show_stages:
        print(stages)
    if show_card_values:
        print(
            "\nCards values are as follows: Ace (11 or 1), 2 through 10 (card number is their value), Jack, Queen and King (10)\n"
        )
    if (p_hand and d_hand and show_dealers_second_card) != None:
        print(
            f"Dealers hand:\n{return_formatted_hand(d_hand, show_second_card = show_dealers_second_card)}"
        )
        print(f"Your hand:\n{return_formatted_hand(p_hand)}")
        if show_dealers_second_card:
            print(f"Dealer's hand is showing {get_hand_value(d_hand)} points")
        else:
            print(
                f"Dealer's hand is showing {d_hand[0][0]} points. Their other card is flipped down."
            )
        print(f"Your hand is showing {get_hand_value(p_hand)} points")


def hit(drawing_hand, non_drawing_hand):
    """
    When this function is called it will use the draw_card
    function to get a UNIQUE new card to add to the drawing hand
    returning the new hand to replace the current drawing hand.
    """
    new_hand = drawing_hand
    new_card = draw_card(drawing_hand, non_drawing_hand)
    new_hand.append(new_card)
    return new_hand


def get_card():
    """
    This functions randomly selects a card and suit for the card
    from the art (blackjack_art) module found in .cards and .suits dictionaries.

    After the card and suit is chosen it will format the card into a tuple
    containing the card value at index 0 and card info and ascii art at
    index 1 of the tuple and return the tuple.
    """

    # There are two seperators (~ & *) in the ascii card.
    # The ~ is where the suit emoji will be placed.
    # The * is where the suit art is placed.
    sep = "~"

    # Set random number, names, art, and indexes of the card.
    suit_index = rand.randint(0, 3)
    suit_name = list(art.suits.keys())[suit_index]
    suit_art = (art.suits[suit_name][0], art.suits[suit_name][1])
    card_index = rand.randint(0, 12)
    card_name = list(art.cards.keys())[card_index]
    card_value = art.cards[card_name][0]
    card_ascii = art.cards[card_name][1]

    # For loop replaces the seperators pos in the string with the proper art/emoji.
    for sel_art in suit_art:
        if sep == "*":
            formatted_sel_art = sel_art.rstrip("\n")
        else:
            formatted_sel_art = sel_art
        card_ascii = card_ascii.replace(sep, formatted_sel_art)
        sep = "*"

    # If the card value is equal to 11 (meaning it's an ace)
    # then the formatted card value to be used in concatenation
    # of the card "Title" above the card art.
    #
    # Otherwise the card formatted card value will be a str of the
    # int value of the card.
    if card_value == 11:
        formatted_card_value = "11 or 1"
    else:
        formatted_card_value = str(card_value)

    # Creates the cards string for printing reasons.
    card = (
        "The "
        + card_name
        + " of "
        + suit_name
        + (f" ({formatted_card_value})")
        + card_ascii
    )
    return (card_value, card)


def draw_card(player_hand=None, dealer_hand=None):
    """
    Takes the a UNIQUE random card from get_card
    and returns the drawn card.

    If the the players hand and dealers hand param
    is set and the card is in one of the hands then
    the function is called again until a new card to
    the game is found.
    """
    # A floated (between 0 and 1) random sleep is
    # necessary to ensure card values are not stacked.
    #
    # Without this two cards with identical values
    # can be drawn if the function is called in succession
    # too quickly.
    time.sleep(rand.uniform(0, 1))

    # Returns a UNIQUE random card or return loops
    # the function until it does.
    drawn_card = get_card()
    if drawn_card in (player_hand, dealer_hand):
        return draw_card(player_hand, dealer_hand)
    else:
        return drawn_card


def get_random_hands():
    """
    Returns both a player card list and a dealer card list that have UNIQUE cards.
    """

    # Create empty lists.
    p_card_list = []
    d_card_list = []

    # While loops will check to make sure card is not already
    # in one of the list and populate the list until both
    # have 2 cards.
    while (len(p_card_list) and len(d_card_list)) != 2:
        new_card = draw_card()
        if new_card not in (p_card_list, d_card_list):
            if len(p_card_list) != 2:
                p_card_list.append(new_card)
            else:
                d_card_list.append(new_card)

    return (p_card_list, d_card_list)


def return_formatted_hand(card_list, show_second_card=True):
    """
    Takes the card list given as the param and returns a formatted
    string of the hand.

    If this function is being used to show the dealers hand then
    a flag param can be toggled to show the second card in the
    dealers hand.
    """
    # Deep copies the passed card list to ensure
    # integrity of the list.
    internal_card_list = copy.deepcopy(card_list)

    # Counts the number of card and num of lines in a card.
    num_cards_in_hand = len(internal_card_list)
    num_lines_in_card = len(internal_card_list[0][1].splitlines())

    # Creates an empty list to add the formatted lines
    # being parsed below to.
    formatted_lines = []

    # Creates a blank string to eventually write said parsed lines to.
    printable_hand = ""

    # If the show_second_card param flag is true, replaces the
    # card title and art with a blank cards.
    if not show_second_card:
        internal_card_list[1] = (0, art.back_of_card)

    # Creates blank strings for each expected line in the printable hand.
    for l in range(num_lines_in_card):
        formatted_lines.append("")

    # For each line in each card, write that line to the correct line
    # in the printable hand.
    for line_i in range(num_lines_in_card):
        for card_i in range(num_cards_in_hand):
            selected_cardline = internal_card_list[card_i][1].splitlines()[line_i]
            if card_i != num_cards_in_hand - 1 and line_i == 0:
                formatted_lines[line_i] += selected_cardline + " | "
            elif card_i != num_cards_in_hand - 1:
                formatted_lines[line_i] += selected_cardline + "  "
            else:
                formatted_lines[line_i] += selected_cardline + "\n"

    # Take each line in the formatted_lines list and write it as a string
    # to the printable_hand.
    for line in formatted_lines:
        printable_hand += line

    return printable_hand


def verify_int_input(msg):
    """
    Takes a the custom message (msg) param and cask the for the users input.

    Displaying the custom message, then check to make sure the input is a decimal.

    If it is then returns the users input, if it isn't ask the user to input an
    interger.
    """
    while True:
        user_input = input(msg)
        if not user_input.isdecimal():
            msg = "Invalid input, please only input decimal number (0-9).\nEnter new amount here: $"
        elif int(user_input) <= 0:
            msg = "Invalid input, you cannot enter zero or a negative number.\nEnter new amount here: $"
        else:
            return int(user_input)


def check_player_bet(player_bank):
    """
    Called to verify that a players bet is both an interger and
    that the player has enough money in their bank.

    Returns players valid bet.
    """

    msg = f"\nYour available funds: ${player_bank}\nPlease enter how much you want to bet this round: $"
    while True:
        player_bet = verify_int_input(msg)
        if not player_bet <= player_bank:
            msg = f"Invalid input, you cannot bet more then you have in your bank.\nYour bank: ${player_bank}\nEnter a new bet here: $"
        else:
            return player_bet


def get_hand_value(card_list):
    """
    Checks the hand value of the card list passed to the function.

    If the hand value is over 21 and aces are present in the hand:

    Will take the number of aces in the hand and subtracts 10 from
    the hand_total until either the hand_total is less than or
    equal to 21, or the number of aces used to subtract 10 reaches 0.

    Returns the hand value found by the function.
    """

    # Init counters.
    hand_total = 0
    num_aces = 0

    # Gets the total value of the hand and number aces in the hand.
    for card in card_list:
        hand_total += card[0]
        if card[0] == 11:
            num_aces += 1

    # If the number of aces in the hand isn't 0 and the hand total
    # is greater then 21 then it will subtract 10 for each ace in
    # the hand until:
    # A. The hand is less than or equal to 21.
    # B. The number of aces in the hand used during subtraction
    #    reaches 0.
    if num_aces > 0 and hand_total > 21:
        while hand_total > 21 and num_aces > 0:
            hand_total -= 10
            num_aces -= 1

    return hand_total


def check_for_bust(hand):
    """
    Takes the passed hand and checks to see if the hand
    is bust.

    Returns True if it is and False if it isn't.
    """
    hand_value = get_hand_value(hand)
    if hand_value > 21:
        return True
    else:
        return False


def check_for_blackjack(hand):
    """
    Takes the passed hand and checks to see if the hand
    has a blackjack.

    Returns True if it is and False if it isn't.
    """

    hand_value = get_hand_value(hand)
    if hand_value == 21:
        return True
    else:
        return False


def compare_hands(player_hand, dealer_hand):
    """
    *Called at the end of the round*

    Takes the player's and dealer's hand and compares the values of them.

    If the of both hand values are equal, or both hands are bust it will
    result in a push.

    If one hand is bust the owner of the other hand wins.

    If the hands are both not bust and one is higher then the other
    then the owner of that hand won the round.

    Returns: Player wins = True --- Dealer wins = False --- Push = "push"
    """
    ph_value = get_hand_value(player_hand)
    dh_value = get_hand_value(dealer_hand)
    is_player_bust = check_for_bust(player_hand)
    is_dealer_bust = check_for_bust(dealer_hand)

    if is_dealer_bust and is_player_bust:
        print("Both player and dealer went bust, resulting in a push.")
        return "push"
    elif ph_value == dh_value:
        print("Both player and dealer have equal hands, resulting in a push.")
        return "push"
    elif ph_value < dh_value:
        if is_dealer_bust:
            return True
        else:
            return False
    else:
        if is_player_bust:
            return False
        else:
            return True


def blackjack(player_bet):
    """
    This is the main function for the game.

    Keep in mind that this is not the starting function,
    it only handles the actual play of the round and doesn't
    track the players bank.
    """

    # Get a random hand for the player and dealer.
    player_hand, dealer_hand = get_random_hands()

    # Round flags.
    round_active = (
        True  # Used as flag for while loop, when set to False is the last run.
    )
    round_ending = (
        False  # Used to allow for one more FULL run of the while loop to run.
    )

    # Player gain/loss counter and flags.
    player_done = False  # When the players is no longer able continue player or passed this is True.
    player_won = None  # This is used as a flag to check the ending game state.
    player_gain_loss = 0  # This is used to keep track of the players gain or loss.

    # Dealer flags.
    show_dealers_second_card = (
        False  # Used to toggle visablity of the dealers second card.
    )

    while round_active:

        # Sets the starting msg to a BLANK list.
        starting_msgs = []

        # Gets the hands values of the current hands.
        dealer_hand_value = get_hand_value(dealer_hand)
        player_hand_value = get_hand_value(player_hand)

        # Checks for blackjack, bust, if the player is
        # done with their hit stage, or if the dealers
        # second card should be shown.
        #
        # If black jack or bust is found, hand it is found
        # in a string will be append to annouce the hand
        # states after the starting_print function is called.
        if check_for_blackjack(dealer_hand):
            player_done = True
            starting_msgs.append("Dealer has blackjack.")
        if check_for_blackjack(player_hand):
            starting_msgs.append("Player has blackjack.")
        if check_for_bust(dealer_hand):
            starting_msgs.append("Dealer is bust.")
        if check_for_bust(player_hand):
            starting_msgs.append("Player is bust.")
            player_done = True
        if player_done:
            show_dealers_second_card = True

        # This calls the function to clear the terminal, and print the art, rules,
        # formatted hands and current scores.
        starting_print(
            show_stages=False,
            show_card_values=True,
            p_hand=player_hand,
            d_hand=dealer_hand,
            show_dealers_second_card=show_dealers_second_card,
        )

        # If their are ANY starting msgs it will loop through them
        # and individually print them after the starting print.
        if starting_msgs != "":
            for msg in starting_msgs:
                print(msg)
                starting_msgs = []

        # Used to end the round and declare a winner or a push.
        if round_ending:
            player_won = compare_hands(player_hand, dealer_hand)
            if player_won == True:
                player_gain_loss += player_bet
                print(f"You won this round! You made ${player_bet}.")
            elif player_won == False:
                player_gain_loss += -(player_bet)
                print(
                    "You lost this round. Your bet is given to the dealer, better luck next round."
                )
            else:
                player_gain_loss = 0
                print("The game ended in a push. Your bet was returned to your bank.")

            round_active = False
            # This input needs to be here to ensure the user knows the ending game state.
            input("Hit enter to continue.")

        # Players hit stage commands and outcomes.
        if player_hand_value < 21 and not player_done:
            player_action = input('Do you wish to "hit" or "pass"?: ').casefold()
            if player_action == "hit":
                player_hand = hit(player_hand, dealer_hand)
            elif player_action == "pass":
                player_done = True
            else:  # If the player does enter an invalid command will print the following and wait
                # for the player to acknowledge their error. Continues the while loop.
                print(
                    'The command you enter was invalid, please only enter "hit" or "pass".'
                )
                input("Hit enter to continue.")

        # Dealers hit stage.
        elif player_done and dealer_hand_value < 17:
            show_dealers_second_card = True
            print("Dealer's hand is not 17 or higher, dealer must hit.")
            # This has to be here to allow the player to read.
            input("Hit enter to continue.")
            dealer_hand = hit(dealer_hand, player_hand)

        # If both the player's and dealer's hit stages are done then
        # then this will end the game after one more full loop.
        else:
            round_ending = True
            show_dealers_second_card = True

    # After the game concludes this will be returned in the start_game function
    # to modify the player's bank account.
    return player_gain_loss


def start_game(passed_game_num=None, passed_player_bank=None):
    """
    This function is used to start the game and is recursively
    called until the player enters (close) into the terminal.

    Also stores the "Global" vars.
    """
    # This calls the function to clear the terminal, and print the art, rules,
    # and stages of the game.
    starting_print(show_stages=True, show_card_values=False)

    # If the game just started then set the game_num to 1
    # and ask the user to create a starting bank account.
    if passed_game_num == None:
        game_num = 1
        player_bank = verify_int_input(
            "\nHow much money do you want to set your starting bank to?: $"
        )
    # If the users bank is 0 after the first or any subsequent game
    # will ask for the user to add funds to the bank account.
    elif passed_player_bank == 0:
        player_bank = verify_int_input(
            "You have no money in your bank!\nHow much money are adding to your bank?: $"
        )
        game_num = passed_game_num + 1
    # If the user has already played their first game and still
    # has money in the bank increases the game number and sets
    # the players bank to the passed player bank.
    else:
        game_num = passed_game_num + 1
        player_bank = passed_player_bank

    # Gets the players bet.
    player_bet = check_player_bet(player_bank)

    # Calls the actual round and after it finishes wiil set
    # the returned gain or loss to the player_gain_loss var.
    player_gain_loss = blackjack(player_bet)

    # After the round is over adds or subtracts (if value negative)
    # the player_gain_loss value to the player bank.
    player_bank += player_gain_loss

    # After the settlement of the game is done ask the user if they wish to continue playing.
    new_game = input(
        'Do you wish to keep playing or close the application, hit enter to continue playing or type "close" or "c" to close.\n'
    ).casefold
    # If the player just hits enter or types anything that isn't "c" or "close".
    # Then calls this function again.
    if new_game not in ("c", "close"):
        start_game(game_num, player_bank)


start_game()
