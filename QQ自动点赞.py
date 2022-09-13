import uiautomator2 as u2

d = u2.connect()
d.app_start('com.tencent.mobileqq')
d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()
while True:
    if d(resourceId="com.tencent.mobileqq:id/c7p" , selected = False).exists:
        d(resourceId="com.tencent.mobileqq:id/c7p" , selected = False).click()
    d.swipe(540 , 1400 , 540 , 800)
    d.xpath('//*[@resource-id="android:id/tabs"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]').click()