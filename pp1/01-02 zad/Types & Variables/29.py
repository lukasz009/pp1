from random import randint

u = int(input("Podaj ile oczek kostki wyrzucił komputer: "))
k = randint(1, 6)
print(f'Komputer wyrzucił: {k}')
print(f'Zgadłeś: {u == k}')

