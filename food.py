from random import randint
from turtle import Turtle


class Food:
    def __init__(self):
        self.food = Turtle()
        self.making_food()

    def making_food(self):
        self.food.pu()
        self.food.shape('circle')
        self.food.color('orange')
        self.food.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def placement(self):
        food_x = randint(-280, 280)
        food_y = randint(-280, 280)
        self.food.goto(food_x, food_y)
