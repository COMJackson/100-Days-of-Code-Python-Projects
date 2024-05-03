# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill_str = input("What was the total bill? $")
tip_str = input("How much tip would you like to give? 10, 12, or 15? ")
people_int = int(input("How many people to split the bill? "))

# Ensure that symbols inputed are removed.
if "$" in bill_str:
    no_symb_bill = bill_str.replace("$", "")
else:
    no_symb_bill = bill_str
if "%" in tip_str:
    no_symb_tip = tip_str.replace("%", "")
else:
    no_symb_tip = tip_str

# Casting types for calculations.
bill_float = float(no_symb_bill)
tip_int = int(no_symb_tip)
tip_percentage = tip_int / 100

# Calculations.
total_tip = bill_float * tip_percentage
total_bill = bill_float + total_tip
bill_per_person = total_bill / people_int

# Formating to 2 decimal places and printer result.
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
