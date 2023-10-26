import pygame
from Direction import Direction

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
running = True
dt = 0

WIDTH = screen.get_width()
HEIGHT = screen.get_height()

player_pos = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
direction: Direction = Direction.RIGHT

test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))

# constances

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "00FF00"
FOOD_COLOR = "FF0000"
BACKGROUND_COLOR = "000000"

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def set_direction(direction_local):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction_local = Direction.UP
    if keys[pygame.K_s]:
        direction_local = Direction.DOWN
    if keys[pygame.K_a]:
        direction_local = Direction.LEFT
    if keys[pygame.K_d]:
        direction_local = Direction.RIGHT

    return direction_local

def check_collisions():
    pass

def game_over():
    pass

while running:

    # CHECK FOR EVERY KIND OF EVENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((175, 215, 70))
    pygame.draw.circle(screen, "red", player_pos, 40)

    screen.blit(test_surface, (200, 250))

    direction = set_direction(direction)

    if direction == Direction.UP:
        player_pos.y -= 300 * dt
    elif direction == Direction.DOWN:
        player_pos.y += 300 * dt
    elif direction == Direction.LEFT:
        player_pos.x -= 300 * dt
    elif direction == Direction.RIGHT:
        player_pos.x += 300 * dt


    if player_pos.y < 0:
        direction = Direction.DOWN
    if player_pos.y > HEIGHT:
        direction = Direction.UP
    if player_pos.x < 0:
        direction = Direction.RIGHT
    if player_pos.x > WIDTH:
        direction = Direction.LEFT

    # DRAW ALL OUR ELEMENTS
    pygame.display.flip()
    # HOW MANY TIMES MAXIMUM CAN THIS WHILE LOOP RUN PER SECOND (TO PREVENT INEQUALITIES)
    dt = clock.tick(60) / 1000

pygame.quit()
