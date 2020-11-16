import random
from turtle import Screen
from car import Car
from player import Player
from level import Level

screen = Screen()
screen.colormode(255)
screen.setup(width=400, height=500)
screen.tracer(0)
screen.listen()

player = Player()
level = Level()

screen.onkey(player.move_player, "Up")

traffic = []
new_car = Car(random.randint(-200, 200))
traffic.append(new_car)
game_is_on = True
while game_is_on:
    if len(traffic) > 0 and traffic[-1].xcor() <= 180:
        new_car = Car(random.randint(-200, 200))
        traffic.append(new_car)
    for car in traffic:
        car.move_forward(level)
        if car.distance(player) < 10:
            game_is_on = False
            level.game_over()
    if player.ycor() > 230:
        level.increase_score()
        player.setposition(0, -200)

    screen.update()

screen.exitonclick()