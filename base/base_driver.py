import time

from appium import webdriver





def init_driver(noReset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '3d9dee6c'
    desired_caps['appPackage'] = 'com.liying.app.fshon'
    desired_caps['appActivity'] = 'com.liying.app.WelcomeActivity'
    # 使用Uiautomator2 可以获取toast  安装命令：cnpm install appium-uiautomator2-driver
    desired_caps['automationName'] = 'Uiautomator2'
    # True表示不重置
    desired_caps['noReset'] = noReset
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(3)
    # 切换到需要操作的句柄 切换报错的原因可能是内置浏览器驱动版本对不上
    driver._switch_to.context('WEBVIEW_com.liying.app.fshon')
    return driver

