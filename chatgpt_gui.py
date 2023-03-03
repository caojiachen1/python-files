from tkinter import *
from tkinter.ttk import *
import openai

def respond(text):
    api_key = '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'
    openai.api_key = api_key

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    completion_tokens = result['usage']['completion_tokens']
    promt_tokens = result['usage']['prompt_tokens']
    respond = result['choices'][0]['message']['content']
    return respond , promt_tokens , completion_tokens

def scrollbar_autohide(bar,widget):
    def show():
        bar.lift(widget)
    def hide():
        bar.lower(widget)
    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())
    
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_input_ = self.__tk_input_()
        self.tk_text_response = self.__tk_text_response()
        self.tk_label_welcome = self.__tk_label_welcome()
        self.tk_input_.bind('<Return>',self.answer)

    def __win(self):
        self.title("ChatGPT")
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_input_(self):
        ipt = Entry(self,font=10)
        ipt.place(x=50, y=70, width=500, height=35)
        return ipt

    def __tk_text_response(self):
        text = Text(self, font=10, state=NORMAL)
        text.place(x=50, y=140, width=500, height=300)
        
        # vbar = Scrollbar(self)
        # text.configure(yscrollcommand=vbar.set)
        # vbar.config(command=text.yview)
        # vbar.place(x=535, y=140, width=15, height=300)
        # scrollbar_autohide(vbar,text)
        return text

    def __tk_label_welcome(self):
        label = Label(self,text="欢迎来到ChatGPT的世界",anchor="center",font='Arial 12 bold')
        label.place(x=150, y=10, width=300, height=50)
        return label
    
    def answer(self,event):
        self.tk_text_response.delete('1.0' , 'end')
        text_in = self.tk_input_.get()
        out = respond(self.tk_input_.get())
        text_out = out[0].replace('\n' , '')
        display_text = f'问:{text_in} ({out[1]} tokens)\n答:{text_out} ({out[2]} tokens)'
        self.tk_text_response.insert('0.0' , display_text)
        self.tk_input_.delete(0 , END)
        with open('D:/chatgpt_history.log' , 'a') as f:
            f.write(display_text + '\n')
        
win = WinGUI()
win.mainloop()
