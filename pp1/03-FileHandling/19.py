import re

tab = []
with open('03-FileHandling/students.txt') as file:
    for line in file:
        temp = re.findall('\d+[^@,]', line)
        if temp and int(temp[0]) < 30:
            temp = line.split(',')
            print('{:7} {:9} {}'.format(temp[0], temp[1], temp[4]), end='')
