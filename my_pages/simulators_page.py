from my_pages.base_page import BasePage
from my_pages.locators import HomePageLocators


class SimulatorsPage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)
        self.driver.get('https://www.btl.gov.il/Simulators/Pages/default.aspx')

    def check_page_loaded(self):
        return self.find_element(*self.locator.logo)