import requests
from bs4 import BeautifulSoup as bs
import re
import tkinter
import tkinter.ttk
import tkinter.messagebox as msgbox

def get():
    global teams_lose , teams_win , scores_lose , scores_win , event , info_list , info_dict , link_list , get_link , j
    teams_lose , teams_win , scores_lose , scores_win = [] , [] , [], []
    event , info_list , link_list , info_dict , get_link = [] , [] , [] , {} , {}
    url = r'https://www.hltv.org/results'
    s = bs(requests.get(url).text , 'html.parser')
    for i in s.find_all('div' , class_ = 'team'):
        status = i.get('class')
        if status == ['team']:
            r = re.search(r'<div class="team">(.*?)</div>' , str(i) , re.IGNORECASE)
            if r is not None:
                teams_lose.append(str(r[1]))
        elif status == ['team' , 'team-won']:
            r = re.search(r'<div class="team team-won">(.*?)</div>' , str(i) , re.IGNORECASE)
            if r is not None:
                teams_win.append(str(r[1]))

    for i in s.find_all('span' , class_ = 'event-name'):
        r = re.search(r'<span class="event-name">(.*?)</span>' , str(i) , re.IGNORECASE)
        if r is not None:
            event.append(str(r[1]))

    for i in s.find_all('span' , class_ = 'score-lost'):
        r = re.search(r'<span class="score-lost">(.*?)</span>' , str(i) , re.IGNORECASE)
        if r is not None:
            scores_lose.append(str(r[1]))

    for i in s.find_all('span' , class_ = 'score-won'):
        r = re.search(r'<span class="score-won">(.*?)</span>' , str(i) , re.IGNORECASE)
        if r is not None:
            scores_win.append(str(r[1]))

    for i in s.find_all('a'):
        j = str(i.get('href'))
        if i.get('class') == ['a-reset'] and j.startswith('/matches') and j not in link_list:
            link_list.append(f'https://www.hltv.org{j}')

    num = teams_lose.__len__()
    info_dict['All'] = []
    for i in range(num):
        info_dict[event[i]] = []

    for i in range(num):
        vs = f'{teams_win[i]}        '.rjust(30) + f'{scores_win[i]}'.rjust(2) + '-' + f'{scores_lose[i]}'.ljust(2) + f'        {teams_lose[i]}'.ljust(30)

        info_list.append(vs)
        if vs not in info_dict[event[i]]:
            info_dict[event[i]].append(vs)
        if vs not in info_dict['All']:
            info_dict['All'].append(vs)
        get_link[vs] = link_list[i]

    content.set(tuple(info_dict['All']))

def get_details():
    global n , s , map , r , team1_score , team2_score , scores , team1 , team2 , teams , info_string

    map , team1_score , team2_score , scores , teams = [] , [] , [] , [] , []
    team1 , team2 , info_string = '' , '' , ''

    try:
        n = results.get(results.curselection())
    except Exception:
        return

    s = bs(requests.get(get_link[str(n)]).text , 'html.parser')

    for i in s.find_all('div' , class_ = 'mapname'):
        r = re.search(r'<div class="mapname">(.*?)</div>' , str(i) , re.IGNORECASE)
        if r is not None:
            map.append(str(r[1]))
    for i in s.find_all('div' , class_ = 'results-team-score'):
        r = re.search(r'<div class="results-team-score">(.*?)</div>' , str(i) , re.IGNORECASE)
        if r is not None:
            scores.append(str(r[1]))

    for i in range(scores.__len__()):
        if (i % 2) ==0:
            team1_score.append(scores[i])
        else:
            team2_score.append(scores[i])

    for i in s.find_all('div' , class_ = 'teamName'):
        r = re.search(r'<div class="teamName">(.*?)</div>' , str(i) , re.IGNORECASE)
        if r is not None:
            teams.append(str(r[1]))

    team1 , team2 = teams[0] , teams[1]

    scores = [f'Map{i + 1}:{map[i]}\n{team1.ljust(25)}{team1_score[i].ljust(2)}-{team2_score[i].rjust(2)}{team2.rjust(25)}' for i in range(team1_score.__len__())]

    for i in scores:
        info_string = info_string + i + '\n'

    msgbox.showinfo('详情' , info_string)
    
def center_window(root : tkinter.Tk , width , height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    root.geometry(size)

root = tkinter.Tk()
root.title('CSGO职业比赛结果查询')
center_window(root , 800 , 600)
root.resizable(False , False)

content = tkinter.StringVar()
content.set('')

get()

comb = tkinter.ttk.Combobox(root , width = 55)
comb['value'] = tuple(info_dict.keys())
comb.current(0)
comb.place(relx = 0.15 , rely = 0.04)
comb.bind('<<ComboboxSelected>>' , lambda event : content.set(tuple(info_dict[str(comb.get())])))

refresh = tkinter.Button(root , text = '刷新' , command = get , width = 5)
refresh.place(relx = 0.7 , rely = 0.035)

detail = tkinter.Button(root , text = '详情' , command = get_details , width = 5)
detail.place(relx = 0.8 , rely = 0.035)

y = tkinter.Scrollbar(root , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)

x = tkinter.Scrollbar(root , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

results = tkinter.Listbox(root , selectmode = tkinter.SINGLE , width = 100 , height = 28 , yscrollcommand = y.set , xscrollcommand = x.set , listvariable = content , justify = 'center')
results.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

y.config(command = results.yview)
x.config(command = results.xview)

root.mainloop()