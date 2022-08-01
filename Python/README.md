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

