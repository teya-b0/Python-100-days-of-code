from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.pu()
    segment.goto(position)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    for seg in segments:
        seg.fd(20)

screen.exitonclick()
