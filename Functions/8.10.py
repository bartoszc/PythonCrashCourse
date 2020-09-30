def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'Great ' + magicians[i]
    return magicians


new_m = make_great(['one', 'two', 'three'])
show_magicians(new_m)
