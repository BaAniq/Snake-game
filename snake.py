from turtle import Turtle
movement = 20


class Snake:

    def __init__(self, ):
        self.segment_list = []
        self.making_segments()

    def making_segments(self):
        x = 0
        y = 0
        for num_segment in range(0, 3):
            segment = Turtle()
            segment.pu()
            segment.shape('square')
            segment.color('white')
            self.segment_list.append(segment)
            segment.goto(x, y)
            x = x - 20

    def move(self):
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            segment_next_x = self.segment_list[seg_num - 1].xcor()
            segment_next_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(segment_next_x, segment_next_y)

    def move_forward(self):
        self.move()
        self.segment_list[0].forward(movement)

    def move_up(self):

        self.segment_list[0].setheading(90)

    def move_down(self):
        self.segment_list[0].setheading(270)

    def move_left(self):
        self.segment_list[0].setheading(180)

    def move_right(self):
        self.segment_list[0].setheading(0)


