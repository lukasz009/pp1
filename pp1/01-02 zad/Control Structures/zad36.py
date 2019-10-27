# liczba podzielna przez 7, przy dzieleniu przez 2,3,4,5,6 daje reszte 1

liczba = 0
flag = False
while flag != True:
    if (
        liczba % 7 == 0
        and liczba % 6 == 1
        and liczba % 5 == 1
        and liczba % 4 == 1
        and liczba % 3 == 1
        and liczba % 2 == 1
    ):
        flag = True
    else:
        flag = False
        liczba += 1

print(
    "Liczba {0} jest podzielna przez 7 oraz przy dzieleniu przez 2,3,4,5,6 daje resztę 1.".format(
        liczba
    )
)

