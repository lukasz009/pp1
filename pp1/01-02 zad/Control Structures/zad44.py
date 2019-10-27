try:
    limit = int(input('Podaj limit prędkości (km/h): '))
    if limit <= 0:
        raise ValueError
    predkosc = float(input('Podaj prędkość pojazdu (km/h): '))
    if predkosc <= 0:
        raise ValueError
    przekroczenie = predkosc - limit
    if przekroczenie <= 0:
        mandat = 0
    elif przekroczenie <= 10:
        mandat = przekroczenie*5
    else:
        mandat = 10*5 + (przekroczenie-10)*15

    print('Mandat: {:.2f} zł'.format(mandat))
except ValueError:
    print('Niepoprawna wartość!')
