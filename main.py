from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
score_number = 0
food.placement()
game_on = True
move = 20
i = 1

screen.listen()
screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_down, key='Down')
screen.onkey(fun=snake.move_left, key='Left')
screen.onkey(fun=snake.move_right, key='Right')
wall = 298
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.xcor() > wall or snake.head.xcor() < -wall or snake.head.ycor() > wall or snake.head.ycor() < -wall:
        snake.head.home()
        time.sleep(0.5)
        score.game_over()
        score_number = 0
        game_on = False

    if snake.head.distance(food.food) < 15:
        food.placement()
        score_number += 1
        score.adding_point(score_number)
        snake.add_segment()

    # collision
    for segment in range(1, len(snake.segment_list)):
        if snake.head.distance(snake.segment_list[segment]) < 1:
            snake.head.home()
            time.sleep(0.5)
            score.game_over()
            score_number = 0
            game_on = False


screen.exitonclick()
