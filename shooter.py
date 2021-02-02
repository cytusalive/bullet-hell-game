import pygame
import sys
import random
from spritesheet_functions import SpriteSheet

#initialize pygame
pygame.init()
pygame.display.set_caption("Touhou")

#initialize screen
screenx = 800
screeny = 700
screen = pygame.display.set_mode((screenx, screeny))
bgcolor = (100, 20, 20)
gamearea = pygame.Surface((520, 680))
gacolor = (50, 100, 180)

#initialize fps
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("character.png")
        image = sprite_sheet.get_image(0, 0, 30, 47)
        self.idle = image
        self.xpos = gamearea.get_width() // 2
        self.ypos = gamearea.get_height() // 2

    
    def draw(self):
        gamearea.blit(self.idle, (self.xpos, self.ypos))

reisen = Player()

while True:
    screen.fill(bgcolor)
    gamearea.fill(gacolor)
    reisen.draw()
    screen.blit(gamearea, (10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
            if event.key == pygame.K_RIGHT:
                
            if event.key == pygame.K_UP:
                
            if event.key == pygame.K_DOWN:
               ''' 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
    pygame.display.update()
    msElapsed = clock.tick(30)