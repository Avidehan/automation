from my_pages.base_page import BasePage
from my_pages.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)
        self.driver.get('https://www.btl.gov.il/Pages/default.aspx')

    def check_page_loaded(self):
        return self.find_element(*self.locator.logo)

    def search_item(self, search_text):
        self.enter_text(self.locator.search_field, search_text)
        self.click(self.locator.search_button)
        return self.search_result().text

    def search_result(self):
        self.wait_element(*self.locator.search_result)
        return self.find_element(*self.locator.search_result)

    def pyment_button(self):
        self.click(self.locator.payments_button)
        return self.get_title()

    def branches_button(self):
        self.click(self.locator.braches_button)
        return self.get_title()

    def personal_service_button(self):
        self.click(self.locator.personal_service_button)
        return self.get_title()
