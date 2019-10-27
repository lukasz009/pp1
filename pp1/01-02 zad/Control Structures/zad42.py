class DivisionByZero(Exception):
    """ Dzielenie przez zero """
    pass

try:
    a = float(input('Podaj liczbę: '))
    b = float(input('Podaj liczbę: '))
    if b == 0:
        raise DivisionByZero
    print('Wynik dzielenia {:.5g}/{:.5g} wynosi {:.5g}'.format(a,b,a/b))
except ValueError:
    print('To nie liczba!')
except DivisionByZero:
    print('Dzielenie przez 0!')