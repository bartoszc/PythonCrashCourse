def sandwich(*ingridients):
    print('Your sandwich: ')
    for ingridient in ingridients:
        print('-' + ingridient)


sandwich('tomato', 'ham', 'cucumber')
sandwich('tomato')
sandwich('tomato', 'ham')