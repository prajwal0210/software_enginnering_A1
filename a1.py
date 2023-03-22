"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Prajwal Jayarama Gowda"
__email__ = "Your Email"
__date__ = "20/03/2023"

##recipes = []
##shopping_list = []

from constants import *

# Write your functions here

def num_hours():
     return 12.5

# GET RECIPE [ls -a]
def get_recipe_name(recipe: tuple[str, str]) -> str:
     return(recipe[0])

# PARSE INGREDIENTS []
def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
  x = raw_ingredient_detail.split()
  amount = float(x[0])
  measure = x[1]
  ingredient = ' '.join(x[2:])
  parse=(amount, measure, ingredient)
  return parse

# CREATE RECIPE
def create_recipe():
   name=input("Please enter the recipe name: ")
   recipe=(name,)
   list=[]
   while True:
     y=input("Please enter an ingredient: ")
     if y=="":
       break
     list.append(y)
   string=','.join(list)
   recipe=recipe+(string,)
   return recipe

# RECIPE INGREDIENTS
def recipe_ingredients(recipe):
    ingredients = recipe[1].split(',')
    parsed_ingredients = []
    for ingredient in ingredients:
        parts = ingredient.strip().split(' ')
        amount = parts[0]
        unit = parts[1]
        name = ' '.join(parts[2:])
##        amount, unit, name = ingredient.strip().split(' ')
        parsed_ingredients.append((float(amount), unit, name))
    return tuple(parsed_ingredients)

# ADD RECIPE
def add_recipe(new_recipe: tuple[str, str],recipes: list[tuple[str, str]]) -> None:
    recipes.append(new_recipe)
    
# FIND RECIPE
def find_recipe(recipe_name: str,
recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
##  search = ""  
  for i in recipes:
    if(recipe_name in i):
       return i
##  if search=="":
##    return None
  return None

# REMOVE RECIPE
def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
  for i in recipes:
    if(name == i[0]):
       recipes.remove(i)
       
# GET INGREDIENTS AMOUNT
def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float, str] | None:
  ing_measure=()
  ingredients_list = recipe[1].split(',')  
  for ing in ingredients_list:
        ing_parts = ing.strip().split() 
        if ingredient in ing_parts[2]:
          amount=float(ing_parts[0])
          measure=ing_parts[1] 
          am_mea=[amount,measure]
          ing_measure=ing_measure+tuple(am_mea)
          return (ing_measure)
  return None 

# DISPLAY INGREDEINTS
##def display_ingredients(ingredients):
##    if ingredients == []:
##        return 
##    # Find the length of the longest text in each column
##    max_amount_length = max(len(str(i[0])) for i in ingredients)
##    max_uni_length = max(len(i[1]) for i in ingredients) + 1
##    max_ing_length = max(len(i[2]) for i in ingredients) + 1
##
##    # Print the table
##    for j in ingredients:
##        amount_str = str(j[0]).rjust(max_amount_length)
##        unit_str = j[1].center(max_uni_length)
##        ingredient_str = j[2].ljust(max_ing_length)
##        print(f"| {amount_str} | {unit_str} | {ingredient_str} |")
def display_ingredients(shopping_list):
    if shopping_list == []:
        return 

    shopping_list = sorted(shopping_list, key=lambda x: x[2])

    # Find the length of the longest text in each column
    max_amount_length = max(len(str(i[0])) for i in shopping_list)
    max_uni_length = max(len(i[1]) for i in shopping_list) + 1
    max_ing_length = max(len(i[2]) for i in shopping_list) + 1

    # Print the table
    for j in shopping_list:
        amount_str = str(j[0]).rjust(max_amount_length)
        unit_str = j[1].center(max_uni_length)
        unit_space_cnt = unit_str.count(' ')
        if unit_space_cnt%2!=0:
            unit_str = unit_str[1:]+' '
        
        ingredient_str = j[2].ljust(max_ing_length)
        print(f"| {amount_str} | {unit_str} | {ingredient_str} |")
        
# ADD TO SHOPPING LIST
def add_to_shopping_list(ingredient_details,shopping_list):

    if shopping_list == []:
        shopping_list.append(ingredient_details)
        return shopping_list
    else :
        for i in range(len(shopping_list)):        
            if shopping_list[i] is not None and shopping_list[i][2] == ingredient_details[2]:
                shopping_list[i] = (shopping_list[i][0] + ingredient_details[0], shopping_list[i][1], shopping_list[i][2])
                return shopping_list
            
    shopping_list.append(ingredient_details)
    return shopping_list

# REMOVE FROM SHOPPING LIST
def remove_from_shopping_list(ingredient_name, amount, shopping_list):
    for i, ingredient in enumerate(shopping_list):
        if ingredient[2] == ingredient_name:
            if ingredient[0] > amount:
                new_amount = ingredient[0] - amount
                shopping_list[i] = (new_amount, ingredient[1], ingredient[2])
                return
            elif ingredient[0] == amount:
                shopping_list.pop(i)
                return
            else:
                shopping_list.pop(i)
##                remove_from_shopping_list(ingredient_name, amount - ingredient[0], shopping_list)
                return

# GENERATE SHOPPING LIST
def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    shopping_list = []
    for i in recipes:
        ing_list = i[1].split(',')
        for item in ing_list:
            shopping_list = add_to_shopping_list(parse_ingredient(item), shopping_list)
    return shopping_list    
    

def sanitise_command(string):
    string = string.strip()
    string = string.lower()
    string = ''.join(char for char in string if not char.isdigit())
    return string

def main():
    """ Write your docstring """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    recipes = []
    shopping_list = []
    # Write the rest of your code here
    while True :
        
        choice = input('Please enter a command: ')
        input_choice = choice.split(' ')
        command = input_choice[0]

        if len(input_choice) >= 2 and input_choice[1].startswith('-'):
            command = command + ' ' + input_choice[1]
        if command == 'H' or choice == 'h':
            print(HELP_TEXT)
        elif command =="add":

            recipe_name=sanitise_command(choice[4:len(choice)])
            recipe = find_recipe(recipe_name, recipe_collection)
            if (recipe != None ):
                add_recipe(recipe,recipes)
            else:
                print("\nRecipe does not exist in the cook book. ")
                print("Use the mkrec command to create a new recipe.\n")
        elif choice == 'ls':
             if recipes:
                print(recipes)
             elif recipes == []:
                  print('No recipe in meal plan yet.')
        elif command == 'ls -a':
            for i in recipe_collection:
                 name = get_recipe_name(i)
                 print(name)
        elif command == 'ls -s':
            display_ingredients(shopping_list)
        elif command=="mkrec":
            new_recipe=create_recipe()
            recipe_collection.insert(len(recipe_collection),new_recipe)
            

        elif command == 'rm -i':
            temp = list(choice[6:len(choice)].split(' '))
            item_amt = float(temp.pop())
            item_name = ' '.join(temp)
            remove_from_shopping_list(item_name, item_amt, shopping_list)

        elif command == 'rm':
            remove_recipe(choice[3:len(choice)],recipes)
            
        elif command == 'g' or command == 'G':
            shopping_list = generate_shopping_list(recipes)
##            for i in recipes:
##                ing_list = i[1].split(',')
##                for item in ing_list:
##                    shopping_list = add_to_shopping_list(parse_ingredient(item), shopping_list)
##            shopping_list = sorted(shopping_list, key=lambda x: x[2])
            display_ingredients(shopping_list)
             
        elif command == 'Q' or command == 'q':
            break
            
            

if __name__ == "__main__":
    main()
