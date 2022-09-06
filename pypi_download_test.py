import requests
import re
from bs4 import BeautifulSoup as bs
import tkinter
import tkinter.messagebox as msgbox
import os

module_name = 'numpy'
d , links , names = {} , [] , []

def download():
    global parent , n , download_link , path
    parent = ''
    try:
        n = listbox.get(listbox.curselection())
    except:
        return
    try:
        download_link = d[n]
        path = os.path.join(r'C:\Users\caoji\Downloads' , n)
        with open(path , mode = 'wb') as f:
            a = requests.get(download_link)
            f.write(a.content)
        msgbox.showinfo('提示' , '下载成功')
        parent = os.path.split(path)[0]
        os.startfile(parent)
    except:
        msgbox.showerror('提示' , '下载失败')
        return

def center_window(root : tkinter.Tk, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

win = tkinter.Tk()
center_window(win , 600 , 600)
win.title('查看')
win.resizable(False , False)

content = tkinter.StringVar()
content.set(' ')

y = tkinter.Scrollbar(win , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)

x = tkinter.Scrollbar(win , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

listbox = tkinter.Listbox(win , selectmode = tkinter.SINGLE , yscrollcommand = y.set , xscrollcommand = x.set , listvariable = content , width = 100 , height = 25)
listbox.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

down = tkinter.Button(win , text = '下载' , command = download , height = 1 , width = 4)
down.place(relx = 0.7 , rely = 0.07)

y.config(command = listbox.yview)
x.config(command = listbox.xview)

url = r'https://pypi.org/project/{}/#files'.format(module_name)
a = requests.get(url)
s = bs(a.text , 'html.parser')
for link in s.find_all('a'):
    u = str(link.get('href'))
    if u[:13] == 'https://files':
        links.append(u)
        k = re.search(r'{}(.*)'.format(module_name) , u , re.IGNORECASE)
        names.append(module_name + str(k.group(1)))
        d[module_name + str(k.group(1))] = u
content.set(tuple(names))

win.mainloop()