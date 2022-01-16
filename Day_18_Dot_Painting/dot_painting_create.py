import dot_painting_extract as dot_cols
import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
dot_colour_list = dot_cols.colour_list
print(dot_colour_list)

def dot_colour():
    colour = random.choice(dot_colour_list)
    return colour


dots_per_row = 10
dots_per_col = 10
dot_size = 20
move_forward = 50
row_gap = 10
screen_buffer = 10

canvas_width = dots_per_row * move_forward * dot_size + (2 * screen_buffer)
canvas_height = dots_per_col * row_gap * dot_size + (2 * screen_buffer)

turtle.setworldcoordinates(0, 0, 500, 500)
tim.hideturtle()
tim.speed(0)
tim.penup()
tim.setpos(screen_buffer, screen_buffer)

dot_num = 0
for number in range(dots_per_row*dots_per_col):
    tim.dot(dot_size, dot_colour())
    dot_num += 1
    tim.forward(move_forward)
    if dot_num % 10 == 0:
        tim.setpos(screen_buffer, screen_buffer + ((dot_num/10)*(dot_size+row_gap)))



screen = turtle.Screen()
tim.screen.exitonclick()



