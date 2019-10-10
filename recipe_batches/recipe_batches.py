#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  test = True
  counter = 0
    
  while test:
    test = False  
    for key, value in ingredients.items():
      if value - recipe[key] >= 0:
        ingredients[key] = value - recipe[key]
        test = True
        if list(recipe.keys())[-1] == key:
          counter += 1
      else: break
    
  return counter


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))