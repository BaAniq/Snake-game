from turtle import Screen, Turtle
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake game")

#snake.shapesize(stretch_wid=20, stretch_len=20)
x = 0
y = 0
for segment in range(0,3):
    snake = Turtle()
    snake.shape('square')
    snake.color('white')
    snake.goto(x,y)
    x = x - 20





screen.exitonclick()
