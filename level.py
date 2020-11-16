from turtle import Turtle
import c


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", move=False, align=c.ALIGNMENT, font=c.FONT)

    def refresh(self):
        self.color('black')
        self.penup()
        self.goto(-100, 200)
        self.write(f"Level: {self.score}", move=False, align=c.ALIGNMENT, font=c.FONT)
        self.hideturtle()
