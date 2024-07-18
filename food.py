from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.7, 0.7)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos = random.randint(-260, 260)
        y_pos = random.randint(-260, 260)

        self.goto(x_pos, y_pos)



