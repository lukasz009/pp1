# NWD
from math import gcd

class NotANaturalNumber(Exception):
    """ Jeżeli liczba nie jest naturalna - tzn. mniejsza od zera lub/i nie-całkowita"""
    pass

try:
    x = int(input('Podaj pierwszą liczbę naturalną: '))
    if x < 0:
        raise NotANaturalNumber
    y = int(input('Podaj drugą liczbę naturalną: '))
    if y < 0:
        raise NotANaturalNumber
    print(f'NWD dla liczb {x} oraz {y} to {gcd(x,y)}')
except (ValueError, NotANaturalNumber):
    print('Podana wartość nie jest liczbą naturalną!')
