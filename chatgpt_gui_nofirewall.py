import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tf
import tkinter.messagebox as msgbox
import openai , os , requests , re , json , contextlib , hashlib
import openai.error
from hashlib import md5
from subprocess import run
from base64 import b64decode

appid = '20230223001572583'
key = 'LbGJ114ECr7RhvK5dS5J'
salt = '1435660288'

ask_sequences = []
sequence_length = 0 #就是历史列表的总长度
error_list = ['apikeyerror' , 'timeout' , 'noapikey' , 'ratelimit' , 'none' , 'apiconnectionerror' , 'error']
spacing = 10
current_font = 'Arial'
fontsize = 10
bold_reflection = ['normal' , 'bold']

def language_detect(text):
    if text == '':
        return ''
    sign = hashlib.md5(f'{appid}{text}{salt}{key}'.encode('utf-8')).hexdigest()
    url = 'https://fanyi-api.baidu.com/api/trans/vip/language'
    url += f'?q={text}&salt={salt}&sign={sign}&appid={appid}'
    try:
        detect_result = requests.get(url).json()
        return detect_result['data']['src']
    except Exception as e:
        print(e)
        return detect_result

def translate(text , from_language = 'auto' , to_language = 'zh'):
    if text == '':
        return ''
    if language_detect(text) == 'zh':
        return text
    text = text.replace('\n' , '')
    text = re.sub(r'(```.*?```)' , '******' , text)
    sign = md5(f'{appid}{text}{salt}{key}'.encode('utf-8')).hexdigest()
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    url += f'?q={text}&from={from_language}&to={to_language}&appid={appid}&salt={salt}&sign={sign}'
    try:
        translate_result = requests.get(url).json()
        return translate_result['trans_result'][0]['dst']
    except Exception as e:
        print(e)
        return translate_result

def check_billing():
    try:
        api_key = os.environ['OPENAI_API_KEY']
        header = {
            'Authorization' : f'Bearer {api_key}'
        }
        a = requests.get('https://visitcjc.top/dashboard/billing/credit_grants' , headers = header).json()
        total_granted = a['total_granted']
        total_used = a['total_used']
        total_available = a['total_available']
    except Exception:
        return 0 , 0 , 0
    return total_granted , total_used , total_available

def respond(text):
    if text == '':
        return 'none'
    try:
        api_key = os.environ['OPENAI_API_KEY']
    except KeyError:
        msgbox.showerror('错误' , '请输入API KEY!')
        return 'noapikey'
    try:
        header = {
            'Authorization' : f'Bearer {api_key}',
            'Content-Type' : 'application/json'
        }
        data = {
            'model' : 'gpt-3.5-turbo',
            'messages' : [{'role' : 'user' , 'content' : text}],
            'stream' : True
        }
        tk_text_response.insert('0.0' , f'问:{tk_input_.get()}\n\n答:')
        tk_text_response.update()
        result = requests.post('https://chatgpt-api.shn.hk/v1/' , headers = header , json = data , stream = True)
        full_respond = ''
        for line in result.iter_lines():
            if line != b'':
                a = line.decode('utf-8').split(':' , 1)[1].strip()
                with contextlib.suppress(Exception):
                    a = json.loads(a)
                    respond = a['choices'][0]['delta']['content']
                    if respond != '\n\n':
                        full_respond += respond
                        tk_text_response.insert('end' , respond)
                        tk_text_response.update()
                        tk_text_response.yview_moveto(1.0)
    except requests.exceptions.ConnectTimeout:
        msgbox.showerror('错误' , '网络连接超时!')
        return 'timeout'
    except requests.exceptions.JSONDecodeError:
        msgbox.showerror('错误' , 'API KEY错误!')
        return 'apikeyerror'
    except openai.error.RateLimitError:
        msgbox.showerror('错误' , '请求频率过高!')
        return 'ratelimit'
    except requests.exceptions.ConnectionError:
        msgbox.showerror('错误' , '连接错误!')
        return 'apiconnectionerror'
    return full_respond

current = sequence_length
display_text = ''
mytext = ''
response_text = ''

def response_translate():
    if language_detect(mytext) == 'zh' and language_detect(response_text) == 'zh' or mytext == '':
        return
    tk_text_response.delete('1.0' , tk.END)
    tk_text_response.insert('0.0' , f'问:{translate(mytext)} \n\n答:{translate(response_text)}')

def show_former_content():
    if mytext == '':
        return
    tk_text_response.delete('1.0' , tk.END)
    tk_text_response.insert('0.0' , display_text)

def answer(event):
    global ask_sequences , sequence_length , current , mytext , response_text , display_text , text_in , text_out
    tk_text_response.delete('1.0' , tk.END)
    text_in = tk_input_.get()
    if text_in == '':
        return
    out = respond(text_in)
    # out = ['fuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuckfuck' , 0 , 0]
    if out in error_list:
        return
    ask_sequences.append(text_in)
    sequence_length += 1
    current = sequence_length
    mytext = text_in
    response_text = out
    display_text = f'问:{text_in}\n\n答:{out}'
    tk_input_.delete(0 , tk.END)
    with open('D:/chatgpt_history.log' , 'a') as f:
        f.write(display_text + '\n\n')

def up(event):
    global current
    if tk_input_.get() not in ask_sequences:
        current = sequence_length
    if current == 0:
        return
    current -= 1
    tk_input_.delete(0 , tk.END)
    tk_input_.insert('0' , ask_sequences[current])

def down(event):
    global current
    if tk_input_.get() not in ask_sequences:
        current = -1
    if current == sequence_length - 1:
        return
    current += 1
    tk_input_.delete(0 , tk.END)
    tk_input_.insert('0' , ask_sequences[current])

def change_apikey():
    root = tk.Toplevel(win)
    root.title('修改API KEY')
    width , height = 600 , 25
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    geometry = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    root.geometry(geometry)

    input_apikey = Entry(root)
    input_apikey.pack(fill = tk.BOTH)
    input_apikey.focus_set()
    def f(event):
        if input_apikey.get() != '':
            run(f'setx OPENAI_API_KEY {input_apikey.get()}'  , shell = True)
            msgbox.showinfo('提示' , '修改成功!请重启程序使其生效')
        root.destroy()
    input_apikey.bind('<Return>' , f)
    root.mainloop()

def check_history():
    if os.path.exists('D:/chatgpt_history.log'):
        os.startfile('D:/chatgpt_history.log')
    else:
        msgbox.showinfo('提示' , '还没有历史记录!')
        return
        
def on_exit():
    if os.path.exists(pic_path):
        os.unlink(pic_path)
    win.destroy()

win = tk.Tk()

win.title('ChatGPT')
width , height = 600 , 500
screenwidth = win.winfo_screenwidth()
screenheight = win.winfo_screenheight()
geometry = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2, (screenheight - height) / 2)
win.geometry(geometry)
win.resizable(False , False)

tk_input_ = Entry(win , font = 10)
tk_input_.place(x = 50 , y = 70 , width = 500 , height = 35)

tk_text_response = tk.Text(win , font = tf.Font(family = current_font , size = fontsize) , state = tk.NORMAL , spacing2 = spacing)
tk_text_response.place(x = 50 , y = 140 , width = 500 , height = 300)

tk_label_welcome = Label(win , text = '欢迎来到ChatGPT的世界' , anchor = 'center' , font = 'Arial 12 bold')
tk_label_welcome.place(x = 150, y = 10, width = 300, height = 50)

tk_button_change_apikey = Button(win , text = '修改API KEY',command = change_apikey)
tk_button_change_apikey.place(x = 50 , y = 20 , width = 90 , height = 30)

tk_button_history = Button(win , text = '查看聊天历史',command = check_history)
tk_button_history.place(x = 460 , y = 20 , width = 90 , height = 30)

tk_button_show_former_content = Button(win, text = '显示原始内容',command = show_former_content)
tk_button_show_former_content.place(x = 130, y = 115, width = 90, height = 25)

tk_button_translate = Button(win, text = '翻译成中文',command = response_translate)
tk_button_translate.place(x = 50, y = 115, width = 70, height = 25)

tk_input_.bind('<Return>',answer)
tk_input_.bind('<Up>' , up)
tk_input_.bind('<Down>' , down)
tk_input_.bind('<Escape>' , lambda e:tk_input_.delete(0 , tk.END))

bold_or_not = tk.IntVar() #1表示加粗,0表示不加粗
bold_or_not.set(0)

def setting():
    setting_panel = tk.Toplevel(win)
    setting_panel.title('设置')
    width , height = 250 , 250
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    geometry = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    setting_panel.geometry(geometry)
    setting_panel.focus_set()

    bill = Label(setting_panel , )

    select_font = Combobox(setting_panel , state = 'readonly')
    select_font['values'] = tf.families()
    select_font.set(current_font)
    select_font.place(x = 70 , y = 70 , width = 150 , height = 24)

    _font = Label(setting_panel,text = '字体',anchor = 'center')
    _font.place(x = 10 , y = 70 , width = 50, height = 25)

    _font_size = Label(setting_panel,text = '文字大小',anchor = 'center')
    _font_size.place(x = 5 , y = 113 , width = 55 , height = 25)

    font_size = tk.Scale(setting_panel , from_ = 1 , to = 30 , resolution = 1 , length = 150 , orient = 'horizontal')
    font_size.place(x = 70 , y = 95)
    font_size.set(fontsize)

    spacing_size = Label(setting_panel,text = '行间距',anchor = 'center')
    spacing_size.place(x = 7 , y = 155 , width = 55 , height = 25)

    spacing_size = tk.Scale(setting_panel , from_ = 1 , to = 30 , resolution = 1 , length = 150 , orient = 'horizontal')
    spacing_size.place(x = 70 , y = 135)
    spacing_size.set(spacing)

    font_bold = Checkbutton(setting_panel , text = '文字加粗' , onvalue = 1 , offvalue = 0 , variable = bold_or_not)
    font_bold.place(x = 22 , y = 190)

    def onexit():
        global current_font , fontsize , spacing
        current_font = select_font.get()
        fontsize = font_size.get()
        spacing = spacing_size.get()
        tk_text_response.config(font = tf.Font(family = current_font , size = fontsize , weight = bold_reflection[bold_or_not.get()]))
        tk_text_response.config(spacing2 = spacing)
        setting_panel.destroy()

    enter_exit = Button(setting_panel , text = '确认' , command = onexit)
    enter_exit.place(x = 130 , y = 210)

    setting_panel.protocol('WM_DELETE_WINDOW' , onexit)
    setting_panel.mainloop()

a_gif = '''iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZ
        cwAAEnQAABJ0Ad5mH3gAAAPPSURBVEhLtZdZLm1BGIXLQfAg+mAMeNOMAQPQjcBkmIB3TYhejIE3TZiCB6JJ9Oxb37rWuXW27V7kWsl
        /dp2/W7Wr+at21d3dXRY+gaqqqlBXVxf6+vrC0dHRm/Y3enp6pHt4eAhZ9ql0ofT2rADBkFRXV79pgv6vra2J4OXlJZydnUleX1
        /D8fGxbPgA4omtr6/X/yIUEjc0NITd3d0QR0PB6Vu0tbWFUqkUWltbJYwETwNf4ond2dn5kLyCmCQ4Dg4OhpGRkdDU1KQ3JBGAkL
        cFT09PEsBbYwP4EkPs6OiocpGT3CkqiBmqoaGhsL+/r54vLCxoTk9PT2WHKJ8A4Pv8/Kw2vsTMz89LTy5yehrKYHHd3t5Gnyzr7+9nTNV
        +fHzUc3FxUbqpqSk9Z2ZmpCfGceiwTU5O6kkMcA505AbEaEHzA7a2tuQACEBvWxy6bGxsLNvc3NR/ByMm39jYkA++wPaUHA6AXsQYLy8v
        ZYzDWzZa4rxKB1JSi8kBvnk9OckNh1+qYqgPDg7k4KFyglRMfH9/L0l1eQGeKnID+4oYMXlcHHJkyNLepz5FyJMTe3h4qFwnJyfvfAK9zo
        OFxHwBO5qUeerq6lJChHbR3ANykCsPOLWaVldXJevr69ny8rISpgvBpNPT07LNzs5mNzc3EtrosAGTAzqEjZzkNg+gzsrY3t6eNTc3Zy0t
        LeUtk5KyavEz4p6WGNjwAcQ4jo6RE4EDv97eXp4hi5VHTincc/eeISUJsD61Y+vs7FTbepOngAtOylBGsY89KleftDrRpurwjEOr8mc
        /o6amhrUSGhsbVa3SU8pPUFtbGy4uLkLs4J+SWVQKfxIi7ujoUK8p8Eh6orjHcajD3Nyc/PJAh627u1v/07d1TgQ/uIS3ic7icVdeXPm
        5BN9dXCxUcpI7Hp/yEyfGou3kvZkuknQ7XV9f/3M7uf4XbqevFhA6xOolIfLtApJP/BMlk5x5n8JDYmlpSf/tlIqD6TWS6lJxTnKRs/CQSI
        /FeHOQQ5qA3ht/IwH42sf6D49FUHQRcCDDPjExUbFqsac+zPP4+Hj5ImAfcgFyv7sIOPh/XX08VSnpwMCA2u5weXEhAAccgUl9nq6srGhPgp
        SYPYoN4EuMLxO0401T7ZSrgthby+SIhw6wFyEBeWJsBjGO9yXPC9FScb2NdhX7vb29sL29Ha6urvR5Eh1l5/7srwsKPgLQYQP4EkMsF3qut
        +Qkd4oKYgPH4eFh1VfaPkAIPj8/15NTBkl1AF9iiCWHO53Hlz/aYp3Vt1IKdLFYfOGjLYRf/vtIDzsit1gAAAAASUVORK5CYII='''
pic = b64decode(a_gif)
pic_path = os.path.join(os.environ['temp'] , 'a.gif')
with open(pic_path , 'wb') as f:
    f.write(pic)
image = tk.PhotoImage(file = pic_path)
tk_button_setting = Button(win , image = image , command = setting)
tk_button_setting.place(x = 560 , y = 0, width = 40, height = 40)
tk_input_.focus_set()
win.protocol('WM_DELETE_WINDOW' , on_exit)
win.mainloop()

