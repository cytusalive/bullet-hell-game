import pygame
from spritesheet_functions import SpriteSheet

class Player:
    def __init__(self, gamearea):   

        sheet = SpriteSheet("character.png")
        # loads all idle frames in a list
        self.idle = []
        image = sheet.get_image(0, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(33, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(65, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(97, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(129, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(161, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(193, 0, 32, 47)
        self.idle.append(image)
        image = sheet.get_image(225, 0, 32, 47)
        self.idle.append(image)

        # loads frames moving left
        self.left = []
        image = sheet.get_image(0, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(33, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(65, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(97, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(129, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(161, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(193, 48, 32, 47)
        self.left.append(image)
        image = sheet.get_image(225, 48, 32, 47)
        self.left.append(image)

        # loads frames moving right
        self.right = []
        image = sheet.get_image(0, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(33, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(65, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(97, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(129, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(161, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(193, 96, 32, 47)
        self.right.append(image)
        image = sheet.get_image(225, 96, 32, 47)
        self.right.append(image)


        self.frame = 0
        self.fps = 0
        self.xpos = gamearea.get_width() // 2
        self.ypos = gamearea.get_height() // 2
        self.direction = "idle"
        self.gamearea = gamearea
        self.image = self.idle

    def draw(self):
        if self.direction == "idle":
            self.gamearea.blit(self.image[self.frame], (self.xpos, self.ypos))
            self.fps += 1
            if self.fps % 3 == 0:
                self.frame += 1
            if self.frame == 8:
                self.frame = 0
        if self.direction == "left":
            self.gamearea.blit(self.left[self.frame], (self.xpos, self.ypos))
            self.fps += 1
            if self.fps % 3 == 0:
                self.frame += 1
            if self.frame == 8:
                self.frame = 3
        if self.direction == "leftrecover":
            self.gamearea.blit(self.left[self.frame], (self.xpos, self.ypos))
            self.fps += 1
            if self.fps % 3 == 0:
                self.frame -= 1
            if self.frame == 0:
                self.direction = "idle"
        if self.direction == "right":
            self.gamearea.blit(self.right[self.frame], (self.xpos, self.ypos))
            self.fps += 1
            if self.fps % 3 == 0:
                self.frame += 1
            if self.frame == 8:
                self.frame = 3
        if self.direction == "rightrecover":
            self.gamearea.blit(self.right[self.frame], (self.xpos, self.ypos))
            self.fps += 1
            if self.fps % 3 == 0:
                self.frame -= 1
            if self.frame == 0:
                self.direction = "idle"
            
    def move(self, changex, changey):
        if self.xpos + self.idle[self.frame].get_width() + changex > self.gamearea.get_width():
            pass
        elif self.xpos + changex < 0:
            pass
        else:
            self.xpos += changex
        if self.ypos + self.idle[self.frame].get_height() + changey > self.gamearea.get_height():
            pass
        elif self.ypos + changey < 0:
            pass
        else:
            self.ypos += changey
