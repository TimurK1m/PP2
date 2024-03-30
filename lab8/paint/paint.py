import pygame 


pygame.init()



WIDTH=800
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))


red=(255,0,0)
blue=(0,255,0)
white=(255,255,255)
black=(0,0,0)

work=True

clock=pygame.time.Clock()

LMBpressed=False

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            work=False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            print("lbm")
            LMBpressed=True
        if event.type==pygame.MOUSEMOTION:
            print(event.pos)
            if LMBpressed:
                pygame.draw.rect(screen,red,(event.pos[0],event.pos[1],1,1))
        if event.type==pygame.MOUSEBUTTONUP and event.button==1:
            print("no lmb")
            LMBpressed=False
    





    pygame.display.flip()
    clock.tick(60)