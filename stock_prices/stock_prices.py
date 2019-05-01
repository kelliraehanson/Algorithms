#!/usr/bin/python

import argparse

def find_max_profit(prices):
  smallest = prices[0]
  biggest = prices[0]

for price in prices:

  if price > biggest:
    biggest = price
  elif price < smallest:
    smallest = price

  # print(f'Smallest: {smallest}')
  # print(f'Biggest: {biggest}')

return biggest - smallest

print(f"Max Profit: {find_max_profit([10, 7, 5, 8, 11, 9]), 6}")
 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
