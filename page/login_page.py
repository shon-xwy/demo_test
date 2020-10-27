'''
@Author:shon
登录页
'''
import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class LoginPage(BaseAction):
    # 用户名输入框
    username = By.XPATH, '//*[@type="text"]'
    # 密码输入框
    password = By.XPATH, '//*[@type="password"]'
    # 登录按钮
    login_sub = By.XPATH, '//*[@id="app"]/div[1]/div[1]/span'
    # 温馨提示的 以后再说
    yihouzaishuo = By.XPATH, '//*[@class="mint-msgbox-btn mint-msgbox-cancel "]'
    # 点击用户登录标题
    login_title = By.XPATH, '//*[@id="app"]/div[1]/header/h1/span'

    @allure.step('输入登录用户名')
    def input_name(self,content):
        # 先清空
        self.delete_text(self.username)
        self.click(self.login_title)
        # 再输入
        self.input(self.username,content)
        time.sleep(1)

    @allure.step('输入登录密码')
    def input_pwd(self,content):
        # 先清空
        self.delete_text(self.password)
        self.click(self.login_title)
        # 再输入
        self.input(self.password,content)
        time.sleep(1)

    @allure.step('输入登录图片验证码')
    def input_code(self, code):
        self.input(self.input_text[2],code)

    @allure.step('点击登录按钮')
    def click_login_button(self):
        self.click(self.login_sub)

    @allure.step('点击温馨提示的 以后再说')
    def click_yihouzaishuo(self):
        self.click(self.yihouzaishuo)




