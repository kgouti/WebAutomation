from pages.Base_page import BasePage
from pages.locators import WishListLocators


class WishList(BasePage):

    def capture_wish_list_product_entries(self):
        wish_list_entries = self.driver.find_elements_by_xpath(WishListLocators.WISH_LIST_TABLE)
        return len(wish_list_entries)