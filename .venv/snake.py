from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.my_snakes = []
        self.create_snake()
        self.head = self.my_snakes[0]

    def create_snake(self):
        for nr in range(3):
            snake = Turtle('square')
            snake.penup()
            snake.color('white')
            snake.goto((nr * (-20)), 0)
            new_snake = snake
            self.my_snakes.append(new_snake)

    def snake_move(self):
        for seg_num in range(len(self.my_snakes) - 1, 0, -1):
            new_x = self.my_snakes[seg_num - 1].xcor()
            new_y = self.my_snakes[seg_num - 1].ycor()
            self.my_snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend_snake(self):
        snake = Turtle('square')
        snake.penup()
        snake.color('white')
        snake.goto((self.my_snakes[-1].xcor() * (-20)), self.my_snakes[-1].ycor())
        new_snake = snake
        self.my_snakes.append(new_snake)

