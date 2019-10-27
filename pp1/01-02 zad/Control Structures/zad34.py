# Płeć oraz wiek na 2018

from datetime import date


class InvalidPESEL(Exception):
    """Niepoprawny miesiąc"""
    pass


pesel = input("Podaj  PESEL: ")

try:
    int(pesel)
    year = pesel[0] + pesel[1]
    month = pesel[2] + pesel[3]

    if int(month) in range(1, 13):
        year = '19' + year
    elif int(month) in range(21, 33):
        year = '20' + year
    elif int(month) in range(81, 93):
        year = '18' + year
    else:
        raise InvalidPESEL

    gender = int(pesel[9])

    if gender in [0, 2, 4, 6, 8]:
        gender = 'kobieta'
    else:
        gender = 'mężczyzna'

    compare_date = 2018
    age = compare_date - int(year)

    print("Płeć: {0}\nWiek : {1}".format(gender, str(age)))

except (ValueError, InvalidPESEL):
    print("Niepoprawny numer PESEL")
