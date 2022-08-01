
# Get input, define last_digit, and remove the 16th digit from the credit card.
credit_card_number = list(input("Please enter the credit card number: "))
last_digit = credit_card_number.pop()

# Make use of enumerate to get the index and value of each number in the credit card number.
for i, number in enumerate(credit_card_number):
    if i % 2 == 0:  # if the index is even (i.e. every other element)
        credit_card_number[i] = int(number) * 2

    # Check is the length of the number is more than a single digit.
    if len(str(credit_card_number[i])) > 1:
        # Break up the number into two digits and add them together
        # Example: 12 := 1 + 2 = 3
        x = str(credit_card_number[i])[0]
        y = str(credit_card_number[i])[1]
        credit_card_number[i] = int(x) + int(y)  # We replace the previous number with our new single digit one.

    # Here we make sure every element is converted to an integer otherwise we have issues with sum() later on.
    credit_card_number[i] = int(credit_card_number[i])

# Add up all the numbers, add the 16th digit, then check if final number is a multiple of 10.
is_valid = (sum(credit_card_number) + int(last_digit)) % 10 == 0
print(f"Is credit card valid: {is_valid}")  # Output answer to user: True or False.
