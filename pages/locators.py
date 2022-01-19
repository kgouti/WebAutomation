from selenium.webdriver.common.by import By


class HomePageLocators:
    # WISH_LIST_RIBBON = (By.XPATH, "//ul[@class='products columns-5']//div[@class='yith-wcwl-add-button']//a[@class='add_to_wishlist single_add_to_wishlist']")
    # WISH_LIST_RIBBON = "//ul[@class='products columns-5']//div[@class='yith-wcwl-add-button']//a[@class='add_to_wishlist single_add_to_wishlist']"
    WISH_LIST_RIBBON = "//div[@class='elementor-shortcode']//ul[@class='products columns-5']//li//div[@class='yith-wcwl-add-button']"
    ACCEPT_ALL_BUTTON = (By.XPATH, "//a[@class='cc-btn cc-accept-all cc-btn-no-href']")
    # ACCEPT_ALL_BUTTON = "//a[@class='cc-btn cc-accept-all cc-btn-no-href']"
    # WISH_LIST_BUTTON = "//div//nav//div[@class='mobile-wishlist visible-xs']//a[@title='Wishlist']"
    WISH_LIST_BUTTON = "//div[@class='header-right col-md-3 hidden-xs']//div[@class='header-wishlist']"


class WishListLocators:
    WISH_LIST_HEADER = (By.XPATH, "//article//header[@class='single-head page-head no-thumbnail']")
    WISH_LIST_TABLE = "//tbody[@class='wishlist-items-wrapper']//tr[@data-row-id]"
