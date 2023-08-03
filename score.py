from turtle import Turtle


class Score:
    def __init__(self):
        self.text = Turtle()
        self.text.pu()
        self.text.goto(0, 280)
        self.text.color('red')
        self.text.hideturtle()
        self.score()

    def score(self):
        self.text.clear()
        self.text.write('Score: 0', False, align='center', font=('Arial', 10, 'normal'))

    def adding_point(self, score_num):
        self.text.clear()
        self.text.write(f'Score: {score_num}', False, align='center', font=('Arial', 10, 'normal'))

    def game_over(self):
        self.text.goto(0, 0)
        self.text.write('GAME OVER', False, align='center', font=('Arial', 13, 'normal'))
        