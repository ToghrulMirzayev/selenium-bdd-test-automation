from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from behave import fixture


@fixture
def browser_chrome(context):
    return context.driver


def before_all(context):
    options = Options()
    context.driver = webdriver.Chrome(service=(Service(ChromeDriverManager().install())), options=options)
