import turtle

blk = (0,0,0)

def rect(height: int, length: int, fill: bool, source):
    rt = turtle.Turtle()
    rt.hideturtle()
    rt.penup()
    rt.goto(0, 0)
    rt.setheading(0)
    rt.pendown()
    rt.speed(0) 
    if fill and source:
        rt.color(source)
        rt.begin_fill()
    else:
        rt.color(source if source else blk)
    for _ in range(2):
        rt.forward(length)
        rt.left(90)
        rt.forward(height)
        rt.left(90)
    if fill and source:
        rt.end_fill()



def carr(cote : int, fill, source):
    ct = turtle.Turtle()
    ct.speed(0)
    if source == None:
        ct.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        ct.color(fcolor)
        ct.begin_fill()

    for x in range(0, 5):
        ct.forward(cote)
        ct.left(90)
    if fill == True:
        ct.end_fill()



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
