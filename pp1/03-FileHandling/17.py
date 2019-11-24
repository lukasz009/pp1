tab = []
with open('03-FileHandling/numbers.txt') as file:
    for line in file:
        if int(line) % 2 == 0:
            tab.append(int(line))
with open('03-FileHandling/evennumbers.txt', 'w+') as file:
    for x in tab:
        file.write(str(x)+'\n')
