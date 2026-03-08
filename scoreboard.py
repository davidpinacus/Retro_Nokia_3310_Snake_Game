from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(y=275, x=0)
        self.color("#0f380f")
        self.score = 0

    def title(self):
        self.write(f"Score: 0", align="center", font=("Courier", 17, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", align="center", font=("Courier", 17, "bold"))

    def increase_score(self):
        self.clear()
        self.penup()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Courier", 17, "bold"))


