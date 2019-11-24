tab = []
with open('03-FileHandling/numbersinrows.txt') as file:
    for line in file:
        tab += line.split(',')
tab = [int(x) for x in tab]
print('Ilość liczb: {}\nSuma: {}'.format(len(tab), sum(tab)))
