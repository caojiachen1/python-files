import requests
from bs4 import BeautifulSoup as bs
import tkinter
import tkinter.ttk

module_name = ''
links = []
page_num = 0
current_page = 1

def search_page(module , page):
    global searchpage , a , s , links , page_num , u
    links = []
    searchpage = r'https://pypi.org/search/?q={}&page={page}'.format(module , page = page)
    a = requests.get(searchpage)
    s = bs(a.text , 'html.parser')
    for link in s.find_all('a'):
        u = str(link.get('href'))
        if u[:8] == '/project':
            links.append(u[9:-1])
    page_num = str(s.find_all('strong')[0])[8:-9]
    page_num = page_num.replace(',' , '')
    try:
        page_num = int(page_num) // 20 + 1
    except:
        page_num = 500
    return links

def search():
    global module_name , current_page
    current_page = 1
    module_name = str(enter.get())
    if module_name == '':
        listbox_content.set('')
        return
    listbox_content.set(tuple(search_page(module_name , current_page)))
    show_page.set(str(current_page) + '/' + str(page_num))

def next_page():
    global current_page
    if module_name == '' or current_page == page_num:
        return
    current_page = current_page + 1
    listbox_content.set(tuple(search_page(module_name , current_page)))
    show_page.set(str(current_page) + '/' + str(page_num))

def prev_page():
    global current_page
    if module_name == '' or current_page == 1:
        return
    current_page = current_page - 1
    listbox_content.set(tuple(search_page(module_name , current_page)))
    show_page.set(str(current_page) + '/' + str(page_num))

root = tkinter.Tk()
root.geometry('400x550')
root.title('python库查询')
root.resizable(False , False)

listbox_content = tkinter.StringVar()
listbox_content.set('')

show_page = tkinter.StringVar()
show_page.set('0/0')

x = tkinter.Scrollbar(root , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

enter = tkinter.Entry(root , width = 30)
enter.place(relx = 0.1 , rely = 0.05)

prev = tkinter.Button(root , text = '<' , command = prev_page)
prev.pack(side = tkinter.LEFT)

next = tkinter.Button(root , text = '>' , command = next_page)
next.pack(side = tkinter.RIGHT)

button = tkinter.Button(root , text = '搜索' , command = search , height = 1 , width = 4)
button.place(relx = 0.65 , rely = 0.04)

down = tkinter.Button(root , text = '下载' , command = None , height = 1 , width = 4)
down.place(relx = 0.8 , rely = 0.04)

listbox = tkinter.Listbox(root , selectmode = tkinter.SINGLE , width = 100 , height = 25 , xscrollcommand = x.set , listvariable = listbox_content)
listbox.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

show = tkinter.Label(root , textvariable = show_page)
show.place(relx = 0.49 , rely = 0.09)

x.config(command = listbox.xview)

root.mainloop()








