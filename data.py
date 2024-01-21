import json


def load_recipes():
    with open ('recipes.json', 'r') as file:
        recipes = json.load (file)
    return recipes


def load_users():
    with open ('users.json', 'r') as file:
        users = json.load (file)
    return users


def save_users(users):
    with open ('users.json', 'w') as file:
        json.dump (users, file)
