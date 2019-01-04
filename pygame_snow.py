import pygame
from pygame.locals import *
import random

pygame.init()
red = (255,0,0)
green = (0,128,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
aqua = (0,255,255)
fuchsia = (255,0,255)
gray = (128,128,128)
lime = (0,255,0)
maroon = (128,0,0)
navy_blue = (0,0,128)
olive = (128,128,0)
purple = (128,0,128)
silver = (192,192,192)
teal = (0,128,128)
yellow = (255,255,0)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Animation")
colors = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


b = [ ]
for coordinates in range(0,50,1):

    a = [random.randint(0,800),random.randint(0,600)]
    b.append(a)
    
fpsclock = pygame.time.Clock()
  

while True:
    for coordinates in range(0,50,1):
        colors = (random.randint(128,255),random.randint(128,255),random.randint(128,255))
        pygame.draw.circle(screen,colors,(b[coordinates]),2)
        b[coordinates] [1]+=1

        

        if b[coordinates][1] >= 600:
            b[coordinates][0]= random.randint(0,800)
            b[coordinates][1]= 0
            

    pygame.display.update()
    fpsclock.tick(1000)

    screen.fill(black)

