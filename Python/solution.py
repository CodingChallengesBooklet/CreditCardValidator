
credit_card_number = list(input("Please enter the credit card number: "))
last_digit = credit_card_number.pop()

for i, number in enumerate(credit_card_number):
    if i % 2 == 0:
        credit_card_number[i] = int(number) * 2
    if len(str(credit_card_number[i])) > 1:
        x = str(credit_card_number[i])[0]
        y = str(credit_card_number[i])[1]
        credit_card_number[i] = int(x) + int(y)
    credit_card_number[i] = int(credit_card_number[i])

is_valid = (sum(credit_card_number) + int(last_digit)) % 10 == 0
print(f"Is credit card valid: {is_valid}")
