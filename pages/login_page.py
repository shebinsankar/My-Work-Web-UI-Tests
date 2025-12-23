from .base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'

    def launch(self):
        self.goto(self.URL)
        self.page.wait_for_load_state("load")

    def login(self, username: str, password: str):
        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()
        self.page.wait_for_load_state("load")
