from page.home_page import HomePage
from page.login_page import LoginPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def home(self):
        return HomePage(self.driver)