import pygame
from spritesheet_functions import SpriteSheet

class Enemy:
    
    def __init__(self, x, y, changex, changey, gamearea):
        sprite_sheet = SpriteSheet("ghost.png")
        image = sprite_sheet.get_image(0, 0, 40, 40)
        self.image = image
        self.xpos = x
        self.ypos = 0
        self.ydes = y
        self.changex = changex
        self.changey = changey
        self.hp = 200
        self.gamearea = gamearea
    
    def move(self):
        if self.ypos < self.ydes:
            self.ypos += 3
            return
        else:
            self.ydes = 0
            self.xpos += self.changex
            if self.xpos > self.gamearea.get_width() or self.xpos < 0:
                self.changex *= -1
                self.xpos += self.changex
            self.ypos += self.changey

    def draw(self):
        self.gamearea.blit(self.image, (self.xpos-20, self.ypos-20))
