for x in range(3):
    if input("Podaj PIN: ") == '0805':
        print('Działa')
        break
    else:
        print('Nieprawidłowy PIN.')
    if x == 2:
        print('Karta zablokowana.')
