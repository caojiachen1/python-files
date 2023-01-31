import pygame
from pygame.locals import *
from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox as msgbox
import os

pic_path , time , xx , yy , x , y , screen , zoom , already , drawn , click , up , down , multiple , zoom_multiple = '' , 0 , 0 , 0 , 0 , 0 , 0 , 1 , False , False , False , False , False , 0 , 1.2
pos_x , pos_y = 0 , 0
fx , fy = 0 , 0
update_back3 = True

#back2是马赛克之后的图层
#back是原图层
#back3是缩放的图层

def ask():
    try:
        global pic_path , x , y , back , back2 , back3 , path , resolution
        if already:
            msgbox.showerror('错误' , '请先关闭已打开的图片窗口！')
            return
        a = filedialog.askopenfilename(title = "选择一张图片" , initialdir = os.getcwd() , filetypes = [('图片' , '*.jpg *.png')])
        if a == '':
            return
        pic_path = a
        back = pygame.image.load(pic_path)
        back2 = pygame.transform.scale(back , (int(x/zoom) , int(y/zoom)))
        back2 = pygame.transform.scale(back2 , (x , y))
        back3 = back2
        x = back.get_width()
        y = back.get_height()
        resolution.set(f' 图片分辨率：{str(x)}x{str(y)}')
        path.set(f'图片地址：{pic_path}')
    except Exception:
        return

def initpygame():
    pygame.init()
    global screen , already
    screen = pygame.display.set_mode((800 , 600) , 0 , 32)
    pygame.display.set_caption("马赛克工具")
    pygame.mouse.set_visible(True)
    already = True

def quitpygame():
    global already
    already = False
    pygame.quit()

def start():  # sourcery skip: low-code-quality
    while True:
        if pic_path == '':
            return
        global back , back2 , back3 , drawn , time , pos_x , pos_y , click , xx , yy , up , down , multiple , update_back3 , fx , fy
        time = 1
        up , down = False , False
        if not already:
            initpygame()
        fx , fy = pygame.mouse.get_pos()
        back2 = pygame.transform.scale(back , (int(x / zoom) , int(y / zoom)))
        back2 = pygame.transform.scale(back2 , (x , y))#及时更新马赛克图层
        if update_back3:
            back3 = back2
        for event in pygame.event.get():
            if event.type == QUIT:
                quitpygame()
                drawn = False
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quitpygame()
                    drawn = False
                    return
                if event.key == K_TAB:
                    pos_x , pos_y = 0 , 0
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    xx , yy = pygame.mouse.get_pos()
                    if (xx < pos_x) or (xx > pos_x + back3.get_width()) or (yy < pos_y) or (yy > pos_y + back3.get_height()):
                        click = False
                elif event.button == 4:
                    if (back3.get_width() < 10000) and (back3.get_height() < 10000):
                        multiple += 1
                        up = True
                        down = False
                elif event.button == 5:
                    if (back3.get_width() > 0) and (back3.get_height() > 0):
                        multiple -= 1
                        down = True
                        up = False
            elif event.type == MOUSEBUTTONUP:
                click = False
        if click:
            nowx , nowy = pygame.mouse.get_pos()
            pos_x += nowx - fx
            pos_y += nowy - fy
        if up == True:
            back3 = pygame.transform.scale(back2 , (int(back2.get_width()*(zoom_multiple**multiple)) , int(back2.get_height()*(zoom_multiple**multiple))))
            nowx , nowy = pygame.mouse.get_pos()
            pos_x -= int((nowx-pos_x)*(zoom_multiple-1))
            pos_y -= int((nowy-pos_y)*(zoom_multiple-1))
            update_back3 = False
        if down == True:
            back3 = pygame.transform.scale(back2 , (int(back2.get_width()*(zoom_multiple**multiple)) , int(back2.get_height()*(zoom_multiple**multiple))))
            nowx , nowy = pygame.mouse.get_pos()
            pos_x += int((nowx-pos_x)*(1-1/zoom_multiple))
            pos_y += int((nowy-pos_y)*(1-1/zoom_multiple))
            update_back3 = False
        screen.fill(0)
        screen.blit(back3 , (pos_x , pos_y))
        drawn = True
        pygame.display.update()

def change(value):
    global zoom , update_back3 , time
    zoom = float(value)
    update_back3 = True
    time = 0

def save():
    global enter
    enter = True
    if already:
        msgbox.showerror('错误' , '请先关闭已打开的图片窗口！')
        return
    if pic_path == '':
        msgbox.showerror('错误提示' , '你还没有打开一个图片')
        return
    elif time == 0:
        msgbox.showerror('错误提示' , '请点击开始按钮初始化')
        return
    path = filedialog.asksaveasfilename(initialdir = os.getcwd() , filetypes = [('图片','.jpg')] , defaultextension = "jpg")
    if path == "":
        return
    pygame.image.save(back2 , path)

def center_window(root : tk.Tk , width , height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

root = tk.Tk()
root.title('马赛克工具')
center_window(root , 300 , 300)
root.resizable(False , False)
em = tk.Frame(root).pack()
asks = tk.Button(em , text = '浏览' , width = 6 , height = 1 , command = ask)
asks.place(relx = 0.1 , rely = 0.33)
draw = tk.Button(em , text = '开始' , width = 6 , height = 1 , command = start)
draw.place(relx = 0.4 , rely = 0.33)
saves = tk.Button(root , text = '保存' , width = 6 , height = 1 , command = save)
saves.place(relx = 0.7 , rely = 0.33)
s = tk.Scale(root , from_ = 1 , to = 20 , resolution = 1 , orient = tk.HORIZONTAL , length = 200 , label = '模糊程度' , command = change)
s.place(relx = 0.16 , rely = 0.05)
path = tk.StringVar()
resolution = tk.StringVar()
path.set('图片地址：暂无图片')
resolution.set('图片分辨率：暂无图片')
t1 = tk.Label(root , textvariable = path , wraplength = 300)
t1.place(relx = 0 , rely = 0.6)
t2 = tk.Label(root , textvariable = resolution)
t2.place(relx = 0 , rely = 0.8)

root.after(0 , start)
root.mainloop()