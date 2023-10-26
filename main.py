import pygame
from Direction import Direction

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
direction: Direction = Direction.RIGHT


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


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)

    direction = set_direction(direction)

    if direction == Direction.UP:
        player_pos.y -= 300 * dt
    elif direction == Direction.DOWN:
        player_pos.y += 300 * dt
    elif direction == Direction.LEFT:
        player_pos.x -= 300 * dt
    elif direction == Direction.RIGHT:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
