from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

mice = Food()
worm = Snake()
score = Scoreboard()

screen.listen()
screen.onkey(worm.up, "Up")
screen.onkey(worm.down, "Down")
screen.onkey(worm.left, "Left")
screen.onkey(worm.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    worm.snake_move()

    if worm.head.distance(mice) < 15:
        mice.refresh()
        score.increase_score()
        worm.extend_snake()

    #Detect colision with wall
    if (worm.head.xcor() > 280 or worm.head.xcor() < -280) or (worm.head.ycor() > 280 or worm.head.ycor() < -280):
        score.game_over()
        game_is_on = False

    for segment in worm.my_snakes[1:]:
        if worm.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False


screen.exitonclick()