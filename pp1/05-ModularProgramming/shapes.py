def drawSquare(x, y, n, existing=None):
    if existing == None:
        import turtle
        pen = turtle.Turtle()
    else:
        pen = existing
    pen.penup()
    pen.setposition(x, y)
    pen.pendown()
    i = 0
    for i in range(4, 0, -1):
        pen.setheading(i*90)
        pen.forward(n)
    if existing == None:
        turtle.done()


def drawGrid(numrows, numcols, cellsize):
    import turtle

    pen = turtle.Turtle()

    for y in range(numrows, 0, -1):
        for x in range(numcols):
            drawSquare(x*100, y*100, cellsize, pen)
    turtle.done()


def drawCircle(x, y, r):
    import turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.setpos(x, y-r)
    pen.pendown()
    pen.circle(r)
    # wróć do środka okręgu
    # pen.setpos(x, y)
    turtle.done()


def drawTriangle(x, y, m):
    import turtle
    pen = turtle.Turtle()
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    pen.seth(0)
    pen.right(60)
    for _ in range(1, 4):
        pen.forward(m)
        pen.right(120)
    turtle.done()


def drawStar():
    import turtle
    pen = turtle.Turtle()

    for i in range(10):
        pen.forward(70)
        if i % 2 == 0:
            pen.left(72)
        else:
            pen.right(144)

    turtle.done()
