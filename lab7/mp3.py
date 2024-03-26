import pygame
import os 

pygame.init()
screen=pygame.display.set_mode((300,300))
list=[]
num=0
stop=False
work=True 
work2=True
dir=os.listdir(r"lab7\music")
for i in dir:
    list.append(i)

    

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            work=False
    pygame.mixer.music.load(f"lab7\\music\\{list[num]}")
    pygame.mixer.music.play()
    work2=True
    while work2:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                work2=False
                work=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    work=False
                    work2=False
                if event.key==pygame.K_d:
                    if num==len(list)-1:
                        num=0
                    else:
                        num+=1
                if event.key==pygame.K_a:
                    if num==0:
                        num=len(list)-1
                    else:
                        num-=1  
                if event.key==pygame.K_SPACE:
                    stop=not stop
                    if stop==True:
                        pygame.mixer.music.pause()
                    elif stop==False:
                        pygame.mixer.music.unpause()
                if not  stop:
                    work2=False

    