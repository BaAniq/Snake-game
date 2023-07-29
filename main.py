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
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()