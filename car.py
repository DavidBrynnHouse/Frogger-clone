import random
from turtle import Turtle
import c


class Car(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.goto(200, position)

    def move_forward(self, level):
        self.forward(-c.MOVE_DISTANCE * .083 * (level.score + 1))
