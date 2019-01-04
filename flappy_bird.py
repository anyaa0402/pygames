import pygame
from pygame.locals import *
import random
import time

pygame.init()

red = (255,0,0)
orange = (255,128,0)
d_yellow = (204,204,0)
dr_yellow = (153,153,0)
yellow = (255,240,0)
li_green = (178,255,102)
l_green = (178,255,102)
green = (76,153,0)
blue = (0,0,255)
brown = (102,51,0)
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Flappy Bird")

xcircle = 400
ycircle = 300
ychange=0
pipechange = 750
uplength = 200
downlength = 325
game = 0
score = 0

def text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("URW Gothic L",size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def cloud(a,b,c,d,e,f):
    pygame.draw.circle(screen,white,(a,b),25)
    pygame.draw.circle(screen,white,(c,d),25)
    pygame.draw.circle(screen,white,(e,f),25)
    

while True:
    pygame.display.update()
    screen.fill((51,255,255))

    cloud(100,100,113,75,126,100)
    cloud(150,450,163,425,176,450)
    cloud(250,250,263,225,276,250)
    cloud(400,175,413,150,426,175)
    cloud(600,400,613,375,626,400)
    cloud(700,130,713,105,726,130)
    
    pygame.draw.rect(screen,li_green,(0,550,800,100))
    pygame.draw.rect(screen,brown,(0,560,800,40))
    
    pygame.draw.circle(screen,yellow,(xcircle, ycircle),20)
    pygame.draw.circle(screen,black,(xcircle + 8,ycircle - 5),5)
    pygame.draw.polygon(screen,orange,((xcircle + 15,ycircle),(xcircle + 15,ycircle + 4),(xcircle + 30,ycircle + 2)),5)
    pygame.draw.polygon(screen,d_yellow,((xcircle - 9,ycircle - 3),(xcircle - 11,ycircle + 5),(xcircle - 30,ycircle - 13)), 7)
    pygame.draw.polygon(screen,yellow,((xcircle - 16,ycircle + 10),(xcircle - 11,ycircle + 16),(xcircle - 22,ycircle + 13)),3)

    
                        
    pygame.draw.rect(screen,green,(pipechange,0,50,uplength))
    pygame.draw.rect(screen,green,(pipechange,downlength,50,600))
    text(str(score), 50,50,black,48)
    pipechange = pipechange - 1                                           

    if pipechange == -50:
        pipechange = 750
        uplength = random.randint(5,445)
        downlength = uplength + 125

    if ycircle == 18:
        print ("collision")
        game = 1

    if ycircle == 582:
        print ("collision")
        game = 1

    if pipechange - 18 <= xcircle <= pipechange + 68 and 18 <= ycircle <= uplength + 18:
        print ("collision")
        game = 1

    if pipechange - 18 <= xcircle <= pipechange + 68 and downlength - 18 <= ycircle <= 582:
        print ("collision")
        game = 1

    if score == 10:
        xcircle = 400
        ycircle = 300
        text("YOU WON!",265,350,black,70)
        pygame.display.update()
        time.sleep(5)
        quit()

    if game == 1:
        xcircle = 400
        ycircle = 300
        text("GAME OVER!",265,350,black,70)
        pygame.display.update()
        time.sleep(5)
        quit()

    if xcircle == pipechange + 50 and uplength <= ycircle <= downlength:
        score = score + 1


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            ychange = -2

        if event.type == KEYUP:
            ychange=1

    ycircle = ycircle + ychange
