from turtle import Turtle


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
        movement = 20
        for seg_num in range(len(self.segment_list) - 1, 0, -1):
            segment_next_x = self.segment_list[seg_num - 1].xcor()
            segment_next_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(segment_next_x, segment_next_y)
        self.segment_list[0].forward(movement)
