from my_pages.home_page import HomePage


class HomeTest:
    def __init__(self, driver):
        self.driver = driver

    def test_load_page(self):
        page = HomePage(self.driver)
        return page.check_page_loaded()

    def test_search_positive(self):
        page = HomePage(self.driver)
        search_result = page.search_item("חשבונות")
        return search_result == "תוצאות חיפוש עבור חשבונות"

    def test_search_negative(self):
        page = HomePage(self.driver)
        search_result = page.search_item("shaxoahds")
        return search_result == "לא נמצאו תוצאות עבור shaxoahds"

    # def test_search_sql(self):
    #     page = HomePage(self.driver)
    #     search_result = page.search_item("'or 1==1")
    #     return  search_result == "'or 1==1"

    def test_pyment_button(self):
        page = HomePage(self.driver)
        result = page.pyment_button()
        return result == "המוסד לביטוח לאומי - תשלומים, דיווחים ושירותים"

    def test_branches_button(self):
        page = HomePage(self.driver)
        result = page.branches_button()
        return result == "סניפים וערוצי שירות | ביטוח לאומי"

    def test_personal_service_button(self):
        page = HomePage(self.driver)
        result = page.personal_service_button()
        return result == "כניסה לשירות אישי"
