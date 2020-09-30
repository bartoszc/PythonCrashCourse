filename = 'answers.txt'

while True:
    answer = input('Why do you like programming? (to break pass "xxx") ')
    if answer == 'xxx':
        break
    with open(filename, 'a') as fileobject:
        fileobject.write(answer + '\n')

