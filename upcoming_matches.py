import requests
import re
from bs4 import BeautifulSoup as bs
import tkinter
import tkinter.messagebox as msgbox
import tkinter.ttk

revert = {
    '时间' : 'time' , 
    '比赛名称' : 'matchname' , 
    '战队' : 'team' , 
    '赛制' : 'format'
}

def filter(filter_type , filter_name):
    '''
        搜索符合筛选的比赛信息,返回符合的所有比赛列表
        filter_type可以是如下:
        matchname(比赛名称)
        team(战队名称)
        format(比赛赛制)
        time(比赛时间)
    '''
    result = []
    if filter_type != 'team':
        for i in range(info_list.__len__()):
            if info_list[i][filter_type] == filter_name:
                result.append(info_list[i])
    elif filter_type == 'team':
        for i in range(info_list.__len__()):
            if filter_name in info_list[i][filter_type]:
                result.append(info_list[i])
    else:
        return None
    return result

def center_window(root : tkinter.Tk , width , height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    root.geometry(size)

def filtered_result_select(event):
    content.set(process(filter('matchname' , str(filtered_names.get()))))

def process(filtered_dict : dict):
    result_dict = []
    for i in range(filtered_dict.__len__()):
        a = filtered_dict[i]
        result_dict.append('{}    {}{}   {}    {}{}\n\n'.format(a['team'][0].rjust(20) , 'vs '.rjust(10) , a['team'][1].rjust(20)  , a['time'].rjust(8) , a['format'].ljust(7) , a['matchname'].ljust(a['matchname'].__len__() + 20)))
    return result_dict

s = bs(requests.get('https://www.hltv.org/matches').text , 'html.parser')
info_list , info , time = [] , {} , ''
for i in s.find_all('a' , class_ = 'match a-reset'):
    info = {}
    s_ = bs(str(i) , 'html.parser')
    for j in s_.find_all('div'):
        if j['class'][0] == 'matchTime':
            if j.string == 'LIVE':
                time = j.string
            else:
                time_ = re.search(r'(.*?):(.*)' , j.string)
                time = '{}:{}'.format(str((int(time_.group(1)) + 6) % 24) , time_.group(2))
        info['time'] = time

    s_ = re.findall(r'<div class="matchTeamName text-ellipsis">(.*?)</div>' , str(i) , re.IGNORECASE)
    if s_.__len__() == 0:
        s_ = ['Unknown' , 'Unknown']
    elif s_.__len__() == 1:
        s_.append('Unknown')
    info['team'] = s_

    s__ = re.search(r'<div class="matchEventName gtSmartphone-only">(.*?)</div>' , str(i) , re.IGNORECASE)
    if s__ == None:
        s__ = re.search(r'<span class="line-clamp-3">(.*?)</span></div>' , str(i) , re.IGNORECASE)
    info['matchname'] = s__.group(1)

    s__ = re.search(r'<div class="matchMeta">(.*?)</div>' , str(i) , re.IGNORECASE).group(1)
    info['format'] = s__

    info_list.append(info)

root = tkinter.Tk()
root.title('CSGO职业比赛赛程查询')
center_window(root , 800 , 600)
root.resizable(False , False)

content = tkinter.StringVar()
content.set('')

filtered_names = tkinter.ttk.Combobox(root , width = 65)
select = []
for i in range(info_list.__len__()):
    a = info_list[i]['matchname']
    if a not in select:
        select.append(a)
filtered_names['value'] = tuple(select)
filtered_names.current(0)
filtered_names.place(relx = 0.2 , rely = 0.05)
filtered_names.bind('<<ComboboxSelected>>' , filtered_result_select)

y = tkinter.Scrollbar(root , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)

x = tkinter.Scrollbar(root , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

results = tkinter.Listbox(root , selectmode = tkinter.SINGLE , width = 100 , height = 28 , yscrollcommand = y.set , xscrollcommand = x.set , listvariable = content , justify = 'right')
results.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

y.config(command = results.yview)
x.config(command = results.xview)

root.mainloop()