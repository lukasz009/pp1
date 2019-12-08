from math import sqrt, pow, pi, factorial, trunc

x = 3.7
y = 4

print('\
    Pierwiastek kwadratowy z {0} wynosi {2}\n\
    {0} do potęgi {1} wynosi {3}\n\
    Pierwiastek {1}-tego stopnia z {0} wynosi {4}\n\
    Pole koła o promieniu {1} wynosi {5}\n\
    Silnia {1} wynosi {6}\n\
    Największa możliwa liczba całkowita <= {0} wynosi {7}\
    '.format(
    x,
    y,
    sqrt(x),
    pow(x, y),
    pow(x, 1/y),
    pi*pow(y, 2),
    factorial(y),
    trunc(x)
))
