import tkinter
import tkinter.messagebox as msgbox
import requests
from bs4 import BeautifulSoup as bs
import re
import os

def get_download_url(module_name):
    if module_name == '':
        return {}
    global url , a , soup , l , links , name_list , d , results , u , name
    url = 'https://pypi.tuna.tsinghua.edu.cn/simple/{}/'.format(module_name)
    a = requests.get(url)
    soup = bs(a.text , 'html.parser')
    l , links , name_list , d = [] , [] , [] , {}
    for link in soup.find_all('a'):
        l.append(link.get('href'))
    for u in l:
        u = str('https://pypi.tuna.tsinghua.edu.cn' + u[5:])
        links.append(u)
        results = re.search(r'{}(.*?)#sha256='.format(module_name) , str(u) , re.IGNORECASE)
        name = module_name + results.group(1)
        name_list.append(name)
    for i in range(name_list.__len__()):
        d[name_list[i]] = links[i]
    return d

def search():
    global module , listbox_content
    module = str(input_module.get())
    listbox_content.set(tuple(get_download_url(module).keys()))

def download():
    global parent
    try:
        n = listbox.get(listbox.curselection())
    except:
        return
    try:
        download_link = get_download_url(module)[n]
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

module = ''

root = tkinter.Tk()
root.title('python模块下载')
root.geometry('780x600')
root.resizable(False , False)

listbox_content = tkinter.StringVar()
listbox_content.set('')

y = tkinter.Scrollbar(root , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)
x = tkinter.Scrollbar(root , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)
listbox = tkinter.Listbox(root , selectmode = tkinter.SINGLE , width = 100 , height = 25 , yscrollcommand = y.set , xscrollcommand = x.set , listvariable = listbox_content)
listbox.pack(side = tkinter.BOTTOM , ipady = 10 , fill = tkinter.Y)
button = tkinter.Button(root , text = '搜索' , command = search , height = 1 , width = 4)
button.place(relx = 0.6 , rely = 0.07)
down = tkinter.Button(root , text = '下载' , command = download , height = 1 , width = 4)
down.place(relx = 0.7 , rely = 0.07)
input_module = tkinter.Entry(root , width = 30)
input_module.place(relx = 0.25 , rely = 0.08)
label = tkinter.Label(root , text = '模块名:')
label.place(relx = 0.18 , rely = 0.08)
y.config(command = listbox.yview)
x.config(command = listbox.xview)
root.mainloop()