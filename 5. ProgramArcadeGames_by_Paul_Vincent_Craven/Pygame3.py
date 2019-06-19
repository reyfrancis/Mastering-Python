import pygame
import random
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (51, 255, 255)
PI = 3.141592653

coor_x = 50
coor_y = 50
dir_x = 1
dir_y = 1
snow_list = []

size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow Animation")

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

screen.fill(BLACK)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    screen.fill(BLACK)

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1]+=1
        
        if snow_list[i][1] > 400:
        # Reset it just above the top
            y = random.randrange(0, 100)
            snow_list[i][1] = y
        # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x


    pygame.display.flip()

    clock.tick(10)
pygame.quit()