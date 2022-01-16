from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("salmon")

# draw a square
# for i in range(1, 5):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line
# for i in range(1, 51):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# draw triangle to decagon
# random colour for each shape

# first define function to draw the shape, calculating the angle size
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# # for loop to draw each shape, then change the pen colour after
# for shape_side in range(3,11):
#     draw_shape(shape_side)
#     pen_r = random.uniform(0,1)
#     pen_g = random.uniform(0,1)
#     pen_b = random.uniform(0,1)
#     tim.pencolor(pen_r, pen_g, pen_b)


# create a random walk for the turtle
# number_of_directions = 4
# tim.width(15)
# tim.speed(9)
# for i in range(1, 100):
#     tim.forward(30)
#     direction_to_turn = random.randint(1,number_of_directions+1)
#     tim.right(90*direction_to_turn)
#     pen_r = random.uniform(0,1)
#     pen_g = random.uniform(0,1)
#     pen_b = random.uniform(0,1)
#     tim.pencolor(pen_r, pen_g, pen_b)

# draw a spirograph
# multiple circles around a point, each a different colour
def random_colour():
    pen_r = random.uniform(0,1)
    pen_g = random.uniform(0,1)
    pen_b = random.uniform(0,1)
    colour = (pen_r, pen_g, pen_b)
    return colour

tim.speed("fastest")
circle_size = 100
for i in range(0,360,10):
    tim.setheading(i)
    tim.color(random_colour())
    tim.circle(circle_size)





screen = Screen()
screen.exitonclick()
