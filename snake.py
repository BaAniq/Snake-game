from turtle import Screen, Turtle
import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)

x = 0
y = 0
segment_list = []
for segments in range(0, 3):
    segment = Turtle()
    segment.pu()
    segment_list.append(segment)
    segment.shape('square')
    segment.color('white')
    segment.goto(x, y)
    x = x - 20

game_on = True
move = 20
i = 1
while game_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segment_list)-1, 0, -1):
        segment_next_x = segment_list[seg_num-1].xcor()
        segment_next_y = segment_list[seg_num-1].ycor()
        segment_list[seg_num].goto(segment_next_x, segment_next_y)
    segment_list[0].forward(move)
    segment_list[0].left(90)



screen.exitonclick()