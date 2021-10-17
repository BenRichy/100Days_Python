from turtle import Turtle, Screen

# create an object called timmy
timmy = Turtle()
print(timmy)
# call methods related to the object timmy
timmy.shape("turtle")
timmy.color("cyan")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()