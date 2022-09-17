import uiautomator2 as u2
import time , os , re , sys
import tkinter.messagebox as msgbox
#滑动到‘去评论’按钮出现

package = {
    'com.smile.gifmaker/com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity' : '快手金币收益页' ,
    'com.smile.gifmaker/com.yxcorp.gifshow.detail.PhotoDetailActivity' : '快手视频页' ,
    'com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity' : '抖音极速版' ,
    'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity' : '快手极速版视频页' , 
    'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity' : '快手极速版收益页' ,
    'com.xiaomi.vipaccount/com.xiaomi.vipaccount.ui.home.page.HomeFrameActivity' : '小米社区主页' ,
    'com.xiaomi.vipaccount/com.xiaomi.vipaccount.newbrowser.NormalWebActivity' : '小米社区签到页' , 
    'com.xunmeng.pinduoduo/com.xunmeng.pinduoduo.ui.activity.HomeActivity' : '拼多多主页' , 
    'com.taobao.litetao/com.taobao.ltao.maintab.MainFrameActivity' : '淘特主页'
}

try:
    os.system('adb devices')
    d = u2.connect()
except:
    msgbox.showerror('错误' , '手机未连接!')
    sys.exit()

def judge(app_name):
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    s = 'com.' + str(s.group(1))
    if package[s] != app_name:
        msgbox.showerror('错误' , '手机未打开{}!'.format(app_name))
        sys.exit()

def current_app():
    a = os.popen('adb shell dumpsys window | findstr mCurrentFocus')
    result = a.read()
    s = re.search(r'mCurrentFocus=Window{.* com.(.*?)}' , result , re.IGNORECASE)
    s = 'com.' + str(s.group(1))
    if s in package.keys():
        return package[s]

def auto_comment():
    d(text="去评论").click()
    time.sleep(0.5)
    d.click(0.248, 0.245)
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/comment_icon").click()
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/editor_holder_text").click()
    time.sleep(2)
    d.xpath('//*[@resource-id="com.smile.gifmaker:id/emoji_quick_send"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]').click()
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/finish_button_wrapper").click()
    time.sleep(0.5)
    d.xpath('//*[@resource-id="com.smile.gifmaker:id/recycler_view"]/android.view.ViewGroup[2]/android.widget.RelativeLayout[1]').long_click()
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/qlist_alert_dialog_item_text", text="删除评论").click()
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/pendant_mask_bg").click()
    time.sleep(0.5)
    d(text="知道了").click()

def auto_praise():
    d(text="去点赞").click()
    time.sleep(0.5)
    d.click(0.244, 0.258)
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/like_icon").click()
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/like_icon").click()
    time.sleep(0.5)
    d(resourceId="com.smile.gifmaker:id/pendant_mask_bg").click()
    time.sleep(0.5)
    d(text="知道了").click()

print(current_app())