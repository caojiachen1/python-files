import uiautomator2 as u2
import os
import pyperclip
import time

class transfer():
    def run(self):
        while True:
            t = self.main()
            d.clipboard = t

    def main(self):
        recent_txt = pyperclip.paste()
        while True:
            txt = pyperclip.paste()
            if txt != recent_txt:
                recent_txt = txt
                return recent_txt
            time.sleep(0.2)

os.system('adb connect 192.168.31.15:6666')
d = u2.connect('192.168.31.15:6666')

transfer().run()