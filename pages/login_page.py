from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def launch(self):
        self.goto(self.URL)

    def login(self, username: str, password: str):
        self.fill('#user-name', username)
        self.fill('#password', password)
        self.click('#login-button')
