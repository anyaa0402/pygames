import pygame
from pygame.locals import *
import random
import time
import pygame_pong_menu
#import pygame_pong_user

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong! - One Player")

l_pad = 300
r_pad = 400
l_pad_change=0
r_pad_change = 0

xcircle = 400
ycircle = 300
xchange = 2
ychange = 1

l_score = 0
r_score = 0

def text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("URW Gothic L",size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def lose():
    screen.fill(black)
    pygame.draw.circle(screen,white,(xcircle,ycircle),20)
    pygame.draw.rect(screen,blue,(0,l_pad,20,100))
    pygame.draw.rect(screen,red,(780,r_pad,20,100))
    pygame.draw.rect(screen,white,(397,0,6,600))
    text(str(r_score), 750,50,red,48)
    text(str(l_score), 50,50,blue,48)
    pygame.display.update()
    time.sleep(1)

def one_player():
    global l_pad, r_pad,xcircle,ycircle,xchange,ychange,l_score,r_score,l_pad_change,r_pad_change

    while True:
        pygame.display.update()
        screen.fill(black)
        pygame.draw.rect(screen,white,(397,0,6,600))
        pygame.draw.rect(screen,blue,(0,l_pad,20,100))
        pygame.draw.rect(screen,red,(780,r_pad,20,100))
        pygame.draw.circle(screen,white,(xcircle,ycircle),20)

        if l_pad <= 0:
            l_pad = 0
        if l_pad >= 500:
            l_pad = 500
        if r_pad <= 0:
            r_pad = 0
        if r_pad >= 500:
            r_pad = 500
            
        l_pad = l_pad + l_pad_change
        r_pad = r_pad + r_pad_change
        
        if xcircle in range(760,780) and ycircle in range(r_pad,r_pad+100):
            xchange = -xchange
        if xcircle in range(20,40) and ycircle in range(l_pad,l_pad+100):
            xchange = -xchange

        if ycircle >=580:    #if ball hits right
            ychange = -ychange
        if ycircle <=20:       #if ball hits left
            ychange = -ychange

        xcircle = xcircle + xchange
        ycircle = ycircle + ychange

        if l_pad <= ycircle:
            l_pad = l_pad + 1

        if l_pad >= ycircle:
            l_pad = l_pad - 1

        
        if xcircle > 800:       #if right loses
            xcircle = 400
            ycircle = 300
            l_score = l_score + 1
            lose()
        text(str(l_score), 50,50,blue,48)

        if xcircle < 0:        # if left loses
            xcircle = 400
            ycircle = 300
            r_score = r_score +1
            lose()
        text(str(r_score), 750,50,red,48)

        if l_score == 10:
            xcircle = 400
            ycircle = 300
            text("BLUE WINS!",265,350,blue,70)
            pygame.display.update()
            time.sleep(5)
            screen.fill(black)
            l_score = 0
            r_score = 0
            pygame_pong_menu.menu()

        if r_score == 10:
            xcircle = 400
            ycircle =  300
            text("RED WINS!",295,350,red,70)
            pygame.display.update()
            time.sleep(5)
            screen.fill(black)
            l_score = 0
            r_score = 0
            pygame_pong_menu.menu()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    r_pad_change = -2
                elif event.key == K_DOWN:
                    r_pad_change = 2

            elif event.type == KEYUP:
                if event.key == K_UP:
                    r_pad_change = 0
                elif event.key == K_DOWN:
                    r_pad_change = 0
