import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
counter = 0
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    print(counter % 1)
    if counter % car_manager.spawn_rate == 1:
        new_car = car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            print("squish")
            game_is_on = False

    # Detect successful crossing
    if player.ycor() >= 270:
        scoreboard.next_level()
        player.next_level()
        car_manager.next_level()




scoreboard.game_over()

screen.exitonclick()






