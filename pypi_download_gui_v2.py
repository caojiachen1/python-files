import requests , tkinter , tkinter.ttk , psutil , time
from bs4 import BeautifulSoup as bs
from pywinauto.application import Application
from pywinauto.keyboard import *
import tkinter.messagebox as msgbox

module_name ,current_module , command = '' , '' , ''
page_num , current_page = 0 , 1
links , names , versions , description , info = [] , [] , [] , [] , []
dict_all = {}

def search_page(module , page):
    global searchpage , a , s , links , page_num , i , names , versions , dict_all
    links , names , versions , description , dict_all = [] , [] , [] , [] , {}
    searchpage = r'https://pypi.org/search/?q={}&page={page}'.format(module , page = page)
    a = requests.get(searchpage)
    s = bs(a.text , 'html.parser')
    for link in s.find_all('a' , class_ = 'package-snippet'):
        links.append(r'https://pypi.org' + str(link['href']))
        s_ = bs(str(link) , 'html.parser')
        for link_ in s_.find_all('span'):
            if link_['class'] == ['package-snippet__name']:
                names.append(link_.string)
            if link_['class'] == ['package-snippet__version']:
                versions.append(link_.string)
        if link.p.string == '':
            description.append('None')
        else:
            description.append(link.p.string)
        # u = str(link.get('href'))
        # if u[:8] == '/project':
        #     links.append(u[9:-1])
    # with open('url.txt' , mode = 'w') as f:
    #     for i in range(names.__len__()):
    #         f.write('{}\n{}\n{}\n{}\n'.format(links[i] , names[i] , versions[i] , description[i]))
    for i in range(names.__len__()):
        dict_all[names[i]] = [versions[i] , links[i] , description[i]]
    page_num = str(s.find_all('strong')[0])[8:-9]
    page_num = page_num.replace(',' , '')
    try:
        page_num = int(page_num) // 20 + 1
    except Exception:
        page_num = 500
    return dict_all

def search(event):
    global module_name , current_page
    current_page = 1
    module_name = str(enter.get())
    if not module_name:
        listbox_content.set('')
        return
    listbox_content.set(tuple(search_page(module_name , current_page).keys()))
    show_page.set(f'{current_page}/{str(page_num)}')

def next_page():
    global current_page
    if module_name == '' or current_page == page_num:
        return
    current_page = current_page + 1
    listbox_content.set(tuple(search_page(module_name , current_page).keys()))
    show_page.set(f'{str(current_page)}/{str(page_num)}')

def prev_page():
    global current_page
    if module_name == '' or current_page == 1:
        return
    current_page = current_page - 1
    listbox_content.set(tuple(search_page(module_name , current_page).keys()))
    show_page.set(f'{str(current_page)}/{str(page_num)}')

def get_pip_command():
    global current_module , command , app , is_open
    try:
        current_module = listbox.get(listbox.curselection())
    except Exception:
        return

    s = bs(requests.get(f'https://pypi.org/project/{current_module}/').text, 'html.parser')

    command = s.find('span' , id = 'pip-command').string

    app = Application().start('wt.exe')
    is_open = False
    while not is_open:
        for i in psutil.process_iter():
            if i.name().lower() == 'cmd.exe':
                is_open = True
        time.sleep(0.1)
    send_keys(command , with_spaces = True , with_newlines = True)

def show_details():
    global current_module
    try:
        current_module = listbox.get(listbox.curselection())
    except Exception:
        return

    a = dict_all[current_module]
    msgbox.showinfo('详情', f'version : {a[0]}\nlink : {a[1]}\ndescription : {a[2]}')

def center_window(root : tkinter.Tk, width, height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

root = tkinter.Tk()
center_window(root , 400 , 550)
root.title('python库查询')
root.resizable(False , False)

listbox_content = tkinter.StringVar()
listbox_content.set('')

show_page = tkinter.StringVar()
show_page.set('0/0')

x = tkinter.Scrollbar(root , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

enter = tkinter.Entry(root , width = 23 , takefocus = True)
enter.place(relx = 0.1 , rely = 0.045)
enter.bind('<Return>' , search)

prev = tkinter.Button(root , text = '<' , command = prev_page)
prev.pack(side = tkinter.LEFT)

to_next = tkinter.Button(root , text = '>' , command = next_page)
to_next.pack(side = tkinter.RIGHT)

detail = tkinter.Button(root , text = '介绍' , command = show_details , height = 1 , width = 4)
detail.place(relx = 0.65 , rely = 0.03)

down = tkinter.Button(root , text = 'pip' , command = get_pip_command , height = 1 , width = 4)
down.place(relx = 0.79 , rely = 0.03)

listbox = tkinter.Listbox(root , selectmode = tkinter.SINGLE , width = 100 , height = 21 , xscrollcommand = x.set , listvariable = listbox_content)
listbox.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

show = tkinter.Label(root , textvariable = show_page)
show.place(relx = 0.49 , rely = 0.1)

x.config(command = listbox.xview)

root.mainloop()