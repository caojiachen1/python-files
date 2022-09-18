import uiautomator2 as u2
import time

d = u2.connect()
d.app_start('com.xiaomi.vipaccount')
i , j , on , visited= 0 , 0 , True , []
while on:
    d.swipe(540 , 1400 , 540 , 600)
    if d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).exists and d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).info['bounds']['bottom'] <= 2000 and i <= 3:
        d(resourceId = "com.xiaomi.vipaccount:id/img_like" , selected = False).click()
        i += 1
    if d(resourceId="com.xiaomi.vipaccount:id/textpart").exists and d(resourceId="com.xiaomi.vipaccount:id/textpart").info['bounds']['bottom'] <= 2000 and j <= 3:
        if d(resourceId="com.xiaomi.vipaccount:id/textpart").info['text'] not in visited:
            visited.append(d(resourceId="com.xiaomi.vipaccount:id/textpart").info['text'])
            d(resourceId="com.xiaomi.vipaccount:id/textpart").click()
            time.sleep(6)
            d.swipe(540 , 1700 , 540 , 1300)
            time.sleep(5)
            d(text = "后退").click()
            j += 1
    on = (i <= 3) or (j <= 3)