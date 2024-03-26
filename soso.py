import pygame

pygame.init()

black=(0,0,0)
col=(100,132,50)
screen=pygame.display.set_mode((700,600))
is_green=True
sur=pygame.Surface((100,100))
im=pygame.transform.scale(pygame.image.load("84-846128_football-clip-art-soccer-ball-clipart-png-transparent.png"),(100,100))
sur.blit(im,(0,0))
work = True 
x=30
yg=0
y=30
xx=50
yy=50
clock=pygame.time.Clock()


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            work=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_green=not is_green
    
    screen.fill(black)
    screen.blit(sur,(100,100))
    screen.blit(rot_center(im,yg,100,100)[0],rot_center(im,yg,100,100)[1])
    

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y-=3
    if pressed[pygame.K_DOWN]:y+=3
    if pressed[pygame.K_RIGHT]:x+=3
    if pressed[pygame.K_LEFT]:x-=3
    if pressed[pygame.K_r]:yg+=1

    if is_green:
        col=(100,132,50)
    else:
        col=(255,128,0)
    
    cub=pygame.draw.rect(screen,col,pygame.Rect(x,y,60,60))
    
    pygame.display.flip()
    clock.tick(60)