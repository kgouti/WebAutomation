from pages.Base_page import BasePage
from pages.locators import HomePageLocators, WishListLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    # def __init__(self):
    #     BasePage.__init__()

    def accept_cookies(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(HomePageLocators.ACCEPT_ALL_BUTTON)
        )
        element.click()

    #
    # accept_element = self.driver.find_element(HomePageLocators.ACCEPT_ALL_BUTTON)
    # if accept_element.is_displayed():
    #     accept_element.click()

    def find_product_columns(self):
        # wish_list_elements = self.driver.find_elements(HomePageLocators.WISH_LIST_RIBBON)
        wish_list_elements = self.driver.find_elements_by_xpath(HomePageLocators.WISH_LIST_RIBBON)
        return wish_list_elements

    def add_product_to_wishlist(self, element):
        element.click()
        time.sleep(1)
        # TODO: Ensure to put handle waits after elements are added to wishlist

    def navigate_to_wish_list_page(self):
        self.driver.find_element_by_xpath(HomePageLocators.WISH_LIST_BUTTON).click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(WishListLocators.WISH_LIST_HEADER, "Wishlist")
            )
        except NoSuchElementException:
            print("Unable to navigate to wish list page")
