import pygame
from pygame.locals import *
import random

pygame.init()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame")

x=300
y=300
xchange = random.randint(1,5)
ychange = random.randint(1,5)


while True:
    screen.fill(black)
    pygame.draw.circle(screen,blue,(x,y),100)
 
    if x<=100:
      xchange = -xchange
      

    if x>= 700:
        xchange =-xchange

        
    if y<= 100:
      ychange = -ychange


    if y>= 500:
      ychange =-ychange



    
    x=x+xchange
    y=y+ychange
    
    pygame.display.update()
    
