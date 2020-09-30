filename = 'guest.txt'

name = input('Enter your guest name: ')
with open(filename, 'w') as fileobject:
    fileobject.write(name)

