from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.hideturtle()
        self.pu()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-5, 370)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
