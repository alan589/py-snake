from turtle import Turtle
from settings import MOVE_DISTANCE, HEADING_DOWN, HEADING_UP, HEADING_RIGHT, HEADING_LEFT, START_LENGTH


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for pos in START_LENGTH:
            new_segment = Turtle("square")
            new_segment.goto(pos)
            new_segment.color("white")
            new_segment.penup()
            self.segments.append(new_segment)

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.tail.xcor(), self.tail.ycor())
        self.segments.append(new_segment)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        heading = self.head.heading()
        if heading != HEADING_DOWN:
            self.head.setheading(HEADING_UP)
    def move_down(self):
        heading = self.head.heading()
        if heading != HEADING_UP:
            self.head.setheading(HEADING_DOWN)
    def move_left(self):
        heading = self.head.heading()
        if heading != HEADING_RIGHT:
            self.head.setheading(HEADING_LEFT)

    def move_right(self):
        heading = self.head.heading()
        if heading != HEADING_LEFT:
            self.head.setheading(HEADING_RIGHT)
