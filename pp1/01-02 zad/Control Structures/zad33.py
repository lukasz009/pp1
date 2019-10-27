class NegativeNumberError(Exception):
    """ Liczba jest ujemna - nie naturalna """
    pass


x = input('Podaj liczbę naturalną: ')
nazwy = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']

try:
    int(x)
    if int(x) < 0:
        raise NegativeNumberError
    print(f'{x} - ', end='')
    for i in x:
        print(nazwy[int(i)],end=' ')
    print()
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except NegativeNumberError:
    print('Podana liczba nie jest naturalna!')