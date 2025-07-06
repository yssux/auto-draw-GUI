import math
import turtle

blk = (0,0,0)

def tri_equi(cote, fill, source):
    trit = turtle.Turtle()
    trit.speed(0)
    trit.hideturtle()
    if source == None:
        trit.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        trit.color(fcolor)
        trit.begin_fill()

    for x in range(1, 4):
        trit.forward(cote)
        trit.left(360 / 3)
    if fill == True:
        trit.end_fill()

def tri_iso(side, base, fill, source):
    trit = turtle.Turtle()
    if source == None:
        trit.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        trit.color(fcolor)
        trit.begin_fill()

    height = (side ** 2 - (base / 2) ** 2) ** 0.5
    # Draw the isosceles triangle
    angle = math.degrees(math.atan(height / (base / 2)))
    # Draw the isosceles triangle
    trit.forward(base)  # Draw the base
    trit.left(180 - angle)  # Turn to draw the first equal side
    trit.forward(side)  # Draw the first equal side
    trit.left(2 * angle)  # Turn to draw the second equal side
    trit.forward(side)
    if fill == True:
        trit.end_fill()

def tri_rect(a, b, fill, source):
    trit = turtle.Turtle()
    if source == None:
        trit.color(blk)
    elif fill == True and bool(source) == True:
        fcolor = source
        trit.color(fcolor)
        trit.begin_fill()
    # Calculate hypotenuse
    c = math.sqrt(a ** 2 + b ** 2)
    angle = math.degrees(math.atan2(b, a))
    # Move to starting position (optional)
    trit.penup()
    trit.goto(-a // 2, -b // 2)  # Centering the triangle
    trit.pendown()
    # Draw the triangle correctly
    trit.forward(a)  # Base
    trit.left(90)
    trit.forward(b)  # Height
    trit.left(90 + angle)
    trit.forward(c)  # Hypotenuse
    if fill == True:
        trit.end_fill()