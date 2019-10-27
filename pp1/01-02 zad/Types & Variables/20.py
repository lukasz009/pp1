import math

# ustawianie promienia koła i pi
pi = math.pi
r = 5

# obliczanie pola i obwodu
P = pi*r**2
O = 2*pi*r

print("""Pole koła o promieniu {0} wynosi {1}
Obwód koła o promieniu {0} wynosi {2}""".format(r,P,O))
