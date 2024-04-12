import pygame 
import sys
import time
import random
from color_palette import *
pygame.init()


work=True


HEIGHT=630
WIDTH=630

def draw_grid():
    for i in range(HEIGHT//2):
        for j in range(WIDTH//2):
            pygame.draw.rect(screen,colorGRAY,(i*CELL,j*CELL,CELL,CELL),1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


screen=pygame.display.set_mode((WIDTH,HEIGHT))
overScreen=pygame.Surface((WIDTH,HEIGHT))

font = pygame.font.SysFont("Verdana", 60)


CELL=30

class Food:
    def __init__(self) -> None:
        self.pos=Point(random.randint(0,WIDTH//CELL),random.randint(0,HEIGHT//CELL))

    def draw(self):
        pygame.draw.rect(screen,colorGREEN,(self.pos.x*CELL,self.pos.y*CELL,CELL,CELL))

    def place_food(self):
        self.pos=Point(random.randint(0,WIDTH//CELL-1),random.randint(0,HEIGHT//CELL-1))

class Point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return f"{self.x},{self.y}"


class Snake:
    def __init__(self):
        self.body=[Point(10,11),Point(10,12),Point(10,13)]
        self.dx=1
        self.dy=0

    def move(self):
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x=self.body[i-1].x
            self.body[i].y=self.body[i-1].y
        if self.body[0].x>HEIGHT//CELL-1:
            self.body[0].x=0
        elif self.body[0].y>WIDTH//CELL-1:
            self.body[0].y=0
        elif self.body[0].x<0:
            self.body[0].x=HEIGHT//CELL-1
        elif self.body[0].y<0:
            self.body[0].y=WIDTH//CELL-1   
        else:
            self.body[0].x+=self.dx
            self.body[0].y+=self.dy
        print(self.body[0].x,self.body[0].y)



    def crush(self):
        for i in range(1,len(self.body)):
            if self.body[0].x==self.body[i].x and self.body[0].y==self.body[i].y:
                pygame.draw.rect(screen,colorRED,(0,0,WIDTH,HEIGHT))
                return True
                

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    
    def check_colision(self,food):
        head=self.body[0]
        tail=self.body[len(self.body)-1]
        if head.x==food.pos.x and head.y==food.pos.y:
            self.body.append(Point(tail.x,tail.y))
            return True
        return False
direction="Right"    
food=Food()
snake=Snake()
clock=pygame.time.Clock()
FPS=5

while work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction!="Left":
                snake.dx = 1
                snake.dy = 0
                direction="Right"
            if event.key == pygame.K_LEFT and direction !="Right":
                snake.dx = -1
                snake.dy = 0
                direction="Left"
            if event.key == pygame.K_UP and direction!="Down":
                snake.dx = 0
                snake.dy = -1
                direction="Up"
            if event.key == pygame.K_DOWN and direction!="Up":
                snake.dx = 0
                snake.dy = 1
                direction="Down"
    draw_grid_chess()
    if snake.crush():
        game_over = font.render("Game Over", True, colorBLACK)
        screen.blit(game_over, (30,250))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    snake.move()
    snake.draw()
    food.draw()


    if snake.check_colision(food):
        print("Got food!")
        food.place_food()
    
    pygame.display.flip()
    clock.tick(FPS)