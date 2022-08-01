# Credit Card Validator in Python
In this code challenge we must validate a credit card using the card's checksum supplied by the card vendor.

## Problem
Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

## Solution

### How checksum works
Credit card vendors want an easy way to validate cards. This is to ensure, when the card is charged, that the card number is correct and therefore the payment can go through. If you've ever paid for something online and entered your card number wrong, you would know the website instantly knows and won't let you continue. Behind the scenes the website is running a checksum algorithm on the card number to ensure it is correct.

### The algorithm behind checksum
Example card number: 4716 1065 5423 0864

1. Take the first 15 digits and double every other digit: 8 7 2 6 2 0 12 5 10 4 4 3 0 8 12 
2. Any numbers that are longer than a single digit we add the two number together (e.g. 12 = 1+2 = 3): 8 7 2 6 2 0 3 5 1 4 4 3 0 8 3
3. Now we add all the numbers together: 56
4. Take the 16th digit and add it onto our sum: 56 + 4 = 60
5. Finally, if our number is a multiple of 10 then it is valid, otherwise it is not.

I recommend you do this on pen and paper first ad it'll help you understand what we're doing.
Try using [this online fake credit card number generator](https://www.creditcardvalidator.org/generator) and doing the algorithm yourself.

Read more:
- [What is Checksum on a credit card?](https://www.sapling.com/7966257/checksum-credit-card)

### Python solution
The Python solution is very similar to the pseudocode written in generalised solution of `README.md`.
There are some Python specific functions/methods used which makes the code a lot more compact. 

To begin with, we get the credit card number from the user and instantly convert it to a list.
We then use `pop()`, a function that removes, and then returns, the last element of a list.
We assign the return of `pop()`, the last number in `credit_card_number`, to `last_digit`.
```python
# Get input, define last_digit, and remove the 16th digit from the credit card.
credit_card_number = list(input("Please enter the credit card number: "))
last_digit = credit_card_number.pop()
```

Next is the meat of our code.
We use `enumerate()` which, in Python, gives us both `i` the current index and `number` the current value at that index (e.g. the current number in `credit_card_number`).
For each number in `credit_card_number` we do the following:
1. Check if the index `i` of the `number` is even. If so we multiply that number by 2.
2. We check if the current number is longer than 1 digit. If so we break up the number and add each digit together.
3. Ensure every number in `credit_card_number` is an integer and not a string because later on we use `sum()` which doesn't like strings.
```python
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
```

Finally, we check if the `credit_card_number` is valid.
We add the sum of the `credit_card_number` and add the `last_digit` to it.
We then check if the result is a multiple of 10 using `% 10 === 0`.
```python
# Add up all the numbers, add the 16th digit, then check if final number is a multiple of 10.
is_valid = (sum(credit_card_number) + int(last_digit)) % 10 == 0
print(f"Is credit card valid: {is_valid}")  # Output answer to user: True or False.
```
