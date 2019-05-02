#!/usr/bin/python

import sys

def making_change(amount, denominations):
  options = [5, 10, 25, 50] 
  cache = [1] * (amount + 1)

  for money in options:
    for biggest in range(money, amount +1):
      change = biggest - money
      cache[biggest] += cache[change]
  
  return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("\n\n** There are {ways} ways to make {amount} cents. ** \n\n".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")