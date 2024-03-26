import pygame

pygame.init()
x=500
y=400
work=True 
screen=pygame.display.set_mode((1000,700))
clock=pygame.time.Clock()

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            work=False
        if event.type==pygame.KEYDOWN:
            continue
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(250,0,0), (x,y),25)

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_d] and x<980: x+=20
    if pressed[pygame.K_a] and x>20: x-=20
    if pressed[pygame.K_s] and y<680: y +=20
    if pressed[pygame.K_w] and y>20: y-=20
    pygame.display.flip()
    clock.tick(60)