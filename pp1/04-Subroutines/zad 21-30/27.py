from functions import liczSamogl

tekst = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'

result = liczSamogl(tekst)

# wypisywanie par ze słownika klucz(key):wartość(result[key])
for key in result:
    print('{} : {}'.format(key, result[key]))
