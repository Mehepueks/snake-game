from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.counter = 0
        self.write(f'Score: {self.counter}', False, ALIGNMENT, FONT)

    def clear_score(self):
        self.clear()

    def increase_score(self):
        self.clear_score()

        self.counter += 1
        self.write(f'Score: {self.counter}', False, ALIGNMENT, FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over!", False, 'center', ('courier', 24, 'normal'))
