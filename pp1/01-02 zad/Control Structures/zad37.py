# mediana

try:
    a = float(input('Podaj pierwszą liczbę: '))
    b = float(input('Podaj drugą liczbę: '))
    c = float(input('Podaj trzecią liczbę: '))
    
    table = [a, b, c]

    table.remove(max(table))
    table.remove(min(table))

    print('Mediana liczb {}, {}, {} to {}'.format(a,b,c,table[0]))

except ValueError:
    print('Podana wartość nie jest liczbą!')
