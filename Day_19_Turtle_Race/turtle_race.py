from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                 prompt="Which turtle will win the race? Enter a colour")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
start_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle_index in all_turtles:
        if turtle_index.xcor() >= 200:
            is_race_on = False
            winning_turtle = turtle_index.pencolor()
            if winning_turtle == user_bet:
                final_result = "win"
            else:
                final_result = "lose"
            print(f"You {final_result}. The winning turtle is {winning_turtle}.")
        rand_distance = random.randint(0,10)
        turtle_index.forward(rand_distance)





