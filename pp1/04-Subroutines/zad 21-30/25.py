from functions import jestImie

name = 'Wojtek'
names = ['Janek', 'Ania', 'Wojtek', 'Zosia']

print('Imiona: {}\nImię: {}\nRezultat: {}'.format(
    ' '.join(names), name, jestImie(name, names)))
