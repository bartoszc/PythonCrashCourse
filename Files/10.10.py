def count_words(filename):
    """Obliczenie przybliżonej liczby słów w danym pliku."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Przepraszamy, ale plik " + filename + " nie istnieje."
        print(msg)
    else:
        # Obliczenie przybliżonej liczby słów w danym pliku.
        words = contents.split()
        num_words = len(words)
        print("Plik " + filename + " zawiera " + str(num_words) + " słów.")


def count_occurences(filename, word):
    """Obliczenie przybliżonej liczby słów w danym pliku."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        num_words = contents.count(word.lower())
        print("Plik " + filename + " zawiera " + str(num_words) + " wystapien słowa "+ word)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
    count_occurences(filename, 'the')

