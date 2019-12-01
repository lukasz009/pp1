from functions import podatek

try:
    x = float(input('Podaj dochód: '))
    assert x > 0
    print('Podatek należny: {:.2f} zł'.format(podatek(x)))
except (ValueError, AssertionError):
    print('Błędny argument')
