#!/usr/bin/python

import sys

def making_change(amount, denominations, cache={}):
  if amount < 5 and amount >= 0:
    return 1
  elif amount < 0 or denominations == []:
    return 0
  else:
    valueOne = making_change(amount - denominations[-1],denominations)
    valueTwo = making_change(amount, denominations[:-1])
    return valueOne + valueTwo 


# penny = 1

# nickel = 5

# dime = 10

# quarters = 25

# half-dollars 50


# As far as base cases go, again, think about some cases where we'd want the
#    recursion to stop executing. What should happen when the amount of cents
#    given is 0? What should happen when the amount of cents given is negative?
#    What about when we've used up all of the available coin denominations?


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")