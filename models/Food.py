from pygame.math import Vector2

from GameService import GameService
from GameObjectInterface import GameObjectInterface
from constants import *
import pygame


class Food(GameObjectInterface):
    def __init__(self, game_service: GameService):
        self.game_service = game_service
        super().__init__(game_service)

        self.pos = self.init_position()

    # draw a square
    def draw_food(self, screen, image):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        screen.blit(image, food_rect)
        # pygame.draw.rect(screen, (126, 166, 114), food_rect)

    def init_position(self) -> Vector2:
        return self.game_service.initial_notify(self)

    def move(self):
        self.game_service.notify(self, self.pos)
