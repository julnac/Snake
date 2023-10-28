from game_functions import *
from constants import *
from models.Food import Food
from models.Snake import Snake
import sys

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# player_pos = pygame.Vector2(GAME_WIDTH / 2, GAME_HEIGHT / 2)
# direction: Direction = Direction.RIGHT


class Main:
    def __init__(self):
        self.snake = Snake(1, 0)
        self.fruit = Food()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_food(screen)
        self.snake.draw_snake(screen)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self):
        pygame.quit()
        sys.exit()

# INITIATING OBJECTS----------------------------
main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# GAME LOOP-------------------------------------
while running:

    # CHECK FOR EVERY KIND OF EVENT------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = (0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = (0, 1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = (1, 0)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = (-1, 0)

    # PROJECTING OBJECTS -----------------------
    screen.fill((199, 215, 156))

    main_game.draw_elements()

    # PLACE FOR EVERY ACTION IN THE GAME !!!-----

    # DRAW ALL OUR ELEMENTS-----------------------
    pygame.display.flip()
    # HOW MANY TIMES MAXIMUM CAN THIS WHILE LOOP RUN PER SECOND (TO PREVENT INEQUALITIES)
    dt = clock.tick(60) / 1000

pygame.quit()
