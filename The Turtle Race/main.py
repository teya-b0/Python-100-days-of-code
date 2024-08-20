import turtle as t
import random


def create_turtles():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []

    for color in colors:

        if color == "red":
            red_tim = t.Turtle(shape="turtle")
            red_tim.color("red")
            red_tim.pu()
            red_tim.goto(x=-480, y=-250)
            turtles.append(red_tim)

        if color == "orange":
            orange_tim = t.Turtle(shape="turtle")
            orange_tim.color("orange")
            orange_tim.pu()
            orange_tim.goto(x=-480, y=-150)
            turtles.append(orange_tim)

        if color == "yellow":
            yellow_tim = t.Turtle(shape="turtle")
            yellow_tim.color("yellow")
            yellow_tim.pu()
            yellow_tim.goto(x=-480, y=-50)
            turtles.append(yellow_tim)

        if color == "green":
            green_tim = t.Turtle(shape="turtle")
            green_tim.color("green")
            green_tim.pu()
            green_tim.goto(x=-480, y=50)
            turtles.append(green_tim)

        if color == "blue":
            blue_tim = t.Turtle(shape="turtle")
            blue_tim.color("blue")
            blue_tim.pu()
            blue_tim.goto(x=-480, y=150)
            turtles.append(blue_tim)

        if color == "purple":
            purple_tim = t.Turtle(shape="turtle")
            purple_tim.color("purple")
            purple_tim.pu()
            purple_tim.goto(x=-480, y=250)
            turtles.append(purple_tim)
    return turtles


race_on = False

screen = t.Screen()
screen.setup(width=1000, height=800)

all_turtles = create_turtles()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color..\n:").lower()

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 480:
            race_on = False
            wining_color = turtle.pencolor()

            if wining_color == user_bet:
                print(f"You've won!\nThe {wining_color} turtle is the winner!")
            else:
                print(f"You've lost!\nThe {wining_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
