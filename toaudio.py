from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import filedialog
from moviepy.editor import *
import os.path

path , audio_path = '' , '' 

def splitname(path):
    global name , suffix
    name , suffix = os.path.splitext(os.path.basename(path))
    suffix = suffix[1:]
    return name , suffix

def center_window(root : Tk, width, height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width)/2 , (screenheight - height)/2)
    root.geometry(size)

def select():
    global path , audio_path , display_content
    path = filedialog.askopenfilename()
    if path == '':
        return
    try:
        a = AudioFileClip(path)
        b = splitname(path)[0]+'.wav'
        parent = os.path.split(path)[0]
        audio_path = os.path.join(parent , b)
        a.write_audiofile(audio_path)
        msgbox.showinfo('成功' , '音频保存成功')
        display_content.set('音频地址:{audiopath}'.format(audiopath = audio_path))
    except:
        msgbox.showerror('失败' , '音频保存失败')

root = Tk()
root.title('视频转音频')
center_window(root , 250 , 150)
root.resizable(False , False)

display_content = StringVar()
display_content.set('音频地址:无')

button = Button(root , text = '浏览' , width = 8 , height = 2 , command = select)
button.place(relx = 0.35 , rely = 0.15)

content = Label(root , textvariable = display_content , wraplength = 225)
content.place(relx = 0 , rely = 0.6)

root.mainloop()