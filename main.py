from GameService import GameService
from GameUI import GameUI
from constants import *

from Enums.GameStatus import GameStatus
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()
running = True
# apple = pygame.image.load('Graphics/apple.png').convert_alpha()
tnt = pygame.image.load('Graphics/TNT.png').convert_alpha()
apple = tnt


def game_over():
    pygame.quit()
    sys.exit()


class Main:

    def __init__(self):
        self.game_service = GameService()
        self.game_ui = GameUI(screen)
        self.game_status = GameStatus.Running

    def update(self):
        self.game_status = self.game_service.update()

        if self.game_status is GameStatus.End:
            game_over()

        # for obj in self.objects:
        #     obj.move(self.objects_location)

    # def check_collision(self):
    #     if self.fruit.pos == self.snake.body[0]:
    #         self.fruit.randomise()
    #         self.snake.add_block()
    #         self.tnts.append(Tnt())

    def count_points(self):
        pass

    def draw_elements(self):
        self.game_ui.draw()

    def set_snake_direction(self, key):
        self.game_service.set_snake_direction(key)


main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# GAME LOOP
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            main_game.set_snake_direction(event.key)

    screen.fill((199, 215, 156))

    main_game.draw_elements()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
