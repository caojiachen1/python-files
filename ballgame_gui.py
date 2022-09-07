import pygame
from pygame.locals import *
import pygame.freetype
import tkinter as tk
import tkinter.messagebox as msgbox

already , shown = False  , False
size = width , height = 400  , 300
speed = [1 , 1]
GOLD = 255 , 215 , 0
plat_length , spline_width , fps , score , difficulty , maxscore , time , screen = 100 , 10 , 5 , 0 , 1  , -1 , 0 , 0

ball = pygame.image.load("D:\\ball.gif")
ball = pygame.transform.scale(ball , (50 , 50))
ballrect = ball.get_rect()

def initpygame():
    global screen , already , fonts
    already = True

    pygame.init()
    fonts = pygame.freetype.Font("C:\\windows\\fonts\\msyh.ttc" , 36)
    screen = pygame.display.set_mode(size , 0 , 32)
    pygame.display.set_caption('弹球小游戏')
    pygame.mouse.set_visible(True)
    pygame.display.set_icon(ball)

def change(value):
    global difficulty , fps , lose , plat_length
    difficulty = int(value)
    fps = 6 - difficulty
    plat_length = 110 - difficulty * 10

def quitpygame():
    global already
    already = False
    pygame.quit()

lose , begin = False , False

def game():
    global fontrect , fontrect2 , fontrect3 , cursorx , cursory , lose , ballrect , score , fps , maxscore , shown , show_max_score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitpygame()
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitpygame()
                return
    ballrect = ballrect.move(speed[0] , speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    if ballrect.bottom > height:
        cursorx , cursory = pygame.mouse.get_pos()
        if ballrect.right > int(cursorx-plat_length/2) and ballrect.left < int(cursorx + plat_length/2):
            speed[1] = -speed[1]
            if not lose:
                score = score + difficulty
        else:
            lose = True
    screen.fill(0)
    screen.blit(ball , (ballrect.left , ballrect.top))
    cursorx , cursory = pygame.mouse.get_pos()
    scoreset = "你的成绩: " + str(score)
    fontrect3 = fonts.render_to(screen , (10 , 10) , scoreset , fgcolor = GOLD , size = 20)
    pygame.draw.line(screen , GOLD , (int(cursorx-plat_length/2) , height) , (int(cursorx + plat_length/2) , height) , spline_width)
    if lose:
        screen.fill(0)
        fontrect = fonts.render_to(screen , (int(width/2-120) , int(height/2-50)) , "你输了！" , fgcolor = GOLD , size = 50)
        fontrect2 = fonts.render_to(screen , (int(width/2-120) , int(height/2-100))  , "成绩：" + str(score)  , fgcolor = GOLD  , size = 30)
        if score>maxscore and not shown:
            if maxscore != -1:
                msgbox.showinfo('新高分'  , '恭喜您获得了新的最高分！')
            maxscore = score
            show_max_score.set('最高分:' + str(maxscore))
            shown = True
    pygame.display.update()
    root.after(fps , game)

def game_main():
    global lose , score , ballrect , shown
    shown , lose = False , False
    ballrect.left , ballrect.top , score = 0 , 0 , 0
    initpygame()
    game()

def center_window(root : tk.Tk , width , height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

root = tk.Tk()
center_window(root , 300 , 200)
root.title('弹球小游戏')
root.resizable(False , False)

show_max_score = tk.StringVar()
show_max_score.set('最高分:无最高分')

difficulty_scale = tk.Scale(root , from_ = 1 , to = 4 , resolution = 1 , orient = tk.HORIZONTAL , command = change , label = '难度' , length = 200)
difficulty_scale.place(relx = 0.175 , rely = 0.15)

start = tk.Button(root , text = '开始游戏' , command = game_main , width = 8 , height = 1)
start.place(relx = 0.4 , rely = 0.65)

max = tk.Label(root , textvariable = show_max_score)
max.place(relx = 0.35 , rely = 0.1)

root.mainloop()
