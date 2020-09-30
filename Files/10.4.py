filename = 'guests_book.txt'

while True:
    name = input('Enter your guest name: (to break pass "xxx") ')
    if name == 'xxx':
        break
    print('Hello, ' + name)
    with open(filename, 'a') as fileobject:
        fileobject.write(name + '\n')

