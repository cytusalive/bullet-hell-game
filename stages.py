import pygame
import random
import math
from enemy import Enemy, Boss
from spritesheet_functions import SpriteSheet
from angle_movement import find_distance, find_angle, calculate_new_xy

class Level:
    def __init__(self, gamearea):
        self.time = 0
        self.gamearea = gamearea
        self.background = False

    def draw(self):
        self.gamearea.blit(self.background, (0, 0))

class Stage_01(Level):
    def __init__(self, gamearea):
        super().__init__(gamearea)
        self.background = SpriteSheet("stage.png").get_image(0, 0, 520, 680)
    

