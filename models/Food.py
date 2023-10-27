from pygame.math import Vector2
from constants import *
import pygame
import random


class Food:
    # create an x and y position
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    # draw a square
    def draw_food(self, screen):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (126, 166, 114), food_rect)

