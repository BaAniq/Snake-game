from turtle import Screen
from snake import Snake
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
game_on = True
move = 20
i = 1

screen.listen()
screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_down, key='Down')
screen.onkey(fun=snake.move_left, key='Left')
screen.onkey(fun=snake.move_right, key='Right')
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()



screen.exitonclick()