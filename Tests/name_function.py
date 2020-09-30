def get_formatted_name(first, last, middle=''):
    """Generuje elegancko sformatowane pełne imię i nazwisko."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
