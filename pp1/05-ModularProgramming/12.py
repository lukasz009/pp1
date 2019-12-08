import shapes as sh

mode = input('Wybierz podpunkt a-e: ')
if mode == 'a':
    print('Okrąg x,y promień r')
    x = int(input('x: '))
    y = int(input('y: '))
    r = int(input('r: '))
    sh.drawCircle(x, y, r)
elif mode == 'b':
    print('Trójkąt x,y bok m')
    x = int(input('x: '))
    y = int(input('y: '))
    m = int(input('m: '))
    sh.drawTriangle(x, y, m)
elif mode == 'c':
    sh.drawStar()
elif mode == 'd':
    pass
else:
    pass
