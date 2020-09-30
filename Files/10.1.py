filename = 'learning_python.txt'

with open(filename) as fileobject:
    lines = fileobject.read()
    print(lines)

with open(filename) as fileobject:
    for line in fileobject:
        print(line)

with open(filename) as fileobject:
    lines = fileobject.read()

print(lines)