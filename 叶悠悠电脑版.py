import uiautomator2 as u2
import time
import sys
import os

os.system('adb devices')
d = u2.connect()
d(resourceId="com.baidu.input:id/input_ed").click()
while True:
    send = input('输入聊天内容：')
    if send == 'stop':
        sys.exit()
    d.send_keys(send)
    d(resourceId="com.baidu.input:id/send_btn").click()
    d.set_fastinput_ime(False)
    time.sleep(4)
    respond = d(resourceId="com.baidu.input:id/content")[-1].info['text']
    print('叶悠悠回复：{}'.format(respond))