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
        sprite_sheet = SpriteSheet("character.png")
        image = sprite_sheet.get_image(0, 0, 30, 47)
        self.idle = image
        self.xpos = gamearea.get_width() // 2
        self.ypos = gamearea.get_height() // 2
    
    def draw(self):
        gamearea.blit(self.idle, (self.xpos, self.ypos))

    def move(self, changex, changey):
        if self.xpos + self.idle.get_width() + changex > gamearea.get_width():
            pass
        elif self.xpos + changex < 0:
            pass
        else:
            self.xpos += changex
        if self.ypos + self.idle.get_height() + changey > gamearea.get_height():
            pass
        elif self.ypos + changey < 0:
            pass
        else:
            self.ypos += changey


class Stage:
    def __init__(self):
        self.sprite = SpriteSheet("stage.png").get_image(0, 0, 520, 680)
        
    def draw(self):
        gamearea.blit(self.sprite, (0, 0))


class Bullet:
    def __init__(self, x, y, speedx, speedy):
        self.xpos = x
        self.ypos = y
        self.speedx = speedx
        self.speedy = speedy
    
    def __repr__(self):
        return str(self.xpos) + str(self.ypos)

    def draw(self):
        pygame.draw.circle(gamearea, (255, 0, 0), (self.xpos, self.ypos), 6, 2)
        pygame.draw.circle(gamearea, (255, 255, 255), (self.xpos, self.ypos), 4)

    def move(self):
        self.xpos += self.speedx
        self.ypos += self.speedy
        if self.xpos < 0 or self.xpos > gamearea.get_width():
            return False
        if self.ypos < 0 or self.ypos > gamearea.get_height():
            return False


background = Stage()        
reisen = Player()
bullets = []
cd = 0
    
while True:
    screen.fill(bgcolor)
    gamearea.fill(gacolor)
    background.draw()
    reisen.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        reisen.move(-6, 0)
    if keys[pygame.K_RIGHT]:
        reisen.move(6, 0)
    if keys[pygame.K_UP]:
        reisen.move(0, -6)
    if keys[pygame.K_DOWN]:
        reisen.move(0, 6)
    
    cd += 1
    if keys[pygame.K_z]:
        if cd % 5 == 0:
            bullets.append(Bullet(reisen.xpos + reisen.idle.get_width()//2, reisen.ypos, 0, -10))

    to_delete = []
    for b in range(len(bullets)):
        if bullets[b].move() == False:
            to_delete.append(b)
        bullets[b].draw()
    
    to_delete.sort(key=None, reverse=True)
    for d in to_delete:
        del bullets[d]

    print(bullets)
    screen.blit(gamearea, (10,10))
    pygame.display.update()
    msElapsed = clock.tick(60)