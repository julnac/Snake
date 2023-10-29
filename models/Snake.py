from pygame.math import Vector2

from Enums.GameObjects import GameObjects
from GameObjectInterface import GameObjectInterface

from constants import *
import pygame


class Snake:
    def __init__(self, game_service):
        self.game_service = game_service
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self, screen):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "yellow", snake_rect)

    def move(self, objects_location):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            # remove last segment
            body_copy = self.body[:-1]
            # add new first segment
            body_copy.insert(0, body_copy[0] + self.direction)
            # assign changes to body
            self.body = body_copy[:]

        objects_location[self.body[0].x][self.body[0].y] = GameObjects.Snake
        objects_location[self.body[len(self.body-1)].x][self.body[len(self.body-1)].y] = GameObjects.Empty

        return objects_location

    def add_block(self):
        self.new_block = True

    def get_head(self):
        return self.body[0]
