filename = 'learning_python.txt'

with open(filename) as fileobject:
    for line in fileobject:
        line = line.replace('Pythonie', 'C')
        print(line.strip())
