from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")

class GameScore(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.start_time = time.time()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        elapsed_time = int(time.time() - self.start_time)
        self.write(f"Level: {self.level}  Time: {elapsed_time}", align="left", font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_scoreboard()

    def display_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def reset(self):
        self.level = 1
        self.start_time = time.time()
        self.update_scoreboard()