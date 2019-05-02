#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  
  if n <= 0:
    return [[]]

  options = [['rock'], ['paper'], ['scissors']]
  if n == 1:
    return options

  outcomes = []
  playRps = rock_paper_scissors(n - 1)
  for option in options:
      for x in playRps:
        outcomes.append(option + x)

  return outcomes

print(f"\n\n** The outcome is: {rock_paper_scissors(1)} **\n\n")

# def rock_paper_scissors(n):
#   outcomes = []
#   options = [['rock'], ['paper'], ['scissors']]

#   if n == 0:
#     return [outcomes]

#   if n == 1:
#     for option in options:
#       outcomes.append([option])
#     return options

#   for i in range(0, 3 ** n):
#     outcomes.append([options[0]]*n)
#   return outcomes

# print(f"The outcome is: {rock_paper_scissors(1)}")


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')