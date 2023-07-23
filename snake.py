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
while game_on:
    screen.update()
    time.sleep(1)
    for segment in segment_list:
        segment.pu()
        segment.forward(move)







screen.exitonclick()
