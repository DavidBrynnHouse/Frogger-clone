from turtle import Turtle
import c


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -200)

    def move_player(self):
        self.forward(c.MOVE_DISTANCE)
