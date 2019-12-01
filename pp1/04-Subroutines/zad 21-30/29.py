from functions import mediana, dominanta

tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

print('Liczby: {}'.format(' '.join([str(i) for i in tab])))
print('Mediana: {}'.format(mediana(tab)))
print('Dominanta: {}'.format(dominanta(tab)))
