from msilib.schema import ComboBox, ListBox
import requests
from bs4 import BeautifulSoup as bs
import re
import tkinter
import tkinter.ttk

def get():
    global teams_lose , teams_win , scores_lose , scores_win , event , info_list , info_dict , current_selection
    teams_lose , teams_win , scores_lose , scores_win = [] , [] , [], []
    event = []
    info_list = []
    info_dict = {}
    url = r'https://www.hltv.org/results'
    s = bs(requests.get(url).text , 'html.parser')
    for i in s.find_all('div' , class_ = 'team'):
        status = i.get('class')
        if status == ['team']:
            r = re.search(r'<div class="team">(.*?)</div>' , str(i) , re.IGNORECASE)
            if r is not None:
                teams_lose.append(str(r.group(1)))
        elif status == ['team' , 'team-won']:
            r = re.search(r'<div class="team team-won">(.*?)</div>' , str(i) , re.IGNORECASE)
            if r is not None:
                teams_win.append(str(r.group(1)))

    for i in s.find_all('span' , class_ = 'event-name'):
        r = re.search(r'<span class="event-name">(.*?)</span>' , str(i) , re.IGNORECASE)
        if r is not None:
            event.append(str(r.group(1)))

    for i in s.find_all('span' , class_ = 'score-lost'):
        r = re.search(r'<span class="score-lost">(.*?)</span>' , str(i) , re.IGNORECASE)
        if r is not None:
            scores_lose.append(str(r.group(1)))

    for i in s.find_all('span' , class_ = 'score-won'):
        r = re.search(r'<span class="score-won">(.*?)</span>' , str(i) , re.IGNORECASE)
        if r is not None:
            scores_win.append(str(r.group(1)))

    num = teams_lose.__len__()
    info_dict['All'] = []
    for i in range(num):
        info_dict[event[i]] = []

    for i in range(num):
        vs = '{}  {}-{}  {}'.format(teams_win[i] , scores_win[i] , scores_lose[i] , teams_lose[i])
        info_list.append(vs)
        if vs not in info_dict[event[i]]:
            info_dict[event[i]].append(vs)
        if vs not in info_dict['All']:
            info_dict['All'].append(vs)

    content.set(tuple(info_dict['All']))

def comb_select(event):
    content.set(tuple(info_dict[str(comb.get())]))

root = tkinter.Tk()
root.title('hltv比赛结果查询')
root.geometry('800x600')
root.resizable(False , False)

content = tkinter.StringVar()
content.set('')

get()

comb = tkinter.ttk.Combobox(root , width = 55)
comb['value'] = tuple(info_dict.keys())
comb.current(0)
comb.place(relx = 0.2 , rely = 0.04)
comb.bind('<<ComboboxSelected>>' , comb_select)

refresh = tkinter.Button(root , text = '刷新' , command = get , width = 5)
refresh.place(relx = 0.75 , rely = 0.035)

y = tkinter.Scrollbar(root , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)

x = tkinter.Scrollbar(root , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

results = tkinter.Listbox(root , selectmode = tkinter.SINGLE , width = 100 , height = 28 , yscrollcommand = y.set , xscrollcommand = x.set , listvariable = content)
results.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

y.config(command = results.yview)
x.config(command = results.xview)

root.mainloop()