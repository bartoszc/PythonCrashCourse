def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    new_m = []

    while magicians:
        new_m.append('Great ' + magicians.pop())
    return new_m


magicians = ['one', 'two', 'three']
new_m = make_great(magicians[:])
show_magicians(new_m)
show_magicians(magicians)
