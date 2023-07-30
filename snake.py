from turtle import Turtle
movement = 20
down = 270
up = 90
left = 180
right = 0


class Snake:

    def __init__(self, ):
        self.segment_list = []
        self.making_segments()
        self.head = self.segment_list[0]

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
        self.head.forward(movement)

    def move_up(self):
        current_direction_angle = self.head.heading()
        if current_direction_angle != down:
            self.head.setheading(up)

    def move_down(self):
        current_direction_angle = self.head.heading()
        if current_direction_angle != up:
            self.head.setheading(down)

    def move_left(self):
        current_direction_angle = self.head.heading()
        if current_direction_angle != right:
            self.head.setheading(left)

    def move_right(self):
        current_direction_angle = self.head.heading()
        if current_direction_angle != left:
            self.head.setheading(right)
