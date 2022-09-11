import os
import tkinter
import time
import tkinter.messagebox as msgbox

stop = False

def type_keys(text):
    text = text.replace(' ' , r'\ ')
    os.system('adb shell input text {}'.format(text))

def swipe(x1 , y1 , x2 , y2):
    os.system('adb shell input swipe {} {} {} {}'.format(str(x1) , str(y1) , str(x2) , str(y2)))

def start():
    global i , get_time
    if time_get.get() == '':
        return
    get_time = int(time_get.get())
    for i in range(get_time // 5 + 1):
        os.system('adb shell input swipe 540 1500 540 800')
        time.sleep(5)
    msgbox.showinfo('结束' , '{}秒自动刷短视频结束！'.format(get_time))

def center_window(root : tkinter.Tk, width, height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

root = tkinter.Tk()
center_window(root , 300 , 150)
root.title('自动刷短视频工具')

time_get = tkinter.Entry(root , width = 15)
time_get.place(relx = 0.25 , rely = 0.2)

text = tkinter.Label(root , text = '秒钟自动刷')
text.place(relx = 0.6 , rely = 0.2)

starting = tkinter.Button(root , text = '开始' , command = start , width = 8 , height = 2)
starting.place(relx = 0.4 , rely = 0.5)

root.mainloop()

