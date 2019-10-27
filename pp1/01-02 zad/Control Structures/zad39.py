# 50 wyrazów Fibbonaciego

a = 0
b = 1
suma = 0

for x in range(0, 50):
    suma += a
    a = b
    b = suma
    print(suma, end=" ")

