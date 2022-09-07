from pywinauto.application import Application
from pywinauto.keyboard import *
import time
import psutil
import os

for i in psutil.process_iter():
    if i.name().lower() in ['cmd.exe' , 'openconsole.exe']:
        os.system('taskkill /F /IM {}'.format(i.name()))

app = Application().start('wt.exe')
is_open = False
while not is_open:
    for i in psutil.process_iter():
        if i.name().lower() == 'cmd.exe':
            is_open = True
    time.sleep(0.1)
send_keys('pip install numpy\n' , with_spaces = True , with_newlines = True)