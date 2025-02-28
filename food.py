from turtle import Turtle, Screen
from random import randint
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, MIN_RANDOM, MAX_RANDOM


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.speed("fastest")
        self.shape("apple.gif")
        self.penup()
        self.move_random_location()

    def move_random_location(self):
        x_coord = randint(MIN_RANDOM, MAX_RANDOM)
        y_coord = randint(MIN_RANDOM - 55, MAX_RANDOM + 10)
        self.goto(x_coord, y_coord)

