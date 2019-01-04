import pygame
from pygame.locals import *
import random
import time
#import pygame_pong_menu

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

xchange = 2
ychange = 1
l_change = 0
r_change = 0
l_score = 0
r_score = 0

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong! - Two Player")

def text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("URW Gothic L",size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def lose():
    screen.fill(black)
    ball.display()
    l_pad.display()
    r_pad.display()
    pygame.draw.rect(screen,white,(397,0,6,600))
    text(str(r_score), 750,50,red,48)
    text(str(l_score), 50,50,blue,48)
    pygame.display.update()
    time.sleep(1)

class Ball:
    def __init__(self,xcircle,ycircle,color,radius):
        self.xcircle = xcircle
        self.ycircle = ycircle
        self.color = color
        self.radius = radius

    def move(self):
        self.xcircle = self.xcircle + xchange
        self.ycircle = self.ycircle + ychange

    def display(self):
        pygame.draw.circle(screen,self.color,(self.xcircle,self.ycircle),self.radius)

class Paddle:
    def __init__(self,xpaddle,ypaddle,color,length,width):
        self.xpaddle = xpaddle
        self.ypaddle = ypaddle
        self.color = color
        self.length = length
        self.width = width

    def move(self,paddlechange):
        self.ypaddle = self.ypaddle + paddlechange

    def display(self):
        pygame.draw.rect(screen,self.color,(self.xpaddle,self.ypaddle,self.length,self.width))

ball = Ball(400,300,white,20)
l_pad = Paddle(0,300,blue,20,100)
r_pad = Paddle(780,400,red,20,100)

while True:
    pygame.display.update()
    screen.fill(black)
    ball.move()
    ball.display()
    l_pad.move(l_change)
    l_pad.display()
    r_pad.move(r_change)
    r_pad.display()
    pygame.draw.rect(screen,white,(397,0,6,600))

    if l_pad.ypaddle <= 0:
        l_pad.ypaddle = 0
    if l_pad.ypaddle >= 500:
        l_pad.ypaddle = 500
    if r_pad.ypaddle <= 0:
        r_pad.ypaddle = 0
    if r_pad.ypaddle >= 500:
        r_pad.ypaddle = 500
        
    l_pad.ypaddle = l_pad.ypaddle + l_change
    r_pad.ypaddle = r_pad.ypaddle + r_change

    if ball.xcircle in range(760,780) and ball.ycircle in range(r_pad.ypaddle,r_pad.ypaddle+100):
        xchange = -xchange
    if ball.xcircle in range(20,40) and ball.ycircle in range(l_pad.ypaddle,l_pad.ypaddle+100):
        xchange = -xchange

    if ball.ycircle >=580:
            ychange = -ychange
    if ball.ycircle <=20:
        ychange = -ychange

        ball.xcircle = ball.xcircle + xchange
        ball.ycircle = ball.ycircle + ychange

    if ball.xcircle > 800:
        ball.xcircle = 400
        ball.ycircle = 300
        l_score = l_score + 1
        lose()
    text(str(l_score), 50,50,blue,48)

    if ball.xcircle < 0:
        ball.xcircle = 400
        ball.ycircle = 300
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

    if r_score == 10:
        xcircle = 400
        ycircle =  300
        text("RED WINS!",295,350,red,70)
        pygame.display.update()
        time.sleep(5)
        screen.fill(black)
        l_score = 0
        r_score = 0


    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    r_change = -1
                elif event.key == K_DOWN:
                    r_change = 1
                elif event.key == K_w:
                    l_change = -1
                elif event.key == K_s:
                    l_change = 1

            elif event.type == KEYUP:
                if event.key == K_UP:
                    r_change = 0
                elif event.key == K_DOWN:
                    r_change = 0
                elif event.key == K_w:
                    l_change = 0
                elif event.key == K_s:
                    l_change = 0
                    
