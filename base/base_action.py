import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 查找单个元素
    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    # 查找一组元素元素，返回列表
    def find_elements(self, feature, timeout=10, poll=1):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    # 点击元素
    def click(self, feature):
        self.find_element(feature).click()

    # 往元素输入
    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    # 获取元素文本
    def get_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self,message):
        """
            toast是否存在
            # message: 预期要获取的toast的部分消息
        """
        message = By.XPATH,"//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        try:
            self.find_element(message,5,0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self,message):
        """
            获取toast的 文本信息
            # message: 预期要获取的toast的部分消息
        """
        if self.is_toast_exist(message):
            message = By.XPATH,"//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
            return self.find_element(message).text
        else:
            raise Exception("toast没有出现在屏幕上")

    def is_feature_exist(self,feature):
        '''
        判断 元素 是否存在
        :param feature:
        :return:
        '''
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    def scroll_page_one_time(self, direction="up"):
        """
        滑动一次屏幕
        :param direction:方向
        "up"：从下往上
        "down"：从上往下
        "left"：从右往左
        "down"：从左往右
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = height / 2
        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y
        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)

    def find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找某个元素的特征
        :param feature:元素的特征
        :param direction:方向
        "up"：从下往上
        "down"：从上往下
        "left"：从右往左
        "down"：从左往右
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)
            if self.driver.page_source == page_source:
                print("到底了")
                break
            page_source = self.driver.page_source

    def is_str_in_page_source(self,str,timeout=10,poll=0.1):
        '''
        如果str在页面元素中，那么返回true
        如果str不在页面元素中，那么返回false
        :param str: 要找的 字符串
        :param timeout:
        :param poll:
        :return:
        '''
        end_time = time.time() + timeout
        while True:
            # 如果结束时间小于当前时间，那么认为超时了
            if end_time < time.time():
                return False
            if str in self.driver.page_source:
                return True
            time.sleep(poll)

    # 按返回键
    def press_back(self):
        self.driver.press_keycode(4)

    # 按回车键
    def press_enter(self):
        self.driver.press_keycode(66)

    # 删除文本内容
    def delete_text(self,feature):
        ele = self.find_element(feature)
        ele.send_keys(Keys.CONTROL,'a') #先全选 中 文本内容
        ele.send_keys(Keys.BACK_SPACE)  # 再删除
