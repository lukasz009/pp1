def czytajWspolczynniki():
    a = int(input('Podaj współczynnik a: '))
    b = int(input('Podaj współczynnik b: '))
    c = int(input('Podaj współczynnik c: '))
    print('Równanie kwadratowe postaci: {}x2{}{}x{}{}=0'.format(
        a, "" if b < 0 else "+", b, "" if c < 0 else "+", c))
    return [a, b, c]


def obliczDelte(params):
    if params[0] == 0:
        raise ZeroDivisionError
    else:
        delta = params[1]**2 - 4*params[0]*params[2]
    return delta


def obliczPierwiastki(params):
    from math import sqrt
    try:
        delta = obliczDelte(params)
        if delta < 0:
            return None
        elif delta == 0:
            x0 = ((-1)*params[1])/(2*params[0])
            return x0
        else:
            x1 = ((-1)*params[1]-sqrt(delta))/(2*params[0])
            x2 = ((-1)*params[1]+sqrt(delta))/(2*params[0])
            return [x1, x2]
    except ZeroDivisionError:
        x = ((-1)*params[2])/params[1]
        return x


def wyswietlPierwiastki(tab):
    
    if tab == None:
        print('')
    elif isinstance(tab, (float, int)):
        print('Pierwiastek równania: x0 = {}'.format(tab))
    else:
        print('Pierwiastki równania: x1 = {}, x2 = {}'.format(tab[0], tab[1]))
