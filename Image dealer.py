import pygame,os
from pygame.locals import *
from sys import exit
pygame.init()
os.system("cls")
dis=pygame.display.Info()
size=width,height=int(dis.current_w/2),int(dis.current_h/2)
screen=pygame.display.set_mode(size,0,32)
pygame.display.set_caption("Test Program")
click=False
GOLD=255,215,0
selected=False
color=0,0,0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==3:
                click=True
                cursorx,cursory=pygame.mouse.get_pos()
        elif event.type==pygame.MOUSEBUTTONUP:
            click=False
            selected=True
    if not selected:
        screen.fill(0)
    if click==True:
        x,y=pygame.mouse.get_pos()
        rect=pygame.draw.rect(screen,(255,255,255),(cursorx,cursory,x-cursorx,y-cursory),2)
    pygame.display.update()

