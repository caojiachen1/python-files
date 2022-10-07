import uiautomator2 as u2
import os
import pyperclip
import time

class transfer():
    def run(self):
        while True:
            t = listen().main()
            d.clipboard = t

class listen():
    def main(self):
        recent_txt = pyperclip.paste()
        while True:
            txt = pyperclip.paste()
            if txt != recent_txt:
                recent_txt = txt
                return recent_txt
            time.sleep(0.2)
        
    def run(self):
        while True:
            t = self.main()
            d.clipboard = t

os.system('adb connect 192.168.31.15:6666')
d = u2.connect('192.168.31.15:6666')

# isnone = True
# while isnone:
#     if d.clipboard is not None:
#         print(d.clipboard)
#         isnone = False
listen().run()