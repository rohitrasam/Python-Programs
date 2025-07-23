ar = [x for x in range(1, 101)]
for item in ar:
    if item % 15 == 0:
        print('{}, fizz buzz'.format(item))
    elif item % 3 == 0:
        print('{}, fizz'.format(item))
    elif item % 5 == 0:
        print('{}, buzz'.format(item))
