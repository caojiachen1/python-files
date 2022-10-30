import requests
import re
from bs4 import BeautifulSoup as bs
import datetime
import tkinter

time = datetime.datetime.now()
year = time.year

abbr = {
    'jan' : 'january',
    'feb' : 'february',
    'mar' : 'march',
    'apr' : 'april',
    'may' : 'may',
    'jun' : 'june',
    'jul' : 'july',
    'aug' : 'august',
    'sep' : 'september',
    'oct' : 'october',
    'nov' : 'november',
    'dec' : 'december'
}

s = bs(requests.get(r'https://www.hltv.org/').text , 'html.parser')
last_update_ = list(s.find_all('span' , class_ = 'normal-weight'))
last_update = str(last_update_[1])
r = re.search(r'<span class="normal-weight">(.*?) of (.*?)</span>' , last_update , re.IGNORECASE)
if r is not None:
    day , month = str(r[1]), abbr[str(r[2]).lower()]
    r = re.search(r'(\d+)' , day)
if r is not None:
    day = int(r[1])
url = f'https://www.hltv.org/ranking/teams/{year}/{month}/{day}'
s = bs(requests.get(url).text , 'html.parser')
teams , points , team_point , show = [] , [] , {} , []
for i in s.find_all('span' , class_ = 'name'):
    r = re.search(r'<span class="name">(.*?)</span>' , str(i) , re.IGNORECASE)
    if r is not None:
        teams.append(r[1])

for i in s.find_all('span' , class_ = 'points'):
    r = re.search(r'<span class="points">((.*?))</span>' , str(i) , re.IGNORECASE)
    if r is not None:
        r = re.search(r'(\d+)', str(r[1])[1:-1], re.IGNORECASE)
    if r is not None:
        points.append(int(r[1]))

for i in range(teams.__len__()):
    team_point[teams[i]] = points[i]
    show.append(f'#{str(i + 1)} {str(teams[i])}          ' + f'{str(points[i])}'.rjust(str(points[0]).__len__(), '0') + '                  ')

def center_window(root : tkinter.Tk , width , height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    root.geometry(size)

win = tkinter.Tk()
center_window(win , 300 , 300)
win.title('CSGO战队排名')
win.resizable(False , False)

content = tkinter.StringVar()
content.set(tuple(show))

y = tkinter.Scrollbar(win , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)

listbox = tkinter.Listbox(win , selectmode = tkinter.SINGLE , yscrollcommand = y.set , listvariable = content , width = 100 , height = 20 , justify = 'right')
listbox.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

y.config(command = listbox.yview)

win.mainloop()


