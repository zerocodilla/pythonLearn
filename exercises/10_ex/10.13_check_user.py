import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    old_username = get_stored_username()

    if not old_username:
        new_username = get_new_username()
        print(f"We'll remember you when you come back, {new_username.title()}!")
        return

    new_username = check_user()

    if new_username == old_username:
        print(f"Welcome back, {old_username.title()}!")
    else:
        print(f"We'll remember you when you come back, {new_username.title()}!")


def check_user():
    """Check whether the current user is the person who last used the program"""
    username = get_stored_username()
    user_check = input(f"Is your name {username}? Please answer 'y' or 'n': ")
    if user_check == 'n':
        username = get_new_username()
    return username

