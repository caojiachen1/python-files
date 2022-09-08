import tkinter
import requests
from bs4 import BeautifulSoup as bs

event , time , info = [] , [] , []

a = requests.get(r'https://www.hltv.org/events')
s = bs(a.text , 'html.parser')
for i in s.find_all('div' , class_ = 'big-events'):
    s_ = bs(str(i) , 'html.parser')
    for j in s_.find_all('div' , class_ = 'big-event-name'):
        event.append(j.string)

    for j in s_.find_all('td'):
        if j.get('class') == ['col-value', 'col-date']:
            time.append(j.text)

for i in range(event.__len__()):
    info.append('{}'.format(event[i]).rjust(40) + '{}'.format(time[i]).rjust(25) + ''.rjust(13))

def center_window(root : tkinter.Tk , width , height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

win = tkinter.Tk()
center_window(win , 500 , 200)
win.resizable(False , False)
win.title('CSGO未来重大赛事')

content = tkinter.StringVar()
content.set(tuple(info))

y = tkinter.Scrollbar(win , width = 20)
y.pack(side = tkinter.RIGHT , fill = tkinter.Y)

x = tkinter.Scrollbar(win , width = 22 , orient = tkinter.HORIZONTAL)
x.pack(side = tkinter.BOTTOM , fill = tkinter.X)

listbox = tkinter.Listbox(win , selectmode = tkinter.SINGLE , yscrollcommand = y.set , xscrollcommand = x.set , listvariable = content , width = 100 , height = 25 , justify = 'right')
listbox.pack(side = tkinter.BOTTOM , fill = tkinter.Y)

y.config(command = listbox.yview)
x.config(command = listbox.xview)

win.mainloop()

