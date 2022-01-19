
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_web_page(self):
        self.driver.get("https://testscriptdemo.com/")
        # return self
