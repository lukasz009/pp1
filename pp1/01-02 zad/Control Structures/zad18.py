for x in range(1, 31):
    if not x % 3 and not x % 5:
        print('BINGO')
    elif not x % 3:
        print('THREE')
    elif not x % 5:
        print('FIVE')
    else:
        print(x)
