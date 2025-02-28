import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from settings import SCREEN_WIDTH, BG_COLOR, SCREEN_HEIGHT, TITLE, KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT, \
    SNAKE_INITIAL_SPEED
from snake import Snake


class Game:

    def __init__(self):
        self.screen = Screen()
        self.screen.addshape("apple.gif")
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)

        self.screen.tracer(0)

        self.game_is_on = True
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()



        self.line_screen = Turtle()
        self.line_screen.penup()
        self.line_screen.goto(-300, 300)
        self.line_screen.pendown()
        self.line_screen.hideturtle()
        self.line_screen.pencolor("white")
        self.line_screen.pensize(2)
        self.line_screen.forward(600)


        self.screen.onkeypress(fun=self.snake.move_up, key=KEY_UP)
        self.screen.onkeypress(fun=self.snake.move_down, key=KEY_DOWN)
        self.screen.onkeypress(fun=self.snake.move_right, key=KEY_RIGHT)
        self.screen.onkeypress(fun=self.snake.move_left, key=KEY_LEFT)

        self.screen.listen()
        self.snake_speed = SNAKE_INITIAL_SPEED

    def run(self):
        game_is_on = True

        while game_is_on:

            print(self.snake.head.xcor(), self.snake.head.ycor())
            self.snake.move()
            self.screen.update()
            time.sleep(self.snake_speed)

            # food collision
            if self.snake.head.distance(self.food) < 20:
                # increase snake speed
                if self.scoreboard.score == 9 or self.scoreboard.score == 19 or self.scoreboard.score == 29:
                    self.snake_speed -= 0.01
                self.scoreboard.increase_score()
                self.food.move_random_location()
                self.snake.extend()

            # tail collision
            for segment in self.snake.segments[1:]:
                if self.snake.head.distance(segment) < 10:
                    self.collision_animation()
                    self.reset_game()

            # wall collision
            if self.snake.head.xcor() <= -300 or self.snake.head.xcor() >= 290 or self.snake.head.ycor() <= -340 or self.snake.head.ycor() >= 300:
                self.collision_animation()
                self.reset_game()


        self.screen.exitonclick()

    def reset_game(self):
        self.clear_screen()
        self.scoreboard.game_over()
        time.sleep(4)
        self.scoreboard.show_score()
        self.snake.reset()
        self.food.showturtle()
        self.food.move_random_location()

    def collision_animation(self):
        for _ in range(3):
            for segment in self.snake.segments:
                segment.hideturtle()
            self.screen.update()
            time.sleep(0.2)
            for segment in self.snake.segments:
                segment.showturtle()
            self.screen.update()
            time.sleep(0.2)

    def clear_screen(self):
        for segment in self.snake.segments:
            segment.goto(1000, 1000)
        self.food.goto(1000, 1000)



