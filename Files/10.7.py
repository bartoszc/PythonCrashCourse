while True:
    try:
        a = int(input('Enter first value: '))
        b = int(input('Enter second value: '))
    except ValueError:
        print('Incorrect values! a or b or both are not numbers')
    else:
        print(a + b)
        break
