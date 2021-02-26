import pygame
import math
import random
from spritesheet_functions import SpriteSheet
from angle_movement import calculate_new_xy, find_angle, find_distance


class Bullet:
    def __init__(self, x, y, speed, angle, gamearea, color=(255, 100, 150)):
        self.xpos = x
        self.ypos = y
        self.speed = speed
        self.angle = angle
        self.power = 10
        self.color = color
        self.gamearea = gamearea
        
    def __repr__(self):
        return str(self.xpos) + str(self.ypos)

    def draw(self):
        pygame.draw.circle(self.gamearea, self.color, (self.xpos, self.ypos), 6, 2)
        pygame.draw.circle(self.gamearea, (255, 255, 255), (self.xpos, self.ypos), 4)

    def move(self):
        self.xpos, self.ypos = calculate_new_xy(self.xpos, self.ypos, self.speed, self.angle)
        if self.xpos < 0 or self.xpos > self.gamearea.get_width():
            return False
        if self.ypos < 0 or self.ypos > self.gamearea.get_height():
            return False
        return True

# returns true if 2 positions are within hitradius in distance
def hitdetect(bullet, target, hitradius):
    distance = find_distance(target.xpos, target.ypos, bullet.xpos, bullet.ypos)
    if distance < hitradius and distance > -hitradius:
        return True
    return False
