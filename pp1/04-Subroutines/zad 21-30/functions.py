def miesiac(n):
    if n < 1 or n > 12:
        return 'Błędny argument'
    nazwy = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec',
             'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    return nazwy[n - 1]


def jestImie(imie, imiona):
    if imie in imiona:
        return 'Imię zawarte jest w wykazie imion'
    else:
        return 'Imię nie znajduje się w wykazie imion'


def podatek(dochod):
    if dochod < 0:
        return False
    elif dochod <= 5000:
        return dochod*0.17
    else:
        return 5000*0.17+(dochod-5000)*0.32


def liczSamogl(tekst):
    vowels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
    temp = []
    for vowel in vowels:
        temp.append(tekst.count(vowel))
    # łączenie 2 list na słownik klucz:wartość
    result = {vowels[i]: temp[i] for i in range(0, len(vowels))}
    # albo
    # result = dict(zip(vowels,temp))
    #
    # a = [1,2,3] b = [4,5,6]
    # zip(a,b) = [(1,4), (2,5), (3,6)] <- 3 tuple - listy bez możliwości zmiany wartości
    # dict(zip(a,b)) = [1:4, 2:5, 3:6]
    return result


def rysujWykres(jezyki, wartosci):
    d = dict(zip(jezyki, wartosci))
    for key in d:
        print('{:>10}: {} {}K'.format(key, '#'*d[key], d[key]))


def mediana(table):
    table.sort()
    if len(table) % 2 == 0:
        # parzysta = średnia 2 środkowych wyrazów
        # int(len(table)/2)-1 -> index wyrazu n/2 (-1 bo index zaczyna się na 0)
        # int(len(table)/2) -> index wyrazu (n/2)+1 (bez +1 bo index od 0)
        return (table[int(len(table)/2)-1] + table[int(len(table)/2)])/2
    else:
        return table[int((len(table)+1)/2)]


def dominanta(table):
    table.sort()
    # max() - znajdź największą wartość
    # set() - przekonwertuj listę na set (unikalne wartości)
    # key - funkcja po której max() będzie porównywał
    # key=table.count - wyszukaj największej liczby dla której table.count(liczba) jest największa - np. dla 1 (w secie) table.count(1) (ile razy w table występuje liczba 1)
    return max(set(table), key=table.count)


def losuj():
    from random import randint
    return randint(1, 50)
