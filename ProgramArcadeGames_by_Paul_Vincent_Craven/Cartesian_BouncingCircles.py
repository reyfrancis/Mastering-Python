''' This code shows that the implementation is coherent with Catersian Coordinate axis '''

import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


PI = math.pi
class Circle:

    def __init__(self, color, radius, x, y):  
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity_x = 5
        self.velocity_y = 5

    def move(self):
            self.x, self.y = my_calculation.Pygame_to_Cartesian(self.x, self.y)
            if self.x > (my_game.width-self.radius) or self.x < self.radius:
                self.velocity_x*=-1

            if self.y > (my_game.height-self.radius) or self.y < self.radius:
                self.velocity_y*=-1

            # Convert coordinates in Cartesian Plane
            print(self.x, self.y)
            
            # Print Coordinates and velocity
            print('X: {}, Y: {}, Vx: {}, Vy: {}'.format(self.x, self.y, self.velocity_x, self.velocity_y))

            # Do calculations in Cartesian Coordinate Plane
            self.x+=self.velocity_x
            self.y+=self.velocity_y

            # Convert coordinates to Pygame Plane
            self.x, self.y = my_calculation.Cartesian_to_Pygame(self.x, self.y)

class Game(Circle):
    def __init__(self, color, title, width, height, fps):
        self.bground_color = color
        self.title = title
        self.width = width
        self.height = height
        self.size = width, height
        self.tick = fps

    def makeScreen(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bground_color)
        self.clock = pygame.time.Clock()


    def main(self, arg_list=None):
        done = False
        while not done:
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True

            if arg_list is None:
                self.circle_list = []
            else:
                self.circle_list = arg_list

            self.screen.fill(self.bground_color)

            for each_circle in self.circle_list:
                each_circle.move()
                pygame.draw.circle(self.screen, each_circle.color, [int(each_circle.x), int(each_circle.y)], int(each_circle.radius))

            pygame.display.flip()
            self.clock.tick(self.tick)

class Calculations(Game):

    def __init__(self, color, title, width, height, fps):
        super().__init__(color, title, width, height, fps)

    def Pygame_to_Cartesian(self, x, y):
        return x, self.height - y

    def Cartesian_to_Pygame(self, x, y):
        return x, self.height - y

my_calculation = Calculations(None, None, 500, 500, None)

my_game = Game(BLACK, 'Bouncing Rectangles', my_calculation.width, my_calculation.height, 60)

x, y = my_calculation.Cartesian_to_Pygame(400, 400)

c1 = Circle(RED, 60, x, y)

my_game.makeScreen()
my_game.main([c1])
pygame.quit()