def wspak(tekst):
    return tekst[::-1]


def spacje(tekst):
    nowy = ''
    for char in tekst:
        nowy += (char+' ')
    return nowy


def wielka(tekst):
    newtekst = ''
    splitted = tekst.split(' ')
    for word in splitted:
        index = 0
        for char in word:
            if index == 0:
                char = char.upper()
            else:
                char = char.lower()
            newtekst += char
            index += 1
        newtekst += ' '
    return newtekst
