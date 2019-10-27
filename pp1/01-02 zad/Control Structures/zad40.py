import random

wyniki = [0] * 6

for x in range(0, 100):
    rzut = random.randint(1, 6)
    wyniki[rzut - 1] += 1

print(
    f"""Szóstka: {wyniki[5]}
Piątka: {wyniki[4]}
Czwórka: {wyniki[3]}
Trójka: {wyniki[2]}
Dwójka: {wyniki[1]}
Jedynka: {wyniki[0]}"""
)

