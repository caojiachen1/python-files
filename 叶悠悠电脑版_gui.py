import tkinter
import os
from sys import exit
import uiautomator2 as u2
import time
import re
import tkinter.messagebox as msgbox
#需要手机打开叶悠悠聊天界面，程序自动将输入内容录入聊天框发送，并获取叶悠悠的回复
#如果没有打开聊天界面或者中途退出聊天界面，程序将直接结束，需要重新启动

def enter(event):
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    if s.group(1) != 'baidu.input/com.baidu.input.platochat.impl.activity.chat.ChatActivity':
        msgbox.showerror('错误' , '手机未打开聊天界面!')
        exit()
    send = entry.get()
    mine.set('我发的消息: {}'.format(send))
    d.send_keys(send)
    d(resourceId="com.baidu.input:id/send_btn").click()
    d.set_fastinput_ime(False)
    time.sleep(4)
    respond_text = d(resourceId="com.baidu.input:id/content")[-1].info['text']
    respond.set('叶悠悠回复: {}'.format(respond_text))
    entry.delete(0 , tkinter.END)

def center_window(root : tkinter.Tk, width, height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

os.system('adb devices')
try:
    d = u2.connect()
    d(resourceId="com.baidu.input:id/input_ed").click()
except:
    msgbox.showerror('错误' , '手机未连接!')
    exit()

root = tkinter.Tk()
center_window(root , 260 , 200)
root.title('叶悠悠')
root.bind('<Escape>' , lambda event:exit())

respond = tkinter.StringVar()
respond.set('叶悠悠回复: 无')

mine = tkinter.StringVar()
mine.set('我发的消息: 无')

entry = tkinter.Entry(root)
entry.place(relx = 0.2 , rely = 0.2)
entry.bind('<Return>' , enter)

respond_ = tkinter.Label(root , textvariable = respond , wraplength = 200)
respond_.place(relx = 0.1 , rely = 0.65)

mine_ = tkinter.Label(root , textvariable = mine , wraplength = 200)
mine_.place(relx = 0.1 , rely = 0.4)

root.mainloop()