from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250,250)
        self.level = 1
        self.speed("fastest")
        self.write(f"Level: {self.level}", font=FONT)
        self.hideturtle()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)



