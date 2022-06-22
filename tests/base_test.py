from selenium import webdriver

from tests.home_test import HomeTest
from tests.nehutIndek_test import NehutIndexTest
from tests.simulators_test import SimulatorsTest


class BaseTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def __call__(self, test_pages):

        try:
            for test_page in test_pages:
                print(type(test_page).__name__)
                # attribute is a string representing the attribute name
                for attribute in dir(test_page):
                    # Get the attribute value
                    attribute_value = getattr(test_page, attribute)
                    # Check that it is callable
                    if callable(attribute_value):
                        # Filter all dunder (__ prefix) methods
                        if attribute.startswith('__') == False:
                            attribute_value()
                            if attribute:
                                print(attribute, "Succeeded")
                                continue
                            print(attribute, "failed")

        finally:
            self.driver.close()


test = BaseTest()
# test([NehutIndexTest(test.driver)])
test([HomeTest(test.driver), SimulatorsTest(test.driver), NehutIndexTest(test.driver)])
