import pygame 
import sys
import cmath


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

clock=pygame.time.Clock()

prevX = 0
prevY = 0

currX = 0
currY = 0

color=colorYELLOW

size=1

mode="line"

LMBpressed=False

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
pygame.draw.circle
def calculate_cicle(x1,x2,y1,y2):
    return abs(cmath.sqrt(((x2-x1)**2)+((y2-y1)**2)))

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = red
                print("color:red")
            elif event.key == pygame.K_g:
                color = colorGREEN
                print("color:green")
            elif event.key == pygame.K_b:
                color = blue
                print("color:blue")
            elif event.key==pygame.K_KP_PLUS:
                size+=1
                print(size)
            elif event.key==pygame.K_KP_MINUS and size>1:
                size-=1
                print(size)
            elif event.key==pygame.K_1:
                mode="line"
                print(mode)
            elif event.key==pygame.K_2:
                mode="square"
                print(mode)
            elif event.key==pygame.K_3:
                mode="cicle"
                print(mode)
            elif event.key==pygame.K_BACKSPACE:
                mode="eraser"
                print(mode)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            print("lbm")
            LMBpressed=True
            prevX = event.pos[0]
            prevY = event.pos[1]
        if event.type==pygame.MOUSEMOTION:
            print(event.pos)
            currX=event.pos[0]
            currY=event.pos[1]
        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            if mode=="line":
                print("no lmb")
                LMBpressed=False
                base_layer.blit(screen, (0, 0))
            elif mode=="square":
                print("no sqr")
                LMBpressed=False
                pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), size)
                base_layer.blit(screen, (0, 0))
            elif mode=="cicle":
                print("no crcl")
                LMBpressed=False
                pygame.draw.circle(screen,color,(prevX,prevY),calculate_cicle(min(prevX,currX),max(prevX,currX),
                min(prevY,currY),max(prevY,currY)),size)
                base_layer.blit(screen, (0, 0))
            elif mode=="eraser":
                print("no lmb")
                LMBpressed=False
                base_layer.blit(screen, (0, 0))
    
    if LMBpressed :
        if mode=="line":
            pygame.draw.line(screen,color,(prevX,prevY), (currX,currY), size)
        elif mode=="square":
            screen.blit(base_layer, (0, 0))
            pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), size)
        elif mode=="cicle":
            screen.blit(base_layer,(0,0))
            pygame.draw.circle(screen,color,(prevX,prevY),calculate_cicle(min(prevX,currX),max(prevX,currX),
            min(prevY,currY),max(prevY,currY)),size)
        elif mode=="eraser":
            pygame.draw.line(screen,black,(prevX,prevY), (currX,currY), size)
        
    if mode=="line":
        prevX=currX
        prevY=currY





    pygame.display.flip()