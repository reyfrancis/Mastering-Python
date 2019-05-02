import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653

class Rectangle:

    def __init__(self, color, size):  
        self.color = color
        self.size = size
        self.x = random.randrange(size, 400-size)
        self.y = random.randrange(size, 500-size)
        self.dir_x = random.choice([1, -1])
        self.dir_y = random.choice([1, -1])
        self.speed = 200/size
    # def check_Peri(self):
        
    def move(self):
            if self.x >= (400-self.size) or self.x <= 0:
                self.dir_x*=-1

            if self.y >= (500-self.size) or self.y <= 0:
                self.dir_y*=-1

            self.x+=(self.speed*self.dir_x)
            self.y+=(self.speed*self.dir_y)

class Game(Rectangle):
    def __init__(self, color, title, width, height, fps):
        self.bground_color = color
        self.title = title
        self.size = width, height
        self.tick = fps

    def makeScreen(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bground_color)
        self.clock = pygame.time.Clock()

    def main(self, arg_rect=None):
        done = False
        while not done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done = True

            if arg_rect is None:
                self.rect_list = []
            else:
                self.rect_list = arg_rect

            self.screen.fill(self.bground_color)

            for i in range(len(self.rect_list)):
                self.rect_list[i].move()
                pygame.draw.rect(self.screen, self.rect_list[i].color, [self.rect_list[i].x, self.rect_list[i].y, 
                    self.rect_list[i].size, self.rect_list[i].size])
            pygame.display.flip()
            self.clock.tick(self.tick)


rect_red = Rectangle(RED, 50)
rect_blue = Rectangle(BLUE, 70)
rect_white = Rectangle(WHITE, 30)
rect_green1 = Rectangle(GREEN, 20)
rect_green2 = Rectangle(GREEN, 10)
my_game = Game(BLACK, 'Bouncing Rectangles', 400, 500, 60)
my_game.makeScreen()
my_game.main([rect_red, rect_blue, rect_white, rect_green1, rect_green2])

