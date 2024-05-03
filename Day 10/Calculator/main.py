import os
from calculator_art import logo

# Control whether the terminal will clear or not.
clear_terminal = True
# Clear the terminal before anything is printed.
if clear_terminal:
    os.system("cls")


# - Calculator Functions - #
# Add
def add(l_num, r_num):
    result = l_num + r_num
    return result


# Subtract
def subtract(l_num, r_num):
    result = l_num - r_num
    return result


# Multiply
def multiply(l_num, r_num):
    result = l_num * r_num
    return result


# Divide
def divide(l_num, r_num):
    result = l_num / r_num
    return result


# ^ Calculator Functions ^ #
#
# - Operator dictonaries - #
operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
operator_msgs = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
}


# ^ Operator dictonaries ^ #
#
# - Helper Functions - #
def return_operation_msg():
    msg = "O͟p͟e͟r͟a͟t͟o͟r͟ | O͟p͟e͟r͟a͟t͟i͟o͟n͟"
    for o in operator_msgs:
        msg += f"\n       {o} : {operator_msgs[o]}"
    return msg + "\n"


def ask_for_ending_action(num):
    ending_msg = (
        f'To continue using your current result ({num}) in the calculator, type "continue" or "c".\n'
        + 'To clear the calculator, type "clear".\n'
        + 'To exit the calculator, type "exit" or "e".\n'
    )

    question_answer = input(ending_msg).casefold()
    return question_answer


def ask_right_input():
    r_num = float(input("What is the number on the right side of the operator?: "))
    return r_num


def ask_left_input():
    l_num = float(input("What is the number on the left side of the operator?: "))
    return l_num


# ^ Helper Functions ^ #
#
# - Main Function - #
def calculator():
    # Print imported logo
    print(logo)

    # Flags and memory var.
    stored_result = None
    calculator_running = True
    first_run = True

    while calculator_running:
        # Init and resets vars every time the loop runs
        right_num = None
        left_num = None
        answer = None

        # Checks to see if it is the first time the while loop runs.
        # If it is then it will ask for both right and left number.
        if first_run:
            left_num = ask_left_input()
            operation_sym = input(return_operation_msg() + "Type in an operator: ")
            right_num = ask_right_input()
            first_run = False

        # If it is not the first time the while loop has run, clears terminal and
        # ask the user which side of the operator the current answer should be on.
        else:
            if clear_terminal:
                os.system("cls")

            print(f"The current result is: {stored_result}")
            operation_sym = input(return_operation_msg() + "Type in an operator: ")

            if operation_sym in ("/", "-"):
                print(
                    f"Please choose the side of the operator to put the current result ({stored_result}) on."
                )
                stored_result_side = input(
                    'Type "l" for left or "r" for right: '
                ).casefold()
            else:
                stored_result_side = "l"

            if stored_result_side == "l":
                left_num = stored_result
                right_num = ask_right_input()
            else:
                right_num = stored_result
                left_num = ask_left_input()

        # Calls the proper function from the operators dict using the
        # selected operation symbol as the key.
        calculation_function = operators[operation_sym]
        # Store the answer returned from the calculation
        answer = calculation_function(left_num, right_num)
        # Stores the answer in memory.
        stored_result = answer

        # Clears the temrinal.
        if clear_terminal:
            os.system("cls")

        # Print the equation as proof the calculator works.
        print(f"{left_num} {operation_sym} {right_num} = {answer}")

        # Ending action, ask if the user wants to continue using
        # the stored result, clear the calculator or exit the program.
        ending_action = ask_for_ending_action(stored_result)

        # If the action is exit or clear then stop the current calculator while loop.
        if ending_action in ("e", "exit", "clear"):
            calculator_running = False

            # If the action was clear recalls the calculator function.
            if ending_action == "clear":
                calculator()


# ^ Main Function ^ #

# Calls the calculator function once to begin the program.
calculator()
