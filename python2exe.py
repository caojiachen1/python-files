from tkinter import *
from tkinter import filedialog
import os
import shutil
from pywinauto.application import Application
import psutil
from pywinauto.keyboard import *
import time

def auto_cmd_type(content):
    global is_open , app
    for i in psutil.process_iter():
        if i.name().lower() in ['cmd.exe' , 'openconsole.exe']:
            os.system('taskkill /F /IM {}'.format(i.name()))
    app = Application().start('wt.exe')
    is_open = False
    while not is_open:
        for i in psutil.process_iter():
            if i.name().lower() == 'cmd.exe':
                is_open = True
        time.sleep(0.1)
    send_keys(content , with_spaces = True , with_newlines = True)

def center_window(root : Tk , width , height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

def select():
    path = filedialog.askopenfilename(initialdir = r'E:/python_files')
    if path == '':
        return
    if not os.path.exists(r'C:\Users\caoji\Desktop\dist'):
        os.makedirs(r'C:\Users\caoji\Desktop\dist')
    path_ = os.path.join(r'C:\Users\caoji\Desktop' , os.path.basename(path))
    shutil.copy(path , path_)
    auto_cmd_type(r'pyinstaller -F -w {} --distpath=C:\Users\caoji\Desktop\dist'.format(path_))
    
root = Tk()
root.title('python打包')
center_window(root , 300 , 150)
root.resizable(False , False)

button = Button(root , text = '浏览' , width = 8 , height = 2 , command = select)
button.place(relx = 0.35 , rely = 0.25)

root.mainloop()