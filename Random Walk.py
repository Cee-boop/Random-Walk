import turtle as t
import colorgram
from turtle import Turtle, Screen
from random import choice
t.colormode(255)
screen = Screen()


# get colour palette:
def get_rgb(c):
    """extracts colours with rgb requirements for turtle module."""
    swatch = []
    for colour in c:
        r = colour.rgb.r
        g = colour.rgb.g
        b = colour.rgb.b
        new_colour = (r, g, b)
        swatch.append(new_colour)
    return swatch


colours = colorgram.extract('-', 10)
palette = get_rgb(colours)


# initialize bot:
carl_bot = Turtle(shape='arrow')
carl_bot.pensize(10)
carl_bot.speed('normal')
carl_bot.color(choice(palette))


# bot logic:
directions = [0, 90, 270, 180]
for _ in range(201):
    carl_bot.color(choice(palette))
    carl_bot.setheading(choice(directions))
    carl_bot.forward(30)


screen.exitonclick()
