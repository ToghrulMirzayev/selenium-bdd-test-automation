from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def wait_until_element_is_absent(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.invisibility_of_element_located(locator))
