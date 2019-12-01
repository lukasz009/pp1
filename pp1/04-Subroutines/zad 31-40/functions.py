def reverseCheeky(tab):
    return tab[::-1]


def reverse(tab):
    revtab = []
    for i in range(len(tab)-1, -1, -1):
        revtab.append(tab[i])
    return revtab


def transpozycja(macierz):
    # deklaracja listy dwuwymiarowej o strukturze macierzy
    tmacierz = [[0 for x in range(len(macierz[0]))]
                for y in range(len(macierz))]
    m = 0
    for rows in macierz:
        n = 0
        for vals in rows:
            # transpozycja: zamień miejscem kolumny i wiersze
            # przypisz macierz[0][0] do tmacierz[0][0]
            # przypisz macierz[0][1] do tmacierz[1][0]
            # przypisz macierz[0][2] do tmacierz[2][0]
            # przypisz macierz[1][0] do tmacierz[0][1]
            # przypisz macierz[1][1] do tmacierz[1][1]
            # przypisz macierz[1][2] do tmacierz[2][1]
            # itp
            tmacierz[n][m] = vals
            n += 1
        m += 1
    return tmacierz


def fib(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return a


def fibR(n, prev=[0, 1]):
    if n == 1:
        return prev[0]
    else:
        a = prev[1]
        b = prev[0]+prev[1]
        return fibR(n-1, [a, b])


def sumaCyfr(val, prev=0):
    if val == 0:
        return 0
    sum = val % 10
    return sum + sumaCyfr(int(val/10), sum)


def suma(tab):
    s = 0
    for val in tab:
        if isinstance(val, int):
            s += val
        else:
            s += suma(val)
    return s


def unique(tab):
    seen = []
    uniques = []
    for val in tab:
        if val not in seen:
            uniques.append(val)
            seen.append(val)
        else:
            uniques.remove(val)
    return uniques


def uppercase(string):
    uppers = []
    for c in string:
        if c.isupper():
            uppers.append(c)
    return ''.join(uppers)


def inrange(n, x, y):
    if n >= x and n <= y:
        return True
    else:
        return False
