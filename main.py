from game_functions import *
from constants import *
from models.Food import Food
from models.Snake import Snake

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

# player_pos = pygame.Vector2(GAME_WIDTH / 2, GAME_HEIGHT / 2)
# direction: Direction = Direction.RIGHT

# INITIATING OBJECTS----------------------------
fruit = Food()
snake = Snake()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# GAME LOOP-------------------------------------
while running:

    # CHECK FOR EVERY KIND OF EVENT------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            snake.move_snake(screen)
        '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)'''

    # PROJECTING OBJECTS -----------------------
    screen.fill((199, 215, 156))

    fruit.draw_food(screen)
    snake.draw_snake(screen)

    # PLACE FOR EVERY ACTION IN THE GAME !!!-----

    # DRAW ALL OUR ELEMENTS-----------------------
    pygame.display.flip()
    # HOW MANY TIMES MAXIMUM CAN THIS WHILE LOOP RUN PER SECOND (TO PREVENT INEQUALITIES)
    dt = clock.tick(60) / 1000

pygame.quit()
