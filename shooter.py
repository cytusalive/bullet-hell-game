import pygame
import sys
import random
import math
from player import Player
from enemy import Enemy
from spritesheet_functions import SpriteSheet
from angle_movement import calculate_new_xy, find_angle


# initialize pygame
pygame.init()
pygame.display.set_caption("Touhou")
gameicon = pygame.image.load("ghost.png")
pygame.display.set_icon(gameicon)
pygame.font.init()
font = pygame.font.SysFont("Arial", 40, True)
font2 = pygame.font.SysFont("Arial", 24, False)
textcolor = (0, 0, 0)

# initialize screen
screenx = 800
screeny = 700
screen = pygame.display.set_mode((screenx, screeny))
bgcolor = (100, 20, 20)
gamearea = pygame.Surface((520, 680))
gacolor = (150, 200, 250)

# initialize fps
clock = pygame.time.Clock()

# stage background
class Stage:
    def __init__(self):
        self.sprite = SpriteSheet("stage.png").get_image(0, 0, 520, 680)
        
    def draw(self):
        gamearea.blit(self.sprite, (0, 0))




class Bullet:
    def __init__(self, x, y, speed, angle, color=(255, 100, 150)):
        self.xpos = x
        self.ypos = y
        self.speed = speed
        self.angle = angle
        self.power = 10
        self.color = color
        
    def __repr__(self):
        return str(self.xpos) + str(self.ypos)

    def draw(self):
        pygame.draw.circle(gamearea, self.color, (self.xpos, self.ypos), 6, 2)
        pygame.draw.circle(gamearea, (255, 255, 255), (self.xpos, self.ypos), 4)

    def move(self):
        self.xpos, self.ypos = calculate_new_xy(self.xpos, self.ypos, self.speed, self.angle)
        if self.xpos < 0 or self.xpos > gamearea.get_width():
            return False
        if self.ypos < 0 or self.ypos > gamearea.get_height():
            return False
        return True

# returns true if 2 positions are within hitradius in distance
def hitdetect(bullet, target, hitradius):
    distance = math.sqrt((target.xpos - bullet.xpos)**2 + (target.ypos - bullet.ypos)**2)
    if distance < hitradius and distance > -hitradius:
        return True
    return False

# initializes stage, player
background = Stage()       
reisen = Player(gamearea)

# allocate an array of enemies
enemies = []

# allocate arrays of player and enemy bullets
player_bullets = []
enemy_bullets = []

# initalize bullet firing cooldown
cd = 0

# variable of player state
focusfire = False

# pausing/ending
pause = False
gameover = False

while True:
    # draw screen, game area, stage background
    screen.fill(bgcolor)
    gamearea.fill(gacolor)
     
    # properly exit when closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # find mouse location, not being used as of now    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()

        # pause/unpause on ESC
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = not pause 

    # find a list of keys being pressed
    keys = pygame.key.get_pressed()

    if pause or gameover:
        if gameover:
            text = font.render("GAME OVER", True, textcolor)
            gamearea.blit(text, (100, 200))
            text2 = font2.render("PRESS ENTER TO RESTART", True, textcolor)
            gamearea.blit(text2, (100, 250))

            # reinitialize everything on ENTER key
            if keys[pygame.K_RETURN]:
                background = Stage()       
                reisen = Player(gamearea)
                enemies = []
                player_bullets = []
                enemy_bullets = []
                cd = 0
                focusfire = False
                pause = False
                gameover = False
        
    else:
        background.draw()
        # preparing movement from key press
        # determine speed from player state
        if focusfire:
            playerspeed = 3
        else:
            playerspeed = 6

        # to use for transitioning between moving and idling
        moved = False

        # if direction key is pressed
        # move in the direction
        # play the next frame in movement animation
        # if changing direction from left or right
        # set frame to play part of current direction animation backwards as recovery animation
        if keys[pygame.K_LEFT]:
            reisen.move(-playerspeed, 0)
            moved = True
            if reisen.direction == "right":
                reisen.frame = 3
                reisen.direction = "rightrecover"
            if reisen.direction == "idle": 
                reisen.frame = 0
                reisen.direction = "left"
        if keys[pygame.K_RIGHT]:
            reisen.move(playerspeed, 0)
            moved = True
            if reisen.direction == "left":
                reisen.frame = 3
                reisen.direction = "leftrecover"
            if reisen.direction == "idle":
                reisen.frame = 0
                reisen.direction = "right"

        # if no direction is pressed
        # if player was moving before
        # play recovery animation until back to idle
        if not moved:
            if reisen.direction == "left":
                reisen.frame = 3
                reisen.direction = "leftrecover"
            if reisen.direction == "right":
                reisen.frame = 3
                reisen.direction = "rightrecover"
        
        # moving up and down with respective keys
        if keys[pygame.K_UP]:
            reisen.move(0, -playerspeed)
        if keys[pygame.K_DOWN]:
            reisen.move(0, playerspeed)
        
        # draw player
        reisen.draw(focusfire)

        # switching between default spread firing or focused firing from player input
        cd += 1
        focusfire = False
        if keys[pygame.K_z]:
            if cd % 5 == 0:
                player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 8, math.radians(-90)))
                player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 8, math.radians(-85)))
                player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 8, math.radians(-95)))
                player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 8, math.radians(-80)))
                player_bullets.append(Bullet(reisen.xpos, reisen.ypos - 23, 8, math.radians(-100)))
        elif keys[pygame.K_x]:
            focusfire = True
            if cd % 5 == 0:
                player_bullets.append(Bullet(reisen.xpos - 12, reisen.ypos - 18, 8, math.radians(-90)))
                player_bullets.append(Bullet(reisen.xpos + 12, reisen.ypos - 18, 8, math.radians(-90)))
                player_bullets.append(Bullet(reisen.xpos - 6, reisen.ypos - 23, 8, math.radians(-90)))
                player_bullets.append(Bullet(reisen.xpos + 6, reisen.ypos - 23, 8, math.radians(-90)))


        # removing out of screen bullets with new list
        nbl = []
        for b in player_bullets:
            b.draw()
            if b.move():
                nbl.append(b)
        player_bullets = nbl

        # enemy spawn timer
        if cd % 180 == 0:
            enemies.append(Enemy(random.randint(0, gamearea.get_width()), random.randint(0, 100), random.randint(-5, 5), 1, gamearea))
        
        # remove enemies when out of screen or hp drop to 0
        to_del = []
        nel = []
        for e in enemies:
            if e.ypos < gamearea.get_height() and e.hp > 0:
                nel.append(e)
            # add index of bullet to delete list if in contact with enemy
            for bi in range(len(player_bullets)):
                bi = len(player_bullets) - 1 - bi
                if hitdetect(player_bullets[bi], e, 25):
                    e.hp -= player_bullets[bi].power
                    to_del.append(bi)
        
        # delete bullets in the contact list
        for bi in to_del:
            del player_bullets[bi]
        
        # moving enemy
        enemies = nel
        for e in enemies:
            e.move()
            e.draw()
            # fires a bullet directly at player by using angle movement functions
            if cd % 60 == 0 and e.ypos <= 600:
                angle = find_angle(e.xpos, e.ypos, reisen.xpos, reisen.ypos)
                enemy_bullets.append(Bullet(e.xpos, e.ypos, 3, angle, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

        # player hitbox
        nbl = []
        for b in enemy_bullets:
            if hitdetect(b, reisen, 10):
                reisen.hp -= b.power
                if reisen.hp <= 0:
                    gameover = True
                continue
            else:
                nbl.append(b)
        enemy_bullets = nbl

        # remove bullets if out of screen
        nbl = []
        for b in enemy_bullets:
            b.draw()
            if b.move():
                nbl.append(b)
        enemy_bullets = nbl
    
    # draw everything on to the screen and tick for 60 fps
    screen.blit(gamearea, (10,10))
    pygame.display.update()
    msElapsed = clock.tick(60)

