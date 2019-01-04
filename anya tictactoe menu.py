import pygame
from pygame.locals import *
#import anya_tictactoe
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((600,600))

def words(msg,x,y,color,size):
    fontobj = pygame.font.SysFont("freesans",size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def menu():
  pygame.display.set_caption("Tic Tac Toe - Menu")

  while True:
      
        pygame.draw.rect(screen,green,(200,175,200,100),10)
        words("START",245,210,green,32)
        pygame.draw.rect(screen,red,(200,325,200,100),10)
        words("QUIT",260,360,red,32)
        words("Tic Tac Toe",150,50,white,60)
        words("Created by Anya Agarwal",190,480,white,20)
        
    

        for event in pygame.event.get():
              if event.type == QUIT:
                    pygame.quit()
                    exit()
              elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                  x,y = event.pos
                  if x in range(200,400) and y in range(175,275):
                      print ("START")
                      screen.fill((0,0,0))
                      anya_tictactoe.tic_tac_toe_game()
                      break
                  if x in range(200,400) and y in range(325,425):
                      print ("QUIT")
                      quit()
                      
        pygame.display.update()
        
menu()
