from pygame import mixer as mr
import random as rd 
import math as m
from tkinter import font
import pygame as pg

pg.init()

width,height = 800,600

screen = pg.display.set_mode((width,height))

background = pg.image.load("islam.png")
mr.music.load("background.wav")
mr.music.play(-1)

pg.display.set_caption("spaceInvaders")
icon = pg.image.load("ufo.png")
pg.display.set_icon(icon)

player = pg.image.load("astronomy.png")
playerX = 370
playerY = 480
playerX_change = 0

enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 10

for i in range(num_of_enemy):
    enemy_img.append(pg.image.load("alien.png"))  
    enemyX.append(rd.randint(0,735 ))
    enemyY.append(rd.randint(50,150 ))
    enemyX_change.append(4)
    enemyY_change.append(40) 

bullet_img = pg.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def bullet_fire(x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bullet_img,(x+16,y+10))

def Player(x,y):
    screen.blit(player,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

def isCollision (enemyX, enemyY, bulletX, bulletY):
    distance = m.sqrt(m.pow((enemyX - bulletX),2) + m.pow(enemyY - bulletY,2))
    if distance < 27:
        return True
    else:
        return False

score_val = 0
font = pg.font.Font("freesansbold.ttf",37)

# textX = 10
# textY = 10
# def show_score(x,y):
#     score = font.render("Score: " + str(score_val),True,(253,48,48))
#     screen.blit(score,(x,y))

running = True


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerX_change = -4
            if event.key == pg.K_RIGHT:
                playerX_change = 4
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerX_change = 0
            if event.key == pg.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mr.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                bullet_fire(playerX,bulletY)      

    screen.blit(background,(0,0)) 
    playerX += playerX_change 
    # screen.fill((0,0,0))
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] > 763:
            enemyX_change[i] = -4
        collision  = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)  
        if collision:
            explosion_sound = mr.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            enemyX[i] = rd.randint(0,735)
            enemyY[i] = rd.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)

    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state=="fire":
        bullet_fire(playerX,bulletY)
        bulletY -= bulletY_change

    # collision  = isCollision(enemyX,enemyY,bulletX,bulletY)  
    # if collision:
    #     bulletY = 480
    #     bullet_state = "ready"
    #     enemyX = rd.randint(0,735)
    #     enemyY = rd.randint(50,150)
    #     score_val += 1
    
    Player(playerX,playerY)
    # show_score(textX,textY)
    pg.display.update()
