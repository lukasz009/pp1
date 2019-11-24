tab = []
with open("03-FileHandling/numbers.", 'r') as tekst:
    for line in tekst:
        tab.append(int(line))
tab.sort()
for n in tab:
    print(n, end=' ')
