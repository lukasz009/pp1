from functions import rzut

wynik = rzut(3)
print('Wyrzucone oczka: ', end='')
for x in wynik:
    print(x, end=' ')
print('\nSuma oczek: {}'.format(sum(wynik)))
