from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.current_score}", align="center", font=("Arial", 14, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME-OVER", False, "center", ("Arial", 24, "normal"))
    def increase_score(self):
        self.current_score += 1
        self.clear()

        self.write(f"Score: {self.current_score}", align="center", font=("Arial", 14, "normal"))
