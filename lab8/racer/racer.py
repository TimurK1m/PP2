import pygame
import random
import sys
import time
pygame.init()

WIDTH=400
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

coin=pygame.transform.scale(pygame.image.load(f"lab8\\racer\\data\\coin.png"),(40,40))


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBLACK)



BACKGROUND=pygame.image.load("lab8\\racer\\data\\AnimatedStreet.png")


INC_SPED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPED,1000)


clock=pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("lab8\\racer\\data\\Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH//2,HEIGHT-55)

    def move(self):
        pressed=pygame.key.get_pressed()
        if pressed [pygame.K_LEFT] and self.rect[0]>0:
            self.rect.move_ip(-5,0)
        if pressed [pygame.K_RIGHT] and self.rect[0] + self.rect[2]< WIDTH:
            self.rect.move_ip(5,0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image=pygame.image.load(f"lab8\\racer\\data\\Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(self.rect[2]//2,WIDTH - self.rect[2]//2),35)

    def move(self):
        if self.rect[1]+self.rect[3]<HEIGHT:
            self.rect.move_ip(0,SPEED)
        else:
            self.rect.center=(random.randint(self.rect[2]//2 , WIDTH- self.rect[2]//2 ),35)

class Coin(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image=coin
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(self.rect[2]//2,WIDTH - self.rect[2]//2),35)

    def move(self):
        if self.rect[1]+self.rect[3]<HEIGHT:
            self.rect.move_ip(0,SPEED)
        else:
            self.rect.center=(random.randint(self.rect[2]//2 , WIDTH- self.rect[2]//2 ),35)

    def place_coin(self):
        self.rect.center=(random.randint(self.rect[2]//2,WIDTH - self.rect[2]//2),35)

SPEED=5
SCORE=0


enemies=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
coins=pygame.sprite.Group()

P1=Player()
E1=Enemy()

C1=Coin()
C2=Coin()
C3=Coin()
C4=Coin()

enemies.add(E1)
all_sprites.add(C1,E1,P1)
coins.add(C1)


FPS=60
work=True

while work:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            work=False

    screen.blit(BACKGROUND,(0,0))

    scores = font_small.render(str(SCORE), True, colorBLACK)
    screen.blit(scores, (10,10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image,entity.rect)


    if pygame.sprite.spritecollideany(P1,coins):
        SCORE+=1
        C1.place_coin()


    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound('lab8\\racer\\data\\crush.wav').play()

        screen.fill(colorRED)
        screen.blit(game_over, (30,250))
        pygame.display.flip()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()


    pygame.display.flip()
    clock.tick(FPS)