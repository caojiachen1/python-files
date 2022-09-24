import uiautomator2 as u2
import time
import tkinter
import tkinter.messagebox as msgbox
import os , sys

i , j , on , visited = 0 , 0 , True , []

try:
    os.system('adb devices')
    d = u2.connect()
except:
    msgbox.showerror('错误' , '手机未连接!')
    sys.exit()

def auto():
    global on , i , j , visited
    d.app_stop('com.xiaomi.vipaccount')
    d.app_start('com.xiaomi.vipaccount')
    while on:
        d.swipe(540 , 1400 , 540 , 600)
        if d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).exists and d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).info['bounds']['bottom'] <= 2000 and i <= 3:
            d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).click()
            i += 1
        if d(resourceId="com.xiaomi.vipaccount:id/textpart").exists and d(resourceId="com.xiaomi.vipaccount:id/textpart").info['bounds']['bottom'] <= 2000 and j <= 3:
            if d(resourceId="com.xiaomi.vipaccount:id/textpart").info['text'] not in visited:
                visited.append(d(resourceId="com.xiaomi.vipaccount:id/textpart").info['text'])
                d(resourceId="com.xiaomi.vipaccount:id/textpart").click()
                time.sleep(6)
                d.swipe(540 , 1700 , 540 , 1300)
                time.sleep(5)
                d(text = "后退").click()
                j += 1
        on = (i <= 3) or (j <= 3)

def check_in():
    d.app_stop('com.xiaomi.vipaccount')
    d.app_start('com.xiaomi.vipaccount')
    time.sleep(1)
    d(resourceId="com.xiaomi.vipaccount:id/iv3").click()
    time.sleep(2)
    try:
        d(text="立即签到").click()
    except:
        msgbox.showerror('错误' , '已经签到!')
        return
    d(text="backIcon").click()

def center_window(root : tkinter.Tk , width , height):
    s_width , s_height = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (s_width - width) / 2 , (s_height - height) / 2)
    root.geometry(size)

win = tkinter.Tk()
center_window(win , 240 , 150)
win.resizable(False , False)
win.title('小米社区')

run = tkinter.Button(win , text = '开始' , command = auto , height = 1 , width = 5).place(relx = 0.4 , rely = 0.24)
auto_check_in = tkinter.Button(win , text = '签到' , command = check_in , height = 1 , width = 5).place(relx = 0.4 , rely = 0.55)

win.mainloop()
