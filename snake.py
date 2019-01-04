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

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")

foodx = (random.randint(1,799) // 20) * 20
foody = (random.randint(1,599) // 20) * 20
snakex = (random.randint(1,799) // 20) * 20
snakey = (random.randint(1,599) // 20) * 20
down = 0
left = 0
right = 0
up = 0
score = 0
score2 = 0
stage = 0
flag = 0
snakelist = []
check = 0

def text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("URW Gothic L",size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def lose():
    print ("collision")
    if stage == 1:
        text("Stage 1",34,30,red,25)
        text(str(score), 50,50,red,48)
    if stage == 2:
        text("Stage 2",184,30,red,25)
        text(str(score2),200,50,red,48)
    down = 0
    up = 0
    left = 0
    right = 0        
    text("YOU LOSE",300,300,red,72)
    pygame.display.update()
    time.sleep(5)
    #quit()

a = pygame.time.Clock()



while True:

    snakelist.insert(0,[snakex,snakey])

    if [snakex,snakey] in snakelist[1:]:
        lose()
    if snakex >= 800:
        lose()
    if snakex < 0:
        lose()
    if snakey >= 600:
        lose()
    if snakey < 0:
        lose()

    if score2 == 5:
        down = 0
        up = 0
        left = 0
        right = 0        
        text("YOU WIN",300,300,lime,72)
        pygame.display.update()
        time.sleep(5)
        quit()
        
    screen.fill(black)
    
    pygame.draw.rect(screen,red,(foodx,foody,20,20)) #food

    text("Stage 1",34,30,white,25)
    if score != 5:
        text(str(score), 50,50,white,48)
    text("Stage 2",184,30,white,25)
    text(str(score2),200,50,white,48)
    
    for segment in snakelist:
        pygame.draw.rect(screen,green,segment+[20,20]) #snake head
    snakelist.pop()

    if snakex == foodx and snakey == foody:
        foodx = (random.randint(0,800) // 20) * 20
        foody = (random.randint(0,600) // 20) * 20
        snakelist.insert(0,[snakex,snakey])
        if stage == 1:
            score = score + 1
        if stage == 2:
            score2 = score2 + 1

    if score < 5:
        if check == 1:
            stage = 2
        else:
            stage = 1
            a.tick(15)

    if score == 5:
        text("5", 50,50,lime,48)
        flag = 1
        stage = 2
        text("Stage 1",34,30,lime,25)
        score = 0
        check = 1

    if flag == 1:
        snakelist = []
        flag = 0

    if stage == 2:
        a.tick(25)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                down = 1
                up = 0
                left = 0
                right = 0
            if event.key == K_UP:
                up = 1
                down = 0
                left = 0
                right = 0
            if event.key == K_RIGHT:
                right = 1
                left = 0
                up = 0
                down = 0
            if event.key == K_LEFT:
                left = 1
                right = 0
                up = 0
                down = 0
                
    if down == 1:
            snakey = snakey + 20
    if up == 1:
            snakey = snakey - 20
    if right == 1:
            snakex = snakex + 20
    if left == 1:
            snakex = snakex - 20
                
