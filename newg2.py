import pygame
import random

pygame.init()

screen=pygame.display.set_mode((1000,800))

pygame.display.set_caption('typing game')
icon=pygame.image.load('001-keyboard.png')
pygame.display.set_icon(icon)

path=('C:/Users/admin/Desktop/alphabet/')
a=pygame.image.load(path+'a.png')
b=pygame.image.load(path+'b.png')
c=pygame.image.load(path+'c.png')
d=pygame.image.load(path+'d.png')
e=pygame.image.load(path+'e.png')

def l1(x,y):
    screen.blit(a,(x,y))
def l2(x,y):
    screen.blit(b,(x,y))
def l3(x,y):
    screen.blit(c,(x,y))
def l4(x,y):
    screen.blit(d,(x,y))
def l5(x,y):
    screen.blit(e,(x,y))

l1x=random.randint(10,930)
l1y=730
l1d=random.choice([0.1,0.3,0.5,0.7,0.9])
l2x=random.randint(10,930)
l2y=730
l2d=random.choice([0.1,0.3,0.5,0.7,0.9])
l3x=random.randint(10,930)
l3y=730
l3d=random.choice([0.1,0.3,0.5,0.7,0.9])
l4x=random.randint(10,930)
l4y=730
l4d=random.choice([0.1,0.3,0.5,0.7,0.9])
l5x=random.randint(10,930)
l5y=730
l5d=random.choice([0.1,0.3,0.5,0.7,0.9])

v=True
while v:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v=False
    
    screen.fill((255,220,200))
    l1y=l1y-l1d
    l1(l1x,l1y)
    l2y=l2y-l2d
    l2(l2x,l2y)
    l3y=l3y-l3d
    l3(l3x,l3y)
    l4y=l4y-l4d
    l4(l4x,l4y)
    l5y=l5y-l5d
    l5(l5x,l5y)
    
    pygame.display.update()
