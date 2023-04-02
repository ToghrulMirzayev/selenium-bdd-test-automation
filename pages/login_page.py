from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//*[@data-test='error']")

    def login(self, username, password):
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_element(self.LOGIN_BUTTON).click()

    def is_error_message_displayed(self):
        return self.wait_for_element(self.ERROR_MESSAGE).is_displayed()
