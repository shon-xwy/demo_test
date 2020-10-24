from appium import webdriver





def init_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '3d9dee6c'
    desired_caps['appPackage'] = 'com.tencent.wstt.gt'
    desired_caps['appActivity'] = 'com.tencent.wstt.gt.activity.GTMainActivity'
    # 使用Uiautomator2 可以获取toast  安装命令：cnpm install appium-uiautomator2-driver
    desired_caps['automationName'] = 'Uiautomator2'
    # 不重置应用
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

