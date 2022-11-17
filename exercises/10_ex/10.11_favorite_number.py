import json


def get_number():
    """Ask a favorite number."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        None
    else:
        return fav_number


def ask_number():
    """Ask user for favorite number."""
    filename = 'favorite_number.json'
    fav_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(fav_number, f)
    return fav_number


def return_number():
    """Return user's favorite number."""
    fav_number = get_number()
    if fav_number:
        print(f"I know your favorite number. It is {fav_number}")
    else:
        fav_number = ask_number()
        print(f"Now I know your favorite number. It is {fav_number}")


return_number()
