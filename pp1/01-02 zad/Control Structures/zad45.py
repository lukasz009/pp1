class LessThanOneError(Exception):
    """ Błąd gdy y < 1 """
    pass

try:
    y = int(input('Podaj y: '))
    if y < 1:
        raise LessThanOneError
    x = 0
    liczba = 1
    
    print('Liczby pierwsze: ', end='')
    while x < y:
        flag = True
        if liczba == 2:
            print(liczba, end=' ')
            x += 1
        elif liczba > 2:
            for d in range(2,liczba):
                if liczba % d == 0:
                    flag = False
                    break
            if flag == True:
                print(liczba, end=' ')
                x += 1
        liczba += 1



except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except LessThanOneError:
    print('N nie może być mniejsze do 1!')