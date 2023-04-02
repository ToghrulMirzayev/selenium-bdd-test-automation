from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@given("the user is on the website")
def open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")


@given("the user is logged in")
def login_to_website(context):
    LoginPage(context.driver).login("standard_user", "secret_sauce")
    LoginPage(context.driver).click_login_button()


@given("the user is on the inventory page")
def open_inventory_page(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")


@when("the user adds a product to the cart")
def add_product_to_cart(context):
    InventoryPage(context.driver).add_product_to_cart()


@then("the user should see the product in the cart")
def verify_product_in_cart(context):
    assert InventoryPage(context.driver).is_product_in_cart(), "Product not in cart"
