x, y = 5, 2
if x > 0:
    if y > 0:
        print(f'Punkt P({x},{y}) znajduje się w pierwszej ćwiartce układu współrzędnych')
    elif y < 0:
        print(f'Punkt P({x},{y}) znajduje się w czwartej ćwiartce układu współrzędnych')
    else:
        print(f'Punkt P({x},{y}) znajduje się na osi OX układu współrzędnych')
elif x < 0:
    if y > 0:
        print(f'Punkt P({x},{y}) znajduje się w drugiej ćwiartce układu współrzędnych')
    elif y < 0:
        print(f'Punkt P({x},{y}) znajduje się w trzeciej ćwiartce układu współrzędnych')
    else:
        print(f'Punkt P({x},{y}) znajduje się na osi OX układu współrzędnych')
else:
    if y != 0:
        print(f'Punkt P({x},{y}) znajduje się na osi OY układu współrzędnych')
    else:
        print(f'Punkt P({x},{y}) znajduje się w punkcie 0,0 układu współrzędnych')
