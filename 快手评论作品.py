import uiautomator2 as u2
import time , os , re , sys
import tkinter.messagebox as msgbox
import tkinter

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
}#手机app包名和中文解释一一对应字典

try:
    os.system('adb devices')
    d = u2.connect()
except Exception:
    msgbox.showerror('错误' , '手机未连接!')
    sys.exit()

def get_current_package_name():
    '''获取当前运行程序的包名'''
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    s = f'com.{str(s[1])}'
    return s
    
def current_app():
    '''获取手机现在运行的当前程序名称,在保存的字典中进行检索,没有收录在字典中的进程页面会返回Unknown,否则返回进程页面名称'''
    s = get_current_package_name()
    return package[s] if s in package.keys() else 'Unknown'

def auto_comment():
    '''快手自动评论刷金币.需要滑动到评论按钮出现在屏幕上'''
    if current_app() != '快手金币收益页':
        msgbox.showerror('错误' , '没有打开快手收益界面!')
        return
    try:
        d(text="去评论").click()
    except Exception:
        msgbox.showerror('错误' , '找不到评论按钮!')
        return
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
   
def auto_praise():
    '''快手自动点赞刷金币.需要滑动到点赞按钮出现在屏幕上'''
    if current_app() != '快手金币收益页':
        msgbox.showerror('错误' , '没有打开快手收益界面!')
        return
    try:
        d(text="去点赞").click()#点击点赞按钮
    except Exception:
        msgbox.showerror('错误' , '找不到点赞按钮!')
        return
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

def auto_withdraw():
    '''快手自动提现'''
    if current_app() != '快手金币收益页':
        msgbox.showerror('错误' , '没有打开快手收益界面!')
        return
    try:
        d(text="领现金").click()#点击领现金按钮
    except Exception:
        msgbox.showerror('错误' , '找不到提现按钮!')
        return
    time.sleep(1)
    try:
        d(text="立即提现").click()#点击立即提现按钮
    except Exception:
        msgbox.showerror('错误' , '已经提现!')
        return
    time.sleep(1)
    d.xpath('//*[@resource-id="app"]/android.view.View[1]/android.view.View[4]').click()
    time.sleep(2)
    d(resourceId="com.smile.gifmaker:id/pay_left_btn").click()#完成
    time.sleep(2)
    d(resourceId="com.smile.gifmaker:id/left_btn").click()#返回

def center_window(root : tkinter.Tk , width , height):
    screenwidth , screenheight = root.winfo_screenwidth() , root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width , height , (screenwidth - width) / 2 , (screenheight - height) / 2)
    root.geometry(size)

win = tkinter.Tk()
center_window(win , 250 , 200)
win.title('快手刷任务')
win.resizable(False , False)

praise = tkinter.Button(win , text = '自动点赞' , command = auto_praise).place(relx = 0.35 , rely = 0.2)
comment = tkinter.Button(win , text = '自动评论' , command = auto_comment).place(relx = 0.35 , rely = 0.4)
withdraw = tkinter.Button(win , text = '自动提现' , command = auto_withdraw).place(relx = 0.35 , rely = 0.6)

win.mainloop()
