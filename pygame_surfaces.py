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
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

s_list = []

for a in range(0,5):
    surface = pygame.Surface((100,100))
    pygame.draw.circle(surface,red,(0,a*100),50)
    s_list.append(surface)



for a in range (0,5):
    screen.blit(s_list[a],(random.randint(0,200),random.randint(0,300)))



pygame.display.update()
