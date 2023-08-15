from turtle import Turtle


class Score:
    def __init__(self):
        self.text = Turtle()
        self.text.pu()
        self.text.goto(0, 280)
        self.text.color('red')
        self.text.hideturtle()
        with open('High_score.txt', 'r') as high_score_file:
            high_score_file.seek(0)
            self.high_score = int(high_score_file.read())
        self.score = 0
        self.score_text()

    def score_text(self):
        self.text.clear()
        self.text.write(f'Score: {self.score} | High score: {self.high_score}', False, align='center', font=('Arial', 10, 'normal'))

    def adding_point(self, score_num):
        self.text.clear()
        self.text.write(f'Score: {score_num} | High score: {self.high_score}', False, align='center', font=('Arial', 10, 'normal'))

    def game_over(self):
        self.text.goto(0, 0)
        self.text.write('GAME OVER', False, align='center', font=('Arial', 13, 'normal'))

    def saving_high_score(self, score_num):
        if score_num > self.high_score:
            with open('High_score.txt', 'w+') as high_score_file:
                high_score_file.write(str(score_num))
            self.high_score = score_num

    def reset(self):
        self.score = 0
