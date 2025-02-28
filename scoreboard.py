from turtle import Turtle
from settings import ALIGNMENT, FONT


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.hideturtle()
        self.load_highscore()
        self.show_score()

    def load_highscore(self):
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
    def save_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, 50)
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.reset_score()
        self.screen.update()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-80, 314)
        self.write(f"HighScore: {self.highscore}  Score: {self.score}", align=ALIGNMENT, font=FONT)
