import pygame
import sys
import random
import math
from player import Player
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

class Enemy:
    def __init__(self, x, y, changex, changey):
        sprite_sheet = SpriteSheet("ghost.png")
        image = sprite_sheet.get_image(0, 0, 40, 40)
        self.image = image
        self.xpos = x
        self.ypos = 0
        self.ydes = y
        self.changex = changex
        self.changey = changey
        self.hp = 100
    
    def move(self):
        if self.ypos < self.ydes:
            self.ypos += 3
            return
        else:
            self.ydes = 0
            self.xpos += self.changex
            if self.xpos > gamearea.get_width() or self.xpos < 0:
                self.changex *= -1
                self.xpos += self.changex
            self.ypos += self.changey

    def draw(self):
        gamearea.blit(self.image, (self.xpos-20, self.ypos-20))



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
        self.power = 10
    
    def __repr__(self):
        return str(self.xpos) + str(self.ypos)

    def draw(self):
        pygame.draw.circle(gamearea, (255, 100, 150), (self.xpos, self.ypos), 6, 2)
        pygame.draw.circle(gamearea, (255, 255, 255), (self.xpos, self.ypos), 4)

    def move(self):
        self.xpos += self.speedx
        self.ypos += self.speedy
        if self.xpos < 0 or self.xpos > gamearea.get_width():
            return False
        if self.ypos < 0 or self.ypos > gamearea.get_height():
            return False
        return True

def hitdetect(bullet, target, hitradius):
    distance = math.sqrt((target.xpos - bullet.xpos)**2 + (target.ypos - bullet.ypos)**2)
    if distance < hitradius and distance > -hitradius:
        return True
    return False

background = Stage()       
reisen = Player(gamearea)
player_bullets = []
enemy_bullets = []
cd = 0

enemies = []


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
    moved = False
    if keys[pygame.K_LEFT]:
        reisen.move(-6, 0)
        moved = True
        if reisen.direction == "right":
            reisen.frame = 3
            reisen.direction = "rightrecover"
        if reisen.direction == "idle": 
            reisen.frame = 0
            reisen.direction = "left"
    if keys[pygame.K_RIGHT]:
        reisen.move(6, 0)
        moved = True
        if reisen.direction == "left":
            reisen.frame = 3
            reisen.direction = "leftrecover"
        if reisen.direction == "idle":
            reisen.frame = 0
            reisen.direction = "right"
    if not moved:
        if reisen.direction == "left":
            reisen.frame = 3
            reisen.direction = "leftrecover"
        if reisen.direction == "right":
            reisen.frame = 3
            reisen.direction = "rightrecover"
    
    if keys[pygame.K_UP]:
        reisen.move(0, -6)
    if keys[pygame.K_DOWN]:
        reisen.move(0, 6)
    
    cd += 1
    if keys[pygame.K_z]:
        if cd % 5 == 0:
            player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 0, -10))
            player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 1, -10))
            player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, -1, -10))
            player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 2, -10))
            player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, -2, -10))
    elif keys[pygame.K_x]:
        if cd % 2 == 0:
            player_bullets.append(Bullet(reisen.xpos - 6, reisen.ypos - 23, 0, -10))
            player_bullets.append(Bullet(reisen.xpos + 6, reisen.ypos - 23, 0, -10))

    nbl = []
    for b in player_bullets:
        b.draw()
        if b.move():
            nbl.append(b)
    player_bullets = nbl

    if cd % 180 == 0:
        enemies.append(Enemy(random.randint(0, gamearea.get_width()), random.randint(0, 100), random.randint(-5, 5), 1))


    
    to_del = []
    nel = []
    for e in enemies:
        if e.ypos < gamearea.get_height() and e.hp > 0:
            nel.append(e)
        for bi in range(len(player_bullets)):
            bi = len(player_bullets) - 1 - bi
            if hitdetect(player_bullets[bi], e, 25):
                e.hp -= player_bullets[bi].power
                to_del.append(bi)
    
    for bi in to_del:
        del player_bullets[bi]
    
    enemies = nel
    for e in enemies:
        e.move()
        e.draw()
        if cd % 60 == 0 and e.ypos <= 600:
            enemy_bullets.append(Bullet(e.xpos, e.ypos, (reisen.xpos - e.xpos)/50, (reisen.ypos - e.ypos)/50))

    nbl = []
    for b in enemy_bullets:
        b.draw()
        if b.move():
            nbl.append(b)
    enemy_bullets = nbl
    


    screen.blit(gamearea, (10,10))
    pygame.display.update()
    msElapsed = clock.tick(60)

