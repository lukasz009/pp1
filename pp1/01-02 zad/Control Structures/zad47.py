# Kwota na monety 5,2,1 zł
class NegativeError(Exception):
    """ Wartość ujemna """
    pass

x = None

try:
    kwota = int(input('Podaj kwotę w zł: '))
    if kwota <= 0:
        raise NegativeError
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą")
except NegativeError:
    print("Kwota nie moze być ujemna!")
else:
    temp = kwota
    x = kwota // 5
    r = kwota % 5
    piatki = x
    if r > 0:
        x = r // 2
        r = r % 2
        dwojki = x
        if r > 0:
            jedynki = r
        else:
            jedynki = 0
    else:
        dwojki = 0
        jedynki = 0
    print("""Kwota {0} zł w monetach:
5 zł - {1} szt
2 zł - {2} szt
1 zł - {3} szt""".format(kwota,piatki,dwojki,jedynki))