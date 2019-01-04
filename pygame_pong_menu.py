import pygame
from pygame.locals import *
import random
import time
import pygame_pong_user
import pygame_pong_comp

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((800,600))


def text(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("URW Gothic L",size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def menu():
    pygame.display.set_caption("Pong! - Menu")

    while True:
        text("Pong!", 280,50,white,130)
        text("Created by Anya Agarwal",240,500,white,40)
        text("QUIT",340,375,red,70)
        text("ONE PLAYER",65,225,green,70)
        text("TWO PLAYER",415,225,green,70)
        pygame.draw.rect(screen,green,(50,200,350,100),10)
        pygame.draw.rect(screen,green,(400,200,350,100),10)
        pygame.draw.rect(screen,red,(300,350,200,100),10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x,y = event.pos
                if x in range(400,750) and y in range(200,300):
                    screen.fill(black)
                    pygame_pong_user.two_player()
                    break
                elif x in range(50,400) and y in range(200,300):
                    screen.fill(black)
                    pygame_pong_comp.one_player()
                    break
                
                elif x in range(300,500) and y in range(350,450):
                    quit()
        

        pygame.display.update()

menu()


