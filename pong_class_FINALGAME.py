import pygame
from pygame.locals import *
import random
import time
import pygame_pong_menu

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

xchange = 3
ychange = 2
l_change = 0
r_change = 0

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong! - Two Player")

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
    ball.move()
    ball.display()
    l_pad.move(l_change)
    l_pad.display()
    r_pad.move(r_change)
    r_pad.display()
    
