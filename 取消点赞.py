import uiautomator2 as u2
import time

d = u2.connect()
d.app_start('com.xiaomi.vipaccount')
d(text="随手拍").click()
i = 0
while True:
    d.swipe(540 , 1400 , 540 , 600)
    if d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = True).exists and d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).info['bounds']['bottom'] <= 2000:
        d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = True).click()