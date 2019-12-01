from functions import transpozycja

macierz = [[1, 2, 0], [0, 0, 3], [5, 1, 1]]

print('\nMacierz: ')
for rows in macierz:
    for vals in rows:
        print(vals, end=' ')
    print()

print('\nMacierz transponowana: ')
for rows in transpozycja(macierz):
    for vals in rows:
        print(vals, end=' ')
    print()
