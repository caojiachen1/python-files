from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as msgbox
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.dns import dns_client
from baidubce.auth.bce_credentials import BceCredentials
import os

class domain():
    def __init__(self , domain):
        self.domain = domain
        self.__AK = 'e785a3c14c8f4f17983173db18244488'
        self.__SK = '39735f09986a480785c1687fd9bed092'
        self.__config = BceClientConfiguration(credentials = BceCredentials(self.__AK, self.__SK), endpoint = 'dns.baidubce.com')
        self.__client = dns_client.DnsClient(self.__config)

    def domain_list(self):
        return [zone.name for zone in self.__client.list_zone().zones]

    def info_list(self):
        return {
            record.rr: {'id': record.id, 'value': record.value , 'type' : record.type , 'status' : record.status , 'ttl' : record.ttl}
            for record in self.__client.list_record(zone_name = self.domain).records
        }

    def create_dns(self , name , type , value):
        if name in list(self.info_list().keys()):
            code = self.update_dns(name , type , value)
            return 1 if code == 1 else 0
        create_record_request = {
            'rr': name,
            'type': type,
            'value': value
        }
        self.__client.create_record(zone_name = self.domain , create_record_request = create_record_request)

    def update_dns(self , name , type , value):
        info = self.info_list()
        if value == info[name]['value'] and type == info[name]['type']:
            msgbox.showwarning('警告' , '已存在相同记录!')
            return 1
        update_record_request = {
            'rr': name,
            'type': type,
            'value': value
        }
        record_id = self.info_list()[name]['id']
        self.__client.update_record(zone_name = self.domain , update_record_request = update_record_request , record_id = record_id)

def enter():
    input_domain_name = input_domain.get()
    split = input_domain_name.split('.')
    name = '@'
    if split.__len__() == 3:#需要主机记录值
        name = split[0]
        input_domain_name = input_domain_name.split('.' , 1)[1]
    elif split.__len__() > 3:
        msgbox.showerror('错误' , '主机记录错误!')
        return
    d = domain(input_domain_name)
    if input_domain_name not in d.domain_list():
        msgbox.showerror('错误' , '域名不存在!')
        return
    try:
        code = d.create_dns(name , rb_type.get() , input_record.get())
        if code == 1:
            return
        msgbox.showinfo('提示' , '成功!')
        with open(r'D:\domain.log' , 'w') as f:
            f.write(input_domain_name)
    except Exception as e:
        print(e)
        msgbox.showerror('错误' , '失败!')

win = Tk()
win.title("域名解析")
width , height = 300 , 200
screenwidth , screenheight = win.winfo_screenwidth() , win.winfo_screenheight()
win.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
win.resizable(False, False)

rb_type = StringVar()
rb_type.set('')

label_domain = Label(win,text="域名",anchor="center")
label_domain.place(x=40, y=20, width=50, height=24)

input_domain = Entry(win)
input_domain.place(x=100, y=20, width=150, height=24)

label_type = Label(win,text="类型",anchor="center")
label_type.place(x=40, y=60, width=50, height=24)

label_record = Label(win,text="记录值",anchor="center")
label_record.place(x=40, y=100, width=50, height=24)

input_record = Entry(win)
input_record.place(x=100, y=100, width=150, height=24)

button_record = Button(win, text="确定",command=enter)
button_record.place(x=110, y=150, width=80, height=35)

rb_A = Radiobutton(win,text="A",variable=rb_type,value='A')
rb_A.place(x=100, y=60, width=80, height=24)

rb_AAAA = Radiobutton(win,text="AAAA",variable=rb_type,value='AAAA')
rb_AAAA.place(x=150, y=60, width=80, height=24)

if os.path.exists(r'D:\domain.log'):
    with open(r'D:\domain.log' , 'r') as f:
        input_domain.insert(0 , f.read())

win.mainloop()