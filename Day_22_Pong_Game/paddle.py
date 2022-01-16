from turtle import Turtle

PADDLE_HEIGHT_STRETCH = 1
PADDLE_WIDTH_STRETCH = 5
MOVE_DISTANCE = 20
STARTING_POSITION = (350,0)


# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=PADDLE_HEIGHT_STRETCH, stretch_wid=PADDLE_WIDTH_STRETCH)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor()-MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

