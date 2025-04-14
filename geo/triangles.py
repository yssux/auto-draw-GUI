import math
import turtle

screen = turtle.Screen()
blk = (0,0,0)

def tri_equi(cote, fill, source):
    screen.cv._rootwindow.deiconify()
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


def tri_iso(side, base, fill, source):
    screen.cv._rootwindow.deiconify()
    t = turtle.Turtle()
    if source == None:
        t.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        t.color(fcolor)
        t.begin_fill()

    height = (side ** 2 - (base / 2) ** 2) ** 0.5
    # Draw the isosceles triangle
    angle = math.degrees(math.atan(height / (base / 2)))

    # Draw the isosceles triangle
    t.forward(base)  # Draw the base
    t.left(180 - angle)  # Turn to draw the first equal side
    t.forward(side)  # Draw the first equal side
    t.left(2 * angle)  # Turn to draw the second equal side
    t.forward(side)
    if fill == True:
        t.end_fill()


def tri_rect(a, b, fill, source):
    screen.cv._rootwindow.deiconify()
    t = turtle.Turtle()
    if source == None:
        t.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        t.color(fcolor)
        t.begin_fill()
    t = turtle.Turtle()
    # Calculate hypotenuse
    c = math.sqrt(a ** 2 + b ** 2)
    angle = math.degrees(math.atan2(b, a))
    # Move to starting position (optional)
    t.penup()
    t.goto(-a // 2, -b // 2)  # Centering the triangle
    t.pendown()
    # Draw the triangle correctly
    t.forward(a)  # Base
    t.left(90)
    t.forward(b)  # Height
    t.left(90 + angle)
    t.forward(c)  # Hypotenuse