#!/usr/bin/python

import sys

def add_combinations(arr, index, result):
  if index == len(arr):
    result.append(list(arr))
    return  
  else:
    for item in ("rock", "paper", "scissors"):
      arr[index] = item
      add_combinations(arr, index + 1, result)

def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  result = []
  num_player = [0] * n
  add_combinations(num_player, 0, result)
  return result



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')