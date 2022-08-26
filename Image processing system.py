import pygame
from pygame.locals import *
import pygame.freetype
from sys import exit
import tkinter as tk
import os
from tkinter import filedialog
pygame.init()
i=os.system("cls")
print("Welcome to image processing system")
print("You can load a picture from your system")
print("You can drag it or scale it")
print("Press TAB to move the picture to (0,0)")
print("Press Q to reload the picture")
pic_path=filedialog.askopenfilename()
zoom_multiple=float(input("Input scale mutiple:"))
# pic_path="D:\\beauty2.jpg"
myfont=pygame.freetype.Font("C:\\Windows\\Fonts\\msyh.ttc",36)
back2=back=pygame.image.load(pic_path)
size_x,size_y=back.get_width(),back.get_height()
screen=pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Image transformer (Press ESC to exit)")
# back=pygame.image.load('D:\\beauty.jpg')
# cursor=pygame.image.load('D:\\icon.jpg')
# cursor=pygame.transform.scale(cursor,(25,25))
# pygame.mouse.set_visible(False)
x,y,nowx,nowy,multiple=0,0,0,0,0
up,down,click=False,False,False
# zoom_multiple=float(input("Input scale mutiple:"))
# zoom_multiple=2
while True:
    up,down=False,False
    fx,fy=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit()
            if event.key==pygame.K_TAB:
                x,y=0,0
            if event.key==pygame.K_q:
                x,y=0,0
                back=pygame.image.load(pic_path)
            if event.key==pygame.K_r:
                pic_path=input("Reload another picture path:")
                back=pygame.image.load(pic_path)
                back2=back
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                click=True
                xx,yy=pygame.mouse.get_pos()
                if (xx<x) or (xx>x+back.get_width()) or (yy<y) or (yy>y+back.get_height()):
                    click=False
            if event.button==4:
                if (back.get_width()<5000) and (back.get_height()<5000):
                    multiple+=1
                    up=True
                    down=False
            elif event.button==5:
                if (back.get_width()>0) and (back.get_height()>0):
                    multiple-=1
                    down=True
                    up=False
        elif event.type==pygame.MOUSEBUTTONUP:
            click=False
    if click:
        nowx,nowy=pygame.mouse.get_pos()
        x+=nowx-fx
        y+=nowy-fy
        # print(x,y)
    if up==True:
        back=pygame.transform.scale(back2,(int(back2.get_width()*(zoom_multiple**multiple)),int(back2.get_height()*(zoom_multiple**multiple))))
        nowx,nowy=pygame.mouse.get_pos()
        x-=int((nowx-x)*(zoom_multiple-1))
        y-=int((nowy-y)*(zoom_multiple-1))
    if down==True:
        back=pygame.transform.scale(back2,(int(back2.get_width()*(zoom_multiple**multiple)),int(back2.get_height()*(zoom_multiple**multiple))))
        nowx,nowy=pygame.mouse.get_pos()
        x+=int((nowx-x)*(1-1/zoom_multiple))
        y+=int((nowy-y)*(1-1/zoom_multiple))
    # print(back.get_width())
    screen.fill(0)
    screen.blit(back,(x,y))
    # screen.blit(cursor,pygame.mouse.get_pos())
    myprint=myfont.render_to(screen,(10,10),"Pic path:"+pic_path,fgcolor=(255,255,255),size=20)
    pygame.display.update()