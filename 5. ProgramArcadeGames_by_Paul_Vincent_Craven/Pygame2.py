import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653

coor_x = 50
coor_y = 50
dir_x = 1
dir_y = 1


size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

screen.fill(BLACK)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [coor_x, coor_y, 50, 50])
    pygame.draw.rect(screen, RED, [coor_x+10, coor_y+10 ,30, 30])
    coor_x+=dir_x
    coor_y+=dir_y
    if coor_x >= 350 or coor_x <= 0:
        dir_x*=-1

    if coor_y >= 450 or coor_y <= 0:
        dir_y*=-1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()