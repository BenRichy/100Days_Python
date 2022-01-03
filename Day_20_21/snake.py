from turtle import Turtle

START_LENGTH = 3
START_X_COORD = 0
BODY_PIECE_GAP = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        start_x_coord = START_X_COORD
        for snake_start_body in range(START_LENGTH):
            snake_body_piece = Turtle(shape="square")
            snake_body_piece.penup()
            snake_body_piece.color("white")
            snake_body_piece.setx(start_x_coord)
            self.snake_body.append(snake_body_piece)
            start_x_coord -= BODY_PIECE_GAP

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
