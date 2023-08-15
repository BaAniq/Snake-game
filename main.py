from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()


def screen_set_up():
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("Snake game")
    screen.tracer(0)


screen_set_up()
snake = Snake()
food = Food()
score = Score()
food.placement()
game_on = True
move = 20
i = 1

screen.listen()


def screen_movement():
    screen.onkey(fun=snake.move_up, key='Up')
    screen.onkey(fun=snake.move_down, key='Down')
    screen.onkey(fun=snake.move_left, key='Left')
    screen.onkey(fun=snake.move_right, key='Right')


def reset():
    time.sleep(1)
    score.saving_high_score(score.score)
    screen.clear()
    screen_set_up()
    screen.listen()
    screen_movement()
    snake.reset()
    score.reset()
    score.score_text()
    food.reset()


screen_movement()

wall = 298
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.xcor() > wall or snake.head.xcor() < -wall or snake.head.ycor() > wall or snake.head.ycor() < -wall:
        reset()
        continue

    if snake.head.distance(food.food) < 15:
        food.placement()
        score.score += 1
        score.adding_point(score.score)
        snake.add_segment()

    # collision
    for segment in range(1, len(snake.segment_list)):
        if snake.head.distance(snake.segment_list[segment]) < 1:
            reset()
        continue


screen.exitonclick()
