import pygame
from pygame.locals import *
import random
import time

pygame.init()

red = (255,0,0)
orange = (255,128,0)
yellow = (255,240,0)
lime = (0,255,0)
green = (76,153,0)
blue = (0,0,255)
brown = (102,51,0)
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((1700,700))
pygame.display.set_caption("Animation")

walk = []
back = []
attack = []

x = 200
y = 200
yattack = 150
xjump = 200
yjump = 50
space = 0
up = 0
right = 0
left = 0

rightwalk = pygame.image.load("walk1.png")
stillwalk = pygame.image.load("walk2.png")
leftwalk = pygame.image.load("walk3.png")
rightback = pygame.image.load("back2.png")
stillback = pygame.image.load("back1.png")
leftback = pygame.image.load("back3.png")
middlejump = pygame.image.load("jump1.png")
leftattack = pygame.image.load("attack1.png")
rightattack = pygame.image.load("attack2.png")

walk.append(rightwalk)
walk.append(stillwalk)
walk.append(leftwalk)
walk.append(stillwalk)

back.append(rightback)
back.append(stillback)
back.append(leftback)

attack.append(leftattack)
attack.append(rightattack)


while True:
    pygame.draw.rect(screen,white,(0,0,1700,400))
    
    screen.blit(leftwalk,(x,y))
    
    if right == 1:
        for display in walk:
            screen.fill(black)
            pygame.draw.rect(screen,white,(0,0,1700,400))
            screen.blit(display,(x,y))
            pygame.display.update()
            time.sleep(0.1)
            x = x + 30
            screen.fill(black)
            pygame.draw.rect(screen,white,(0,0,1700,400))

    if x > 1700:
        x = 0

    if left == 1:
        for display in back:
            screen.fill(black)
            pygame.draw.rect(screen,white,(0,0,1700,400))
            screen.blit(display,(x,y))
            pygame.display.update()
            time.sleep(0.1)
            x = x - 30
            screen.fill(black)
            pygame.draw.rect(screen,white,(0,0,1700,400))

        if x < 0:
            x = 1700

    if up == 1:
        screen.fill(black)
        pygame.draw.rect(screen,white,(0,0,1700,400))
        screen.blit(middlejump,(x-100,yjump))
        pygame.display.update()
        time.sleep(0.2)
        x = x + 100
        screen.fill(black)
        pygame.draw.rect(screen,white,(0,0,1700,400))
        up = 0
        

    if space == 1:
        for display in attack:
            screen.fill(black)
            pygame.draw.rect(screen,white,(0,0,1700,400))
            screen.blit(display,(x-200,yattack))
            pygame.display.update()
            time.sleep(0.15)
            x = x + 300
            yattack = yattack - 50
            screen.fill(black)
            pygame.draw.rect(screen,white,(0,0,1700,400))
            space = 0
        x = x - 500
        yattack = 150
             


        
        

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                space = 1
                up = 0
                right = 0
                left = 0
            elif event.key == K_UP:
                up = 1
                space = 0
                right = 0
                left = 0
            elif event.key == K_RIGHT:
                right = 1
                space = 0
                up = 0
                left = 0
            elif event.key == K_LEFT:
                left = 1
                space = 0
                up = 0
                right = 0

        elif event.type == KEYUP:
            if event.key == K_SPACE:
                space = 0
            elif event.key == K_UP:
                up = 0
            elif event.key == K_RIGHT:
                right = 0
            elif event.key == K_LEFT:
                left = 0





            
