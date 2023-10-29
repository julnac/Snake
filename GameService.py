import pygame
from pygame.math import Vector2

from Enums.GameStatus import GameStatus
from MediatorInterface import MediatorInterface
from models import Food, Tnt
from Enums.GameObjects import GameObjects
from constants import *
import random
from Enums.CollisionEffect import CollisionEffect
from models.Food import Food
from models.Snake import Snake
from models.Tnt import Tnt


def create_board():
    board = [
            [GameObjects.Empty for _ in range(0, CELL_NUMBER + WALL_ADJ)]
            for _ in range(0, CELL_NUMBER + WALL_ADJ)
        ]

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if i is 0:
                board[i][j] = GameObjects.Wall
            if i is CELL_NUMBER:
                board[i][j] = GameObjects.Wall
            if j is 0:
                board[i][j] = GameObjects.Wall
            if j is CELL_NUMBER:
                board[i][j] = GameObjects.Wall

    return board


class GameService(MediatorInterface):
    def __init__(self):
        self.objects_location = create_board()
        self.snake = Snake(self)
        self.objects = [
            Food(self),
            [Tnt(self)]
        ]

    def notify(self, game_object, position):

        if type(game_object) is Food:
            print("do food")
        if type(game_object) is Tnt:
            print("do tnt")

    def initial_notify(self, game_object) -> Vector2:

        if type(game_object) is Food:
            print("find food pos")
            return self.find_random_position()
        if type(game_object) is Tnt:
            print("find tnt pos")
            return self.find_random_position()

    def find_random_position(self) -> Vector2:
        # could be better
        while True:

            x = random.randint(WALL_ADJ, CELL_NUMBER - 1 + WALL_ADJ)
            y = random.randint(WALL_ADJ, CELL_NUMBER - 1 + WALL_ADJ)

            if self.objects_location[x][y] is GameObjects.Empty:
                return Vector2(x, y)

    def check_collision(self) -> CollisionEffect:
        next_move = self.snake.get_head() + self.snake.direction

        if self.objects_location[next_move.x][next_move.y] is GameObjects.Empty:
            return CollisionEffect.Lack

        if self.objects_location[next_move.x][next_move.y] is GameObjects.Apple:
            return CollisionEffect.Reward

        if self.objects_location[next_move.x][next_move.y] is GameObjects.Snake:
            return CollisionEffect.Death

        if self.objects_location[next_move.x][next_move.y] is GameObjects.Tnt:
            return CollisionEffect.Death

        if self.objects_location[next_move.x][next_move.y] is GameObjects.Wall:
            return CollisionEffect.Death

    def update(self):
        collision_effect = self.check_collision()

        self.check_fail(collision_effect)

        self.snake.move(self.objects_location)

    def check_fail(self, collision_effect):

        if collision_effect is CollisionEffect.Reward:
            # self.count_points()
            return GameStatus.Running

        if collision_effect is CollisionEffect.Death:
            return GameStatus.End

    def set_snake_direction(self, key):
        if key == pygame.K_UP:
            if self.snake.direction[1] != 1:
                self.snake.direction = (0, -1)
        if key == pygame.K_DOWN:
            if self.snake.direction[1] != -1:
                self.snake.direction = (0, 1)
        if key == pygame.K_RIGHT:
            if self.snake.direction[0] != -1:
                self.snake.direction = (1, 0)
        if key == pygame.K_LEFT:
            if self.snake.direction[0] != 1:
                self.snake.direction = (-1, 0)

    def draw(self):

