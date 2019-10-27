# BMI
def oblicz_bmi(waga,wzrost):
    bmi =  waga/(wzrost/100)**2
    if bmi < 18.5:
        return bmi,'niedowaga'
    elif bmi >= 18.5 and bmi < 25:
        return bmi,'waga prawidłowa'
    elif bmi >=25 and bmi < 30:
        return bmi,'nadwaga'
    else:
        return bmi,'otyłość'

class LessThanOneError(Exception):
    """ Błąd gdy wartość <= 0 """
    pass

try:
    wzrost = float(input('Podaj wzrost w cm: '))
    if wzrost <= 0:
        raise LessThanOneError
    waga = float(input('Podaj wagę w kg: '))
    if waga <= 0:
        raise LessThanOneError
    print('Wskaźnik BMI: {0:.2f} ({1})'.format(oblicz_bmi(waga,wzrost)[0],oblicz_bmi(waga,wzrost)[1]))
except ValueError:
    print('Podana wartość jest nieprawidłowa!')
except LessThanOneError:
    print('Wartość nie może być mniejsza od 1!')