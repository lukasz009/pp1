from random import randint

for x in range(1,8):
    table = []
    print(f'{x}', end='')
    while len(table) < 6:
        numer = randint(1,49)
        if numer not in table:
            table.append(numer)
    table.sort()
    for val in table:
        print(' {0:4d}'.format(val), end='')
    print()