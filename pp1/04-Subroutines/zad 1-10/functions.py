
def wyswietl(table):
    """ wyświetla cyfry w układzie 3xN """
    n = 0
    for x in table:
        assert int(x), "W tablicy znajdują się elementy nie będące cyframi"
        if n > 0 and n % 3 == 0:
            print()
        print(f'{x} ', end='')
        n += 1
    print()