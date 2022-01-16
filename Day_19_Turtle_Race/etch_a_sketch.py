from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.right(5)


def rotate_anticlockwise():
    tim.left(5)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_anticlockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
