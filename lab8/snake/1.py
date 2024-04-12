import random
import pygame
import sys

pygame.init()



WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))


red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

work=True

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen,red,(0,0,100,100),20)
    pygame.display.flip()
