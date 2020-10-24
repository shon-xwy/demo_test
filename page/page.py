from page.search_page import SearchPage
from page.setting_page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)