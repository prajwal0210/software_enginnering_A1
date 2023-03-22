"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
_author_ = "Rohan Kumar"
_email_ = "r.kumar1@uqconnect.edu.au"
_date_ = "03/03/2023"

from constants import *
from typing import List, Tuple

def get_recipe_name(recipe: Tuple[str, str]) -> str:
    return recipe[0]


def parse_ingredient(raw_ingredient_detail: str) -> Tuple[float, str, str]:
    amount, measure, ingredient = raw_ingredient_detail.split()
    return float(amount), measure, ingredient


def create_recipe() -> Tuple[str, str]:
    name = input("Enter recipe name: ")
    ingredients = []
    while True:
        ingredient_detail = input("Enter ingredient detail (amount measure ingredient): ")
        if not ingredient_detail:
            break
        ingredients.append(parse_ingredient(ingredient_detail))
    return name, '\n'.join([f"{amount} {measure} {ingredient}" for amount, measure, ingredient in ingredients])


def recipe_ingredients(recipe: Tuple[str, str]) -> List[Tuple[float, str, str]]:
    return [parse_ingredient(detail) for detail in recipe[1].split('\n')]


def add_recipe(new_recipe: Tuple[str, str], recipes: List[Tuple[str, str]]) -> None:
    recipes.append(new_recipe)


def find_recipe(recipe_name: str, recipes: List[Tuple[str, str]]) -> Tuple[str, str] or None:
    for recipe in recipes:
        if recipe[0] == recipe_name:
            return recipe
    return None


def remove_recipe(name: str, recipes: List[Tuple[str, str]]) -> None:
    for i, recipe in enumerate(recipes):
        if recipe[0] == name:
            recipes.pop(i)
            return


def get_ingredient_amount(ingredient: str, recipe: Tuple[str, str]) -> Tuple[float, str] or None:
    for amount, measure, name in recipe_ingredients(recipe):
        if name == ingredient:
            return amount, measure
    return None


def add_to_shopping_list(ingredient_details: Tuple[float, str, str], shopping_list: List[Tuple[float, str, str]]) -> None:
    for i, existing_detail in enumerate(shopping_list):
        if existing_detail[2] == ingredient_details[2]:
            shopping_list[i] = (existing_detail[0] + ingredient_details[0], existing_detail[1], existing_detail[2])
            return
    shopping_list.append(ingredient_details)


def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: List[Tuple[float, str, str]]) -> None:
    for i, detail in enumerate(shopping_list):
        if detail[2] == ingredient_name:
            new_amount = detail[0] - amount
            if new_amount > 0:
                shopping_list[i] = (new_amount, detail[1], detail[2])
            else:
                shopping_list.pop(i)
            return


def generate_shopping_list(recipes: List[Tuple[str, str]]) -> List[Tuple[float, str, str]]:
    shopping_list = []
    for recipe in recipes:
        for ingredient_detail in recipe_ingredients(recipe):
            add_to_shopping_list(ingredient_detail, shopping_list)
    return shopping_list


def display_shopping_list(shopping_list: List[Tuple[float, str, str]]) -> None:
    print("Shopping List:")
    for amount, measure, ingredient in shopping_list:
        print(f"{amount} {measure} {ingredient}")


def sanitise_command(command: str) -> str:
    return command.strip().lower().split()[0]


def main():
   
    
 recipes = []
 shopping_list = []


while True:
        print("Welcome to the recipe manager!")
        command = input("Enter a command: ")
        command = sanitise_command(command)

        if command == 'h':
            print(HELP_TEXT)

        elif command == 'mkrec':
            new_recipe = create_recipe()
            add_recipe(new_recipe, recipes)

        elif command.startswith('add '):
            recipe_name = command[4:].strip()
            recipe = find_recipe(recipe_name, recipes)
            if recipe:
                ingredient_details = input("Enter ingredient details (amount, unit, name): ")
                ingredient_details = parse_ingredient(ingredient_details)
                add_to_shopping_list(ingredient_details, shopping_list)
            else:
                print(f"Recipe {recipe_name} not found in cookbook.")

        elif command.startswith('rm '):
            recipe_name = command[3:].strip()
            remove_recipe(recipe_name, recipes)

        elif command.startswith('rm -i '):
            ingredient_detail = command[6:].strip()
            ingredient_detail = ingredient_detail.split(' ')
            ingredient_name = ' '.join(ingredient_detail[:-1])
            amount = float(ingredient_detail[-1])
            remove_from_shopping_list(ingredient_name, amount, shopping_list)

        elif command == 'ls':
            for recipe in recipes:
                print(get_recipe_name(recipe))

        elif command == 'ls -a':
            for recipe in recipes:
                print(f"{get_recipe_name(recipe)}: {recipe[1]}")

        elif command == 'ls -s':
            display_shopping_list(shopping_list)

        elif command == 'g' or command == 'G':
            ingredients = generate_shopping_list(recipes)
            for ingredient in ingredients:
                add_to_shopping_list(ingredient, shopping_list)

        elif command == 'q' or command == 'Q':
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please enter 'h' for help.")

if _name_ == "_main_":
        main()
