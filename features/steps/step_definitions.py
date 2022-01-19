from behave import given,when,then, use_step_matcher
from pages.Base_page import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.wishlist import WishList
import time

use_step_matcher("parse")


@when("{item_number} products are added to wish list")
def step_impl(context, item_number):
    """
    :param item_number: Number of items to add to wish list
    :type context: behave.runner.Context
    """
    print(int(item_number))
    context.home_page = HomePage(context.driver)
    context.home_page.accept_cookies()
    wish_list_elements = context.home_page.find_product_columns()

    for e in range(int(item_number)):
        print('Element added to wishlist: {}'.format(e))
        context.home_page.add_product_to_wishlist(wish_list_elements[e])
    time.sleep(10)  # TODO: Remove this and handle wait in add_product_to_wishlist
    context.home_page.navigate_to_wish_list_page()


@given("website is open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    web_driver = prime_web_driver(context)
    context.base_page = BasePage(web_driver)
    context.base_page.open_web_page()


@when("wish list page is opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.wish_list_page = WishList(context.driver)
    context.entries = context.wish_list_page.capture_wish_list_product_entries()
    print("No Of entries: {}".format(context.entries))


@then("{item_num} items are displayed")
def step_impl(context, item_num):
    """
    :param item_num: No of items to validate in the wish list
    :type context: behave.runner.Context
    """
    assert int(item_num) == context.entries


def prime_web_driver(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    return context.driver
