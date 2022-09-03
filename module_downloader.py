import tkinter
import requests
import re
import tkinter.messagebox as msgbox
from bs4 import BeautifulSoup as bs

module_name = 'winrt'
url = 'https://pypi.tuna.tsinghua.edu.cn/simple/{}/'.format(module_name)
a = requests.get(url)
soup = bs(a.text , 'html.parser')
l , links , name_list , d = [] , [] , [] , {}
for link in soup.find_all('a'):
    l.append(link.get('href'))
for u in l:
    u = str('https://pypi.tuna.tsinghua.edu.cn' + u[5:])
    links.append(u)
    results = re.search(r'winrt(.*?)#sha256=' , str(u))
    name = 'winrt' + results.group(1)
    name_list.append(name)
for i in range(name_list.__len__()):
    d[name_list[i]] = links[i]
for names in d.keys():
    with open(names , mode = 'wb') as f:
        a = requests.get(d[names])
        f.write(a.content)