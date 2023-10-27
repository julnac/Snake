from Snake import Snake
from Food import Food


class Main:
    def __init__(self):
        self.snake = Snake(1, 0)
        self.fruit = Food()

    def update(self):
        self.snake.move_snake()

    def draw_elements(self):
        self.fruit.draw_food(screen)
        self.snake.draw_snake(screen)

