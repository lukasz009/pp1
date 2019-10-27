try:
    x = float(input('Podaj pierwszą liczbę: '))
    y = float(input('Podaj drugą liczbę: '))
    z = float(input('Podaj trzecią liczbę: '))
    tablica = [x,y,z]
    tablica.sort()
    print(f'Liczby rosnąco: {tablica}')
except ValueError:
    print('Podana wartość nie jest liczbą!')
