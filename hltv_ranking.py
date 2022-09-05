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
a = requests.get(r'https://www.hltv.org/')
s = bs(a.text , 'html.parser')
last_update_ = []
for i in s.find_all('span' , class_ = 'normal-weight'):
    last_update_.append(i)
last_update = str(last_update_[1])
r = re.search(r'<span class="normal-weight">(.*?) of (.*?)</span>' , last_update , re.IGNORECASE)
if r is not None:
    day = str(r.group(1))
    month = str(r.group(2))
    month = abbr[month.lower()]
    r = re.search(r'(\d+)' , day)
    if r is not None:
        day = int(r.group(1))
url = r'https://www.hltv.org/ranking/teams/{}/{}/{}'.format(year , month , day)
a = requests.get(url)
s = bs(a.text , 'html.parser')
teams = []
points = []
team_point = {}
show = []
for i in s.find_all('span' , class_ = 'name'):
    r = re.search(r'<span class="name">(.*?)</span>' , str(i) , re.IGNORECASE)
    if r is not None:
        teams.append(r.group(1))
for i in s.find_all('span' , class_ = 'points'):
    r = re.search(r'<span class="points">((.*?))</span>' , str(i) , re.IGNORECASE)
    if r is not None:
        r = str(r.group(1))[1:-1]
        r = re.search(r'(\d+)' , r , re.IGNORECASE)
        if r is not None:
            points.append(int(r.group(1)))

for i in range(teams.__len__()):
    team_point[teams[i]] = points[i]
    show.append(r'#{} {}'.format(str(i+1) , str(teams[i])) + '          ' + r'{}'.format(str(points[i])).rjust(3 , '0') + '                  ')

win = tkinter.Tk()
win.geometry('300x300')
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


