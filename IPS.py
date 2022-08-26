import pygame
from pygame.locals import *
import pygame.freetype
from sys import exit
import tkinter as tk
from tkinter import filedialog
import os

os.system("cls")
pic_path=''
x,y,nowx,nowy,multiple,fx,fy,zoom_multiple=0,0,0,0,0,0,0,2
up,down,click=False,False,False

def ips():
    global x,y,nowx,nowy,multiple,up,down,click,pic_path,fx,fy
    pygame.init()
    back2=back=pygame.image.load(pic_path)
    myfont=pygame.freetype.Font("C:\\Windows\\Fonts\\msyh.ttc",36)
    size_x,size_y=back.get_width(),back.get_height()
    screen=pygame.display.set_mode((800,600),0,32)
    pygame.display.set_caption("Image transformer (Press ESC to exit)")
    pygame.mouse.set_visible(True)
    while True:
        up,down=False,False
        fx,fy=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    exit()
                if event.key==K_TAB:
                    x,y=0,0
                if event.key==K_q:
                    x,y=0,0
                    back=pygame.image.load(pic_path)
            elif event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
                    xx,yy=pygame.mouse.get_pos()
                    if (xx<x) or (xx>x+back.get_width()) or (yy<y) or (yy>y+back.get_height()):
                        click=False
                if event.button==4:
                    if (back.get_width()<10000) and (back.get_height()<10000):
                        multiple+=1
                        up=True
                        down=False
                elif event.button==5:
                    if (back.get_width()>0) and (back.get_height()>0):
                        multiple-=1
                        down=True
                        up=False
            elif event.type==MOUSEBUTTONUP:
                click=False
        if click:
            nowx,nowy=pygame.mouse.get_pos()
            x+=nowx-fx
            y+=nowy-fy
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
        screen.fill(0)
        screen.blit(back,(x,y))
        myprint=myfont.render_to(screen,(10,10),"Pic path:"+pic_path,fgcolor=(255,255,255),size=20)
        pygame.display.update()

def get():
    s=e1.get()
    global zoom_multiple
    zoom_multiple=float(s)

def select_file():
    filename=filedialog.askopenfilename(title='Select a picture',initialdir='/')
    global pic_path
    pic_path=filename
    ips()

root=tk.Tk()
root.title('图片查看器')
root.resizable(True,True)
root.geometry('300x200')
open_button=tk.Button(root,text='选择图片',command=select_file)
open_button.place(relx=0.4,rely=0.1)
#pic_path=filedialog.askopenfilename()
l1=tk.Label(root,text='缩放倍数')
l1.place(relx=0.05,rely=0.5)
e1=tk.Entry(root,bd=5)
e1.place(relx=0.25,rely=0.5)
enterbutton=tk.Button(root,text='确定',command=get)
enterbutton.place(relx=0.8,rely=0.5)
root.mainloop()