from my_pages.simulators_page import SimulatorsPage


class SimulatorsTest():
    def __init__(self, driver):
        self.driver = driver

    def test_load_page(self):
        page = SimulatorsPage(self.driver)
        return page.check_page_loaded()
