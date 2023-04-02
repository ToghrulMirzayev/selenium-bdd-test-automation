from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("the user is on the login page")
def open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")


@when("the user enters valid username and password")
def enter_valid_credentials(context):
    LoginPage(context.driver).login("standard_user", "secret_sauce")


@when("the user enters invalid username and password")
def enter_invalid_credentials(context):
    LoginPage(context.driver).login("invalid_user", "invalid_password")


@when("clicks on the login button")
def click_login_button(context):
    LoginPage(context.driver).click_login_button()


@then("the user should see title text")
def verify_title_text(context):
    assert InventoryPage(context.driver).is_title_text_displayed(), "Failed to login. Title text not displayed"


@then("the user should see an error message")
def verify_error_message(context):
    assert LoginPage(context.driver).is_error_message_displayed(), "Error message not displayed"
