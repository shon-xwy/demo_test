import time

import allure

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver(False)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.step('登录成功的用例')
    @pytest.mark.parametrize("args", analyze_file('login_data.yaml','test_login'))
    def test_login_success(self,args):
        username = args['username']
        password = args['password']
        self.page.home.click_login_button()
        self.page.login.input_name(username)
        self.page.login.input_pwd(password)
        self.page.login.click_login_button()
        # self.page.login.click_yihouzaishuo()
        assert self.page.home.find_login_button() == False

