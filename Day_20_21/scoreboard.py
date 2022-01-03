from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.speed("fastest")
        self.write(f"Score: {self.score}", font=("Arial", 16, "bold"), align="center")
        self.hideturtle()


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=("Arial", 16, "bold"), align="center")