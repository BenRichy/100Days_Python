from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.speed("fastest")
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
        self.hideturtle()


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align="center")