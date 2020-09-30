import json


def get_stored_number():
    filename = 'your_number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    number = input("What is your favourite number? ")
    filename = 'your_number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
        return number


def my_number():
    """Przywitanie użytkownika z użyciem jego imienia."""
    number = get_stored_number()
    if number:
        print("Your favourite number is " + number + "!")
    else:
        number = get_new_number()
        print("Your favourite number: " + number + " was saved.")


my_number()
