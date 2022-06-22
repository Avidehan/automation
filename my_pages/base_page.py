from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_driver(self, url):
        self.driver.get(url)

    def click(self, locator):
        try:
            self.find_element(*locator).click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.hover(self.find_element(*locator))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()
            print("\n * ELEMENT NOT CLICKABLE! --> %s" % (locator[1]))

    def enter_text(self, locator, text):
        element = self.find_element(*locator)
        element.send_keys(text)
        return element

    def get_title(self) -> str:
        return self.driver.title

    def find_element(self, *locator):
        return self.wait_element(*locator)

    def find_all_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_url(self):
        return self.driver.current_url

    def hover(self, element):
        if type(element) is tuple:
            element = self.find_element(*element)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def select_element(self, locator, select_by):
        self.click(locator)
        select = Select(self.find_element(*locator))
        select.select_by_visible_text(select_by)
