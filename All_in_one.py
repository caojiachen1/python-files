import tkinter
import tkinter.messagebox as msgbox
import tkinter.ttk
import uiautomator2 as u2
import sys , os
import requests
import re
from bs4 import BeautifulSoup as bs
import time
# from 快手评论作品 import *
# from 小米社区刷成长值 import *
# from 叶悠悠电脑版_gui import *

package = {
        'com.smile.gifmaker/com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity' : '快手金币收益页' ,
        'com.smile.gifmaker/com.yxcorp.gifshow.detail.PhotoDetailActivity' : '快手视频页' ,
        'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity' : '抖音极速版' ,
        'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity' : '快手极速版视频页' , 
        'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity' : '快手极速版收益页' ,
        'com.xiaomi.vipaccount/com.xiaomi.vipaccount.ui.home.page.HomeFrameActivity' : '小米社区主页' ,
        'com.xiaomi.vipaccount/com.xiaomi.vipaccount.newbrowser.NormalWebActivity' : '小米社区签到页' , 
        'com.xunmeng.pinduoduo/com.xunmeng.pinduoduo.ui.activity.HomeActivity' : '拼多多主页' , 
        'com.taobao.litetao/com.taobao.ltao.maintab.MainFrameActivity' : '淘特主页' , 
        'com.miui.home/com.miui.home.launcher.Launcher' : '手机主页' , 
        'com.xiayin.task/com.example.zhuoxin_task.MainActivity' : '优赏吧'
}

try:
    os.system('adb devices')
    d = u2.connect()
except:
    msgbox.showerror('错误' , '手机未连接!')
    sys.exit()

def get_current_package_name():
    '''获取当前运行程序的包名'''
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    s = 'com.' + str(s.group(1))
    return s

def current_app():
    '''获取手机现在运行的当前程序名称,在保存的字典中进行检索,没有收录在字典中的进程页面会返回Unknown,否则返回进程页面名称'''
    s = get_current_package_name()
    if s in package.keys():
        return package[s]
    else:
        return 'Unknown'

class xiaomi_community:
    def __init__(self) -> None:
        self.i = 0
        self.j = 0
        self.visited = []
        self.on = True

    def auto(self):
        d.app_stop('com.xiaomi.vipaccount')
        d.app_start('com.xiaomi.vipaccount')
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

    def check_in(self):
        d.app_stop('com.xiaomi.vipaccount')
        d.app_start('com.xiaomi.vipaccount')
        time.sleep(1)
        d(resourceId="com.xiaomi.vipaccount:id/iv3").click()
        time.sleep(2)
        try:
            d(text="立即签到").click()
        except:
            msgbox.showerror('错误' , '已经签到!')
            return
        d(text="backIcon").click()

class kuaishou:
    def __init__(self) -> None:
        pass

    def auto_comment(self):
        '''快手自动评论刷金币.需要滑动到评论按钮出现在屏幕上'''
        if current_app() != '快手金币收益页':
            msgbox.showerror('错误' , '没有打开快手收益界面!')
            return
        try:
            d(text="去评论").click()
        except:
            msgbox.showerror('错误' , '找不到评论按钮!')
            return
        try:
            time.sleep(1)
            d.click(0.248, 0.245)#点击左上角视频
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/comment_icon").click()#打开评论区
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/editor_holder_text").click()#点击评论框
            time.sleep(2)
            d.xpath('//*[@resource-id="com.smile.gifmaker:id/emoji_quick_send"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()#点击表情输入
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/finish_button_wrapper").click()#点击发送按钮
            time.sleep(1)
            d.xpath('//*[@resource-id="com.smile.gifmaker:id/recycler_view"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]').long_click()#长按已经发送的评论
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/qlist_alert_dialog_item_text", text="删除评论").click()#删除已经发送的评论
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/pendant_mask_bg").click()#返回
            time.sleep(1)
            d(text="知道了").click()
        except:
            msgbox.showerror('错误' , '失败!')
            return

    def auto_praise(self):
        '''快手自动点赞刷金币.需要滑动到点赞按钮出现在屏幕上'''
        if current_app() != '快手金币收益页':
            msgbox.showerror('错误' , '没有打开快手收益界面!')
            return
        try:
            d(text="去点赞").click()#点击点赞按钮
        except:
            msgbox.showerror('错误' , '找不到点赞按钮!')
            return
        try:
            time.sleep(1)
            d.click(0.244, 0.258)#点击左上角视频
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/like_icon").click()#点赞
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/like_icon").click()#取消点赞
            time.sleep(1)
            d(resourceId="com.smile.gifmaker:id/pendant_mask_bg").click()#返回
            time.sleep(1)
            d(text="知道了").click()
        except:
            msgbox.showerror('错误' , '失败!')
            return

    def auto_withdraw(self):
        '''快手自动提现'''
        if self.current_app() != '快手金币收益页':
            msgbox.showerror('错误' , '没有打开快手收益界面!')
            return
        try:
            d(text="领现金").click()#点击领现金按钮
        except:
            msgbox.showerror('错误' , '找不到提现按钮!')
            return
        time.sleep(1)
        try:
            d(text="立即提现").click()#点击立即提现按钮
        except:
            msgbox.showerror('错误' , '已经提现!')
            return
        try:
            time.sleep(1)
            d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[4]').click()
            time.sleep(2)
            d(resourceId="com.smile.gifmaker:id/pay_left_btn").click()#完成
            time.sleep(2)
            d(resourceId="com.smile.gifmaker:id/left_btn").click()#返回
        except:
            msgbox.showerror('错误' , '失败!')
            return

class kuaishou_light:
    def __init__(self) -> None:
        pass

    def withdraw(self):
        if current_app() != '快手极速版收益页':
            msgbox.showerror('错误' , '没有打开快手极速版收益界面!')
            return
        try:
            d.xpath('//android.widget.ListView/android.view.View[1]/android.view.View[2]').click()
        except:
            msgbox.showerror('错误' , '没有找到兑换金币按钮!')
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
            d.click(0.478, 0.407)
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

class douyin_light:
    def __init__(self) -> None:
        pass

    def withdraw(self):
        d.app_stop('com.ss.android.ugc.aweme.lite')
        d.app_start('com.ss.android.ugc.aweme.lite')
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

class youshangba:
    def __init__(self) -> None:
        pass

    def sign_in(self):
        d.app_stop('com.xiayin.task')
        d.app_start('com.xiayin.task')
        time.sleep(5)
        try:
            d.click(0.5 , 0.95)
            time.sleep(2)
            d(description="立即签到").click()
        except:
            msgbox.showerror('错误' , '失败!')
            return

def center_window(root : tkinter.Tk , width , height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    root.geometry(size)

root = tkinter.Tk()
center_window(root , 800 , 700)
root.title('手机自动化合集')
root.resizable(False , False)

xiaomi_community_ = xiaomi_community()
kuaishou_ = kuaishou()
kuaishou_light_ = kuaishou_light()
douyin_light_ = douyin_light()
youshangba_ = youshangba()

frame_xiaomi_community = tkinter.LabelFrame(root , text = '小米社区')
frame_xiaomi_community.place(relx = 0.02 , rely = 0.02 , relheight = 0.2 , relwidth = 0.24)
frame_kuaishou = tkinter.LabelFrame(root , text = '快手')
frame_kuaishou.place(relx = 0.25 , rely = 0.02 , relheight = 0.4 , relwidth = 0.3)
frame_kuaishou_light = tkinter.LabelFrame(root , text = '快手极速版')
frame_kuaishou_light.place(relx = 0.53 , rely = 0.02 , relheight = 0.2 , relwidth = 0.2)
frame_douyin_light = tkinter.LabelFrame(root , text = '抖音极速版')
frame_douyin_light.place(relx = 0.53 , rely = 0.22 , relheight = 0.2 , relwidth = 0.2)
frame_youshangba = tkinter.LabelFrame(root , text = '优赏吧')
frame_youshangba.place(relx = 0.02 , rely = 0.22 , relheight = 0.2 , relwidth = 0.232)

run = tkinter.Button(frame_xiaomi_community , text = '自动浏览点赞' , command = xiaomi_community_.auto , height = 1 , width = 10)
run.place(in_ = frame_xiaomi_community , relx = 0.25 , rely = 0.1)
auto_check_in = tkinter.Button(frame_xiaomi_community , text = '签到' , command = xiaomi_community_.check_in , height = 1 , width = 6)
auto_check_in.place(in_ = frame_xiaomi_community , relx = 0.3 , rely = 0.5)

praise = tkinter.Button(frame_kuaishou , text = '自动点赞' , command = kuaishou_.auto_praise)
praise.place(relx = 0.35 , rely = 0.2)
comment = tkinter.Button(frame_kuaishou , text = '自动评论' , command = kuaishou_.auto_comment)
comment.place(relx = 0.35 , rely = 0.4)
withdraw = tkinter.Button(frame_kuaishou , text = '自动提现' , command = kuaishou_.auto_withdraw)
withdraw.place(relx = 0.35 , rely = 0.6)

kuaishou_light_withdraw = tkinter.Button(frame_kuaishou_light , text = '提现' , command = kuaishou_light_.withdraw , height = 2 , width = 6)
kuaishou_light_withdraw.place(relx = 0.35 , rely = 0.26)

douyin_light_withdraw = tkinter.Button(frame_douyin_light , text = '提现' , command = douyin_light_.withdraw , height = 2 , width = 6)
douyin_light_withdraw.place(relx = 0.35 , rely = 0.26)

youshangba_sign_in = tkinter.Button(frame_youshangba , text = '签到' , command = youshangba_.sign_in , height = 2 , width = 6)
youshangba_sign_in.place(relx = 0.35 , rely = 0.26)









root.mainloop()
