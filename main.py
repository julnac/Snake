from Enums.GameObjects import GameObjects
from constants import *
from Enums.CollisionEffect import CollisionEffect
from models.Food import Food
from models.Snake import Snake
from models.Tnt import Tnt
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


def create_board():
    wall_adjustment = 1
    board = [
            [GameObjects.Empty for _ in range(0, CELL_NUMBER + wall_adjustment)]
            for _ in range(0, CELL_NUMBER + wall_adjustment)
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


class Main:

    def __init__(self):
        self.snake = Snake()
        self.objects = [
            Food(),
            [Tnt()]
        ]
        self.objects_location = create_board()

    def update(self):

        collision_effect = self.check_collision()
        self.check_fail(collision_effect)
        self.snake.move(self.objects_location)

    def check_collision(self) -> CollisionEffect:
        next_move = self.snake.body[0] + self.snake.direction

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

    # def check_collision(self):
    #     if self.fruit.pos == self.snake.body[0]:
    #         self.fruit.randomise()
    #         self.snake.add_block()
    #         self.tnts.append(Tnt())

    def check_fail(self, collision_effect):

        if collision_effect is CollisionEffect.Reward:
            self.count_points()

        if collision_effect is CollisionEffect.Death:
            game_over()

    def count_points(self):
        pass

    def draw_elements(self):
        self.fruit.draw_food(screen, apple)
        self.snake.draw_snake(screen)
        for t in self.tnts:
            t.draw_tnt(screen, tnt)


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
                if main_game.snake.direction[1] != 1:
                    main_game.snake.direction = (0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction[1] != -1:
                    main_game.snake.direction = (0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction[0] != -1:
                    main_game.snake.direction = (1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction[0] != 1:
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
