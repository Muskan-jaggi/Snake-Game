import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr = Screen()
scr.setup(600, 600)
scr.title("Snake Game")
scr.bgcolor("black")
scr.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detection of collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.gameover()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.gameover()









scr.exitonclick()
