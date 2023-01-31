import tkinter
import tkinter.messagebox as msgbox
import tkinter.ttk
import uiautomator2 as u2
import sys , os , time

done = {
    'xiaomi_community' : [0 , 0] , 
    'kuaishou_light' : 0 , 
    'douyin_light' : 0 , 
    'taobao' : 0
}

try:
    os.system('adb devices')
    os.system('adb connect 192.168.31.15:6666')
    d = u2.connect('192.168.31.15:6666')
except:
    msgbox.showerror('错误' , '手机未连接!')
    sys.exit()

class xiaomi_community:
    def __init__(self) -> None:
        self.i = 0
        self.j = 0
        self.visited = []
        self.on = True

    def auto(self):
        self.__init__()
        global done
        try:
            d.app_stop('com.xiaomi.vipaccount')
            d.app_start('com.xiaomi.vipaccount')
        except:
            msgbox.showerror('错误' , '没有安装小米社区!')
            return
        while self.on:
            d.swipe(540 , 1400 , 540 , 600)
            if d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).exists and d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).info['bounds']['bottom'] <= 2000 and self.i <= 3:
                d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).click()
                self.i += 1
            if d(resourceId="com.xiaomi.vipaccount:id/textpart").exists and d(resourceId="com.xiaomi.vipaccount:id/textpart").info['bounds']['bottom'] <= 2000 and self.j <= 3:
                if d(resourceId="com.xiaomi.vipaccount:id/textpart").info['text'] not in self.visited:
                    self.visited.append(d(resourceId="com.xiaomi.vipaccount:id/textpart").info['text'])
                    d(resourceId="com.xiaomi.vipaccount:id/textpart").click()
                    time.sleep(6)
                    d.swipe(540 , 1700 , 540 , 1300)
                    time.sleep(5)
                    d(text = "后退").click()
                    self.j += 1
            self.on = (self.i <= 3) or (self.j <= 3)
        done['xiaomi_community'][0] += 1
        done_or_not_.refresh()

    def check_in(self):
        global done
        try:
            d.app_stop('com.xiaomi.vipaccount')
            d.app_start('com.xiaomi.vipaccount')
        except:
            msgbox.showerror('错误' , '没有安装小米社区!')
            return
        time.sleep(1)
        d(resourceId="com.xiaomi.vipaccount:id/iv3").click()
        time.sleep(2)
        try:
            d(text="立即签到").click()
        except:
            msgbox.showerror('错误' , '已经签到!')
            return
        d(text="backIcon").click()
        done['xiaomi_community'][1] += 1
        done_or_not_.refresh()

class kuaishou_light:
    def __init__(self) -> None:
        pass

    def withdraw(self):
        global done
        try:
            d.xpath('//android.widget.ListView/android.view.View[1]/android.view.View[2]').click()
        except:
            msgbox.showerror('错误' , '没有找到兑换金币按钮!')
            done['kuaishou_light'] = False
            return
        try:
            time.sleep(2)
            d(text="随时兑换").click()
            time.sleep(2)
            d(text="全部兑换").click()
            time.sleep(2)
            d(text="立即兑换").click()
            time.sleep(2)
            d(text="查看流水信息").click()
            time.sleep(2)
            d(text="领现金").click()
            time.sleep(2)
            d(text="立即兑换").click()
            time.sleep(2)
            d(text="极速到账").click()
            time.sleep(2)
            d(resourceId="com.tencent.mm:id/g1").click()
            time.sleep(2)
            d(text="立即兑换").click()
            time.sleep(2)
            d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[4]').click()
            time.sleep(2)
            d(text="知道了").click()
            time.sleep(2)
            d(resourceId="com.kuaishou.nebula:id/left_btn").click()
            time.sleep(2)
            d(resourceId="com.kuaishou.nebula:id/left_btn").click()
            time.sleep(2)
            d(resourceId="com.kuaishou.nebula:id/pay_left_btn").click()
        except:
            msgbox.showerror('错误' , '失败!')
            return
        done['kuaishou_light'] += 1
        done_or_not_.refresh()

class douyin_light:
    def __init__(self) -> None:
        pass

    def withdraw(self):
        global done
        try:
            d.app_stop('com.ss.android.ugc.aweme.lite')
            d.app_start('com.ss.android.ugc.aweme.lite')
        except:
            msgbox.showerror('错误' , '没有安装抖音极速版!')
            return
        time.sleep(2)
        try:
            d(resourceId="com.ss.android.ugc.aweme.lite:id/dzp").click()
            time.sleep(3)
            d.xpath('//*[@resource-id="com.ss.android.ugc.aweme.lite:id/a-z"]/android.widget.FrameLayout[1]/com.lynx.tasm.behavior.ui.text.FlattenUIText[5]').click()
            time.sleep(2)
            d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[2]/android.view.View[12]').click()
            time.sleep(4)
            d.click(0.5 , 0.425)#确认提现
            time.sleep(4)
            d.click(900 , 1860)#3
            d.click(540 , 2000)#5
            d.click(900 , 2160)#9
            d.click(900 , 2160)#9
            d.click(900 , 2160)#9
            d.click(900 , 1860)#3
            time.sleep(3)
            d(resourceId="com.ss.android.ugc.aweme.lite:id/gn").click()
            time.sleep(2)
            d(resourceId="com.ss.android.ugc.aweme.lite:id/a7-").click()
        except:
            msgbox.showerror('错误' , '失败!')
            return
        done['douyin_light'] += 1
        done_or_not_.refresh()

class taobao:
    def __init__(self) -> None:
        pass

    def get_coins(self):
        global done
        try:
            d.app_stop('com.taobao.taobao')
            d.app_start('com.taobao.taobao')
        except:
            msgbox.showerror('错误' , '没有安装淘宝!')
            return
        time.sleep(2)
        try:
            d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]').click()
            time.sleep(2)
            d.xpath('//*[@resource-id="module-container"]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]').click()
        except:
            msgbox.showerror('错误' , '失败!')
            return
        done['taobao'] += 1
        done_or_not_.refresh()

class yeyouyou:
    def __init__(self) -> None:
        self.respond = tkinter.StringVar()
        self.respond.set('叶悠悠回复: 无')
        self.mine = tkinter.StringVar()
        self.mine.set('我发的消息: 无')

    def enter(self , event):
        send = yeyouyou_entry.get()
        if send == '':
            return
        try:
            d(resourceId = "com.baidu.input:id/input_ed").click()
        except:
            msgbox.showerror('错误' , '手机未打开聊天界面!')
            return
        try:
            self.mine.set('我发的消息: {}'.format(send))
            d.send_keys(send)
            d(resourceId = "com.baidu.input:id/send_btn").click()
            d.set_fastinput_ime(False)
            time.sleep(4)
            respond_text = d(resourceId = "com.baidu.input:id/content")[-1].info['text']
            self.respond.set('叶悠悠回复: {}'.format(respond_text))
            yeyouyou_entry.delete(0 , tkinter.END)
        except:
            msgbox.showerror('错误' , '失败!')
            return

class done_or_not:
    def __init__(self) -> None:
        self.xiaomi_community_run = tkinter.StringVar()
        self.xiaomi_community_run.set(str(done['xiaomi_community'][0]))
        self.xiaomi_community_run_is_done = tkinter.Label(frame_xiaomi_community , textvariable = self.xiaomi_community_run)
        self.xiaomi_community_run_is_done.place(relx = 0.7 , rely = 0.15)
        
        self.xiaomi_community_auto_check_in = tkinter.StringVar()
        self.xiaomi_community_auto_check_in.set(str(done['xiaomi_community'][1]))
        self.xiaomi_community_auto_check_in_is_done = tkinter.Label(frame_xiaomi_community , textvariable = self.xiaomi_community_auto_check_in)
        self.xiaomi_community_auto_check_in_is_done.place(relx = 0.6 , rely = 0.55)

        self.kuaishou_light = tkinter.StringVar()
        self.kuaishou_light.set(str(done['kuaishou_light']))
        self.kuaishou_light_is_done = tkinter.Label(frame_kuaishou_light , textvariable = self.kuaishou_light)
        self.kuaishou_light_is_done.place(relx = 0.7 , rely = 0.35)

        self.douyin_light = tkinter.StringVar()
        self.douyin_light.set(str(done['douyin_light']))
        self.douyin_light_is_done = tkinter.Label(frame_douyin_light , textvariable = self.douyin_light)
        self.douyin_light_is_done.place(relx = 0.7 , rely = 0.35)

        self.taobao = tkinter.StringVar()
        self.taobao.set(str(done['taobao']))
        self.taobao_is_done = tkinter.Label(frame_taobao , textvariable = self.taobao)
        self.taobao_is_done.place(relx = 0.7 , rely = 0.35)

    def refresh(self):
        self.xiaomi_community_run.set(done['xiaomi_community'][0])
        self.xiaomi_community_auto_check_in.set(str(int(done['xiaomi_community'][1])))
        self.kuaishou_light.set(str(int(done['kuaishou_light'])))
        self.douyin_light.set(str(int(done['douyin_light'])))
        self.taobao.set(str(int(done['taobao'])))

def center_window(root : tkinter.Tk , width , height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 - 60 , (screenheight - height) / 2 - 60)
    root.geometry(size)

root = tkinter.Tk()
center_window(root , 800 , 700)
root.title('手机自动化合集')
root.resizable(False , False)

frame_xiaomi_community = tkinter.LabelFrame(root , text = '小米社区')
frame_xiaomi_community.place(relx = 0.02 , rely = 0.02 , relheight = 0.2 , relwidth = 0.24)
frame_kuaishou_light = tkinter.LabelFrame(root , text = '快手极速版')
frame_kuaishou_light.place(relx = 0.25 , rely = 0.02 , relheight = 0.2 , relwidth = 0.24)
frame_douyin_light = tkinter.LabelFrame(root , text = '抖音极速版')
frame_douyin_light.place(relx = 0.02 , rely = 0.22 , relheight = 0.2 , relwidth = 0.24)
frame_taobao = tkinter.LabelFrame(root , text = '淘宝')
frame_taobao.place(relx = 0.25 , rely = 0.22 , relheight = 0.2 , relwidth = 0.24)
frame_yeyouyou = tkinter.LabelFrame(root , text = '叶悠悠')
frame_yeyouyou.place(relx = 0.02 , rely = 0.42 , relheight = 0.5 , relwidth = 0.9)

done_or_not_ = done_or_not()
xiaomi_community_ = xiaomi_community()
kuaishou_light_ = kuaishou_light()
douyin_light_ = douyin_light()
taobao_ = taobao()
yeyouyou_ = yeyouyou()

xiaomi_community_run = tkinter.Button(frame_xiaomi_community , text = '自动浏览点赞' , command = xiaomi_community_.auto , height = 1 , width = 10)
xiaomi_community_run.place(in_ = frame_xiaomi_community , relx = 0.25 , rely = 0.1)
xiaomi_community_auto_check_in = tkinter.Button(frame_xiaomi_community , text = '签到' , command = xiaomi_community_.check_in , height = 1 , width = 6)
xiaomi_community_auto_check_in.place(in_ = frame_xiaomi_community , relx = 0.3 , rely = 0.5)

kuaishou_light_withdraw = tkinter.Button(frame_kuaishou_light , text = '提现' , command = kuaishou_light_.withdraw , height = 2 , width = 6)
kuaishou_light_withdraw.place(relx = 0.35 , rely = 0.26)

douyin_light_withdraw = tkinter.Button(frame_douyin_light , text = '提现' , command = douyin_light_.withdraw , height = 2 , width = 6)
douyin_light_withdraw.place(relx = 0.35 , rely = 0.26)

taobao_check_in = tkinter.Button(frame_taobao , text = '签到' , command = taobao_.get_coins , height = 2 , width = 6)
taobao_check_in.place(relx = 0.35 , rely = 0.26)

yeyouyou_entry = tkinter.Entry(frame_yeyouyou , width = 80)
yeyouyou_entry.place(relx = 0.1 , rely = 0.2)
yeyouyou_entry.bind('<Return>' , yeyouyou_.enter)
yeyouyou_respond_ = tkinter.Label(frame_yeyouyou , textvariable = yeyouyou_.respond , wraplength = 1000)
yeyouyou_respond_.place(relx = 0.1 , rely = 0.65)
yeyouyou_mine_ = tkinter.Label(frame_yeyouyou , textvariable = yeyouyou_.mine , wraplength = 1000)
yeyouyou_mine_.place(relx = 0.1 , rely = 0.4)

root.bind('<Escape>' , lambda event:exit())

root.mainloop()