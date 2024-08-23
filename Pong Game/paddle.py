from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.shapesize(5, 1)
        self.pu()
        self.x = location[0]
        self.y = location[1]
        self.goto(self.x, self.y)

    def move_up(self):
        if self.ycor() < 230:
            y = self.ycor() + 20
            self.goto(self.x, y)

    def move_down(self):
        if self.ycor() > -230:
            y = self.ycor() - 20
            self.goto(self.x, y)

