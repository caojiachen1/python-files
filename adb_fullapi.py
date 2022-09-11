import os , re

def get_current_application():
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    return('com.{}'.format(s.group(1)))

def run_application(activity_name):
    os.system('adb shell am start {}'.format(activity_name))

def type_keys(text):
    text = text.replace(' ' , r'\ ')
    os.system('adb shell input text {}'.format(text))

def swipe(x1 , y1 , x2 , y2):
    os.system('adb shell input swipe {} {} {} {}'.format(str(x1) , str(y1) , str(x2) , str(y2)))

def tap(x , y):
    os.system('adb shell input mouse tap {} {}'.format(x , y))

a = get_current_application()
print(a)
