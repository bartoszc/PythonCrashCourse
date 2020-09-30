from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


d1 = Die()
for i in range(10):
    d1.roll_die()

d2 = Die(10)
for i in range(10):
    d2.roll_die()

d3 = Die(20)
for i in range(10):
    d3.roll_die()