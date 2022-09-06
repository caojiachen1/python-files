import tkinter as tk
from tkinter import filedialog
import os
import tkinter.messagebox as msgbox

def center_window(root : tk.Tk, width, height):
    screenwidth  =  root.winfo_screenwidth()
    screenheight  =  root.winfo_screenheight()
    size  =  '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

root = tk.Tk()
root.title('获取文件地址')
center_window(root , 250 , 150)
path = ''
a = tk.StringVar()
a.set('无文件')

def select():
    global path , a
    path = filedialog.askopenfilename(initialdir = os.getcwd(),filetypes = [('所有文件' , '.*')])
    if path == '':
        return
    root.clipboard_clear()
    root.clipboard_append(path)
    a.set('文件地址：' + path)
    msgbox.showinfo('提示' , '文件地址已经复制到剪切板')

b = tk.Button(root,text = '获取' , command = select , width = 7 , height = 2)
b.place(relx = 0.38 , rely = 0.15)

text = tk.Label(root , textvariable = a , wraplength = 250)
text.place(relx = 0,rely = 0.6)

root.mainloop()