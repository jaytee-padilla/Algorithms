#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  total_batches = 0
  temp_list = [] # will be used to check if at least 1 batch can be made or not

  # check if each of the keys that exist in recipe all exist in ingredients, if they don't, 0 batches can be created due to lack of proper ingredients
  if all(key in ingredients.keys() for key in recipe.keys()): # NOTE: all() takes a single parameter, an iterable. Not sure if this effects time complexity
    for key, value in ingredients.items():
      temp_list.append(value >= recipe.get(key))

    # if the recipe and ingredients match up, check if there's enough to make a whole batch
    # if there isn't, return the current value of total_batches
    if all(temp_list) == False:
      return total_batches
    else:
      while all(temp_list) == True:
        for key, value in recipe.items():
          cur_ingredient = ingredients.get(key)
          cur_ingredient -= value

        total_batches += 1

  else:
    return total_batches





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5}
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))