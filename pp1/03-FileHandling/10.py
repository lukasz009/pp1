table = [32, 16, 5, 8, 24, 7]
with open('tablica13.txt', 'w') as file:
    for x in table:
        file.write(str(x) + '\n')