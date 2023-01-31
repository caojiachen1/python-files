import os , re

def get_current_application():
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    return f'com.{s[1]}'

def run_application(activity_name):
    os.system(f'adb shell am start {activity_name}')

def type_keys(text):
    text = text.replace(' ' , r'\ ')
    os.system(f'adb shell input text {text}')

def swipe(x1 , y1 , x2 , y2):
    os.system(f'adb shell input swipe {str(x1)} {str(y1)} {str(x2)} {str(y2)}')

def tap(x , y):
    os.system(f'adb shell input mouse tap {x} {y}')

a = get_current_application()
print(a)
