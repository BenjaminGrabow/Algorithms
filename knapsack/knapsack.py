#!/usr/bin/python

import sys
from collections import namedtuple
from operator import itemgetter

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  compare = []
  
  for item in items:
    add_value = dict()
    add_value["result"] = item.value / item.size
    add_value["index"] = item.index
    add_value["size"] = item.size
    add_value["value"] = item.value
    compare.append(add_value)
  
  sorted_list = sorted(compare, key = lambda i: i["result"],reverse=True)
  trackCapacity = sorted_list[0]["size"]
  trackValue = sorted_list[0]["value"]
  resultIndicies = [sorted_list[0]["index"]]

  for index,item in enumerate(sorted_list):
    if index != 0 and trackCapacity + item["size"] <= capacity:
      trackCapacity += item["size"]
      trackValue += item["value"]
      resultIndicies.append(item["index"])

  resultIndicies.sort()
  
  return {"Value": trackValue, "Chosen": resultIndicies}



if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')