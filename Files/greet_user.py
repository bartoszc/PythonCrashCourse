import json


def get_stored_username():
    """Pobranie imienia z pliku, o ile taki istnieje."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("Jak masz na imię? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username


def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    username = get_stored_username()
    if username:
        print("Witamy ponownie, " + username + "!")
    else:
        username = get_new_username()
        print("Twoje imię zostało zapisane i będzie używane później, " + username + "!")


greet_user()
