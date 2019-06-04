''' @TODO: 
1. Meriam's Dynamics Book Problem 271 in Chapter 3. Solve for the correct values. (done)
2. Rewrite the implementation for balls > 2
4. Fix bug when self.restitution != 1 (done)
3. Make a comprehensive tutorial at Github 
'''

import pygame, random, math
import numpy as np
from Calc import CollisionCalculations as cal

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = math.pi


class Circle:
    # Give birth to a circle!
    def __init__(self, color, radius):  
        self.color = color
        self.radius = radius
        self.x = random.randrange(radius, my_game.width-radius)
        self.y = random.randrange(radius, my_game.height-radius)
        self.velocity_x = (40/radius + random.randrange(1,5))*random.choice([1, -1])
        self.velocity_y = (40/radius + random.randrange(1,5))*random.choice([1, -1])
        self.abs_velocity = math.sqrt(pow(self.velocity_x, 2) + pow(self.velocity_y, 2))
        self.mass = radius/10
    

    def move(self):
        # Convert coordinates into Cartesian Plane.
        self.x, self.y = my_calculation.ConvertAxis(self.x, self.y)

        # Check if it hits the wall.
        if self.x > (my_game.width-self.radius) or self.x < self.radius:
            self.velocity_x*=-1

        if self.y > (my_game.height-self.radius) or self.y < self.radius:
            self.velocity_y*=-1

        # Do calculations in Cartesian Coordinate Plane.
        self.x+=self.velocity_x
        self.y+=self.velocity_y

        # Convert coordinates to Pygame Plane.
        self.x, self.y = my_calculation.ConvertAxis(self.x, self.y)


class Game(Circle):
    def __init__(self, color, width, height, fps, CoefficientRestitution):
        self.bground_color = color

        if CoefficientRestitution == 1:
            self.title = 'Elastic Collision'.format(CoefficientRestitution)
        else:
            self.title = 'Inelastic Collision, Coefficient of Restitution: {}'.format(CoefficientRestitution)

        self.width = width
        self.height = height
        self.size = width, height
        self.tick = fps
        self.restitution = CoefficientRestitution

    def makeScreen(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bground_color)
        self.clock = pygame.time.Clock()


    def collisions(self):
        position = [0, 0]
        i = 0
        for i in range(len(self.circle_list)):
            k = 0
            for k in range(len(self.circle_list)):
                print('i: {}, k: {}'.format(i, k))
                # Check if two different circles are selected.
                if self.circle_list[i] != self.circle_list[k]:

                    if my_calculation.CheckNotSameCircles(self.circle_list[k].x, self.circle_list[k].y, position[0], position[1]) == True:

                        position = [self.circle_list[i].x, self.circle_list[i].y]
                        CenterDistance = math.hypot((self.circle_list[i].x - self.circle_list[k].x), (self.circle_list[i].y - self.circle_list[k].y))
                        if CenterDistance <= self.circle_list[i].radius + self.circle_list[k].radius:

                            # Get the angle of collision between two circles, that is, the arctangent of their respective centers with respect to positive x-axis.
                            CenterAngle = math.atan2(self.circle_list[k].y - self.circle_list[i].y, self.circle_list[k].x - self.circle_list[i].x)


                            cal_vAx, cal_vAy, cal_vBx, cal_vBy = cal.Compute(self.circle_list[i].mass, self.circle_list[k].mass, self.circle_list[i].velocity_x, 
                                self.circle_list[i].velocity_y, self.circle_list[k].velocity_x, self.circle_list[k].velocity_y, 
                                CenterAngle, self.restitution)

                            # Correcting the arctangent function so that it outputs values from 0 - 2*pi.
                            CenterAngle = my_calculation.InvTrigCorrection(CenterAngle)

                            # The CenterAngle is the angle between the line between two centers with respect to the positive x-axis.
                            # We transform that into angle theta, that is, how much angle does the y-axis rotated to become y'-axis
                            # or x-axis to be x'-axis.
                            CenterAngle-=PI/2
 
                            # Convert the vector velocity from (x, y) to (x', y').
                            self.circle_list[i].velocity_x, self.circle_list[i].velocity_y = my_calculation.RotateAxis(self.circle_list[i].velocity_x, self.circle_list[i].velocity_y, CenterAngle)
                            self.circle_list[k].velocity_x, self.circle_list[k].velocity_y = my_calculation.RotateAxis(self.circle_list[k].velocity_x, self.circle_list[k].velocity_y, CenterAngle)

                            velocity_update = [0, 0]

                            velocity_update[1] = (self.circle_list[i].mass*self.circle_list[i].velocity_y+self.circle_list[k].mass*self.circle_list[k].velocity_y+(self.circle_list[i].mass*self.circle_list[i].velocity_y-self.circle_list[i].mass*self.circle_list[k].velocity_y)*self.restitution)/(self.circle_list[i].mass+self.circle_list[k].mass) 
                            velocity_update[0] = velocity_update[1] - (self.circle_list[i].velocity_y - self.circle_list[k].velocity_y)*self.restitution

                            self.circle_list[i].velocity_y = velocity_update[0]
                            self.circle_list[k].velocity_y = velocity_update[1]
     
                            # Convert the vector velocity from (x, y) to (x', y').
                            self.circle_list[i].velocity_x, self.circle_list[i].velocity_y = my_calculation.RotateAxis(self.circle_list[i].velocity_x, self.circle_list[i].velocity_y, -CenterAngle)
                            self.circle_list[k].velocity_x, self.circle_list[k].velocity_y = my_calculation.RotateAxis(self.circle_list[k].velocity_x, self.circle_list[k].velocity_y, -CenterAngle)

                    else:
                        position = [self.circle_list[i].x, self.circle_list[i].y]

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

            my_game.collisions()

            i = 0
            for i in range(len(self.circle_list)):
                self.circle_list[i].move()

                pygame.draw.circle(self.screen, self.circle_list[i].color, [int(self.circle_list[i].x), int(self.circle_list[i].y)], int(self.circle_list[i].radius))
            pygame.display.flip()
            self.clock.tick(self.tick)


class Calculations(Game):
    def __init__(self, color, width, height, fps, CoefficientRestitution):
        super().__init__(color, width, height, fps, CoefficientRestitution)

    # Change the position of the origin from the uppermost left to lowermost left.
    # Basically, the origin position can't be change but we can convert every coordinate in our traditional
    # Cartesian coordinate system to work with Pygame's coordinate system.
    # As a quick example. Say we want to draw a circle in 50, 50. We should get Pygame's coordinate equivalent by:
    # x, y = Pygame_coorEquivalent(class, 50, 50)
    def ConvertAxis(self, x, y):
        return x, self.height - y

    @classmethod 
    def CheckNotSameCircles(self, curr_x, curr_y, prev_x, prev_y):
        if curr_x == prev_x and curr_y == prev_y:
            print('\n')
            return False
        else:
            print('\n')
            return True

    # Convert the values of x, y to rotated axis or to the line of contact.
    @classmethod  
    def RotateAxis(cls, x, y, angle):
        A = np.array([[math.cos(angle), -math.sin(angle)],
                      [math.sin(angle),  math.cos(angle)]])
        X = np.array([x, y])

        return np.dot(A, X)

    # The output values of inverse trigonometric functions are in radians and between pi and -pi.
    # This can be confusing if you are familiar working with 0 to 2*pi.
    # In this function we add 2*pi to negative output values, that is, the range would be 0 to 2*pi for all real domain
    @classmethod             
    def InvTrigCorrection(cls, angle):
        if angle < 0:
            angle+=2*PI
        if angle > PI and angle < 2*PI:
            angle-=PI
        return angle



###----------------------------RUN------------------------###
my_calculation = Calculations(None, 500, 500, None, None)
my_game = Game(BLACK, my_calculation.width, my_calculation.height, 60, 1)

c1 = Circle(RED, 50)
c2 = Circle(BLUE, 20)
c3 = Circle(WHITE, 30)
c4 = Circle(GREEN, 60)

my_game.makeScreen()
my_game.main([c1, c2, c3, c4])
pygame.quit()