import pygame
import random
import math
from enemy import Enemy, Boss
from spritesheet_functions import SpriteSheet
from angle_movement import find_distance, find_angle, calculate_new_xy

class Level:
    def __init__(self, gamearea):
        self.timer = 0
        self.gamearea = gamearea
        self.background = False
        self.enemies = []

    def draw(self):
        self.gamearea.blit(self.background, (0, 0))

class Stage_01(Level):
    def __init__(self, gamearea, playerbulletlist, enemybulletlist):
        super().__init__(gamearea)
        self.background = SpriteSheet("stage.png").get_image(0, 0, 520, 680)
        self.playerbullets = playerbulletlist
        self.enemybullets = enemybulletlist
    
    def update(self):
        if cd % 180 == 0:
           self.enemies.append(Enemy(random.randint(0, gamearea.get_width()), (random.randint(0, gamearea.get_width()), random.randint(0, 400)), 3, 150, gamearea, enemy_sprite))

        self.timer += 1
