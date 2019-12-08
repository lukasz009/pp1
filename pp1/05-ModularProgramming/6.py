import csv
from statistics import mean

mode = input('Zadanie A czy B? ')

if mode == 'a':
    with open('05-ModularProgramming/employees.csv', newline='') as f:
        reader = csv.reader(f)
        c = 0
        for row in reader:
            if c == 0:
                print('{:<5}{:<15}{:<15}{:<6}{:<34}'.format(
                    '#', row[0].upper(), row[1].upper(), row[2].upper(), row[3].upper()))
                line = '='*75
                print(line)
            else:
                print('{:<5}{:<15}{:<15}{:<6}{:<25}'.format(
                    c, row[0], row[1], row[2], row[3]))
            c += 1
else:
    with open('05-ModularProgramming/employees.csv', newline='') as f:
        reader = csv.reader(f)
        c, ages = 0, []
        for row in reader:
            if c != 0:
                ages.append(row[2])
            c += 1
        ages = [int(x) for x in ages]
        print(mean(ages))
