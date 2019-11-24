table = [['Marek', 'Zelnik', 'zelnik@sed.pl'], [
    'Ewa', 'Maj', 'maje@wp.pl'], ['Piotr', 'Wyga', 'wygap@gop.pl']]

with open('03-FileHandling/plik.csv', 'w+') as file:
    file.write('Imie,Nazwisko,Email\n')
    for items in table:
        for item in items:
            file.write(item+',')
        file.write('\n')
