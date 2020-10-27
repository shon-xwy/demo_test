'''
@Author:shon
首页
'''
import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    # 我的账户
    wodezhuanghu = By.XPATH, '//*[@class="iconfont icon-user"]'
    # 登录按钮
    login_button = By.XPATH, '//*[@class="jp-index__service"]'

    @allure.step('点击我的账户')
    def click_wodezhuanghu(self):
        self.click(self.wodezhuanghu)

    @allure.step('点击首页的登录按钮')
    def click_login_button(self):
        self.click(self.login_button)

    def is_login(self,page):
        # 判断有没有登录
        if self.is_feature_exist(self.login_button):
            self.click_wodezhuanghu  # 点击我的账户
            page.login.input_name('ycy888')
            page.login.input_pwd('qwe123')
            page.login.click_login_button  # 点击登录

    def find_login_button(self):
        return self.is_feature_exist(self.login_button)



