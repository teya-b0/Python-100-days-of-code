import colorgram
import turtle as t
import random


def extract_colors(image, number_of_colors):

    colors_list = []
    colors = colorgram.extract(image, number_of_colors)

    for color in colors:
        colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return colors_list


rgb_list = extract_colors("Img/hirst-spot.jpg", 30)

t.colormode(255)
timmy = t.Turtle()
timmy.pu()
timmy.ht()
timmy.speed(0)

screen = t.Screen()

pos = -250

for row in range(10):
    pos += 50
    timmy.goto(-250, pos)
    for _ in range(10):
        color = random.choice(rgb_list)
        timmy.dot(20, color)
        timmy.fd(50)

screen.exitonclick()
