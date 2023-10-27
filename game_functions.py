import pygame
from Direction import Direction
from constants import *


def next_turn():
    pass


def set_direction(direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = Direction.UP
    if keys[pygame.K_s]:
        direction = Direction.DOWN
    if keys[pygame.K_a]:
        direction = Direction.LEFT
    if keys[pygame.K_d]:
        direction = Direction.RIGHT

    return direction


def bounce_from_wall(direction, player_pos):
    if player_pos.y < 0:
        direction = Direction.DOWN
    if player_pos.y > GAME_HEIGHT:
        direction = Direction.UP
    if player_pos.x < 0:
        direction = Direction.RIGHT
    if player_pos.x > GAME_WIDTH:
        direction = Direction.LEFT

    return direction


def check_collisions():
    pass


def game_over():
    pass
