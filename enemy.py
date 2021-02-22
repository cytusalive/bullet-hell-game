import pygame
from angle_movement import find_angle, calculate_new_xy, find_distance
from spritesheet_functions import SpriteSheet

class Enemy:
    
    def __init__(self, x, destination, speed, hp, gamearea):
        sprite_sheet = SpriteSheet("ghost.png")
        image = sprite_sheet.get_image(0, 0, 40, 40)
        self.image = image
        self.xpos = x
        self.ypos = 0
        self.xdes, self.ydes = destination
        self.speed = speed
        self.hp = hp
        self.gamearea = gamearea
    
    def move(self):
        distance = find_distance(self.xpos, self.ypos, self.xdes, self.ydes)
        if distance < self.speed:
            self.xpos, self.ypos = self.xdes, self.ydes
        else:
            angle = find_angle(self.xpos, self.ypos, self.xdes, self.ydes)
            self.xpos, self.ypos = calculate_new_xy(self.xpos, self.ypos, self.speed, angle)

    def draw(self):
        self.gamearea.blit(self.image, (self.xpos-20, self.ypos-20))
