file1 = 'cats.txt'
file2 = 'dogs.txt'


def working_with_files(*files):
    """Obliczenie przybliżonej liczby słów w danym pliku."""
    for file in files:
        try:
            with open(file) as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            pass
        else:
            print(contents + '\n')


working_with_files(file1, file2)
