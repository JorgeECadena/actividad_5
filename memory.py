from random import *
from turtle import *
from freegames import path

car = path('car.gif')
colors = [(randrange(256), randrange(256), randrange(256)) for _ in range(32)]
#tiles = list(range(32)) * 2
tiles = colors * 2
state = {'mark': None}
hide = [True] * 64

colormode(255)
shuffle(tiles)

def rgb_to_hex(rgb):
    """Convert (R, G, B) tuple to hex format for Turtle."""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def square(x, y, fill_color=None):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()

    if fill_color:
        fill_hex = rgb_to_hex(fill_color)
        color("black", fill_hex)
    else:
        color("black", "white")


    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        x, y = xy(count)

        if hide[count]:
            square(x, y)
        elif state['mark'] == count:
            square(x, y, tiles[count])

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        square(x, y, tiles[mark])
    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
