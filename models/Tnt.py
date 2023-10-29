from pygame.math import Vector2

from GameObjectInterface import GameObjectInterface
from MediatorInterface import MediatorInterface
from constants import *
import pygame
import random


class Tnt(GameObjectInterface):
    def __init__(self, game_service):
        super().__init__(game_service)
        self.randomise()

    def draw_tnt(self, screen, image):
        tnt_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        screen.blit(image, tnt_rect)

    def randomise(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)