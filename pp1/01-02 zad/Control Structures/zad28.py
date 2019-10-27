a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
for x in range(1, a + 1):
    if x == 1 or x == a:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")
