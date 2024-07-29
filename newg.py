import pygame
import random

pygame.init()
path=('C:/Users/admin/Desktop/New folder/')
screen=pygame.display.set_mode((800,700))

pygame.display.set_caption(path+'typing game')
icon=pygame.image.load(path+'001-alien.png')
pygame.display.set_icon(icon)

bg=pygame.image.load(path+'back.png')

user=pygame.image.load(path+'001-rocket.png')
X=360
Y=600

bullet=pygame.image.load(path+'b1.png')
bx=X+15##############################
by=Y

alien1=pygame.image.load(path+'001-space-ship-2.png')
alien2=pygame.image.load(path+'002-space-ship.png')
alien3=pygame.image.load(path+'003-space-ship-1.png')

def play(x,y):
    screen.blit(user,(x,y))

def shoot(x,y):
    screen.blit(bullet,(x,y))

def comp1(x,y):
    screen.blit(alien1,(x,y))

def comp2(x,y):
    screen.blit(alien2,(x,y))

def comp3(x,y):
    screen.blit(alien3,(x,y))

d1=1
cx1=random.randint(0,740)
cy1=random.randint(0,30)
d2=1
cx2=random.randint(0,740)
cy2=random.randint(0,30)
d3=1
cx3=random.randint(0,740)
cy3=random.randint(0,30)
a=[]
b=[]
v2=0
v=True
while v:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X=X-20
                if X < 0:
                    X=800
                    
            if event.key == pygame.K_RIGHT:
                X=X+20
                if X >800:
                    X=0
                
            if event.key == pygame.K_UP:
                Y=Y-20
                if Y < 550:
                    Y=550

            if event.key == pygame.K_DOWN:
                Y=Y+20
                if Y > 630:
                    Y=630

            if event.key == pygame.K_s:
                a.append(X)
                #print(a)
                #print(a[0])
                a=a[:1]
                b.append(Y)
                #print(b)
                #print(b[0])
                b=b[:1]

                bx=a[0]
                by=b[0]

            by=by-0.001
            if by<(-28):
                b.clear()
                a.clear()
                bx=X+15
                by=Y
                break
                
    screen.blit(bg,(0,0))
    shoot(bx,by)
    play(X,Y)

    cx1=(cx1+0.1*d1)
    if cx1 > 740:
        d1=(-1)
        cy1=cy1+10
    if cx1<0:
        d1=(1)
        cy1=cy1+10
    comp1(cx1,cy1)

    cx2=(cx2+0.08*d2)
    if cx2 > 740:
        d2=(-1)
        cy2=cy2+20
    if cx2<0:
        d2=(1)
        cy2=cy2+20
    comp2(cx2,cy2)

    cx3=(cx3+0.05*d3)
    if cx3 > 740:
        d3=(-1)
        cy3=cy3+30
    if cx3<0:
        d3=(1)
        cy3=cy3+30
    comp3(cx3,cy3)

    pygame.display.update()
