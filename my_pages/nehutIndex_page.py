from selenium.webdriver import Keys

from my_pages.base_page import BasePage
from my_pages.locators import NehutIndexPageLocators


class NehutIndexPage(BasePage):
    def __init__(self, driver):
        self.locator = NehutIndexPageLocators
        super().__init__(driver)
        self.driver.get('https://www.btl.gov.il/Simulators/NehutIndex/Pages/NecutCalc-aspx.aspx')

    def check_page_loaded(self):
        return self.find_element(*self.locator.logo)

    def insert_committee_type(self, select):
        self.select_element(self.locator.committee_type, select)

    def insert_main_section(self, text):
        element = self.enter_text(self.locator.main_section, text)
        self.hover(element)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def insert_subsection(self, text):
        element = self.enter_text(self.locator.subsection, text)
        self.hover(element)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.DOWN)
        element.send_keys(Keys.ENTER)

    def insert_description_of_the_defect(self, text):
        self.enter_text(self.locator.description_of_the_defect, text)

    def insert_disability_percentage(self, percentage):
        self.enter_text(self.locator.disability_percentage, percentage)

    def insert_deta_from(self, year, month):
        self.hover(self.enter_text(self.locator.datepicker_from, Keys.SPACE))
        self.select_element(self.locator.date_from_year, year)
        self.select_element(self.locator.date_from_month, month)
        self.click(self.locator.date_from_day)

    def insert_deta_until(self, year, month):
        self.hover(self.enter_text(self.locator.datepicker_until, Keys.SPACE))
        self.select_element(self.locator.date_until_year, year)
        self.select_element(self.locator.date_until_month, month)
        self.click(self.locator.date_until_day)

    def button_eavesdropping(self):
        self.click(self.locator.eavesdroppin)

    def simulator_table(self):
        return self.find_element(*self.locator.result_table)

    def next_button(self):
        self.click(self.locator.next)

    def get_disability_percentage_error(self):
        self.hover(self.enter_text(self.locator.disability_percentage, Keys.TAB))
        return self.find_element(*self.locator.disability_percentage_error).text

    def test_simulator_nehutIndex(self, committee_type, main_section, subsection,
                                  description_of_the_defect, percentage,
                                  from_year, from_month, until_month, until_year):
        self.insert_committee_type(committee_type)
        self.insert_main_section(main_section)
        self.insert_subsection(subsection)
        self.insert_description_of_the_defect(description_of_the_defect)
        # optional
        # self.insert_disability_percentage(percentage)
        self.insert_deta_from(from_year, from_month)
        self.insert_deta_until(until_year, until_month)
        self.button_eavesdropping()
