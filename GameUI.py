class GameUI:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.fruit.draw_food(self.screen, apple)
        self.snake.draw_snake(self.screen)
        for t in self.tnts:
            t.draw_tnt(screen, tnt)
