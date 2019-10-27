# Program obliczy sumę i średnią arytmetyczną dowolnej ilości liczb wprowadzonych z klawiatury. 
# Wprowadzenie liczby 0 kończy działanie programu.

try:
    c = 0
    suma = 0
    while True:    
        a = int(input('Podaj liczbę: '))
        if a == 0:
            srednia = suma/c
            break
        c += 1
        suma += a
    print(f'REZULTAT: Liczb: {c}, Suma={suma}, Średnia={srednia}')
except ValueError:
    print('To nie liczba!')