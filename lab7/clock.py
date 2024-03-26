import pygame 
import datetime

pygame.init()


angle=0
clock=pygame.time.Clock()
work=True 
screen=pygame.display.set_mode((1400,800))
screen.fill((250,250,250))
time1=pygame.Surface((700,525))
time2=pygame.Surface((700,525))
time2.fill((30,50,70))
black=(0,0,0)
img=pygame.transform.scale(pygame.image.load(r"lab7\jped\mickeyclock.jpeg"),(700,525))
img2=pygame.transform.scale_by(pygame.image.load(r"lab7\jped\pngwing.com.png"),(0.25,0.25))
time1.blit(img,(0,0))
time2.blit(img,(0,0))


def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect




while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            work=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            angle-=1
            break
    
    screen.fill((0,0,0))
 
    
    screen.blit(time1,(0,0))
    time1.blit(img,(0,0))
    screen.blit(time2,(700,0))
    time2.blit(img,(0,0))
    
    now=datetime.datetime.now()
    curs=now.strftime("%S")
    surm=now.strftime("%M")
    pygame.time.wait(1000)

    time1.blit(rot_center(img2,-(int(curs)*2),700//2,525//2)[0],rot_center(img2,-(int(curs)*2),700//2,525//2)[1])
    time2.blit(rot_center(img2,-(int(surm)*2),700//2,525//2)[0],rot_center(img2,-(int(surm)*2),700//2,525//2)[1])
    

    pygame.display.flip()
    clock.tick(60)