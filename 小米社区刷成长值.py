import uiautomator2 as u2
import time

d = u2.connect()
d.app_start('com.xiaomi.vipaccount')
# d(resourceId="com.xiaomi.vipaccount:id/iv3").click()
# d(text="立即签到").click()
# d(text="backIcon").click()
d(text="随手拍").click()
i = 0
j = 0
on = True
while on:
    d.swipe(540 , 1400 , 540 , 600)
    if d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).exists and d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).info['bounds']['bottom'] <= 2000 and i <= 5:
        d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).click()
        i += 1
    if d(resourceId = "com.xiaomi.vipaccount:id/tv_content").exists and j <= 6:
        d(resourceId = "com.xiaomi.vipaccount:id/tv_content").click()
        time.sleep(5)
        d.swipe(540 , 1700 , 540 , 1300)
        time.sleep(5)
        d(text = "后退").click()
        j += 1
    on = (i <= 5) or (j <= 5)
    print(i , j)