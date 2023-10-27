from pygame.math import Vector2
from constants import *
import pygame
import random


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self, screen):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "red", snake_rect)

    def move_snake(self, direction):
        # remove last segment
        body_copy = self.body[:-1]
        # add new first segment
        body_copy.insert(0, body_copy[0] + self.direction)
        # assign changes to body
        self.body = body_copy[:]


