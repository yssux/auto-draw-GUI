import turtle

blk = (0,0,0)

def rect(height, length, fill, source):
    t = turtle.Turtle()
    if source == None:
        t.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        t.color(fcolor)
        t.begin_fill()

    t.forward(length)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(height)
    if fill:
        t.end_fill()


def carr(cote, fill, source):
    t = turtle.Turtle()
    if source == None:
        t.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        t.color(fcolor)
        t.begin_fill()

    for x in range(0, 5):
        t.forward(cote)
        t.left(90)
    if fill == True:
        t.end_fill()


def triang(cote, fill, source):
    t = turtle.Turtle()
    if source == None:
        t.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        t.color(fcolor)
        t.begin_fill()

    for x in range(1, 4):
        t.forward(cote)
        t.left(360 / 3)
    if fill == True:
        t.end_fill()


def circle(rad, fill, source):
    t = turtle.Turtle()
    if source == None:
        t.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        t.color(fcolor)
        t.begin_fill()
    t.circle(rad)
    if fill == True:
        t.end_fill()
