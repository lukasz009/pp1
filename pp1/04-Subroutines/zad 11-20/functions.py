def suma(items):
    """ Funkcja wyświetlająca tablicę oraz sumę wartości """

    suma = 0
    try:
        for item in items:
            suma += item

        print(f"Tablica: {items}")
        print(f"Suma wartości: {suma}")
    except (ValueError, TypeError):
        print("Podany argument nie jest tablicą lub elementy nie są liczbami!")


def suma19(N):
    if isinstance(N, str) or N < 1:
        return 'Błędny argument'
    elif N == 1:
        return 1
    else:
        return N + suma19(N-1)


def potega(x, y):
    if y == 0:
        return 1
    else:
        return x * potega(x, y-1)


def rzut(ile=1):
    """ Funkcja symulująca rzut kostką """
    from random import randint

    table = []
    for _ in range(0, ile):
        table.append(randint(1, 6))

    return table


def wystepuje(co, gdzie):
    """ Sprawdza, czy dany element występuje w tablicy """

    for x in gdzie:
        if x == co:
            flag = True
            break
        else:
            flag = False

    if flag:
        print("Rezultat: Podana liczba występuje w tablicy.")
    else:
        print("Rezultat: Podana liczba nie występuje w tablicy.")
