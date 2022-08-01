# CreditCardValidator
In this code challenge we must validate a credit card using the card's checksum supplied by the card vendor.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/CreditCardValidator?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/CreditCardValidator?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/CreditCardValidator?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/CreditCardValidator?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/CreditCardValidator/main?style=for-the-badge)

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

### pseudocode 
Here's some pseudocode to showcase how an implementation of the algorithm could look like.
<br>
First, we get the `credit_card_number` from user input, and the `last_digit` from the last number of `credit_card_number`.
We also remove the last digit from the `credit_card_number` so it doesn't mess with any of our calculations for the time being.
```python
credit_card_number = INPUT
last_digit = LAST NUMBER OF credit_card_number
REMOVE LAST NUMBER OF credit_card_number
```

Next, we loop over the `credit_card_number` and run a series of checks.
1. Check if `i` is a multiple of 2. This allows every other number in `credit_card_number` is multiplied by 2.
2. Check the lengths of the number and add the two digits if the number is longer than a single digit (e.g. >9).
3. We add the current number to our `sum` variable which is adding up all of our numbers as we loop over `credit_card_number`.
```python
i = 0
sum = 0
LOOP UNLESS i = LENGTH OF credit_card_number
    IF i IS MULTIPLE OF 2
        credit_card_number[i] = credit_card_number[i] * 2
    IF LENGTH OF credit_card_number[i] IS MORE THAN 1
        x = credit_card_number[i][0]
        y = credit_card_number[i][1]
        credit_card_number[i] = x + y
    sum = sum + credit_card_number[i]
END
```

Finally, we add the `last_digit` (the 16th digit of the `credit_card_number` to the `sum`).
If the `sum` is a multiple of 10 it is valid, otherwise it is invalid.
```
sum = sum + last_digit
IF sum IS MULTIPLE OF 10
    OUTPUT "Credit card number is valid!"
ELSE
    OUTPUT "Credit card numebr is invalid!"
```
