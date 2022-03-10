# turtle only works with gif files as images
import turtle
import pandas as pd

states_info = pd.read_csv("50_states.csv")

# load in map background
screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# set variables to count correct guesses and current score
correct_guesses = []
score = 0

# max score is 50
while score < 50:
    #user input to guess state
    answer_state = screen.textinput(title=f"Guess the State ({score}/50)",
                                    prompt="What's another state?")
    #convert state name to same format as csv input
    answer_state = answer_state.title()

    # check if state name is in list
    if states_info['state'].eq(answer_state).any():
        #check if state has already been guessed
        if answer_state in correct_guesses:
            continue
        #if not already guessed do the following
        correct_guesses.append(answer_state)
        score += 1
        # get x and y coords to paste name
        answer_x = float(states_info["x"][states_info["state"] == answer_state])
        answer_y = float(states_info["y"][states_info["state"] == answer_state])

        # write state name in correct location
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.pencolor("black")
        answer_turtle.penup()
        answer_turtle.goto(answer_x,answer_y)
        answer_turtle.pendown()
        answer_turtle.write(answer_state)

    if answer_state == "Exit":

        # get missing states
        missing_states = states_info[~states_info["state"].isin(correct_guesses)]
        missing_states.to_csv("missing_states.csv")
        screen.bye()





screen.exitonclick()